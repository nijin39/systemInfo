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

@app.route("/getCpuLoad")
def getCpuLoad():
	f=open("system.data","rb")
	systemInfo = pickle.load(f)
	f.close()
	print systemInfo['cpuLoad']
	return json.dumps(systemInfo['cpuLoad'])

@app.route("/getService")
def getService():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
        return jsonify(result=systemInfo['service'])

@app.route("/getSwap")
def get_swap():
    	'''load swap info from file, map key is "swap"'''
   	f=open("system.data", "rb")
    	swapLog = pickle.load(f)
    	f.close()
    	return jsonify(result=swapLog['swap'])

@app.route("/getSystemInfo")
def getSysLog():
	f=open("system.data","rb")
	systemInfo = pickle.load(f)
        f.close()
        return jsonify(result=systemInfo['sysInfo'])

@app.route("/getLastLogin")
def getLastLogin():
    	f = open("system.data","rb")
    	systemInfo = pickle.load(f)
    	f.close()
    	return jsonify(result=systemInfo['lastLog'])

@app.route("/getDiskUsage")
def getDiskUasge():
	f = open("system.data","rb")
	systemInfo = pickle.load(f)
	f.close()
	return jsonify(result=systemInfo['diskUsage'])

@app.route("/getMemInfo")
def getMemUsage():
        f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
        return jsonify(result=systemInfo['memUsage']) 

@app.route("/getNetwork")
def getNetwork():
	f=open("system.data","rb")
	systemInfo = pickle.load(f)
	f.close()
	return jsonify(result=systemInfo['networkLog'])

@app.route("/getCpuInfo")
def getCpuInfo():
    	f = open("system.data","rb")
    	systemInfo = pickle.load(f)
    	f.close()
    	return jsonify(result=systemInfo['cpuInfo'])

@app.route("/getPing")
def getPing():
	f=open("system.data","rb")
        systemInfo = pickle.load(f)
        f.close()
	return jsonify(result = systemInfo['ping'])

@app.route('/index')
def index():  
    return render_template('index.html')  # render a template
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',8080)), debug=True)
