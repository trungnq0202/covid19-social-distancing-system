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
                    #if not turn_on_qr_reader():
                    #    distances.clear()
                    #    continue
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
                if len(distances) >= 1:
                    if abs(distances[-1] - dist) > 2:
                        distances.append(dist)
                else:
                    distances.append(dist)


        print("Number of people:" + str(num_people))
        time.sleep(0.5)
      


def detect_entry():

    sensor_exit_distances = []
    sensor_entry_distances = []
    num_people = 0 
    
    while True:
        
        # exit case
        if len(sensor_exit_distances) == 2:
            if abs(calculate_motion(sensor_exit_distances)) > 3:
                print("Somebody exits")
                print(sensor_exit_distances)
                num_people -= 1
                notify_person_action("exit")
                display_message("Good Bye")
                update_num_people(num_people)
            
                sensor_entry_distances.clear()
                time.sleep(2)
            sensor_exit_distances.clear()
        
        # Entry case
        if len(sensor_entry_distances) == 2:
            print(sensor_entry_distances)
            if abs(calculate_motion(sensor_entry_distances)) > 3:
                if num_people < 5:
                    print("Somebody entry")
                    print(sensor_entry_distances)
                    display_message("Welcome")
                    num_people += 1
                    notify_person_action("enter")
                    update_num_people(num_people)

                else: 
                    display_message("Too many people")
                    print("Too many people")
                    
                sensor_exit_distances.clear()
                time.sleep(2)
            sensor_entry_distances.clear() 
            print(sensor_entry_distances)
        

        sensor_exit_dist = u_sensor.get_distance()
        sensor_entry_dist = get_dist()
        print("Entry: "+ str(sensor_entry_dist))
        print("Exit: " + str(sensor_exit_dist))
        if sensor_exit_dist < 70:
            sensor_exit_distances.append(sensor_exit_dist)

        if sensor_entry_dist < 200:
            sensor_entry_distances.append(sensor_entry_dist)
        
        print("Number of people:" + str(num_people))
        time.sleep(1)



if __name__ == "__main__":
    detect_entry()
