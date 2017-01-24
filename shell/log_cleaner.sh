#!/bin/bash
clean()
{
for fileName in $(ls *.log)
do
		echo "" > $fileName
		echo $fileName "Clean done!!"	
done
}

file()
{
cat /dev/nul > $fileName
echo $fileName "Done!!"
}

usage()
{
echo "log_cleaner is used for making empty of *.log."
echo ""
echo "Arguments:"
echo "	-n		Clean all of *.log under current path"
echo "	-f		Clean the fie you want"
echo "	-h		Print this help"
}
if [ $# -le 0 ]; then
usage
else
	while getopts "f:nh" arg
	do
		case $arg in
			n)
			clean
			;;
			f)
			fileName=$2
			file 
			;;
			h)
			usage
			;;
		esac	
	done
fi	
