#!/usr/bin/python3
import os
import subprocess
class nwchk():
	def __init__(self, a):
		#pass
		#self.dev = a
		self.devChk(a) # 呼叫nwchk就會執行
		self.devLink(a)# 呼叫nwchk就會執行
	def devChk(self,a):
		print (a)
		os.system("cat /sys/class/net/" + a + "/statistics/tx_bytes")

	def devLink(self,a):
		s=subprocess.getoutput("cat /sys/class/net/" + a + "/operstate")
		if s == 'up':
			print ( a + ' is link up' )
		else:
			print ( a + ' is link unknow' )

'''class nwchk2: 
#這裡也是可以work的
	def __init__(self, a):
		#pass
		self.dev = a #<= 

	def devChk(self,a):
		print (a)
		os.system("cat /sys/class/net/" + a + "/statistics/tx_bytes")

	def devLink(self,a):
		s=subprocess.getoutput("cat /sys/class/net/" + a + "/operstate")
		if s == 'up':
			print ( a + ' is link up' )
		else:
			print ( a + ' is link unknow' )'''
if __name__ == '__main__':
	dev = nwchk('enp0s25')
	#dev.devChk('enp0s25')
	dev.devLink('enp0s25')
