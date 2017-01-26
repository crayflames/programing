#! /usr/bin/env python3
import sys
import os
import getopt
t=100 #if t at heere will be show 'UnboundLocalError: local variable 't' referenced before assignment'
dst=''
src=''
cut=''
def check(a):
  if not a.strip():
  	pass
  else:
    print (a + 'is null')

def main(argv):
	dev={}
	t=100
	try:
		opts, args = getopt.getopt(argv,"hs:d:c:m:")
	except getopt.GetoptError:
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('help')
		elif opt in ("-s", "--sourcedev"):
			global src
			print(t)
			dev['src'] = arg 
			print('t=' , dev['src'])
		elif opt in ("-d", "--destination"):
			global dst #'global' should be used
			dev['dst'] =arg
			print(dev['dst'])
		elif opt in ("-c", "--count"):
			global cut
			dev[ 'cut' ] = arg 
			print(dev['cut'])
		elif opt in ("-m", "--mtu"):
			dev[ 'mnt' ] = arg 
			print(dev['mnt'])
	for _ in dev:
		check(_)
	print ('test')
	print (dev)

if __name__ == "__main__":
	main(sys.argv[1:])
	dstDev='enp0s25'
	cmd = 0
	dstMac=os.system('cat /sys/class/net/' + dstDev + '/address')
	print (dstMac)
 # print (dst)
  #print (cut)
