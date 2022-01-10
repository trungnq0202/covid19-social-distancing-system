import time
import statistics
from cv2 import fastAtan2
import requests
import asyncio

from requests.models import Response
# from threading import Timer
from starlette.datastructures import URL

from qrCode import turn_on_qr_reader, keep_alive
from lcd16x2 import display_message
from apiHelper import RequestsApi
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor

QR_SERVER_HOST="http://0.0.0.0:8000/"
ACTIVE_FLAG_TIME = 1

server = RequestsApi()
qr_server = RequestsApi(base_url=QR_SERVER_HOST)
m_sensor_entry = GroveMiniPIRMotionSensor(6)
m_sensor_exit = GroveMiniPIRMotionSensor(2)


# m_sensor_entry_flag = False
m_sensor_exit_flag = False
num_people = 0

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

def set_update_people_server_flag(flag):
    response = server.post("roomMonitor/setFlag/{}".format(flag))
    if response.ok is False:
            print(response.raise_for_status())

def check_valid_qr():
    #Request the server to allow streaming the qr code scaning process
    response = qr_server.post("qr_code/setStatus/pending")
    response = qr_server.get("qr_code/start_scanning")
    if response.ok is False:
        print(response.raise_for_status())

    result = response.json()
    if (result == "success"):
        return True
    else:
        return False
    
    # while(True):
    #     time.sleep(0.5)
    #     response = qr_server.get("qr_code/getStatus")
    #     cur_status = response.json()
    #     if (cur_status == "pending"):
    #         continue
    #     elif (cur_status == "success"):
    #         return True
    #     else:
    #         return False


def handle_person_entry():
    global num_people
    if num_people == 5:
        display_message("Too many people")
    elif num_people > 0:
        set_update_people_server_flag(True)
        if not check_valid_qr():
            return
        display_message("Welcome")
        num_people += 1
        notify_person_action("enter")
        update_num_people(num_people)
        set_update_people_server_flag(False)

def handle_person_exit():
    global num_people
    num_people -= 1
    notify_person_action("exit")
    display_message("Good Bye")
    update_num_people(num_people)

def m_sensor_entry_callback():
    # global m_sensor_entry_flag
    global m_sensor_exit_flag
    global num_people
    #Entry case
    if m_sensor_exit_flag == False:
        print("Somebody enters")
        handle_person_entry()

    #Exit case
    else:
        print("Somebody exits")
        handle_person_exit()
        m_sensor_exit_flag = False

def m_sensor_exit_callback():
    global m_sensor_exit_flag
    m_sensor_exit_flag = True

def detect_entry():
    num_people = 0
 
    m_sensor_entry.on_detect = m_sensor_entry_callback
    m_sensor_exit.on_detect = m_sensor_exit_callback

    while True:
        time.sleep(0.2)
    


if __name__ == '__main__':
    detect_entry()