#!/usr/bin/python3
import re
#取代字串  類似sed
text= 'one , two , three'
word='one'
cmdRt=re.sub(word, '123' , text)
print (cmdRt)

#比對輸入格式符合macaddress \w 接受數字及英文大小寫
x='1s:3s:dg:r4:66:xs'
m = re.match(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',x)
if m:
	print(x + ' is address Format.')
else:
	print(x + ' is not a address.')
