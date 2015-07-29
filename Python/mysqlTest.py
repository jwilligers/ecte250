#!/usr/bin/python
import MySQLdb
import time


db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")

curs=db.cursor()

id = 5

temp = 23.54
for id in range(1,100):
	time = time.time()
	print timestamp
	curs.execute ("INSERT INTO data values("+str(id)+ ","+time+","+ str(temp+id/10.0)+")")
	time.sleep(1)
db.commit()
print "Data committed"

