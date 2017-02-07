#!/usr/bin/python3
import sys
import os
import subprocess
def run(server="client",*args):
	if server=="server":
		print (server)
	elif server=="client":
		print (server)

def devLink(a):
	s=subprocess.getoutput("cat /sys/class/net/" + a + "/operstate")
	if s == 'up':
		print ( a + ' is link up' )
	else:
		print ( a + ' is link unknow' )

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
	tx_err=os.system("cat /sys/class/net/" + a+ "/statistics/tx_errors")
if len(sys.argv) < 1:
	pass
srcDev='enp0s25'
TestResult(srcDev)
run("server")
devLink('enp0s25')