#!/bin/env python
# -*- coding: utf8 -*-
import os
import re
import sys

def fio():
	diskList=os.popen('ls /dev/sd*').read()
	diskList=diskList.split('\n')
	while '' in diskList:
		diskList.remove('')
	for _ in diskList:
		_ = re.sub('[0-9]','',_)
		print("filename=" + _ )
	sys.exit(0)
def scan():
	cmd='ls -l /sys/class/enclosure/*/*/device/block/sd*|grep enclosure | awk -F "/" \'{print $6 " " $9}\' |tr -d ":"| sort'

	totalDisk=[]
	for _ in range(108):
		totalDisk.append(_)
	#driveList=subprocess.getoutput(cmd) #Check Disk slot for python3
	driveList=os.popen(cmd).read() #Check Disk slot for python2

	print("SlotNum"+'\t' + 'Device')
	listTemp=driveList.split('\n') 	#Parse
	curDisk=[] 			#Generate a list for OS current disk saving
	
	while '' in listTemp:
		listTemp.remove('')
	for _ in listTemp:
		qq=list(_.split(' '))
		z1=qq[0]
		z2=qq[1]
		print( z1 + ' -> ' + z2 ) 		#Output DriveList
		zt=re.sub('[a-zA-Z]','',z1) 		#Parese
		zt1=(int(zt)) 				#int Disk Number to compare
		curDisk.append(zt1) 			#Add to list for comparing.

	#Comparing Result
	s1=set(totalDisk)
	s2=set(curDisk)

	result=list(s1.difference(s2))
	if result:
		result.sort()
		if len(result)>1:
			disklostNum=' drives'
		else:
			disklostNum=' drive'
		print('===> Warning '+ str(len(result))+ disklostNum +' lost <===')
		for i in result:
			print( 'Slot' + str(i)+' is not exist')
	sys.exit(0)
if __name__ == "__main__":
	if len(sys.argv) < 2:
		scan()
	if sys.argv[1] == 'fio':
		fio()

	
