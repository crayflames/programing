#! /usr/bin/env python3
# -*- coding: utf8 -*-
import sys
import os
import getopt
import subprocess
import multiprocessing
def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hs:d:c:m:")
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
        print('help')
      elif opt in ("-s", "--sourcedev"):
        print(arg)
      elif opt in ("-d", "--destination"):
        print(arg)
      elif opt in ("-c", "--count"):
        print(arg)
      elif opt in ("-m", "--mtu"):
        print(arg)

if __name__ == "__main__":
  #main(sys.argv[1:])
  s='enp0s25'
  #subprocess.call(['ethtool', '-S', s])
subprocess.getoutput('lsmod | grep video')
list=[]
i=0
list=os.listdir('/proc/net/pktgen/')
print(len(list))
print(list[i+2])
coreNum=multiprocessing.cpu_count()
for i in range(int(coreNum)):
  print ('kpktgend_'+str(i))