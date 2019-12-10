#!/bin/bash
IFS=$'\n'
log="~/Desktop/SledgeHammer/SN3_Hotplug_Stress.log"
diskList=$(ls -l /sys/class/enclosure/*/*/device/block/sd*|grep enclosure | awk -F "/" '{print $6 " " $9}' |tr -d ":"| sort)
dmesg -C
ipmitool sel clear

rm -f $log
for i in $diskList
do
	t1=$(echo $i | awk '{print $1}')
	t2=$(echo $i | awk '{print $2}')
	echo "Wait for unplug " $t1 $t2 | tee -a $log
	while [ -e /dev/$t2 ]
		do 
		echo -n "." | tee -a $log
		sleep 1
	done
	echo "I am Waiting $t1 $t2" | tee -a $log
	while [ ! -e /dev/$t2 ]
		do
		echo -n "." | tee -a $log
		sleep 1
	done

	if [ -e /dev/$t2 ]; then
		echo $t2 "detected!!" | $log
		echo "Perform $t2 1min Stress..." | tee -a $log
		echo "===Perform $t2 fio===" | tee -a $log
		fio --direct=1 --iodepth 16 --thread --rw=read --ioengine=libaio --bs=256k --numjobs=4 --runtime=60 --group_reporting --name=$t2 --filename=/dev/$t2| tee -a $log
		sleep 5
	fi

done

unset IFS
