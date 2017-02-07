#! /usr/bin/env python3
# -*- coding: utf8 -*-
import subprocess
#執行程式用
subprocess.call(['ethtool', '-S', 'enp0s25'])
subprocess.check_call(['ethtool', '-S', 'enp0s25'])
#要將輸出結果存進變數
s=subprocess.getoutput('cat /sys/class/net/enp0s25/operstate')
print(s)
