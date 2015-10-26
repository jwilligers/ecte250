#!/usr/bin/python
import MySQLdb
import time
import random
import serial

db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")
curs = db.cursor()

createDatabase = True

source = "Serial"  # CSV or Serial
i = 1

# MQ2,MQ4,MQ6,MQ9,Humidity,Temp
if createDatabase:
	print("Dropping Table")
	curs.execute("DROP TABLE IF EXISTS sensorData")
	print("Creating table")
	curs.execute("""	CREATE TABLE sensorData (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	flammablegas FLOAT NULL DEFAULT NULL,
	methane FLOAT NULL DEFAULT NULL,
	LPG FLOAT NULL DEFAULT NULL,
	carbonmonoxide FLOAT NULL DEFAULT NULL,
	temperature FLOAT NULL DEFAULT NULL,
	humidity FLOAT NULL DEFAULT NULL
	)
	""")
	db.commit()

if source == "CSV":
	filename = "gasData.txt"
	with open(filename) as f:
		for line in f:
			values = line.split(",")
			flammablegas = values[0]
			methane = values[1]
			carbonmonoxide = values[2]
			lpg = values[3]
			humidity = values[4]
			temperature = values[5]

			curs.execute("INSERT INTO sensorData VALUES(" +
                         str(i) + "," +
                         str(flammablegas) + "," +
                         str(methane) + "," +
                         str(carbonmonoxide) + "," +
                         str(lpg) + "," +
                         str(humidity) + "," +
                         str(temperature) + ")")
			db.commit()
			i += 1

	print ("Data committed")
	print(str(i))

if source == "Serial":
	ser = serial.Serial('/dev/ttyACM0', 9600)
	print(ser.portstr)
	i = 0
	while True:
		i += 1
		values = ser.readline()
		values = ser.readline().split(",")
		print(values)
		if (len(values) == 6):
			flammablegas = values[0]
			print("Flammable Gas = " + flammablegas )
			methane = values[1]
			print("Methane = " + methane)
			carbonmonoxide = values[2]
			lpg = values[3]
			humidity = values[4]
			temperature = values[5]

			curs.execute("INSERT INTO sensorData VALUES(" +
			str(i) + "," +
			str(flammablegas) + "," +
			str(methane) + "," +
			str(carbonmonoxide) + "," +
			str(lpg) + "," +
			str(humidity) + "," +
			str(temperature) + ")")
			db.commit()
			i += 1
			print ("Data committed")
			print(str(i))
		else:
			print ("Invalid Data")
