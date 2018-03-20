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

for((;1;))
do
	echo "This is loop"
done

for (( i=1 ; i<=s ; i++))
do
	echo $i
done