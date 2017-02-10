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

dev={'srcDev':'','dstDev':'','testCNT':'15000','testMTU':'1500'}

dstresult=0
bilateral=0
coreNum=multiprocessing.cpu_count()
kpklist=[]
for i in range(coreNum) : 
	if os.path.exists('/proc/net/pktgen/kpktgend_'+str(i)) :
		kpklist.append('/proc/net/pktgen/kpktgend_'+str(i))
a=0
PGDEV = kpklist[a]


class nwchk:
	def __init__(self,a):
		self.devChk(a)
		self.devLink(a)
	def devChk(self , a):
		#確認裝置是否存在
		if not os.path.exists("/sys/class/net/" + str(a)):
			print ( a + " is not exist")
			sys.exit(2)

	def devLink(self, a):
		#print 裝置狀態
		s=open('/sys/class/net/' + str(a) + '/operstate').readline().strip()
		#print 出連線狀態
		if not s == 'up':
			print ( a + ' is link unknow' )
			sys.exit(2)

	def devMac(self, a):
		#2/8比對輸入的格式需符合macaddress的格式 [英文數字][英文數字]:[英文數字][英文數字]		
		m = re.match(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',a)
		if m:
			dev['dstMac']=a
		else:
			self.devChk(a)
			global dstresult
			#2/8判斷目標port 是否為本機的，是的話 dstresult 為1			
			dstresult=1
			dev['dstMac']=open('/sys/class/net/' + a + '/address').readline().strip()

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

def TestResult(a,b):
	strTime=subprocess.getoutput("cat /proc/net/pktgen/" + a + "| grep Result | awk '{print $3}' | awk -F '(' '{ print $1/1000000 }'")
	totTras=subprocess.getoutput("cat /sys/class/net/" + a + "/statistics/tx_bytes | awk '{print $1/1024/1024}'")
	totCount=subprocess.getoutput("cat /proc/net/pktgen/" + a + "| grep sofar | awk '{print $2}'")
	perMB=subprocess.getoutput("cat /proc/net/pktgen/" + a + "| grep Mb/sec | awk '{print $2}'")
	print ("Test Result :")
	print ("Total running time\t: " + str(strTime) + " secs")
	print ("Performance\t\t: " + str(perMB) + " MB")
	print ("Packet size\t\t: " + str(dev['testMTU']))
	print ("Parameter Count\t\t: " + str(dev['testCNT']) )
	print ("Total transfer count\t: " + str(totCount) )
	print ("Total transfer MB\t: " + str(totTras) + "MB")
	print ('=== Error Check ' + dev['srcDev'] + '===')
	subprocess.call(['ethtool', '-S', dev['srcDev']])
	global dstresult
	if dstresult == 1:
		#2/8判斷目標port 是否為本機的，是的話 dstresult 為1，在最後輸出目標port的errorcheck
		print ('=== Error Check ' + dev['dstDev'] + '===')
		subprocess.call(['ethtool', '-S', dev['dstDev']])

def pgset(a):
	global PGDEV
	cmd='echo "' + a + '"'+' > ' + PGDEV
	os.system(cmd)
	result='cat' + PGDEV + '| fgrep "Result: OK:"'
	if not result.strip():
		os.system("cat " + PGDEV + "| fgrep Result")

def pg(a):
	global PGDEV
	os.system("print inject > " + PGDEV)
	print (PGDEV)

def adddev():
	pgset ('add_device ' + dev['srcDev'] )
	pgset ("max_before_softirq 1000000")

def addconfig():
	pgset ('clone_skb 1000000')
	pgset ('pkt_size ' + dev['testMTU'])
	print ("Configuring devices " + dev['srcDev'])
	pgset ('dst_mac ' + dev['dstMac'] )
	print ("Src port " + dev['srcDev'] + "--> Dst port: dstDev Mac: " + dev['dstMac'])
	pgset ("count " + dev['testCNT'])
	pgset ("delay 0")

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hs:d:c:m:D")
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit(2)
		elif opt in ("-s", "--sourcedev"):
			dev['srcDev']  = arg
		elif opt in ("-d", "--destination"):
			dev['dstDev'] = arg
		elif opt in ("-c", "--count"):
			dev['testCNT'] = arg
		elif opt in ("-m", "--mtu"):
			dev['testMTU'] = arg
		elif opt in ("-b", "--bilateral"):
			global
			bilateral=1

	for _ in dev:
		if not dev.get(_):
			print(_ + "is not set")
			sys.exit(2)
	
	s=nwchk(dev['srcDev'])
	s.devMac(dev['dstDev'])

	cmdRt=os.system('lsmod | grep pktgen')
	print (cmdRt)
	if cmdRt == 0 :
		pass
	else:
		cmd='modprobe pktgen'
		cmdRt=os.system(cmd)
		if cmdRt == 0 :
			pass
		else:
			print ('pktgen not loaded')

	print ("Adding devices to run.")
	pgset ("rem_device_all")
	adddev()

	## Configure the individual devices
	global PGDEV
	PGDEV="/proc/net/pktgen/" + dev['srcDev']
	addcconfig()

	PGDEV='/proc/net/pktgen/pgctrl'

	print ("Running... ctrl^C to stop")
	pgset ("start")
	print ("Done")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	main(sys.argv[1:])
	TestResult(dev['srcDev'],dev['dstDev'])
