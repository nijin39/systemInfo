# -*- coding:utf-8 -*-

import commands
import subprocess
from subprocess import Popen,PIPE


def getHostname():
    '''get System Hostname'''
    return commands.getstatusoutput('cat /etc/hostname')[1]
 
def getKernel():
    '''get System Kernel Version'''
    return commands.getstatusoutput('uname -r')[1]

def getOSVersion():
    CMDOUTPUTCOLUMN = 1
        # 튜플 실행 결과 (0, 'No LSB modules are available.\nDistributor ID:\tLinuxMint\nDescription:\tLinux Mint 17.3 Rosa\nRelease:\t17.3\nCodename:\trosa')
        # 01. 두번째 행 얻기 
        # 02. 개행문자 기준으로 문자열 자르기
    cmdResult = commands.getstatusoutput("lsb_release -a")[CMDOUTPUTCOLUMN].split('\n') 
    for cmdResultLine in cmdResult:
                # 03. 정보가 포함된  찾기
        if cmdResultLine.find("Description") != -1:
            #04. OS 정보가 포함된 열을 얻기 위해 탭을 기준으로 문자열 가르고 두번째 열을 반환한다. 
	      # Description:\tLinux Mint 17.3 Rosa\n
            return cmdResultLine.split('\t')[1]

