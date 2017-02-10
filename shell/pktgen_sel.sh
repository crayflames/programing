#! /bin/sh
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
echo "	Host port to port"
echo "		./pktgen.sh [SrcDEV] [DstDEV] [Count]"
echo " 	[Count] setting as 0 is inifinit loop"
echo "MTU 1500 : 1 count eq 4.4kb"
echo "MTU 9014 : 1 count eq 8.8kb"
DevSrc=$(ifconfig -a | grep HWaddr | awk '{print $1}')
echo $DevSrc > DEV.file
DevList=$(cat DEV.file | awk '{print $1 " " $2}')
echo "	On this OS you can type format as below"
echo "		Port to Port	./pktgen.sh -P $DevList"
rm -f DEV.file
}
lsmod | grep pktgen 
[ $? == 1 ] &&  modprobe pktgen 


TestResult(){
strTime=$(cat /proc/net/pktgen/$srcDev | grep Result | awk '{print $3}' | awk -F '(' '{ print $1/1000000 }')
totTras=$(cat /sys/class/net/$srcDev/statistics/tx_bytes | awk '{print $1/1024/1024}')

totCount=$(cat /proc/net/pktgen/$srcDev | grep sofar | awk '{print $2}')
perMB=$(cat /proc/net/pktgen/$srcDev | grep Mb/sec | awk '{print $2}')
tx_aborted_err=$(cat /sys/class/net/$srcDev/statistics/tx_aborted_errors)
tx_carrier_err=$(cat /sys/class/net/$srcDev/statistics/tx_carrier_errors)
tx_err=$(cat /sys/class/net/$srcDev/statistics/tx_errors)
if [ $rx = 0 ]; then
rx_crc_err=$(cat /sys/class/net/$dstDev/statistics/rx_crc_errors)
totRecv=$(cat /sys/class/net/$dstDev/statistics/rx_bytes | awk '{print $1/1024/1024}')
rx_package_end=$(cat /sys/class/net/$dstDev/statistics/rx_bytes)
rx_package_rsl=$(( $rx_package_end - $rx_package_org )) 
rx_err=$(cat /sys/class/net/$dstDev/statistics/rx_errors)
rx_frame_err=$(cat /sys/class/net/$dstDev/statistics/rx_frame_errors)
rx_length_err=$(cat /sys/class/net/$dstDev/statistics/rx_length_errors)
rx_missed_err=$(cat /sys/class/net/$dstDev/statistics/rx_missed_errors)
rx_over_err=$(cat /sys/class/net/$dstDev/statistics/rx_over_errors)
fi

echo "Test Result :"
echo "Total running time 	: $strTime sec"
echo "Performance        	: $perMB"
echo "packet size	 	: $pktSIZE"
echo "Parameter Count  	: $testCNT"
echo "Total transfer count	: $totCount"
echo "Total transfer MB	: $totTras"
echo "Total receive count	: $rx_package_rsl"
echo "Total receive MB	: $totRecv"
echo "tx_aborted_err		: $tx_aborted_err"
echo "tx_carrier_err		: $tx_carrier_err"
echo "tx_err			: $tx_err"
echo "rx_crc_err		: $rx_crc_err"
echo "rx_err			: $rx_err"
echo "rx_frame_err		: $rx_frame_err"
echo "rx_length_err		: $rx_length_err"
echo "rx_missed_err		: $rx_missed_err"
echo "rx_over_err		: $rx_over_err"
}
devList() {
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


srcDevChk(){
while [ -z "$srcDev" ];do
read -p "Please enter SrcDevice: " srcDev
done

LinkExist $1

}

dstDevChk(){
while [ -z "$dstDev" ];do
read -p "Please enter DstDevice: " dstDev
done
devLen=${#dstDev}
if [ "$devLen" -eq 17 ]; then
rx=1
dstMac=$1
return
else
rx=0
LinkExist $1
dstMac=$(cat /sys/class/net/$dstDev/address)
rx_package_org=$(cat /sys/class/net/$dstDev/statistics/rx_bytes)
fi
}


setCnt(){
[ $1 -ge 0 2>/dev/null ] && tstCnt=$1 || echo "Test counter is null. default is 15000. 0 is loop "
if [ "$testCnt" == 0 ];then
read -p "Please enter time limit: " timeTest
timeLimit=1
fi
}

setPkt(){
[ $1 -ge 0 2>/dev/null ] && pktSize=$1 || echo "Test counter is null. default is 1514."
while [ "$pktSize" == 0 ];do
echo "Package should not be 0"
read -p "Please enter package_size: " pktSize
done

}


#Paramter check if null then exit
#[ $# -le 0 ] && usage && exit 1

function pgset(){
    local result

    echo $1 > $PGDEV

    result=`cat $PGDEV | fgrep "Result: OK:"`
    if [ "$result" = "" ]; then
         cat $PGDEV | fgrep Result:
    fi
}

function pg(){
    echo inject > $PGDEV
    cat $PGDEV
}


#Check pktgen module 
##Check target device shoule be  exist, Need update more device to 2way stress

read -p "Please enter SrcDevice: " srcDev
srcDevChk $srcDev
read -p "Please enter DstDevice: " dstDev 
dstDevChk $dstDev
read -p "Please enter TestCount	: " testCnt
timeLimit=0
setCnt $testCnt
#trap 'INT' sleep $timeTest
read -p "Please enter package_size: " pktSize
setPkt $pktSize

testCNT=${tstCnt:-15000}

echo "Adding devices to run" 
PGDEV=/proc/net/pktgen/kpktgend_0
pgset "rem_device_all"
pgset "add_device $srcDev"
pgset "max_before_softirq 1000000"

## Configure the individual devices
PGDEV=/proc/net/pktgen/$srcDev
pgset "clone_skb 1000000"
pktSIZE=${pktSize:-1514}
pgset "pkt_size $pktSIZE"
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

TestResult #$srcDev $dstDev
