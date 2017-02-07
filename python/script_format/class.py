#!/usr/bin/python3
import os
import subprocess
class nwchk:
	#def __init__(self, a):
		#pass
	#	self.devChk(a)
	#	self.devLink(a)
	def devChk(self , a):
		print (a)
		os.system("cat /sys/class/net/" + a + "/statistics/tx_bytes")

	def devLink(self, a ):
		s=subprocess.getoutput("cat /sys/class/net/" + a + "/operstate")
		if s == 'up':
			print ( a + ' is link up' )
		else:
			print ( a + ' is link unknow' )

if __name__ == '__main__':
	dev = nwchk()
	#dev.devChk('enp0s25')
	dev.devChk('enp0s25')
