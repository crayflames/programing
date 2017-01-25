#! /usr/bin/env python3
import sys
import os
import getopt
t=100 #if t at heere will be show 'UnboundLocalError: local variable 't' referenced before assignment'
dst=''
def check(a):
  if not a.strip():
    print (a + 'is null')

def main(argv):
	t=100
	try:
		opts, args = getopt.getopt(argv,"hs:d:c:m:")
	except getopt.GetoptError:
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('help')
		elif opt in ("-s", "--sourcedev"):
			print(t)
			t=arg
			print('t=' , t)
		elif opt in ("-d", "--destination"):
			global dst #'global' should be used
			dst=arg
			print(dst)
		elif opt in ("-c", "--count"):
			cut=arg
			print(arg)
		elif opt in ("-m", "--mtu"):
			print(arg)
	check(dst)

if __name__ == "__main__":
  main(sys.argv[1:])
 
 # print (dst)
  #print (cut)
