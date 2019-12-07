# -*- coding: utf8 -*-
#!/usr/local/bin/Python3
import os
import re
import subprocess
cmd='lsscsi'

totalDisk=[]
for i in range(108):
	totalDisk.append(i)
s=subprocess.getoutput(cmd) #Check Disk slot
print("SlotNum"+'\t' + 'Device')
print(s)
x=s.split('\n') #Parse 
curDisk=[] #Generate a list for OS current disk saving
for i in x:
	qq=list(i.split(' '))
	z1=qq[0]
	z2=qq[1]
	zt=re.sub('[a-zA-Z]','',z1) #Parese
	zt1=(int(zt)) #int Disk Number to compare
	curDisk.append(zt1) #Add to list for comparing.

#Comparing Result
s1=set(totalDisk)
s2=set(curDisk)
result=list(s1.difference(s2))
result.sort()
for i in result:
	print( 'Slot' + str(i)+' is not exist')