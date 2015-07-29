import mysql.connector

connection = mysql.connector(user='root', password='elect1', host=127.0.0.1',database='SensorData')


connection.close()