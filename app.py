from flask import Flask, render_template
from flask import jsonify
import commands
import pickle
import os
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/getPing")
def getPing():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(result = systemInfo['ping'])

@app.route("/getSystem")
def getSysInfo():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(systemInfo['sysInfo'])

@app.route("/getCpuLoad")
def getCPULoad():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return json.dumps(systemInfo['cpuLoad'])

@app.route("/getCpuInfo")
def getCpuInfo():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(systemInfo['cpuInfo'])

@app.route("/getNetworkUsage")
def getNetworkUsage():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(result=systemInfo['networkUsage'])

@app.route("/getDiskUsage")
def getDiskUsage():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(result=systemInfo['diskUsage'])

@app.route("/getMemUsage")
def getMemUsage():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(systemInfo['memUsage'])

@app.route("/getSwapUsage")
def getSwapUsage():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(systemInfo['swapUsage'])

@app.route("/getErrorLog")
def getErrorLog():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(result = systemInfo['errorLog'])

@app.route("/getWarnLog")
def getWarnLog():
	f=open("system.data","rb")
	systemInfo = pickle.load(f)
        f.close()
        return jsonify(result = systemInfo['warnLog'])

@app.route("/getLastLogin")
def getLastLogin():
	f=open("system.data","rb")
	systemInfo = pickle.load(f)
        f.close()
        return jsonify(result = systemInfo['lastLog'])

@app.route("/getService")
def getService():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
        return jsonify(result=systemInfo['service'])

@app.route('/index')
def index():  
    return render_template('index.html')  # render a template
	
@app.route('/index2')
def index2():  
    return render_template('index2.html')  # render a template

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
