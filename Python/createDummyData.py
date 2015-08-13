#!/usr/bin/python
import MySQLdb
import time
import random

db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")
curs=db.cursor()

createDatabase = True
createDummyData = True
if createDatabase:
	curs.execute ("DROP TABLE IF EXISTS sensorData")
	curs.execute ("""	CREATE TABLE sensorData (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	pirDetection tinyint(1) NULL DEFAULT NULL,
	temperature FLOAT NULL DEFAULT NULL,
	humidity FLOAT NULL DEFAULT NULL,
	varResistor FLOAT NULL DEFAULT NULL
	)
	""")
	db.commit()
	print "Database created"

if createDummyData:
	temp = 23.54
	for i in range(1,100):
		timestamp = time.time()
		rand = random.randrange(0,10)
		print timestamp
		print ("INSERT INTO data values("+str(i)+ ","+ str(timestamp) +"," +  str(rand%2==0) +"," + str(temp+rand) + "," + str(i/1.0) +"," + str(i/10.0*pow(i,0.5)) + ")")
	#	curs.execute ("INSERT INTO data values("+str(i)+ ","+ time+"," +  random%2==0 +"," + str(temp+random)+ "," + i/1.0 +","+ i/10.0*pow(i,0.5) ")")
		time.sleep(1)
	db.commit()
	print "Data committed"
