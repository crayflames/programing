#! /bin/bash
a="-i /dev/sda" #unworkable
b="/dev/null"
array=($(a) )
#Test time per second
for file in ${array[@]}
do
	echo "smartctl $file"
done


for each in {1..5};
do
	echo $each
done