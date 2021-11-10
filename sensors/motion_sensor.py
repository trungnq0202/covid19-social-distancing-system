import time
 
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

# Motion sensor connected to port D5
# Ultrasonic sensor connected to port D16
m_sensor = GroveMiniPIRMotionSensor(5)
u_sensor = GroveUltrasonicRanger(16)
people = 0

# Ultrasonic and motion sensor are opposite from each other (motion at door, ultra at wall)
# Person leaving -> distance between ultra sensor and person increases
# Person entering -> distance between ultra sensor and person decreases
def on_detect():
    global people
    print('prev: {} cm, curr: {} cm'.format(prev, cur))
    if prev > cur:
        if people < 5:
            # Scan QR code here
            people += 1
        else:
            # Send warning here
            print("Too many people")
    else:
        if people > 0:
            people -= 1
    time.sleep(1)
    
m_sensor.on_detect = on_detect

while True:
    # cur: current distance; prev: distance 1 second ago
    cur = u_sensor.get_distance()
    time.sleep(1)
    prev = cur
    cur = u_sensor.get_distance()
    print(people)
