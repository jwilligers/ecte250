from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager()
ard = ArduinoApi(connection = connection)

ard.pinMode (13, ard.OUTPUT)

for i in range(10000):
	ard.digitalWrite(13, (i+1) % 2)
	sleep(0.2)