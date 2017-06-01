
#! /usr/bin/env python3
# -*- coding: utf8 -*-
## pktgen.conf -- configuration for send on devices
## Modified 02/8 ver3
import os
import sys
import getopt
import subprocess
import re
import multiprocessing

def usage():
	print ("\t Please follow format to stress Ethernet device \n \
\t such as : \n \
\t Host port to port \n \
\t pktgen_mod.py -s eth0 -d eth1 -c 15000 -m 1500\n \
\t Host port to MAC \n \
\t pktgen_mod.py -s eth0 -d 00:00:00:00:00:00 -c 15000 -m 1500\n \
\t [Count] setting as 0 is inifinit loop \n \
\t MTU 1500 : 1 count eq 4.4kb \n \
\t MTU 9014 : 1 count eq 8.8kb")
	sys.exit(1)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	cmdRt=subprocess.getoutput('lsmod | grep pktgen')
	print (cmdRt)
	if cmdRt == 0 :
		pass
	else:
		cmdRt=subprocess.getoutput('modprobe pktgen')
		if cmdRt == 0 :
			pass
		else:
			print ('pktgen not found')
	main(sys.argv[1:])
	TestResult(dev['srcDev'],dev['dstDev'])