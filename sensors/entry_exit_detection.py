import time

from qrCode import turn_on_qr_reader
from lcd16x2 import display_message
from apiHelper import RequestsApi

from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

server = RequestsApi()

def update_num_people(num_people):
    response = server.put("humanEntryAndExit/update/people/{}".format(num_people))
    if response.ok is False:
            print(response.raise_for_status())


def notify_person_action(action):
    response = None
    if action == "enter":
        response = server.post("humanEntryAndExit/PersonEnter")
    else:
        response = server.post("humanEntryAndExit/PersonExit")
    if response.ok is False:
            print(response.raise_for_status())

            
def detect():

    # Ultrasonic sensor connected to port D16
    u_sensor = GroveUltrasonicRanger(16)
    num_people = 0
    update_num_people(num_people)
    distances = []

    # Ultrasonic and motion sensor are opposite from each other (motion at door, ultra at wall)
        # Perosn leaving -> distance between ultra sensor and person increases
        # Person entering -> distance between ultra sensor and person decreases
    while True:
        if len(distances) == 3:
            print(distances)
            if distances == sorted(distances):
                if num_people > 0:
                    num_people -= 1
                    print("Somebody exits")
                    notify_person_action("exit")
                    update_num_people(num_people)
            elif distances == sorted(distances, reverse=True):
                if num_people < 5:
                    """
                    Scan QR code here
                    """
                    num_people += 1
                    print("Somebody enters")

                    if not turn_on_qr_reader():
                        display_message("Invalid QR")
                        continue
                    display_message("Welcome")

                    notify_person_action("enter")
                    update_num_people(num_people)
                else:
                    """
                    Send warning here
                    """
                    display_message("Too many people")
                    print("Too many people")
            distances.clear()
        else:
            distances.append(u_sensor.get_distance())

        print("Number of people:" + str(num_people))
        time.sleep(1)
      

if __name__ == "__main__":
    detect()
