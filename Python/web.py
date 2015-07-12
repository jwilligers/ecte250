from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	user = {'nickname': 'Josh'}
	return render_template('index.html',title='Home',user=user)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
