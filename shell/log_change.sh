#!/bin/bash
usage(){
    echo ""
    echo "Use for change file name with [KEY]_file.log"


}

read -p "Please input keyword for name of allfile:" name
[ -z $name ] && usage && exit 1
echo "Below files will be changed name"
DIRs=$(ls *.log)
for f in $DIRs
do 
	echo $f
done

DIR1=$(ls *.log)
for g in $DIR1
do 
	mv $g $name\_$g
done

echo "Finally file name as below"
DIR3=$(ls *.log)
for h in $DIR3
do 
	echo $h
done
