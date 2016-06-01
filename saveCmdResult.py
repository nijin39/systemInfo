#!/usr/bin/env python
import pickle
import systemInfo

superMap={}

errorLog=[]

for item in systemInfo.getErrLog().items():
	errorLog.append( {'message' : item[0], 'count' : item[1] } )

errorLogMap = {'errorLog':errorLog}
superMap.update(errorLogMap)

warnLog=[]

for item in systemInfo.getWarnLog().items():
        warnLog.append( {'message' : item[0], 'count' : item[1] } )

warnLogMap = {'warnLog':warnLog}
superMap.update(warnLogMap)

# Cpu Load
cpuLoad = {'cpuLoad' : systemInfo.getCPULoad()}
superMap.update(cpuLoad)

#cpu
#cpu-info ={'cpumodel':systemInfo.getcpumodel(), 'cpuspeed':systemInfo.getCpuSpped}
#superMap.update(cpu-info)

# Service Tab
service=[]
# initialization
sshStatus = 'offline'
telnetStatus = 'offline'
webStatus = 'offline'
oracleStatus = 'offline'
mysqlStatus = 'offline'
rdpStatus = 'offline'

# if service port exists, service status changes
for item in systemInfo.getListenPort():
	if item == '21':
		sshStatus = 'online'
	elif item == '22':
      		telnetStatus = 'online'
	elif item == '80':
      		webStatus = 'online'
	elif item == '1521':
      		oracleStatus = 'online'
	elif item == '3306':
      		mysqlStatus = 'online'
	elif item == '3389':
      		rdpStatus = 'online'

service.append( {'status' : sshStatus, 'name' : 'SSH', 'port' : '21' } )
service.append( {'status' : telnetStatus, 'name' : 'telnet', 'port' : '22' } )
service.append( {'status' : webStatus, 'name' : 'WEB', 'port' : '80' } )
service.append( {'status' : oracleStatus, 'name' : 'Oracle', 'port' : '1521' } )
service.append( {'status' : mysqlStatus, 'name' : 'MySql', 'port' : '3306' } )
service.append( {'status' : rdpStatus, 'name' : 'RDP', 'port' : '3389' } )
serviceMap = {'service':service}
superMap.update(serviceMap)

superMap.update({'swap': systemInfo.getSwapInfo()})

sysInfo = {'OSVersion':systemInfo.getOSVersion(), 'Kernel':systemInfo.getKernel(), 'Hostname':systemInfo.getHostname(), 'Uptime' : systemInfo.getUptime(), 'LastBoot' : systemInfo.getLastBoot(), 'Date' : ' '.join(systemInfo.getDate()), 'CurrentUser' : systemInfo.getCurrentUser()}
sysInfoMap = {'sysInfo':sysInfo}
superMap.update(sysInfoMap)


# lastlog
lastLog=[]

for item in systemInfo.getLastLogin().items():
    lastLog.append({'hostId':item[0], 'Date':item[1]})

lastLogMap = {'lastLog':lastLog}
superMap.update(lastLogMap)

#
#DISKINFORMATION_TABLE
disklist = []
for item in systemInfo.getDiskInformation():
	disklist.append( {'filesystem':item[0],'mount':item[5],'use':item[4],'avail':item[3],'used':item[2],'size':item[1]} )
	
diskMap = {'diskUsage':disklist}
superMap.update(diskMap)


#Ping 
pingData=[]
for item in systemInfo.getPing().items():
        pingData.append( {'host' : item[0], 'time' : item[1] } )
pingMap = {'ping':pingData}
superMap.update(pingMap)

#memdata
memdata = systemInfo.getMemInfo()
dic = {'memUsage':memdata}
superMap.update(dic) 

#network
networkLog=[]
networkLogMap = {'networkLog' : systemInfo.getNetwork()}
superMap.update(networkLogMap)

#CPU INFO
cpuInfo=[]
cpuInfoMap = {'cpuInfo':systemInfo.getCpuInfo()}
superMap.update(cpuInfoMap)

f=open("/home/nijin39/DEV/pythonedu/sysinfo/system.data","wb")
pickle.dump( superMap ,f)
f.close()
