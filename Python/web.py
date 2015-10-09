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
config.range = (0, 1024)
config.human_readable = True
config.show_dots = False
config.truncate_label = -1

gasID = {'flammablegas': 0, 'methane': 1, 'LPG': 2, 'temp': 3, 'carbonmonoxide': 4, 'temperature': 5, 'humidity': 6}
gasArray = ["FG", "FG", 0, 1023],["FG", "FG", 0, 1023],["FG", "FG", 0, 1023],["FG", "FG", 0, 1020], ["CO", "Carbon Monoxide", 0, 1050],["temp", "Temperature", 0, 50],["humidity", "Humidity", 0, 100]

@app.route('/')
@app.route('/Home')
def index():
    user = {'nickname': 'Josh'}
    return render_template('index.html', title='Home', user=user, selected="Home")

@app.route('/Settings')
def settings():
    user = {'nickname': 'usename'}
    return render_template('index.html', title='Settings', user=user, selected="Settings")

@app.route('/gas/<gas>')
def showGasInfo(gas):
    user = {'nickname': 'Hudson'}
    return render_template('gasInfo.html', title=gas, gas=gas, user=user)

@app.route('/barchart/<gas>/<time>')
def forecast(gas, time):


    cursor.execute('SELECT * FROM sensorData')
    results = cursor.fetchall()
    i = 0
    id = []
    flammablegas = []
    methane = []
    temperature = []
    humidity = []
    LPG = []
    carbonmonoxide = []

    if gas == "flammablegas":
        config.range = (200, 350)
    if gas == "methane":
        config.range = (300, 400)
    if gas == "humidity":
        config.range = (10, 30)
    if gas == "LPG":
        config.range = (500, 800)
    if gas == "carbonmonoxide":
        config.range = (200, 400)
    if gas == "temperature":
        config.range = (30, 60)


    line_chart = pygal.Line(config)
    line_chart.title = gasArray[gasID[gas]][1]
    line_chart.x_labels = id
    for rows in results:
        id.append(int(results[i][0]))
        flammablegas.append((int(results[i][1])))
        methane.append((int(results[i][2])))
        LPG.append(int(results[i][3]))
        carbonmonoxide.append(int(results[i][4]))
        temperature.append(int(results[i][5]))
        humidity.append(int(results[i][6]))
        i += 1
    if gas == "flammablegas":
       line_chart.add('Flammable Gas', flammablegas)
    if gas == "methane":
       line_chart.add('Methane', methane)
    if gas == "humidity":
        line_chart.add('Humidity', humidity)
    if gas == "LPG":
        line_chart.add('LPG', LPG)
    if gas == "carbonmonoxide":
       line_chart.add('Carbon Monoxide', carbonmonoxide)
    if gas == "temperature":
        line_chart.add('Temperatuure', temperature)

    return Response(response=line_chart.render(), content_type='image/svg+xml')


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(debug=True, host='0.0.0.0')
