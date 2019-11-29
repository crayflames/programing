#!/bin/bash

actOn(){
	echo sg_ses --dev-slot-num=$1 --set=fault $2
	sg_ses --dev-slot-num=$1 --set=fault $2
	echo sg_ses --dev-slot-num=$1 --get=fault $2
	sg_ses --dev-slot-num=$1 --get=fault $2
	}
clroff(){
	echo sg_ses --dev-slot-num=$1 --clear=fault $2
	sg_ses --dev-slot-num=$1 --clear=fault $2
	echo sg_ses --dev-slot-num=$1 --clear=fault $2
	sg_ses --dev-slot-num=$1 --get=fault $2
	}
actLoa(){
	echo sg_ses --dev-slot-num=$1 --set=locate $2
	sg_ses --dev-slot-num=$1 --set=locate $2
	echo sg_ses --dev-slot-num=$1 --get=locate $2
	sg_ses --dev-slot-num=$1 --get=locate $2
	}
clrLoa(){
	echo sg_ses --dev-slot-num=$1 --clear=locate $2
	sg_ses --dev-slot-num=$1 --clear=locate $2
	echo sg_ses --dev-slot-num=$1 --get=locate $2
	sg_ses --dev-slot-num=$1 --get=locate $2
	}
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
	actOn $i $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	actOn $i $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	actOn $i $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	actOn $i $t2
	done
fi
sleep 3

echo Tunf off LED
if [ $t1 == 0 ];then
	for i in {0..27}
	do
	clroff $i $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	clroff $i $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	clroff $i $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	clroff $i $t2
	done
fi


echo Turn on locate

if [ $t1 == 0 ];then
	for i in {0..27}
	do
	actLoa $i $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	actLoa $i $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	actLoa $i $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	actLoa $i $t2
	done
fi

echo clear locate
if [ $t1 == 0 ];then
	for i in {0..27}
	do
	clrLoa $i $t2
	done
fi
if [ $t1 == 1 ];then
	for i in {28..54}
	do
	clrLoa $i $t2
	done
fi
if [ $t1 == 2 ];then
	for i in {55..82}
	do
	clrLoa $i $t2
	done
fi
if [ $t1 == 3 ];then
	for i in {83..107}
	do
	clrLoa $i $t2
	done
fi

done
unset IFS

