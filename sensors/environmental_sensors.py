import time
import requests
from seeed_dht import DHT
from grove.grove_moisture_sensor import GroveMoistureSensor

def scan():
    # Temperature sensor is connected to port D18
    # Moisture sensor is connected to port A0
    t_sensor = DHT("11", 18)
    mois_sensor = GroveMoistureSensor(0)

    while True:
        humi, temp = t_sensor.read()
        mois = mois_sensor.moisture
        
        if 0 <= mois and mois < 300:
            level = 'dry'
        elif 300 <= mois and mois < 600:
            level = 'moist'
        else:
            level = 'wet'
        
        print('temperature {}C, humidity {}%'.format(temp, humi))
        print('moisture: {}, {}'.format(mois, level))
        
        # Add data to database by calling an API
        requests.post("http://127.0.0.1:8000/envi/add/{}/{}/{}/{}".format(humi, temp, mois, level))
        time.sleep(10)
        
scan()