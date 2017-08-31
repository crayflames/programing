#!/bin/sh
IP=$1
SOL=$2
if [ SOL = 'de' ]; then
	SOL = 'deactivate'
else
	SOL = 'activate'

ipmitool -H $IP -U admin -P admin -I lanplus sol $SOL