#! /usr/bin/env python3
# -*- coding: utf8 -*-
#modify 1024
import sys
import subprocess
from time import strftime , localtime
import os

tstItem={'CPU':'','MEM':'','HDD':'0','tstTime':'60','OCP':'0'}
Mem=subprocess.getoutput("cat /proc/meminfo | grep MemAvailable | awk '{print $2/1024*0.85}'")
Cpu=subprocess.getoutput('nproc')
tTime=strftime("%Y%m%d%H%M",localtime())

def usage():
	print( "Generate System full loading via $0 [FULL | CPU | MEM ] [Time :default is 60 secs if not set]")
	print ("./Stressapptest.py FULL 3600")
	print ("./Stressapptest.py CPU 3600")
	print ("./Stressapptest.py MEM 3600")
def chkOCP():
	OCPdev=[]
	ethlist=os.listdir('/sys/class/net')
	for _ in ethlist:
		cmdRt=subprocess.getoutput('cat /sys/class/net/' + str(_) + '/operstate')   
		if cmdRt=='up':
			if re.findall('br',_):
				break
			#if not ['br0','br1','br2']:
			OCPdev.append(a)
	if not len(OCPdev) == 2 :
		print("OCP is no link. Test is not Available. ")
		kpTest=input("Keep testing without OCP? [y/n]: ")
		if kpTest in ['y','Y','Yes','YES']:
			print("Keep test... start stressapptest")
			tstItem['OCP']=0
		else:
			sys.exit(2)

def chkHDD():
	cmdRt=subprocess.call('which fio',shell=True)
	if cmdRt==0:
		subprocess.getoutput('fio -v')
	else:
		subprocess.call('rpm -ivh librdmacm1-1.0.19.1-4.3.1.aarch64.rpm',shell=True)
		subprocess.call('rpm -ivh fio-2.2.8-2.el7.aarch64.rpm',shell=True)
	if os.path.exists('/dev/nvme0n1'):
		print("*"*30)
		print("Fio NVMe test ...at backgound")
		print("*"*30)
		subprocess.call('nohup fio --direct=1 --iodepth=160 --thread -rw=rw --rwmixread=50 --ioengine=libaio --bs=4k --time_based --numjobs=60 --runtime='+ tstItem['tstTime'] +' --group_reporting --name=nvme1 --filename=/dev/nvme0n1 --output='+ fiolog + '&',shell=True)
	else:
		print("NVMe is not exist. ")
		print("Check SAS HBA 9400-8e")
		cmdRt=subprocess.call("lsscsi | grep 'LSI'")
		if cmdRt == 0:
			HDDlist=subprocess.call("lsscsi | grep 'SEAGATE'")
			print("*"*30)
			print("Fio HDD test ...at backgound")
			print("*"*30) #SAS command not correct.
			subprocess.call('nohup fio --direct=1 --iodepth=160 --thread -rw=rw --rwmixread=50 --ioengine=libaio --bs=4k --time_based --numjobs=60 --runtime='+ tstItem['tstTime'] +' --group_reporting --name=nvme1 --filename=/dev/nvme0n1 --output='+ fiolog + '&',shell=True)
		else:
			kpTest=input("Keep testing without SAS? [y/n]: ")
			if kpTest in ['y','Y','Yes','YES']:
				print("Keep going... ")
				tstItem['HDD']=0
			else:
				sys.exit(2)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
		sys.exit(2)
	if sys.argv[1] == 'FULL':
		tstItem['CPU']=1
		tstItem['MEM']=1
		tstItem['HDD']=0
		tstItem['OCP']=0
		log='stressapptest_FULL_' + tTime + '.log'
		fiolog='fio_HDD_' + tTime + '.log'
		OCPlog='pktgen_OCP_' + tTime + '.log'
	elif sys.argv[1] == 'CPU':
		tstItem['CPU']=1
		log='stressapptest_CPU_' + tTime + '.log'
	elif sys.argv[1] == 'MEM':
		tstItem['MEM']=1
		log='stressapptest_MEM_' + tTime + '.log'
	
	if tstItem['CPU']==1:
		tstItem['CPU']='-C ' + str(Cpu)
	if tstItem['MEM']==1:
		tstItem['MEM']='-M ' + str(Mem)

	tstItem['tstTime']=sys.argv[2]
	print('Check Devices...')

	if tstItem['HDD'] == 1:
		chkHDD()
	if tstItem['OCP'] == 1:
		chkOCP()
		pktTime=int(tstItem['tstTime'])*1000000
		print("*"*30)
		print("Pktgen OCP test start...at backgound")
		print("*"*30)	
		subprocess.call('python3 pkt3generater.py -s ' + OCPdev[0] + ' -d ' + OCPdev[1] + ' -c ' + str(pktTime) + ' -b -E > '+ OCPlog + ' &',shell=True)

	print("***************************")
	print("Start test stressapptest...")
	print("***************************")
	cmd='./stressapptest '+ tstItem['CPU'] + ' ' + tstItem['MEM'] + ' -m ' + str(Cpu) + ' -i '+ str(Cpu) + ' -s '+ tstItem['tstTime'] + ' -l '+ os.getcwd() + '/' + log

	cmdRt=subprocess.call(cmd ,shell=True)
	if cmdRt == 0:
		print('stressapptest log path at ' + os.getcwd() + '/' + log)
	if tstItem['NVMe']==1:
		print('fio test log path at '+ os.getcwd() + '/' + fiolog  )
