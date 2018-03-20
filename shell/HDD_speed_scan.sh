#! /bin/bash
tHDD=$(lsscsi | grep SEAGATE | awk '{print $7}')
fName=HDD_smart_info.log
fCunt=$(lsscsi | grep SEAGATE -c)

#Check tmp log exist if exist delete it
[ -e $fName ] && rm -f $fName ||touch $fName

#Check smartctl tool is exist
which smartctl > /dev/null
[ $? -le 0 ] || echo "No smartctl tool found"
#Test time per second
for file in $tHDD
do 
#Read HDD SN & speed & health result
	echo "== $file ==" | tee -a $fName
	smartctl -i $file | grep 'Serial Number:' | tee -a $fName
	smartctl -i $file | grep 'current' | tee -a $fName
	smartctl -H $file | grep result |awk '{print "self test result: "$6}' | tee -a $fName
done
#filter result log

echo \n
echo \n
echo "Test Total HDD count = $fCunt" | tee -a $fName

