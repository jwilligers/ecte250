#!/usr/bin/python
import MySQLdb
import time
import random

db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")
curs=db.cursor()

createDatabase = True
createDummyData = False
# MQ2,MQ4,MQ6,MQ9,Humidity,Temp
if createDatabase:
	curs.execute ("DROP TABLE IF EXISTS sensorData")
	curs.execute ("""	CREATE TABLE sensorData (
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
	print ("Database sensorData created")

	curs.execute ("DROP TABLE IF EXISTS thresholds")
#	curs.execute ("CREATE TABLE thresholds (	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,	upperlimit FLOAT NULL DEFAULT NULL)")
#	db.commit()
#	print "Database thresholds created"

if createDummyData:
	temp = 23.54
	for i in range(1,40):
		timestamp = time.time()
		rand = random.randrange(0,10)
		#print timestamp
		#sql = "INSERT INTO sensorData(id,pirDetection, temperature, humidity, varResistor) VALUES (" + str(i) + ", 2, 3.3, 4.3, 0.34);"
		#print(sql)
		#curs.execute (sql)
		#curs.execute ("INSERT INTO sensorData values("+str(i)+ ","+ str(rand%2==0) +"," + str(temp+rand) + "," + str(i/1.0) +"," + str(i/10.0*pow(i,0.5)) + ")")
		curs.execute ("INSERT INTO sensorData values("+str(i)+ ","+ str(rand%2==0) +"," + str(temp+rand) + "," + str(rand) +"," + str(i) + ")")
		print(str(i))
	#	curs.execute ("INSERT INTO data values("+str(i)+ ","+ time+"," +  random%2==0 +"," + str(temp+random)+ "," + i/1.0 +","+ i/10.0*pow(i,0.5) ")")
#		time.sleep(0.2)
	db.commit()
	print "Data committed"
