from flask import Flask, Response, render_template, jsonify
from flask.ext.mysql import MySQL
import pygal

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
	return render_template('index.html',title='Home',user=user, selected = "Home")
@app.route('/Settings')
def settings():
	user = {'nickname': 'Hudson'}
	return render_template('index.html',title='Home',user=user, selected = "Settings")
@app.route('/barchart/')
def forecast():
    """ render svg graph """
    bar_chart = pygal.Bar(width=450 ,height=300)
    bar_chart.title = "Barchart"
    inside,outside,params = [21,21.2,22,21,24.5,23.5],[15,18,20,34,23,23],['Monday','Tuesday','Wednesday', 'Thursday', 'Friday']
    bar_chart.add('Inside', inside)
    bar_chart.add('Outside', outside)
    bar_chart.x_labels = params
    return Response(response=bar_chart.render(), content_type='image/svg+xml')

if __name__ == '__main__':
	app.config['DEBUG'] = True
	app.run(debug=True, host='0.0.0.0')
