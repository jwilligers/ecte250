from flask import Flask, Response, render_template, jsonify
from flask.ext.mysql import MySQL
import pygal

app = Flask(__name__)

DEBUG = True

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'elect1'
app.config['MYSQL_DATABASE_DB'] = 'SensorData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

config = pygal.Config()

config.show_legend = False
config.human_readable = True
config.show_x_labels = True
config.height = 400
config.width = 550
config.interpolate = 'cubic'
config.range = (0, 40)
config.human_readable = True
config.show_dots = False
config.truncate_label = -1


gasID = {'CO': 0, 'temp': 1, 'humidity': 2, 'LPG': 3}
gasArray = ["CO", "Carbon Monoxide", 0, 50],["temp", "Temperature", 0, 50],["humidity", "Humidity", 0, 100]

@app.route('/')
@app.route('/Home')
def index():
    user = {'nickname': 'Josh'}
	return render_template('index.html',title='Home',user=user, selected = "Home")

@app.route('/Settings')
def settings():
    user = {'nickname': 'usename'}
    return render_template('index.html',title='Settings',user=user, selected = "Settings")


@app.route('/gas/<gas>')
def showGasInfo(gas):
    user = {'nickname': 'Hudson'}
    return render_template('gasInfo.html',title=gas, gas = gas, user=user)



@app.route('/barchart/<gas>/<time>')
def showgas(gas, time):
    cursor.execute('SELECT * FROM sensorData')
    results = cursor.fetchall()
    i = 0
    id = []
    temperature = []
    humidity = []
    pir_detection = []
    var_resistor = []

    line_chart = pygal.Line(config)
#    line_chart.title = gasArray[gasID[gas]][1]
    line_chart.x_labels = id
    for rows in results:
        id.append(int(results[i][0]))
        pir_detection.append((int(results[i][1])))
        temperature.append(int(results[i][2]))
        humidity.append(int(results[i][3]))
        var_resistor.append(int(results[i][4]))
        i += 1
    if gas == "temp":
        line_chart.add('Temperature', temperature)
    if gas == "humidity":
        line_chart.add('Humidity', humidity)
    if gas == "pir":
        line_chart.add('PIR Detection', pir_detection)
    if gas == "var":
        line_chart.add('Variable Resistor', var_resistor)


    return Response(response=line_chart.render(), content_type='image/svg+xml')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(debug=True, host='0.0.0.0')
