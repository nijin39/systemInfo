from flask import Flask, render_template
from flask import jsonify
import commands
import pickle
import os

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/ping")
def get_ping():
	ping_data = commands.getoutput('ping -c 5 www.google.com | grep rtt')
	ping_list = pingdata.split('=')
	pint_list2 = ping_list[1].strip().split('/')
	ping_Data = ping_list2[0:3]	

	dic = {"min/avg/max":ping_Data}
	return jsonify(results=dic)

@app.route("/getErrorLog")
def getErrorLog():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(result=systemInfo['errorLog'])

@app.route("/getWarnLog")
def getWarnLog():
	f=open("system.data","rb")
	systemInfo = pickle.load(f)
        f.close()
        return jsonify(result=systemInfo['warnLog'])

@app.route('/index')
def index():  
    return render_template('index.html')  # render a template
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
