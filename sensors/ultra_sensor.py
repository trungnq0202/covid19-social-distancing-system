import time
import requests
from apiHelper import PATH
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

def scan():
    # Ultrasonic sensor connected to port D16
    u_sensor = GroveUltrasonicRanger(16)
    people = 0
    requests.put(PATH + "humanEntryAndExit/update/people/{}".format(people))
    distances = []

    # Ultrasonic and motion sensor are opposite from each other (motion at door, ultra at wall)
    # Perosn leaving -> distance between ultra sensor and person increases
    # Person entering -> distance between ultra sensor and person decreases
    while True:
        if len(distances) == 3:
            print(distances)
            if distances == sorted(distances):
                if people > 0:
                    people -= 1
                    print("Somebody exits")
                    requests.post(PATH + "humanEntryAndExit/PersonExit")
                    requests.put(PATH + "humanEntryAndExit/update/people/{}".format(people))
            elif distances == sorted(distances, reverse=True):
                if people < 5:
                    """
                    Scan QR code here
                    """
                    people += 1
                    print("Somebody enters")
                    requests.post(PATH + "humanEntryAndExit/PersonEnter")
                    requests.put(PATH + "humanEntryAndExit/update/people/{}".format(people))
                else:
                    """
                    Send warning here
                    """
                    print("Too many people")
            distances.clear()
        else:
            distances.append(u_sensor.get_distance())
        print(people)
        time.sleep(1)
      
scan()
