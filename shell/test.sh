#! /bin/bash
PCIeDev="
17 00 0
65 00 0
"
IFS=$'\n'
cmdClr="diag -d pci -p pcidevice -t clearerrreg -b "
cmdShow="diag -d pci -p pcidevice -t errreg -b "
for item in $PCIeDev
do
	echo $cmdClr $item
	echo $cmdShow $item
done
unset IFS