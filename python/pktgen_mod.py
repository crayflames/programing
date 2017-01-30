#! /usr/bin/env python3
# -*- coding: utf8 -*-
## pktgen.conf -- configuration for send on devices
## Modified 01/26 ver1
import os
import sys
import getopt
import subprocess

dev={'srcDev':'','dstDev':'','testCNT':'15000','testMTU':'1500'}
PGDEV = '/proc/net/pktgen/kpktgend_0'
class nwchk:
	def __init__(self,a):
		print (a)
		self.devChk(a)
		self.devLink(a)
	def devChk(self , a):
		#確認裝置是否存在
		if not os.path.exists("/sys/class/net/" + str(a)):
			print ( a + " is not exist")
			sys.exit(2)


	def devLink(self, a):
		#print 裝置狀態
		s=subprocess.getoutput("cat /sys/class/net/" + str(a) + "/operstate")
		#print 出連線狀態
		if not s == 'up':
			print ( a + ' is link unknow' )
			sys.exit(2)
	def devMac(self, a):
		#將輸入的dev 置換成mac 傳回 需搭配 line 133 : 	dev['dstMac']=dev['devmac'] 做切換的動作
		self.devChk(a)		
		dev['devmac']=subprocess.getoutput('cat /sys/class/net/' + a + '/address')
		

	def devList():
		os.system("ip addr | grep ether")

def usage():
	print ("\t Please follow format to stress Ethernet device \n \
\t such as : \n \
\t Host port to port \n \
\t pktgen_mod.py -s eth0 -d eth1 -c 15000 -m 1500\n \
\t [Count] setting as 0 is inifinit loop \n \
\t MTU 1500 : 1 count eq 4.4kb \n \
\t MTU 9014 : 1 count eq 8.8kb")
	sys.exit(1)

def TestResult(a):
	#rx_package_end=$(cat /sys/class/net/$dstDev/statistics/rx_bytes)
	#rx_package_rsl=$(( $rx_package_end - $rx_package_org ))
	strTime=subprocess.getoutput("cat /proc/net/pktgen/" + a + "| grep Result | awk '{print $3}' | awk -F '(' '{ print $1/1000000 }'")
	totTras=subprocess.getoutput("cat /sys/class/net/" + a + "/statistics/tx_bytes | awk '{print $1/1024/1024}'")
	#totRecv=$(cat /sys/class/net/$dstDev/statistics/rx_bytes | awk '{print $1/1024/1024}')
	totCount=subprocess.getoutput("cat /proc/net/pktgen/" + a + "| grep sofar | awk '{print $2}'")
	perMB=subprocess.getoutput("cat /proc/net/pktgen/" + a + "| grep Mb/sec | awk '{print $2}'")
	tx_aborted_err=subprocess.getoutput("cat /sys/class/net/" + a + "/statistics/tx_aborted_errors")
	tx_carrier_err=subprocess.getoutput("cat /sys/class/net/" + a + "/statistics/tx_carrier_errors")
	tx_err=subprocess.getoutput("cat /sys/class/net/" + a + "/statistics/tx_errors")
	#rx_crc_err=$(cat /sys/class/net/$dstDev/statistics/rx_crc_errors)
	##rx_err=$(cat /sys/class/net/$dstDev/statistics/rx_errors)
	#rx_frame_err=$(cat /sys/class/net/$dstDev/statistics/rx_frame_errors)
	#rx_length_err=$(cat /sys/class/net/$dstDev/statistics/rx_length_errors)
	#rx_missed_err=$(cat /sys/class/net/$dstDev/statistics/rx_missed_errors)
	#rx_over_err=$(cat /sys/class/net/$dstDev/statistics/rx_over_errors)

	print ("Test Result :")
	print ("Total running time        : " + str(strTime) + " secs")
	print ("Performance               : " + str(perMB) + " MB")
	print ("packet size               : " + str(dev['testMTU']))
	print ("Parameter Count	   	  : " + str(dev['testCNT']) )
	print ("Total transfer count      : " + str(totCount) )
	print ("Total transfer MB 	  : " + str(totTras) + "MB")
	#print "Total receive count       : $rx_package_rsl"
	#print "Total receive MB  : $totRecv"
	print ("tx_aborted_err            : " + str(tx_aborted_err) )
	print ("tx_carrier_err            : " + str(tx_carrier_err) )
	print ("tx_err                    : " + str(tx_err) )
	#print "rx_crc_err                : $rx_crc_err"
	#print "rx_err                    : $rx_err"
	#print "rx_frame_err              : $rx_frame_err"
	#print "rx_length_err             : $rx_length_err"
	#print "rx_missed_err             : $rx_missed_err"
	#print "rx_over_err               : $rx_over_err"

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

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hs:d:c:m:")
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

	for _ in dev:
		if not dev.get(_):
			print(_ + "is not set")
			sys.exit(2)
	
	s=nwchk(dev['srcDev'])
	s.devMac(dev['dstDev'])
	dev['dstMac']=dev['devmac']

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
	pgset ('add_device ' + dev['srcDev'] )
	pgset ("max_before_softirq 1000000")

	## Configure the individual devices
	global PGDEV
	PGDEV="/proc/net/pktgen/" + dev['srcDev']
	pgset ('clone_skb 1000000')
	pgset ('pkt_size ' + dev['testMTU'])

	#pgset "min_pkt_size 60"
	#pgset "max_pkt_size 1500"

	print ("Configuring devices " + dev['srcDev'])
	pgset ('dst_mac ' + dev['dstMac'] )
	print ("Src port " + dev['srcDev'] + "--> Dst port: dstDev Mac: " + dev['dstMac'])
	pgset ("count " + dev['testCNT'])
	pgset ("delay 0")

	PGDEV='/proc/net/pktgen/pgctrl'

	print ("Running... ctrl^C to stop")
	pgset ("start")
	print ("Done")

	TestResult(dev['srcDev']) 

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	main(sys.argv[1:])
