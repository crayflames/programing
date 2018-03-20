#! /usr/bin/env python3
# -*- coding: utf8 -*-
for i in range(2):
	print (i)
for _ in ['CPU0','CPU1']:
	cmd ='ipmi ' +BMCIP + ' sdr' + ' | grep '+ _+'_DIMM'