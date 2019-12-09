# -*- coding: utf8 -*-
#!/bin/env python
import os
import re
cmd='ls -l /sys/class/enclosure/*/*/device/block/sd*|grep enclosure | awk -F "/" \'{print $6 " " $9}\' |tr -d ":"| sort'

totalDisk=[]
for i in range(108):
	totalDisk.append(i)
#s=subprocess.getoutput(cmd) #Check Disk slot for python3
driveList=os.popen(cmd).read() #Check Disk slot for python2

print("SlotNum"+'\t' + 'Device')
x=driveList.split('\n') #Parse
curDisk=[] #Generate a list for OS current disk saving

for i in x:
	if not i:
		x.remove(i)
	else:
		qq=list(i.split(' '))
		z1=qq[0]
		z2=qq[1]
		print( z1 + ' -> ' + z2 ) #Output DriveList
		zt=re.sub('[a-zA-Z]','',z1) #Parese
		zt1=(int(zt)) #int Disk Number to compare
		curDisk.append(zt1) #Add to list for comparing.

#Comparing Result
s1=set(totalDisk)
s2=set(curDisk)

result=list(s1.difference(s2))
if    result:
	result.sort()
	if len(result)>1:
		disklostNum=' drives'
	else:
		disklostNum=' drive'
	print('===> Warning '+ str(len(result))+ disklostNum +' lost <===')
	for i in result:
		print( 'Slot' + str(i)+' is not exist')
