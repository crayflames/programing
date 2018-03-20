#! /usr/bin/env python3
# -*- coding: utf8 -*-
## pktgen.conf -- configuration for send on devices
## Modified 07/14
import os
import sys
import getopt
import subprocess
import re
import time
res=[]
dev={'testCNT':'15000','testMTU':'1500','bilateral':'0'}
err={'errchk':'0','dstresult':'0'}
coreNum=subprocess.getoutput('nproc')
setSrcCount=0
setDstCount=0
devSRC={}
devDST={}
tTime=time.strftime("%Y%m%d%H%M",time.localtime())
logFile='pktgen_'+ tTime +'.log'
if os.path.exists(logFile):
	os.remove(logFile)
def SRClist(a):
	global setSrcCount
	setSrcCount+=1
	devSRC['src'+str(setSrcCount)]=a

def DSTlist(a):
	global setDstCount
	setDstCount+=1
	devDST['dst'+str(setDstCount)]=a

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
			err['dstresult']=1
			dev['dstMac']=open('/sys/class/net/' + a + '/address').readline().strip()
	def setMTU(self,a):
		if not setmtu == '1500': 
			cmd='ifconfig ' + a + ' mtu ' + dev['testMTU']
			subprocess.call(cmd,shell=True)
		else:
			cmd='ifconfig ' + a + ' mtu ' + dev['testMTU']
			subprocess.call(cmd,shell=True)	

def logwrite(a):
	global tTime
	global logFile
	pktRs=open(logFile,'a+')
	pktRs.write( a + '\n')
	pktRs.close()

def TestResult():
	for i in res:
		if os.path.exists('/proc/net/pktgen/'+ i):
			if res.count(i) > 1:
				res.remove(i)
			logwrite("=== " + i + " ===")
			strTime=subprocess.getoutput("cat /proc/net/pktgen/" + i + "| grep Result | awk '{print $3}' | awk -F '(' '{ print $1/1000000 }'")
			totTras=subprocess.getoutput("cat /sys/class/net/" + i + "/statistics/tx_bytes | awk '{print $1/1024/1024}'")
			totCount=subprocess.getoutput("cat /proc/net/pktgen/" + i + "| grep sofar | awk '{print $2}'")
			perMB=subprocess.getoutput("cat /proc/net/pktgen/" + i + "| grep Mb/sec | awk '{print $2}'")
			logwrite("Test Result :")
			logwrite("Total running time\t: " + str(strTime) + " secs")
			logwrite("Performance\t\t: " + str(perMB) + " MB")
			logwrite("Packet size\t\t: " + str(dev['testMTU']))
			logwrite("Parameter Count\t\t: " + str(dev['testCNT']) )
			logwrite("Total transfer count\t: " + str(totCount) )
			logwrite("Total transfer MB\t: "+ str(totTras) + "MB")
		if err['errchk'] == 1:
			logwrite('=== Error Check ' + i + ' ===')
			logwrite(subprocess.getoutput('ethtool -S '+ i +'| grep err'))
	for _ in open('pktgen_'+ tTime +'.log','r',encoding='UTF-8'):
		print(_,end='')

def pgset(a):
	global PGDEV
	cmd='echo "' + a + '"'+' > ' + PGDEV
	subprocess.call(cmd,shell='True')
	result='cat' + PGDEV + '| fgrep "Result: OK:"'
	if not result.strip():
		subprocess.call("cat " + PGDEV + "| fgrep Result",shell="True")

def pg(a):
	global PGDEV
	subprocess.call("print inject > " + PGDEV,shell='True')
	print (PGDEV)

def adddev():
	pgset ('add_device ' + devSRC['src'+str(setSrcCount)] )
	pgset ("max_before_softirq 1000000")

def addconfig():
	pgset ('clone_skb 1000000')
	pgset ('pkt_size ' + dev['testMTU'])
	print ("Configuring devices " + devSRC['src'+str(setSrcCount)])
	pgset ('dst_mac ' + dev['dstMac'] )
	print ("Src port " + devSRC['src'+str(setSrcCount)] + "--> Dst port: dstDev Mac: " + dev['dstMac'])
	pgset ("count " + dev['testCNT'])
	pgset ("delay 0")