def getLastBoot():
    ''' last boot 년-월-일 시:분 형태로 출력한다. '''
    popen = subprocess.Popen('last boot', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()

    # 스페이스를 기준으로 문자열을 나누어준 뒤, 저장한다.
    # 월 데이터의 경우, 문자열에 해당하는 숫자 String값을 넣어준다.
    newStr = stdoutdata.split()
    
    year = newStr[-1]
    
    # 영어로 표시된 월 데이터를 숫자로 표시해주기 위해 사전을 사용한다.
    monthDic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
             'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    month = monthDic[newStr[-4]]
           
    day = newStr[-3]
    
    # 시간 데이터를 :으로 split한 뒤, 시와 분 데이터로 저장한다.
    times = newStr[-2]
    times = times.split(':')
    hour = times[0]
    minute = times[1]
    
    
    result = '{:>4}-{:>2}-{:>2} {:>2}:{:>2}'.format(year,month,day,hour,minute)
    return result

def getCurrentUser():
    '''System Information part
       Get current user count and id '''
    
    command = 'who'
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    results = stdoutdata
    
    # Parsing
    userList = results.split('\n')
    
    # initialization
    userCount = 0
    userNames = []
    
    # Current User Counting
    for user in userList:
        if len(user) > 0:
            userCount += 1
            userDetail = user.split(' ')
            userNames.append(userDetail[0])
            
    
    # Return
    dic = {'userCount':userCount,'userNames':userNames}
    return dic

def getNetwork():
    # Execute commands and parsing
    text = commands.getstatusoutput('netstat -ni')
    text = text[1]
    text = text.split("\n")
    
    #put the interface name in the list
    index = 0

    interfaces = []
    for line in text :
        # delete title row
        if index < 2 :
            index += 1
            continue
        
        interfaces.append(line.split()[0])
     
    #create commands with the interface name from the list
    returnVal = []
    for interface in interfaces :
        result = commands.getstatusoutput('/sbin/ifconfig ' + interface)[1]
        result2 = result.split("\n")[1].split(":")[1].split(" ")[0]
        result = result.split("\n")[-2]
        result = result.split("(")
        
        dic = {'interface' : interface, 'ip' : result2, 'receive':result[1].split(")")[0], 'transmit':result[2].split(")")[0]}
        returnVal.append(dic)
    
    return returnVal


def doFree():
    popen = Popen("free",stdout=PIPE,stderr=PIPE,shell=True)
    out,err = popen.communicate()
    return out.split()

def doFreeH():
    popen = Popen("free -h",stdout=PIPE,stderr=PIPE,shell=True)
    out,err = popen.communicate()
    return out.split()

def getMemInfo():
#popen = object for process open
#out, err = result of process
#dic = summary of memory info
#7: total of  mem, 8: used of  mem, 9: free of mem, 10:shared of mem, 11: buffer of mem, 12:cached of mem 
    out = doFree()
    used = float(out[8])
    total = float(out[7])
    if total == 0.0:
        total = 1.0
    out = doFreeH()
    dic = {'total':out[7],'used':out[8],'free':out[9],'use':str(int(used/total*100)) + '%'}
    return dic

def getSwapInfo():
    # popen = object for process open
    # out, err = result of process
    # dic = summary of swap info
    #18: total of wap, 19: used of swap, 20: free of swap
    out = doFree()
    used = float(out[19])
    total = float(out[18])
    if total == 0.0:
        total = 1.0
    out = doFreeH()
    dic = {'total':out[18],'used':out[19],'free':out[20],'use':str(int(used/total*100)) + '%'}
    return dic

def getLastLogin():
    text = commands.getoutput('lastlog')
    #convert string type and split by space and put in to result
    temp =  str(text).split("\n")
    list = []
    dic={}
    del temp[0]
    for line in temp:
        word = str(line).split()
        if not word[1].startswith('**'):
            dic={'hostId': word[0], 'Date':word[3]+' '+word[4]+ ' '+word[5]+' '+word[6]}
            list.append(dic)
    return list

def getCPULoad():
    # Execute commands and parsing
    text = commands.getoutput('uptime').split()
    
    # return values: [1m, 5m, 10m]
    return text[7][:-1],text[8][:-1],text[9]

def getUptime():
	# 02. 결과 값을 , 를 기준으로 나누어 결과값을 출력한다
	sqlResult = commands.getstatusoutput('uptime')
	upTimeResult = sqlResult[1].split(',')
	return upTimeResult[0]

def getDiskInformation():
    '''get System Disk'''
    # Disk 사용량을 string으로 읽어서 info에 저장
    tmpinfo = commands.getoutput('df -Pkh')
 
    # string으로 읽은 데이터를 행단위로  리스트로 쪼개기
    information = tmpinfo.split('\n')[1:]
 
    diskInformation = [[0 for col in range(7)] for row in range(len(information))]
    
    # 열단위로 리스트 쪼갠 뒤 저장
    for count in range(0,len(information)):
        diskInformation[count] = information[count].split()  
    return diskInformation

def getPing():
    pingList = ['www.google.com','www.facebook.com','www.yahoo.com','www.samsung.com']
    result = {}
    for item in pingList:
    	#01. ping결과 중 경과시간에 해당하는 라인만 저장 
    	pingOutput = commands.getoutput('ping -c 1 ' + item + ' | grep rtt')
    
        	#02. =으로 스플릿한 후, /로 스플릿하여 반응속도만 추출 
    	listOfSplitByEq = pingOutput.split(' = ')
        if listOfSplitByEq[0] == '':
            result[item] = '---'
        elif len(listOfSplitByEq) == 1 :
	    result[item] = '---'
        else:
    	    listOfSplitBySlash = listOfSplitByEq[1].strip().split('/')
    
    	#03. min, avg, max 순으로 리스트에 저장 
    	    pingData = listOfSplitBySlash[0:3]
            result[item] = pingData[1]

    return result

def getCpuTime():
    # get Cpu date & time : format "day, month, day, hour, minute, seconds, time slot, year"
    return commands.getstatusoutput('date "+%a %b %d %H:%M:%S %Z %Y"')[1]

def getCpuInfo():
    #01. CPU 정보에 대한 결과 값얻
    text = str(commands.getstatusoutput('cat /proc/cpuinfo')[1])
    #02. 개행문자 기준으로 문자열 자르
    text = text.split("\n")
    #03. 각 줄에 대하여 필요한 모델로 시작하는지 체크
    #04. 필요한 내용은 변수에 저장하
    for line in text:
        if line.rstrip('\n').startswith('model name'):
            model_name = line.rstrip('\n').split(':')[1].strip()
        if line.rstrip('\n').startswith('cpu cores'):
            cores = line.rstrip('\n').split(':')[1].strip()
        if line.rstrip('\n').startswith('cpu MHz'):
            speed = line.rstrip('\n').split(':')[1].strip()
        if line.rstrip('\n').startswith('cache size'):
            cache = line.rstrip('\n').split(':')[1].strip()
        if line.rstrip('\n').startswith('bogomips'):
            bogomips = line.rstrip('\n').split(':')[1].strip()
    #05. 결과값에 사전형으로 내용을 저장 후 리
    results = {"Model": model_name,
          "Cores": cores,
          "Speed": speed + " Mhz",
          "Cache": cache,
          "Bogomips": bogomips}
    
    return results

# remove duplicate values in array
def removeDup(li):
    my_set = set()
    res = []
    for e in li:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    
    return res

def getListenPort():
# read string from netstat command and split to lines
    cmdResult = commands.getoutput('netstat -tupln')
    line = cmdResult.split('\n')
    remDupList = []
    
    # find suitable port numbers
    for word in line:
        if word.find('0.0.0.0:*') > 0:
            index = word.find(':')
            port = (word[index+1 : index+6]).strip()
            if int(port, 10) < 5000:
                remDupList = remDupList +[port]

    # remove duplicate port numbers
    portList = list(removeDup(remDupList))
    return portList

def getDate():
    #get date : form == weekday[0], month[1] day[2] year[3] hh:mm:ss[4] UTC[5]
    Monparse = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    Month = commands.getoutput("date '+%m'")
    ToDay = Monparse[Month] + commands.getoutput("date '+ %_d'")
    return ToDay 

def getErrLogPrev():
	#get syslog contains 'error' keyword at today
	#form == month day hh:mm:ss hostname Message ...
	LogData = commands.getoutput("cat /var/log/syslog | grep '^" + getDate() + "' | grep -ie 'error'")
	return LogData.split('\n')

def getWarnLogPrev():
	#get syslog contains 'warn' keyword at today
	#form == month day hh:mm:ss hostname Message ...
	ToDaySplit = getDate()
	LogData = commands.getoutput("cat /var/log/syslog | grep '^" + getDate() + "' | grep -ie 'warning'")
	return LogData.split('\n')

def getErrLog():
	#get syslog error message split by hostname
	#form == [date , message]
	#and return result dictionary{message : count}
	LogDataSplit = getErrLogPrev()
	result = {}
	if LogDataSplit[0] != '':
		for row in LogDataSplit:
			LogDataMessage = row.split(" " + commands.getoutput("hostname") + " ")
			if LogDataMessage[1] in result:
				result[LogDataMessage[1]] = result[LogDataMessage[1]] + 1
			else:
				result[LogDataMessage[1]] = 1

	return result

def getWarnLog():
	#get syslog warning message split by hostname
	#form == [date , message]
	#and return result dictionary{message : count}
	LogDataSplit = getWarnLogPrev()
	result = {}
	if LogDataSplit[0] != '':
		for row in LogDataSplit:
			LogDataMessage = row.split(" " + commands.getoutput("hostname") + " ")
			if LogDataMessage[1] in result:
				result[LogDataMessage[1]] = result[LogDataMessage[1]] + 1
			else:
				result[LogDataMessage[1]] = 1

	return result
