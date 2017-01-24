#!/usr/bin/env python
import commands
import time
import os
count=1
BMCIP = "192.3.1.146"
logfile = "cycle.log"
poweroncount=0
while 1 :
	cmd ="ipmitool -H " + BMCIP + " -U admin -P admin -I lanplus chassis power status | awk '{print $4}'"
	pwrstat=commands.getoutput(cmd)
	if pwrstat=='off':
		f=open(logfile,'a+')
		f.write("===================================\n")
		f.write(str(count) + '\n')
		localtime = time.asctime(time.localtime(time.time()))
		f.write(localtime + '\n')
		f.write(pwrstat + '\n')
		time.sleep(5)
		cmd ='ipmitool -I lanplus -H' +BMCIP + ' -U admin -P admin chassis power on'
		os.system(cmd)
		f.write("Power on system" + '\n')
		print count
		count=count+1
		poweroncount=0
		time.sleep(3)
	else:
		f=open(logfile,'a+')
		print "Power is on " + str(poweroncount)
		f.write("Power is on " + str(poweroncount))
		poweroncount=poweroncount+1
		time.sleep(20)


		
