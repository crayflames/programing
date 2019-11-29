#!/bin/bash

lsSlg=$(lsscsi -g| grep FOXCONN | grep 'SledgeHammer' | awk '{print $4 " " $7}' | sort)
IFS=$'\n'
for i in $lsSlg
do
t1=$(echo $i | awk '{print $1}'| tr -d '[a-zA-Z]|_')
t2=$(echo $i | awk '{print $2}')
echo Turn on LED
if [ $t1 == 0 ];then
	for i in {0..27}
	do
	echo sg_ses --dev-slot-num=$i --set=fault $t2
	sg_ses --dev-slot-num=$i --set=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	echo sg_ses --dev-slot-num=$i --set=fault $t2
	sg_ses --dev-slot-num=$i --set=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	echo sg_ses --dev-slot-num=$i --set=fault $t2
	sg_ses --dev-slot-num=$i --set=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	echo sg_ses --dev-slot-num=$i --set=fault $t2
	sg_ses --dev-slot-num=$i --set=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
sleep 3

echo Tunf off LED
if [ $t1 == 0 ];then
	for i in {0..27}
	do
	echo sg_ses --dev-slot-num=$i --clear=fault $t2
	sg_ses --dev-slot-num=$i --clear=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	echo sg_ses --dev-slot-num=$i --clear=fault $t2
	sg_ses --dev-slot-num=$i --clear=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	echo sg_ses --dev-slot-num=$i --clear=fault $t2
	sg_ses --dev-slot-num=$i --clear=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	echo sg_ses --dev-slot-num=$i --clear=fault $t2
	sg_ses --dev-slot-num=$i --clear=fault $t2
	echo sg_ses --dev-slot-num=$i --get=fault $t2
	sg_ses --dev-slot-num=$i --get=fault $t2
	done
fi


echo Turn on locate

if [ $t1 == 0 ];then
	for i in {0..27}
	do
	echo sg_ses --dev-slot-num=$i --set=locate $t2
	sg_ses --dev-slot-num=$i --set=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	echo sg_ses --dev-slot-num=$i --set=locate $t2
	sg_ses --dev-slot-num=$i --set=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	echo sg_ses --dev-slot-num=$i --set=locate $t2
	sg_ses --dev-slot-num=$i --set=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	echo sg_ses --dev-slot-num=$i --set=locate $t2
	sg_ses --dev-slot-num=$i --set=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi

echo clear locate
if [ $t1 == 0 ];then
	for i in {0..27}
	do
	echo sg_ses --dev-slot-num=$i --clear=locate $t2
	sg_ses --dev-slot-num=$i --clear=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	echo sg_ses --dev-slot-num=$i --clear=locate $t2
	sg_ses --dev-slot-num=$i --clear=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	echo sg_ses --dev-slot-num=$i --clear=locate $t2
	sg_ses --dev-slot-num=$i --clear=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	echo sg_ses --dev-slot-num=$i --clear=locate $t2
	sg_ses --dev-slot-num=$i --clear=locate $t2
	echo sg_ses --dev-slot-num=$i --get=locate $t2
	sg_ses --dev-slot-num=$i --get=locate $t2
	done
fi

echo $t2
done
unset IFS

