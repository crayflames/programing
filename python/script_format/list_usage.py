#! /usr/bin/env python3
# -*- coding: utf8 -*-
import os
import multiprocessing
os.system('modprobe pktgen')
coreNum=multiprocessing.cpu_count()
kpklist=[]
for i in range(coreNum) : 
	if os.path.exists('/proc/net/pktgen/kpktgend_'+str(i)) :
		kpklist.append('/proc/net/pktgen/kpktgend_'+str(i))
print(kpklist)
for i in kpklist:
	print(i)
#remove
kpklist.remove('/proc/net/pktgen/kpktgend_0')
print ('remove ')
print(kpklist)
#append
kpklist.append('/proc/net/pktgen/kpktgend_0')
print('append ')
print(kpklist)
#count
s=kpklist.count('/proc/net/pktgen/kpktgend_0')
print('count '+str(s))
kpklist.sort()
#sort
print(kpklist)
#反向
kpklist.reverse()
print(kpklist)
#加入另一個清單字典
dst={'a1':'1','b1':'2'}
lslist=('a','b','c')
kpklist.extend(lslist)
kpklist.extend(dst.keys())
print(kpklist)
print(kpklist[1])
#Reading a file and save to list.
i=open('/home/roger/Desktop/test.log','r')
#讀取檔案篩選eth0的行
for line in i:
	if "eth0" in line:
		#行切割後
		for e in line.strip().split('\n'):
			#再切割欄位
			a.append(e.split())
for i in range(len(a)):
	#取第三欄
	ap.append(a[i][2])