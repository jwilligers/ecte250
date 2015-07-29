import MySQLdb


db = MySQLdb.connect("localhost", "root", "elect1", "SensorData")

curs=db.cursor()