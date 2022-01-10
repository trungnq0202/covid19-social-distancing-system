import time
 
from cv2 import fastAtan2
from starlette.datastructures import URL

from qrCode import turn_on_qr_reader
from lcd16x2 import display_message
from apiHelper import RequestsApi
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor

QR_SERVER_HOST="http://0.0.0.0:8000/"
ACTIVE_FLAG_TIME = 1

server = RequestsApi()
qr_server = RequestsApi(base_url=QR_SERVER_HOST)
m_sensor_entry = GroveMiniPIRMotionSensor(5)
m_sensor_exit = GroveMiniPIRMotionSensor(12)


m_sensor_entry_flag = False
m_sensor_exit_flag = False
flag = False
num_people = 0
total_enter = 0
total_exit = 0

def update_num_people():
    global num_people
    global total_enter
    global total_exit
    response = server.put("humanEntryAndExit/update/people/{}/{}/{}".format(num_people, total_enter, total_exit))
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
    print("somebody entering")
    global num_people
    global total_enter
    global flag

    if num_people == 5:
        display_message("Too many people")
    elif num_people >= 0:
        # if not check_valid_qr():
        #     return
        num_people += 1
        total_enter += 1
        print(num_people)
        display_message("Welcome")
        # update_num_people()
        # set_update_people_server_flag(False)

    flag = True


def handle_person_exit():
    print("somebody exiting")
    global num_people
    global total_exit
    global flag
    if num_people > 0:
        num_people -= 1
        total_exit += 1
        print(num_people)
        display_message("Good Bye")
        # update_num_people()
        flag = True


def m_sensor_entry_callback():
    print("detect entry")
    global m_sensor_entry_flag
    m_sensor_entry_flag = True


def m_sensor_exit_callback():
    print("detect exit")
    global m_sensor_exit_flag
    m_sensor_exit_flag = True


def detect():
    
    global m_sensor_entry_flag
    global m_sensor_exit_flag
    global num_people
    global flag

    while True:
        m_sensor_entry.on_detect = m_sensor_entry_callback
        m_sensor_exit.on_detect = m_sensor_exit_callback

        #Entry case
        if m_sensor_entry_flag == True:
           for _ in range(20):
               m_sensor_exit.on_detect = handle_person_entry
               if flag == True:
                   flag = False
                   break
               time.sleep(0.2)
               print("entry case")


        #Exit case
        if m_sensor_exit_flag == True:
            for _ in range(20):
               m_sensor_entry.on_detect = handle_person_exit
               if flag == True:
                   flag = False
                   break
               time.sleep(0.2)
               print("exit case")

        #print("resetting")
        m_sensor_exit_flag = False
        m_sensor_entry_flag = False
        time.sleep(0.2)
    


if __name__ == '__main__':
    detect()
    # while True:
    #     m_sensor_entry.on_detect = m_sensor_entry_callback
    #     m_sensor_exit.on_detect = m_sensor_exit_callback
    #     time.sleep(0.2)