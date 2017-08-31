#!/usr/bin/python3
#This block is if not
import os
cmd = '/home/roger/Desktop'

if os.path.exists(cmd + '/test'):
	print("true")

if not os.path.exists(cmd + '/test'):
	# file not exist do this
	print ("not exists")
	#os.mkdir(cmd + '/test')
else:
	print ("not exists")
cmd = "lsmod | grep pktgen"
cmdRt = os.system(cmd)
if not cmdRt:
	print ('module load')
else:
	## output this because module is not load
	print ('module not load')

# this block is if is not:
a=1
b=2
if a is not b:
	print ('same')
else:
	print ('Not same')
