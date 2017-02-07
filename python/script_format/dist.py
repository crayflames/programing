#! /usr/bin/env python3
import os
def argchk(a):
	if not a.strip():
		print (a + 'is not set')
		sys.exit(2)
	else:
		print (a)
dev={}
dev['src'] = 'test'
dev['dst'] = 2
print(dev)
print(dev['src'])
dev['src'] = 'sdfs'
print(dev['src'])
dev['ano'] = 4
print(dev)
del dev['ano']
print(dev)

for _ in dev:
	argchk(_)
print ('dddd ' + dev['src'])
dev['src']='enp0s25'
dstMac=os.system('cat /sys/class/net/' + dev['src'] + '/address')