#! /usr/bin/env python3
# -*- coding: utf8 -*-
s=open("/sys/class/net/" + a + "/statistics/tx_aborted_errors").readline().strip()
#Replace s=subprocess.getoutput('cat /sys/class/net/'+ a +'/statistics/tx_aborted_errors')