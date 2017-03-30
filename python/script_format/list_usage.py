#! /usr/bin/env python3
# -*- coding: utf8 -*-
import os
import multiprocessing
coreNum=multiprocessing.cpu_count()
kpklist=[]
for i in range(coreNum) : 
	if os.path.exists('/proc/net/pktgen/kpktgend_'+str(i)) :
		kpklist.append('/proc/net/pktgen/kpktgend_'+str(i))
print(kpklist)
PGDEV = kpklist[2]
print(PGDEV)
for i in kpklist:
	print(i)