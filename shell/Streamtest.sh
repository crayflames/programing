#!/bin/bash
export PATH=$(pwd):$PATH
sockets=$(lscpu | grep 'Socket(s)' | awk '{print $2}')
cores=$(nproc)
echo "Follow Norman step"

memSize=$(printf "%.f" $(cat /proc/meminfo | grep MemAvailable | awk '{print $2/1024/1024}')) 

if [ "$memSize" -lt "128" ];then
	tDIMM="512M"
else
	tDIMM="1G"
fi

stream_length=("100k" $tDIMM )

single(){
	
	for i in ${stream_length[@]}
	do
	        echo "./stream -M $i -P $cores > stream_1cores_$i.log 2>&1" 
	        stream -M $i -P $cores > stream_1cores_$i.log 2>&1
	done

}
dual(){
	
	for i in ${stream_length[@]}
	do
		echo "./stream -M $i -P $cores > stream_2cores_$i.log 2>&1"
		./stream -M $i -P $cores > stream_2cores_$i.log 2>&1
	done

	for stl in ${stream_length[@]}
	do
		for((mNum=0;mNum<=1;mNum++)) 
		do
			for((nNum=0;nNum<=1;nNum++))
			do
				sleep 3
				echo "stream -M $stl -P $cores numactl -m $mNum -N $nNum > stream_2cores_"$stl"_numctrl_M"$mNum"_N"$nNum".log 2>&1"
				stream -M $stl -P $cores numactl -m $mNum -N $nNum > stream_2cores_"$stl"_numctrl_M"$mNum"_N"$nNum".log 2>&1
			done
		done
	done
}

if [ $sockets -eq '1' ];then
	echo "sockets=1"
	single
else
	echo "sockets=2"
	dual
fi
