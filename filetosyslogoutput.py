# Richard Bevan
# Stops a Services AI Engine
# Picks up syslog old file, changes data and time and spits it out as new file
# New File spat out as syslog to 192.168.99.100
#!/usr/bin/env python
import os,sys,win32serviceutil,time,win32service,re,shutil,random,datetime,time,socket,struct,logging,logging.handlers,_mssql,subprocess
from colorama import init
def lab5():
    # Parsing issues causing AIE Spool
    # Open File as F1 and New File as f2
    print('Starting Lab...')
    # Stop AIEENGINE quick way of building up DAT Files as its not processing 
    service = "lraieengine"
    win32serviceutil.StopService(service)
    time.sleep(20)
    f1 = open('C:\\LogRhythm\\labs\\syslog\\syslogold.log', 'r')
    f2 = open('C:\\LogRhythm\\labs\\syslog\\syslognew.log', 'w')
    # Replace date and time in file
    for line in f1:
        f2.write(line.replace('Jun 30 2018 09:00', time.strftime("%b %d %Y %H:%M")))
    # Close Files
    f1.close()
    f2.close()
    time.sleep(10)
    # The syslog stuff
    my_logger = logging.getLogger('LRLogger')
    my_logger.setLevel(logging.INFO)
    handler = logging.handlers.SysLogHandler(address = ('192.168.99.100',514))
    #IP address of LR syslog Listener
    my_logger.addHandler(handler)
    syslogfile = 'C:\\LogRhythm\\labs\\syslog\\syslognew.log'
    with open (syslogfile) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            my_logger.info(line)
            line = fp.readline()
            cnt += 1
    time.sleep(240)
    win32serviceutil.StartService(service)
    print('')
    print('Lab Complete.')
    time.sleep(10)
