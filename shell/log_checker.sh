#!/bin/bash

allfile()
{
for file in $(ls *)
do
	echo "=========================================="
	echo "filename:" $file
	echo "search:		" $keyWord
	echo "=========================================="
	cat $file | grep -ia $keyWord | uniq
	keyCount=$(cat $file | grep -ia "$keyWord" | wc -l)
	echo ""
	echo "  ==========Keywork count :" $keyCount "=========="
	echo "=========================================="
	echo ""
done
}

string()
{
echo "filename:" $fileName
echo "search:	 " $keyWord
echo "=======================Begin=========================="
cat $fileName | grep -i 'keyWord' | sort | uniq
keyCount=$(cat $fileName | grep -ia "$keyWord" | wc -l)
echo "========================END==========================="
echo "Keywork count:	" $keyCount
}

#check functio is verified for spec keyword. Just a test
check()
{
bus=$(cat 941310000453_Error_Detction.log | grep "[1]" | grep -i "receiver" -B 23 | grep "bus" | sort |uniq)
receiver=$(cat 941310000453_Error_Detction.log | grep "[1]" | grep -i "receiver")
for error in $bus
do
	echo $bus
	(error++)
	for count in $receiver
	do
		echo $receiver
		(count++)
		continue 2
	done
done
}

diff()
{
diff -b -B $fileA $fileB
}

usage()
{

		echo "log_checker - Roger Hu/SIT/EPBG/CESBG@2013/6/7"
		echo ""
		echo "log_checkser is used for log filer with specified keyword"
		echo "And make a counter for appearance counter of keyword"
		echo ""
		echo "Arguments:"
		echo "	-f 			Check specified file name with keyword"
		echo "				ex: log_checker -f log.log \"failed\""
		echo "	-t			The specified keywork as you want"
		echo "				ex: log_checker -t \"failed\"		It will filter all file under the path with keyword failed"
		echo "	-s			Save result as a file"
		echo "	-h  or  -?		Print this messages for help"
		
}




if [ $# -le 0 ]; then
usage
else
while getopts "t:v:d:hsf:" arg
do 
	case $arg in		
		f)
		shift
		fileName=$1
		keyWord=$2
		string fileName,keyWord
		;;

		n)
		echo $@
		;;

		t)
		keyWord=$2
		allfile keyWord
		;;

		
		h)
		usage
		exit 1
		;;
		
		d)
		fileA=$2
		fileB=$3
		diff fileA,fileB
		;;

		s)
		echo $1
		echo $2
		echo $3
		echo $4
		echo 345
		check
		;;
		*)
		;;
	esac
			

done
fi
