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

#cpu
#cpu-info ={'cpumodel':systemInfo.getcpumodel(), 'cpuspeed':systemInfo.getCpuSpped}
#superMap.update(cpu-info)


f=open("system.data","wb")
pickle.dump( superMap ,f)
f.close()
