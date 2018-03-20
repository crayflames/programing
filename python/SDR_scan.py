#!/usr/bin/env python
# -*- coding: utf8 -*-
import commands
import time
import os
#一定時間scan temp
count=1
BMCIP = "171"
logfile = "SDR_" + BMCIP +".log"
if os.path.exists(logfile):
	os.remove(logfile)
while 1 :
	cmd ="ipmi " + BMCIP + " power status | awk '{print $4}'"
	pwrstat=commands.getoutput(cmd)
	if pwrstat=='on':
		f=open(logfile,'a+')
		f.write("===================================\n")
		f.write(str(count) + '\n')
		localtime = time.asctime(time.localtime(time.time()))
		f.write(localtime + '\n')
		time.sleep(5)
		f.write("System SDR status" + '\n')
		cmd ='ipmi ' +BMCIP + ' sdr' + ' | grep _DIMM_ '
		os.system(cmd)
		cmdRt=commands.getoutput(cmd)
		f.write(cmdRt + '\n')
		print (count)
		count=count+1
		f.close()
		time.sleep(30)
