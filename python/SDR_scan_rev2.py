#!/usr/bin/env python
# -*- coding: utf8 -*-
import commands
import time
import os
#不斷抓sel，當sel報出問題(Critical)時，去抓sdr的溫度
#針對溫度會過熱的問題
count=1
BMCIP = "171"
logfile = "/home/roger/Desktop/Osmium/log/QIS_verified/SDR_" + BMCIP +".log"
if os.path.exists(logfile):
	os.remove(logfile)
print("Wait for temp issue...")
print("BMC IP: " + BMCIP)
while 1 :
	cmd ="ipmi " + BMCIP + " sel | grep Critical"
	cmdRt=os.system(cmd)
	if cmdRt == 0:
		f=open(logfile,'a+')
		f.write("===================================\n")
		f.write('Loop : '+str(count) + '\n')
		localtime = time.asctime(time.localtime(time.time()))
		print (localtime)
		f.write(localtime + '\n')
		f.write("System SDR status" + '\n')
		cmd ='ipmi ' +BMCIP + ' sdr' + ' | grep _DIMM_'
		os.system(cmd)
		cmdRt=commands.getoutput(cmd)
		f.write(cmdRt + '\n')
		cmdRt=commands.getoutput("ipmi " + BMCIP + " sel")
		f.write(cmdRt + '\n')
		os.system( 'ipmi ' + BMCIP + ' sel clear' )
		print (count)
		count=count+1
		f.write("===================================\n")
		f.close()
