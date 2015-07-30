from flask import Flask
from flask import render_template
from flask import jsonify
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'elect1'
app.config['MYSQL_DATABASE_DB'] = 'SensorData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def index():
	user = {'nickname': 'Josh'}
	return render_template('index.html',title='Home',user=user)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
