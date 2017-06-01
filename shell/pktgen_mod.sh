#! /bin/bash
## pktgen.conf -- configuration for send on devices
tx_aborted_err=0
tx_carrier_err=0
tx_err=0
rx_crc_err=0
rx_err=0
rx_frame_err=0
rx_length_err=0
rx_missed_err=0
rx_over_err=0

usage(){
	#echo "Function: port to port || mac to mac. "
	#echo "          Counter by User setting. "
	echo "Please follow format to stress Ethernet device"
	echo "such as : "
	echo "  Host port to port"
	echo "          ./pktgen.sh [SrcDEV] [DstDEV] [Count]"
	echo "  [Count] setting as 0 is inifinit loop"
	echo "MTU 1500 : 1 count eq 4.4kb"
	echo "MTU 9014 : 1 count eq 8.8kb"
	DevSrc=$(ifconfig -a | grep HWaddr | awk '{print $1}')
	echo $DevSrc > DEV.file
	DevList=$(cat DEV.file | awk '{print $1 " " $2}')
	echo "  On this OS you can type format as below"
	echo "		Port to Port    ./pktgen.sh -P $DevList 15000"
	echo "		Port to MAC     ./pktgen.sh -M eth0 00:00:00:00:00:00 15000"
	rm -f DEV.file
}

lsmod | grep pktgen
if [ $? -eq 1 ]; then
	modprobe pktgen > /dev/null 2>&1
fi
TestResult(){
	#rx_package_end=$(cat /sys/class/net/$dstDev/statistics/rx_bytes)
	#rx_package_rsl=$(( $rx_package_end - $rx_package_org ))
	strTime=$(cat /proc/net/pktgen/$srcDev | grep Result | awk '{print $3}' | awk -F '(' '{ print $1/1000000 }')
	totTras=$(cat /sys/class/net/$srcDev/statistics/tx_bytes | awk '{print $1/1024/1024}')
	#totRecv=$(cat /sys/class/net/$dstDev/statistics/rx_bytes | awk '{print $1/1024/1024}')
	totCount=$(cat /proc/net/pktgen/$srcDev | grep sofar | awk '{print $2}')
	perMB=$(cat /proc/net/pktgen/$srcDev | grep Mb/sec | awk '{print $2}')
	tx_aborted_err=$(cat /sys/class/net/$srcDev/statistics/tx_aborted_errors)
	tx_carrier_err=$(cat /sys/class/net/$srcDev/statistics/tx_carrier_errors)
	tx_err=$(cat /sys/class/net/$srcDev/statistics/tx_errors)
	#rx_crc_err=$(cat /sys/class/net/$dstDev/statistics/rx_crc_errors)
	##rx_err=$(cat /sys/class/net/$dstDev/statistics/rx_errors)
	#rx_frame_err=$(cat /sys/class/net/$dstDev/statistics/rx_frame_errors)
	#rx_length_err=$(cat /sys/class/net/$dstDev/statistics/rx_length_errors)
	#rx_missed_err=$(cat /sys/class/net/$dstDev/statistics/rx_missed_errors)
	#rx_over_err=$(cat /sys/class/net/$dstDev/statistics/rx_over_errors)

	echo "Test Result :"
	echo "Total running time        : $strTime sec"
	echo "Performance               : $perMB"
	echo "packet size               : $pktSize"
	echo "Parameter Count	   	  : $testCNT"
	echo "Total transfer count      : $totCount"
	echo "Total transfer MB 	  : $totTras MB"
	#echo "Total receive count       : $rx_package_rsl"
	#echo "Total receive MB  : $totRecv"
	echo "tx_aborted_err            : $tx_aborted_err"
	echo "tx_carrier_err            : $tx_carrier_err"
	echo "tx_err                    : $tx_err"
	#echo "rx_crc_err                : $rx_crc_err"
	#echo "rx_err                    : $rx_err"
	#echo "rx_frame_err              : $rx_frame_err"
	#echo "rx_length_err             : $rx_length_err"
	#echo "rx_missed_err             : $rx_missed_err"
	#echo "rx_over_err               : $rx_over_err"
}

devList(){
	ifconfig -a | grep HWaddr
}

LinkStat(){
	[ -e /sys/class/net/$1 ] && [ "$OPERSTATE" != "up"  ]
	[ $? -eq 1 ] && ( echo "$1 not found ! DevList :" && devList ) || echo "$1 no link detected" && exit 1
}
#Check device of parameter is currect, if not then exist
LinkExist(){
	[ -e /sys/class/net/$1 ] || LinkStat $1
	OPERSTATE=$(cat /sys/class/net/$1/operstate)
	[ "$OPERSTATE" == "up"  ] || LinkStat $1
	return
}

setCnt(){
	[ -z $1 ] && usage
	[ $1 -ge 0 > /dev/null 2>&1 ] || (echo "Please set up test counter. 0 as loop " )
	tstCnt=$1
	break
}

#Paramter check if null then exit
[ $# -le 0 ] && usage && exit 1

pgset(){
    local result

    echo $1 > $PGDEV

    result=`cat $PGDEV | fgrep "Result: OK:"`
    if [ "$result" == "" ]; then
         cat $PGDEV | fgrep Result:
    fi
}

pg(){
    echo inject > $PGDEV
    cat $PGDEV
}

#Check pktgen module 

p2p(){
	devArray=$@
	i=1
	z=$#
	for paraMeter in $@
	do
		modPara=$(( $i%2 ))
		#Last of parameter is count
		if [ $i == $z ]; then
			setCnt $paraMeter
		fi
		#Judge parameter is src or dst
		if [ $modPara == 1 ]; then
			srcDev=$paraMeter
			LinkExist $srcDev
		else
			dstDev=$paraMeter
			LinkExist $dstDev
		fi
		(( i++ ))
	done

	##Check target device shoule be  exist, Need update more device to 2way stress
	if [ -z $dstDev ]; then
		echo $dstDev
		echo "Please setup Target Device or Test Counter"
		usage
		exit 1
	else
		dstMac=$(cat /sys/class/net/$dstDev/address)
	fi
}

p2mac(){
	srcDev=$1
	LinkExist $srcDev
	dstMac=$2
	tstCnt=$3
}

while getopts "P:M:" arg
do
	case $arg in
		P)
		shift
		echo $1 $2 $3
		p2p $1 $2 $3
		;;
		M)
		shift
		p2mac $1 $2 $3
		;;
		*)
		usage
		exit 1
		;;
		
	esac
done
## Settings for pktgen params

testCNT=${tstCnt:-15000}
echo "Adding devices to run". 
pktSize=1500
PGDEV=/proc/net/pktgen/kpktgend_0
pgset "rem_device_all"
pgset "add_device $srcDev"
pgset "max_before_softirq 1000000"

## Configure the individual devices
PGDEV=/proc/net/pktgen/$srcDev
pgset "clone_skb 1000000"
pgset "pkt_size $pktSize"
#pgset "min_pkt_size 60"
#pgset "max_pkt_size 1500"

echo "Configuring devices $srcDev"
pgset "dst_mac $dstMac"
echo "Src port $srcDev --> Dst port: $dstDev Mac: $dstMac"
pgset "count $testCNT"
pgset "delay 0"


PGDEV=/proc/net/pktgen/pgctrl

echo "Running... ctrl^C to stop"
pgset "start"
echo "Done"

TestResult $srcDev $dstDev
