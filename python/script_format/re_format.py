#! /usr/bin/python3
# -*- coding: utf8 -*-
import re
x=input('input :')
print(x)
m = re.match(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',x)
if m:
	print(x + ' is address Format.')
else:
	print(x + ' is not a address.')