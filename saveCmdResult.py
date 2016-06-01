#!/usr/bin/python

import pickle
import sys
sys.path.append('/home/nijin39/DEV/pythonedu/sysinfo')
import systemInfo

superMap={}

#SYSTEM_INFORMATION_TABLE
hostname = systemInfo.getHostname()
os = systemInfo.getOSVersion()
kernel = systemInfo.getKernel()
uptime = systemInfo.getUptime().lstrip()
lastboot = systemInfo.getLastBoot()
current_user = str(systemInfo.getCurrentUser()['userCount'])
server_time = systemInfo.getCpuTime()
systemData = {'hostname':hostname,'os':os,'kernel':kernel,'uptime':uptime,'lastboot':lastboot,'current-user':current_user,'server-time':server_time}
systemMap = {'sysInfo':systemData}
superMap.update(systemMap) 

#NETWORK_USAGE_TABLE
networkMap = {'networkUsage':systemInfo.getNetwork()}
superMap.update(networkMap)


#LOAD_AVERAGE_TABLE
loadMap = {'cpuLoad': systemInfo.getCPULoad()}
superMap.update(loadMap)

#CPU_INFORMATION_TABLE
cpuInfo = systemInfo.getCpuInfo()
cpuMap = {'cpuInfo':cpuInfo}
superMap.update(cpuMap)

#DISK_USAGE_TABLE
disklist = []
for item in systemInfo.getDiskInformation():
	disklist.append( {'filesystem':item[0],'mount':item[5],'use':item[4],'free':item[3],'used':item[2],'total':item[1]} )
	
diskMap = {'diskUsage':disklist}
superMap.update(diskMap)

#MEMORY_USAGE_TABLE
memdata = systemInfo.getMemInfo()
memMap = {'memUsage':memdata}
superMap.update(memMap)

#SWAP_USAGE_TABLE
swapdata = systemInfo.getSwapInfo()
swapMap = {'swapUsage':swapdata}
superMap.update(swapMap)

#ERROR_LOGS_TABLE
errorLog=[]
for item in systemInfo.getErrLog().items():
	errorLog.append( {'message' : item[0], 'count' : item[1] } )

errorLogMap = {'errorLog':errorLog}
superMap.update(errorLogMap)

#WARNING_LOGS_TABLE
warnLog=[]
for item in systemInfo.getWarnLog().items():
        warnLog.append( {'message' : item[0], 'count' : item[1] } )

warnLogMap = {'warnLog':warnLog}
superMap.update(warnLogMap)

#LAST_LOGIN_TABLE
lastLog=[]

lastLogMap = {'lastLog':systemInfo.getLastLogin()}
superMap.update(lastLogMap)

#PING_STATUS_TABLE
pingData=[]
for item in systemInfo.getPing().items():
        pingData.append( {'host' : item[0], 'time' : item[1] } )

pingMap = {'ping':pingData}
superMap.update(pingMap)

#SERVICE_STATUS_TABLE
service=[]
# initialization
sshStatus = 'OFFLINE'
telnetStatus = 'OFFLINE'
webStatus = 'OFFLINE'
oracleStatus = 'OFFLINE'
mysqlStatus = 'OFFLINE'
rdpStatus = 'OFFLINE'

# if service port exists, service status changes
for item in systemInfo.getListenPort():
	if item == '21':
		sshStatus = 'ONLINE'
	elif item == '22':
      		telnetStatus = 'ONLINE'
	elif item == '80':
      		webStatus = 'ONLINE'
	elif item == '1521':
      		oracleStatus = 'ONLINE'
	elif item == '3306':
      		mysqlStatus = 'ONLINE'
	elif item == '3389':
      		rdpStatus = 'ONLINE'

service.append( {'status' : sshStatus, 'name' : 'SSH', 'port' : '21' } )
service.append( {'status' : telnetStatus, 'name' : 'telnet', 'port' : '22' } )
service.append( {'status' : webStatus, 'name' : 'WEB', 'port' : '80' } )
service.append( {'status' : oracleStatus, 'name' : 'Oracle', 'port' : '1521' } )
service.append( {'status' : mysqlStatus, 'name' : 'MySql', 'port' : '3306' } )
service.append( {'status' : rdpStatus, 'name' : 'RDP', 'port' : '3389' } )
serviceMap = {'service':service}
superMap.update(serviceMap)

#cpu
#cpu-info ={'cpumodel':systemInfo.getcpumodel(), 'cpuspeed':systemInfo.getCpuSpped}
#superMap.update(cpu-info)


f=open("/home/nijin39/DEV/pythonedu/sysinfo/system.data","wb")
pickle.dump( superMap ,f)
f.close()
