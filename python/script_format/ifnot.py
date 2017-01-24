#!/usr/bin/python3
import os
cmd = '/home/roger/Desktop'
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