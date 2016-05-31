from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return "HEELO WORLD!"

@app.route("/json")
def jsontest():
	cpuSpeed = "2.4"
	dic = {'speed':cpuSpeed}
	return jsonify(results=dic) 


if __name__ == "__main__":
	app.run()

