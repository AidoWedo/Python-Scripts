#!/usr/bin/env python
import os,sys,win32serviceutil,time,win32service,re,shutil,random,datetime,time,socket,struct,logging,logging.handlers,_mssql,subprocess
from colorama import init
init()

def lab7():
    # New Lab - Unidentified logs
    print('Starting Lab...')
    #files
    rules = open("C:\\LogRhythm\\labs\\flatfile\\IDS\\CustomIDSlog.txt",'a')
    f = open("C:\\LogRhythm\labs\\flatfile\\rules_challenge_data.txt")
    file = f.read()
    logs = file.split("----------------")
    for log in logs:
        configs = log.split(',,')
        wait = int(configs[0].strip())
        print('wait time: '+str(wait))
        type = configs[1]
        time.sleep(wait)
        message = configs[2].lstrip()
        print ('Log Message: '+message)
        # replace the substitutions
	host = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	print ("Host IP: "+str(host))
	message = message.replace('[host]', host)
	dhost = socket.inet_ntoa(struct.pack('>I',random.randint(1, 0xffffffff)))
	print ("Destination Host IP: "+str(dhost))
	message = message.replace('[dhost]', dhost)
        # replace the time
	# Time format: 9/26/2015 3:30:30 PM
	now = datetime.datetime.now()
	message = message.replace('[time]', now.strftime("%m/%d/%Y %I:%M:%S %p"))
    	if (type == "ACTION"):
	    rules.write(message)
            rules.flush()
    print('')
    print('Lab Complete.')
    time.sleep(10)

 

