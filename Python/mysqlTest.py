#!/usr/bin/python
import MySQLdb
import time


db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")

curs=db.cursor()

id = 4
timestamp = int(time.time())
temp = 23.54
curs.execute ("INSERT INTO data values("+str(id)+ ","+str(timestamp)+","+ str(temp)+")")

db.commit()
print "Data committed"

