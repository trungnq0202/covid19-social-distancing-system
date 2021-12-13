import time
import statistics

from qrCode import turn_on_qr_reader
from lcd16x2 import display_message
from apiHelper import RequestsApi

from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from second_sensor import get_dist

server = RequestsApi()
u_sensor = GroveUltrasonicRanger(16)


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


def calculate_motion(distances):
    avg_dist = statistics.mean(distances[0:len(distances)-1])
    return distances[-1] - avg_dist # positive for exit and negative for entry


            
def detect():

    # Ultrasonic sensor connected to port D16
    num_people = 0
    update_num_people(num_people)
    distances = []

    # Ultrasonic and motion sensor are opposite from each other (motion at door, ultra at wall)
        # Perosn leaving -> distance between ultra sensor and person increases
        # Person entering -> distance between ultra sensor and person decreases
    while True:
        if len(distances) == 5:
            print(distances)
            diff = calculate_motion(distances)
            if diff >= 2:
                if num_people > 0:
                    num_people -= 1
                    print("Somebody exits")
                    notify_person_action("exit")
                    display_message("Good Bye")
                    update_num_people(num_people)
            elif diff <= -2:
                if num_people < 5:
                    """
                    Scan QR code here
                    """
                    print("Somebody enters")
                    if not turn_on_qr_reader():
                        distances.clear()
                        continue
                    display_message("Welcome")
                    num_people += 1
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
            dist = u_sensor.get_distance()
            if dist <= 100:
                distances.append(dist)

        print("Number of people:" + str(num_people))
        time.sleep(1)
      


def detect_entry():

    sensor_in_distances = []
    sensor_out_distances = []
    num_people = 0 
    
    while True:
        sensor_in = False
        sensor_out = False
        # exit case
        if len(sensor_in_distances) == 3 and abs(calculate_motion(sensor_in_distances)) > 10:
            sensor_in = True
            print("Somebody exits")
            notify_person_action("exit")
            display_message("Good Bye")
            update_num_people(num_people)
            sensor_in_distances.clear()
            sensor_out_distances.clear()
        # Entry case
        if len(sensor_in_distances) == 3 and abs(calculate_motion(sensor_out_distances)) > 10:
            sensor_out = True
            if num_people < 5:
                print("Somebody entry")
                display_message("Welcome")
                num_people += 1
                notify_person_action("enter")
                update_num_people(num_people)
                sensor_in_distances.clear()
                sensor_out_distances.clear()
            else: 
                display_message("Too many people")
                print("Too many people")
                sensor_in_distances.clear()
                sensor_out_distances.clear()

        sensor_in_distances.append(u_sensor.get_distance())
        sensor_out_distances.append(get_dist())
        print("Number of people:" + str(num_people))
        time.sleep(1)



if __name__ == "__main__":
    detect_entry()
