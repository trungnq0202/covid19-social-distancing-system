import time
 
from cv2 import fastAtan2
from starlette.datastructures import URL

from qrCode import turn_on_qr_reader, keep_alive
from lcd16x2 import display
from apiHelper import RequestsApi
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor

QR_SERVER_HOST="http://0.0.0.0:8000/"
ACTIVE_FLAG_TIME = 1

server = RequestsApi()
qr_server = RequestsApi(base_url=QR_SERVER_HOST)
m_sensor_entry = GroveMiniPIRMotionSensor(6)
m_sensor_exit = GroveMiniPIRMotionSensor(2)


m_sensor_entry_flag = False
m_sensor_exit_flag = False
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
    global num_people
    global total_enter

    if num_people == 5:
        display("Too many people")
    elif num_people >= 0:
        # if not check_valid_qr():
        #     return
        num_people += 1
        total_enter += 1
        display("Welcome")
        update_num_people()
        set_update_people_server_flag(False)


def handle_person_exit():
    global num_people
    global total_exit

    num_people -= 1
    total_exit += 1
    display("Good Bye")
    update_num_people()


def m_sensor_entry_callback():
    global m_sensor_entry_flag
    m_sensor_entry_flag = True


def m_sensor_exit_callback():
    global m_sensor_exit_flag
    m_sensor_exit_flag = True


def detect():
    
    global m_sensor_entry_flag
    global m_sensor_exit_flag
    global num_people

    while True:
        m_sensor_entry.on_detect = m_sensor_entry_callback
        m_sensor_exit.on_detect = m_sensor_exit_callback

        #Entry case
        if m_sensor_entry_flag == True:
           for _ in range(3):
               m_sensor_exit.on_detect = handle_person_entry
               time.sleep(0.5)


        #Exit case
        if m_sensor_exit_flag == True:
            for _ in range(3):
               m_sensor_entry.on_detect = handle_person_exit
               time.sleep(0.5)

        m_sensor_exit_flag = False
        m_sensor_entry_flag = False
        time.sleep(0.2)
    


if __name__ == '__main__':
    detect()