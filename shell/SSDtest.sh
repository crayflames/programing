#!/bin/bash
tHDD=$1
ignore=$2
if [ $# -eq 0 ]; then
	echo "This script is used to tuning in SSD performance erase 5times before test by fio"
	echo "$0 [TestHDD] such as sdb"
	echo "$0 [TestHDD] noerase ***ignore erase to test device"
fi
log=/home/SUT1_N2_Intel_M2_perf_result.log
hdparm -I /dev/$tHDD > $log
smartctl -i /dev/$tHDD >> $log
prepare(){
	if [ -z parameter.fio ]; then
		rm -f parameter.fio
	fi
echo "[global]
ioengine=libaio
direct=1
thread
time_based
#rwmixread=50
group_reporting
new_group
runtime=60
iodepth=32
filename=/dev/"$tHDD"
numjobs=20
stonewall
[read128k]
readwrite=read
bs=128k
[write128k]
readwrite=write
bs=128k" > parameter.fio
}
erase(){
	if [ $ignore == "noerase"]; then
		echo "Running fio"
	else
		for each in {1..5}
		do
			dd if=/dev/zero of=/dev/$tHDD bs=1M oflag=direct
			echo "$each times done!!"
		done
	fi
}
erase
if [ "$?" -eq 0 ];then
	which fio
	if [ "$?" -eq 0 ];then
		fio parameter.fio | tee -a $log
			if [ "$?" -eq 0 ];then
				echo 'success log path at $log'
			else
				echo 'Somethings wrong?'
				exit 1
			fi
	else
		echo "fio not install"
	fi
else
	echo "fail"
fi