def usage():
	print ("Usage: \n \
	\t Network package generater for Python3 \n \
	\t How to use : \n \
	\t such as : \n \
	\t Host port to port \n \
	\t ./pkt3generater.py -s eth0 -d eth1 -c [count]] -b\n \
	\t Host port to MAC \n \
	\t ./pkt3generater.py -s eth0 -d 00:00:00:00:00:00 -c 15000 -m 1500 \n \
	\t -s : source port \n \
	\t -d : destination port \n \
	\t -c : count [Count] setting as 0 is inifinit loop \n \
	\t -m : MTU size \n \
	\t -b : test two-way \n \
	\t -E : Test finish with error check \n \
	\t MTU 1500 : 1 count eq 4.4kb \n \
	\t MTU 9014 : 1 count eq 8.8kb")
	sys.exit(1)

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hs:d:c:m:bE")
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit(2)
		elif opt in ("-s", "--sourcedev"):
			SRClist(arg)
		elif opt in ("-d", "--destination"):
			DSTlist(arg)
		elif opt in ("-c", "--count"):
			dev['testCNT'] = arg
		elif opt in ("-m", "--mtu"):
			dev['testMTU'] = arg
		elif opt in ("-b", "--bilateral"):
			dev['bilateral'] = 1
		elif opt in ("-E", "--errchk"):
			err['errchk'] = 1

	for _ in dev:
		if not dev.get(_):
			print(_ + "is not set")
			sys.exit(2)
	global setSrcCount
	global setDstCount
	pgset ("rem_device_all")
	print ("Adding devices to run.")
	s=nwchk(devSRC['src'+str(setSrcCount)])
	subprocess.call('ethtool -G ' + devSRC['src'+str(setSrcCount)] + ' tx 1024',shell=True)
	s.devMac(devDST['dst'+str(setDstCount)])
	s.setMTU(dev['testMTU'])
	adddev()
	
	## Configure the individual devices
	global PGDEV
	PGDEV="/proc/net/pktgen/" + devSRC['src'+str(setSrcCount)]
	addconfig()
	res.append(devSRC['src'+str(setSrcCount)])
	#change device for test two-way
	#5/28
	if dev['bilateral'] == 1:
		srcBil=devSRC['src'+str(setSrcCount)]
		dstBil=devDST['dst'+str(setDstCount)]
		setDstCount+=1
		setSrcCount+=1
		devDST['dst'+str(setDstCount)]=srcBil
		devSRC['src'+str(setSrcCount)]=dstBil
		global a
		a+=1
		PGDEV = kpklist[a]
		s=nwchk(devSRC['src'+str(setSrcCount)])
		subprocess.call('ethtool -G ' + devSRC['src'+str(setSrcCount)] + ' tx 1024')
		s.devMac(devDST['dst'+str(setDstCount)])
		adddev()
		PGDEV="/proc/net/pktgen/" + devSRC['src'+str(setSrcCount)]
		addconfig()
		res.append(devSRC['src'+str(setSrcCount)])

	PGDEV='/proc/net/pktgen/pgctrl'

	print ("Running... ctrl^C to stop")
	pgset ("start")
	print ("Done")
	s.setMTU('1500')

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	cmdRt=subprocess.call('lsmod | grep pktgen > /dev/null 2>&1',shell='True')
	if cmdRt == 0 :
		cmdRt=subprocess.call('rmmod pktgen > /dev/null 2>&1',shell='True')
	cmdRt=subprocess.call('modprobe pktgen > /dev/null 2>&1',shell='True')
	if cmdRt == 0 :
		pass
	else:
		print ('pktgen not implentment')
	kpklist=[]
	for i in range(int(coreNum)) : 
		if os.path.exists('/proc/net/pktgen/kpktgend_'+str(i)) :
			kpklist.append('/proc/net/pktgen/kpktgend_'+str(i))
	a=0
	PGDEV = kpklist[a]
	main(sys.argv[1:])
	TestResult()
