#! /usr/bin/env python3
# -*- coding: utf8 -*-
import subprocess
subprocess.call(['ethtool', '-S', 'enp0s25'])
s=subprocess.getoutput('cat /sys/class/net/enp0s25/operstate')
print(s)
subprocess.check_call(['ethtool', '-S', 'enp0s25'])