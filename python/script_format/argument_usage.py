#!/usr/bin/env python3
import argparse
parser=argparse.ArgumentParser()
#positional arguments  
#似乎都不能省略
#這裡echo square的順序是不變的 echo先
parser.add_argument("echo",help="echo echo")
#type 可以指定參數或字串 例如: -v 123 or -v string ]
parser.add_argument("square",help="Display a square of a given number",type=int)

#optional arguments
##type 可以指定參數或字串 例如: -v 123 or -v string
parser.add_argument("-v","--verbose",help="increase output verbosity",type=str,choices=['a1','b','c'])

parser.add_argument("-t","--test",help="test help",action="count",default=0)
#store_true 有呼叫再執行 false 有呼叫就不執行
parser.add_argument("-a","--aaa",help="aaaa",action="store_true")

parser.parse_args()
args=parser.parse_args()
if args.verbose == 'a1':
	print(args.verbose)

if args.echo:
	print("echo echo2")
	print(args.square**2)
if args.test >=2 :
	#這裡會存成數字 -ttt 就存3次 
	s=args.test
	print("s="+str(s))
	print(args.square**args.test)
if args.aaa:
	print(args.aaa)
