#! /bin/bash
#0717
export PATH=$(pwd):$PATH
chmod 777 stressapptest
Mem=$(cat /proc/meminfo | grep MemAvailable | awk '{print $2/1024*0.85}')
tstTime=$(date '+%Y%m%d%H%M')
Cpu=$(nproc)
tTime=$2
Time=${tTime:-60}
CPU=0
MEM=0
NVME=0
mkdir -p $(pwd)/testlog

case $1 in
        FULL)
                CPU=1
                MEM=1
                NVME=1
				log=testlog/stressapptest_FULL_$tstTime.log
				fiolog=testlog/fio_NVMe_$tstTime.log
        ;;
        CPU)
                CPU=1
				log=testlog/stressapptest_CPU_$tstTime.log
        ;;
        MEM)
                MEM=1
				log=testlog/stressapptest_MEM_$tstTime.log
        ;;
        *)
        echo "Generate System full loading via $0 [FULL | CPU | MEM ] [Time :default is 60 secs if not setting]"
        echo "./Stressapptest.sh FULL 3600"
        echo "./Stressapptest.sh CPU 3600"
        echo "./Stressapptest.sh MEM 3600"
        exit 1
        ;;
esac
if [ $CPU -eq 1 ]; then
        tCPU="-C $Cpu "
fi

if [ $MEM -eq 1 ]; then
        tMEM="-M $Mem "
fi

echo "Check Tools..."
if [ $NVME -eq 1 ]; then
	if [ -e /dev/nvme0n1 ]; then
	    echo "Check FIO"
		which fio
		if [ $? -eq 0 ];then
			echo "FIO is already install."
			fio -v
		else
			echo "Install FIO..."
			rpm -ivh librdmacm1-1.0.19.1-4.3.1.aarch64.rpm
			rpm -ivh fio-2.2.8-2.el7.aarch64.rpm
		fi
		echo "***************************"
		echo "Fio NVMe test start..."
		echo "***************************"
		nohup fio --direct=1 --iodepth=16 --thread --rw=rw --rwmixread=50 --ioengine=libaio --bs=4k --time_based --numjobs=32 --runtime=$Time --group_reporting --name=nvme1 --filename=/dev/nvme0n1 --output=$(pwd)/$fiolog &
   	else
		echo "NVMe is not exist. Test is not Available. "
		read -p "keep testing without NVMe? :[y/n]" yes
		if [ $yes == "y" ]; then
			echo "start test stressapptest"
			NVME=0
		else
			exit 1
		fi
	fi
fi

echo "Check stressapptest"
which stressapptest

echo "***************************"
echo "Start test stressapptest..."
echo "***************************"
stressapptest $tCPU $tMEM -m $Cpu -i $Cpu -s $Time  -l $(pwd)/$log  

if [ $? -eq 0 ];then
    echo "stressapptest log path is $(pwd)/$log"
fi
if [ $NVME -eq 1 ]; then
	echo "fio test log path is $(pwd)/$fiolog"
fi
