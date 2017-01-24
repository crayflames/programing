#! /usr/bin/env python3
## pktgen.conf -- configuration for send on devices
import os
import sys
import getopt
import subprocess

tx_aborted_err=0
tx_carrier_err=0
tx_err=0
rx_crc_err=0
rx_err=0
rx_frame_err=0
rx_length_err=0
rx_missed_err=0
rx_over_err=0

class nwchk:
	#def __init__(self, a):
	#	self.devChk(a)
	#	self.devLink(a)
	def devChk(self , a):
		if not os.path.exists("/sys/class/net/" + a)
			print ( a + " is not exist")
			sys.exit(2)
		s=subprocess.getoutput("cat /sys/class/net/" + a + "/operstate")
		if s == 'up':
			print ( a + ' is link up' )
		else:
			print ( a + ' is link unknow' )
			sys.exit(2)
	def devList():
		os.system("ifconfig -a | grep ether")

def usage():
#print "Function: port to port || mac to mac. "
#print "          Counter by User setting. "
	print "Please follow format to stress Ethernet device"
	print "such as : "
	print "  Host port to port"
	print 'pktgen_mod.py -s eth0 -d eth1 -c 15000 -m 1500'
	print "  [Count] setting as 0 is inifinit loop"
	print "MTU 1500 : 1 count eq 4.4kb"
	print "MTU 9014 : 1 count eq 8.8kb"
	DevSrc=os.system("ifconfig -a | grep ether | awk '{print $1}'")
	print $DevSrc > DEV.file
	DevList=$(cat DEV.file | awk '{print $1 " " $2}')
	print "  On this OS you can type format as below"
	print "          Port to Port    ./pktgen.sh -P $DevList"
	rm -f DEV.file
	sys.exit(1)


def TestResult(a):
	#rx_package_end=$(cat /sys/class/net/$dstDev/statistics/rx_bytes)
	#rx_package_rsl=$(( $rx_package_end - $rx_package_org ))
	strTime=os.system("cat /proc/net/pktgen/" + a + "| grep Result | awk '{print $3}' | awk -F '(' '{ print $1/1000000 }'")
	totTras=os.system("cat /sys/class/net/" + a + "/statistics/tx_bytes | awk '{print $1/1024/1024}'")
	#totRecv=$(cat /sys/class/net/$dstDev/statistics/rx_bytes | awk '{print $1/1024/1024}')
	totCount=os.system("cat /proc/net/pktgen/" + a + "| grep sofar | awk '{print $2}'")
	perMB=os.system("cat /proc/net/pktgen/" + a + "| grep Mb/sec | awk '{print $2}'")
	tx_aborted_err=os.system("cat /sys/class/net/" + a + "/statistics/tx_aborted_errors")
	tx_carrier_err=os.system("cat /sys/class/net/" + a + "/statistics/tx_carrier_errors")
	tx_err=os.system("cat /sys/class/net/" + a + "/statistics/tx_errors")
	#rx_crc_err=$(cat /sys/class/net/$dstDev/statistics/rx_crc_errors)
	##rx_err=$(cat /sys/class/net/$dstDev/statistics/rx_errors)
	#rx_frame_err=$(cat /sys/class/net/$dstDev/statistics/rx_frame_errors)
	#rx_length_err=$(cat /sys/class/net/$dstDev/statistics/rx_length_errors)
	#rx_missed_err=$(cat /sys/class/net/$dstDev/statistics/rx_missed_errors)
	#rx_over_err=$(cat /sys/class/net/$dstDev/statistics/rx_over_errors)

	print "Test Result :"
	print "Total running time        : " + strTime + "secs"
	print "Performance               : " + perMB + "MB"
	print "packet size               : " + pktSize
	print "Parameter Count	   	  : " + testCNT
	print "Total transfer count      : " + totCount
	print "Total transfer MB 	  : " + totTras + "MB"
	#print "Total receive count       : $rx_package_rsl"
	#print "Total receive MB  : $totRecv"
	print "tx_aborted_err            : " + tx_aborted_err
	print "tx_carrier_err            : " + tx_carrier_err
	print "tx_err                    : " + tx_err
	#print "rx_crc_err                : $rx_crc_err"
	#print "rx_err                    : $rx_err"
	#print "rx_frame_err              : $rx_frame_err"
	#print "rx_length_err             : $rx_length_err"
	#print "rx_missed_err             : $rx_missed_err"
	#print "rx_over_err               : $rx_over_err"


#Paramter check if null then exit
#[ $ -le 0 ] && usage && exit 1

def pgset():
    local result

    print $1 > $PGDEV

    result=`cat $PGDEV | fgrep "Result: OK:"`
    if "$result" = "":
         cat $PGDEV | fgrep Result:

def pg():
    print inject > $PGDEV
    cat $PGDEV


#Check pktgen module 

def p2p():
	devArray=($@)
	i=0
	for paraMeter in ${devArray[@]}
		(( i++ ))
		modPara=$(( $i%2 ))
		#Last of parameter is count
		[ $paraMeter == ${devArray[$#-1]} ] && [ $modPara == 1 ] && setCnt $paraMeter
		#Judge parameter is src or dst
		if [ $modPara == 1 ]; then
			srcDev=$paraMeter
			LinkExist $srcDev
		else:
			dstDev=$paraMeter
			LinkExist $dstDev

##Check target device shoule be  exist, Need update more device to 2way stress
if [ -z $dstDev ]:
	print dstDev
	print "Please setup Target Device or Test Counter"
	usage()
	sys.exit(1)
else
	dstMac=os.system(cat /sys/class/net/$dstDev/address)

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hs:d:c:m:")
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
        usage()
        sys.exit()
      elif opt in ("-s", "--sourcedev"):
		srcDev = arg
      elif opt in ("-d", "--destination"):
		dstDev = arg
      elif opt in ("-c", "--count"):
      	testCNT = arg
      elif opt in ("-m", "--mtu"):
      	testMTU = arg

if __name__ == "__main__":
	if len(sys.argv) < 1:
		usage()
	main(sys.argv[1:])
s=nwchk()
s.devChk(srcDev)
s.devChk(dstDev)
cmdRt=os.system(lsmod | grep pktgen)
if cmdRt == 1 :
	cmd='modprobe pktgen'
	os.system(cmd)

testCNT=${tstCnt:-15000}
print "Adding devices to run". 
pktSize=testMTU
PGDEV=/proc/net/pktgen/kpktgend_0
pgset "rem_device_all"
pgset "add_device " + srcDev
pgset "max_before_softirq 1000000"

## Configure the individual devices
cmd = "PGDEV=/proc/net/pktgen/" + srcDev
os.system(cmd)
cmd = "pgset 'clone_skb 1000000'"
os.system(cmd)
cmd = "pgset 'pkt_size '" + pktSize
os.system(cmd)
#pgset "min_pkt_size 60"
#pgset "max_pkt_size 1500"

print "Configuring devices $srcDev"
pgset "dst_mac $dstMac"
print "Src port $srcDev --> Dst port: $dstDev Mac: $dstMac"
pgset "count $testCNT"
pgset "delay 0"


PGDEV=/proc/net/pktgen/pgctrl

print "Running... ctrl^C to stop"
pgset "start" 
print "Done"

TestResult(srcDev) 
