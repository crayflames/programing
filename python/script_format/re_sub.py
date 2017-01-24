#!/usr/bin/python3
import re
text= 'one , two , three'
word='one'
cmdRt=re.sub(word, '123' , text)
print (cmdRt)