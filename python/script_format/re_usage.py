#!/usr/bin/python3
import re
text= 'one , two , three'
word='one'
cmdRt=re.sub(word, '123' , text)
print (cmdRt)

x=input('input => ')
print(x)
m = re.match(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',x)
if m:
	print(x + ' is address Format.')
else:
	print(x + ' is not a address.')