#!/usr/bin/python
import MySQLdb


db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")

curs=db.cursor()

curs.execute ("DELETE * FROM data")

db.commit()
print "Database cleared"
