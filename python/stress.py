#!/usr/bin/python
#-*-coding: utf-8-*-
 
import os
import sys
import time
import commands
import multiprocessing

fio='fio'
fioFolder='fio-2.2.10'
fioFile='fio-2.2.10.tar.gz'
stress='stress'
stressFolder='stress-1.0.4'
stressFile='stress-1.0.4.tar.gz'
testPath=os.path.dirname(__file__)
def run_start():
	tools=[fio,stress]
	for i in tools:
		cmd = 'which ' + i
		cmdRt = os.system(cmd)
		if cmdRt == 0:
			print i + ' is already install.'
		else:
			print ("Start install " + i)
			cmd = 'tar -xzvf ' + i
			os.system(cmd)
			if cmdRt == 0:
				print cmd + " is ok"
			else:
				print cmd + " is error"
				sys.exit(-1)
			if i == fio:
				os.chdir(fioFolder)
			elif i == stress:
				os.chdir(stressFolder)
			cmd = "./configure && make && make install"
			cmdRt = os.system(cmd)
			if cmdRt == 0 :
				print cmd + " is ok"
				os.chdir(testPath)
			else:
				print cmd + " is error"
				sys.exit(-1)				

def run(secs):
	print ('Start run stress')
	coreNum=multiprocessing.cpu_count()
	cmd = 'nohup stress -c ' + str(coreNum) + ' -t ' + str(secs) + ' -m 320 &'
	os.system(cmd)
	cmdRt=os.system(cmd)
	if cmdRt == 0 :
		print (cmd + ' start')
	else:
		print (cmd + ' fail')
	time.sleep(5)
	cmd = "lsscsi | awk '{print $NF}' | sed 1d"
	cmd = commands.getoutput(cmd)
	if not cmd.strip():
		print ('No testable hd found!')
	else:
		diskList = cmd.split('\n')
		for disk in diskList:
			cmd = 'nohup fio --direct=1 --iodepth=16 --cpumask=1 --thread --rw=read --ioengine==libaio --bs=256k --time_based --runtime=' + str(secs) + ' --numjobs=1 --group_reporting --new_group --name=' + disk + ' --filename=' + disk + ' &'
			print (cmd + ' is start')
			cmdRt=os.system(cmd)
	time.sleep(secs)

def run_end():
    '''run the stress end.'''
    print 'run the stress end.'
 
if __name__ == '__main__':
    print 'please input time/secs (default 3600).'
    if len(sys.argv) == 1:
        print 'we use default number(1hour).'
        run_start()
        run(3600)
        run_end()
    else:
        print 'we use the number(secs) : ', sys.argv[1]
        run_start()
        run(float(sys.argv[1]))
        run_end()
