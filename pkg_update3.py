#!/usr/bin/env python3
import os
import time
import subprocess
def update_package():
	os.system( pkg + ' update')
        os.system( pkg + ' -y upgrade')
	ud_pkg=['rpm', 
		'make',
		'lsscsi', 
		'sg3-utils', 
		'iperf',
		'ipmitool',
		'sysstat',
		'nfs-common',
		'smartmontools',
		'nvme-cli',
		'stress',
		'fio']
	for i in ud_pkg:
		print ("=== update " + i + " ===")
		cmd = pkg + ' -y install ' + i
                print (cmd)
		os.system(cmd)
		time.sleep(1)
		print ("=== update finish ===")

if __name__ == '__main__':
	cmd = os.system('ping -c 1 8.8.8.8')
	if cmd == 0:
                osDis=subprocess.getoutput('cat /etc/issue').strip('\n').split()[0]
                if osDis == 'Ubuntu':
                        pkg = 'apt'
                else:
                        pkg = 'yum'
        	update_package()
	else:
        	print "Network is not available..."
