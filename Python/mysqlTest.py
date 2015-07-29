#!/usr/bin/python
import MySQLdb
import time


db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")

curs=db.cursor()

id = 5

temp = 23.54
for id in range(5,100):
	timestamp = int(time.time())
	print timestamp
	curs.execute ("INSERT INTO data values("+str(id)+ ","+str(timestamp)+","+ str(temp+id/10)+")")

db.commit()
print "Data committed"

