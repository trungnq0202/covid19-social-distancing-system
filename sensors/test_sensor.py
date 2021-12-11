import csv

from qrCode import turn_on_qr_reader
from lcd16x2 import display_message
from apiHelper import RequestsApi

from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT
from grove.grove_moisture_sensor import GroveMoistureSensor

u_sensor = GroveUltrasonicRanger(16)
t_sensor = DHT("11", 18)
mois_sensor = GroveMoistureSensor(0)

humi, temp = t_sensor.read()
mois = mois_sensor.moisture

data = []

for i in range(100):
	u_sensor.get_distance()

file = open('ultrasonic.csv', 'w+', newline ='')
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(data)