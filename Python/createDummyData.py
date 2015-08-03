#!/usr/bin/python
import MySQLdb
import time
import random


db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")

curs=db.cursor()

id = 5

temp = 23.54
for id in range(1,100):
	time = time.time()
	random = random.randrange(0,10)
	print time
	curs.execute ("INSERT INTO data values("+str(id)+ ","+time+","+ str(temp+random)+")")
	time.sleep(1)
db.commit()
print "Data committed"
