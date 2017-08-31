#! /bin/bash
#0829
export PATH=$(pwd):$PATH
Mem=$(cat /proc/meminfo | grep MemAvailable | awk '{print $2/1024*0.85}')
tstTime=$(date '+%Y%m%d%H%M')
Cpu=$(nproc)
tTime=$2
Time=${tTime:-60}
CPU=0
MEM=0
NVME=0
NET=0
mkdir -p $(pwd)/testlog

Network(){
	which iperf3
	if [ "$?" -eq 0 ];then
		echo "Iperf3 installed"
	else
		echo "Install iperf3"
		rpm -ivh iperf3-3.0.11-1.el7.centos.aarch64.rpm
	fi
	if [ "$1" == "Server" ];then
		echo "***************************"
		echo "Iperf Server start..."
		echo "***************************"
		nohup iperf3 -s -i 10 > $Netlog &
	elif [ "$1" == "Client" ];then
		echo "Running as Client"
		read -P "Input Iperf Server IP[]: " ServerIP
		ping -c $ServerIP
		if [ "$?" -eq 0 ]; then
			echo "***************************"
			echo "Iperf Client start..."
			echo "***************************"
			nohup iperf3 -c $ServerIP -i 10 -t $Time -P 8 > $Netlog &
		else
			echo "Server no exist  See you ~bye~!"
			exit 1
		fi
	fi
}

while getopts "F:CMT" arg; 
do
	case $arg in
	        F)
	            CPU=1
	            MEM=1
	            NVME=1
	            NET=1
	            IPerf=$OPTARG    
				log=testlog/stressapptest_FULL_$tstTime.log
				fiolog=testlog/fio_NVMe_$tstTime.log
				Netlog=testlog/iperf_$IPerf_$tstTime.log
	        ;;
	        C)
	            CPU=1
				log=testlog/stressapptest_CPU_$tstTime.log
	        ;;
	        M)
	            MEM=1
				log=testlog/stressapptest_MEM_$tstTime.log
	        ;;
	        T)
				tTime=$OPTARG
			;;
	        *)
	        echo "Generate System full loading via $0 {FULL [Server|Client] | CPU | MEM } [Time :default is 60 secs if not setting]"
	        echo "./Stressapptest.sh -F [Server|Client] -T 3600"
	        echo "./Stressapptest.sh -F -T 3600 ***Test without Network"
	        echo "./Stressapptest.sh -C -T 3600"
	        echo "./Stressapptest.sh -M -T 3600"
	        exit 1
	        ;;
	esac
done

if [ $CPU -eq 1 ]; then
    tCPU="-C $Cpu "
fi

if [ $MEM -eq 1 ]; then
    tMEM="-M $Mem "
fi
if [ $NET -eq 1 ]; then
	if [ $IPerf == "Server" ];then
		Network $IPerf
	elif [ $IPerf == "Client" ]; then
		Network $IPerf
	elif [ $IPerf == "" ]; then
		#Test without network
		break
	else
		echo "Please input iperf position Server or Client ?"
	fi 
fi 

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
		nohup fio --direct=1 --iodepth=16 --thread -rw=rw --rwmixread=50 --ioengine=libaio --bs=4k --time_based --numjobs=32 --runtime=$Time --group_reporting --name=nvme1 --filename=/dev/nvme0n1 --output=$(pwd)/$fiolog &
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
if [ $NET -eq 1 ]; then
	echo "Iperf test log path is $(pwd)/$Netlog"
fi