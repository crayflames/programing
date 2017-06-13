#!/usr/bin/env python3
import matplotlib.pyplot as plt
a=[]
i=open('/home/roger/Desktop/test.log','r')
#讀取檔案篩選eth0的行
for line in i:
	if "eth0" in line:
		#行切割後
		for e in line.strip().split('\n'):
			#再切割欄位
			a.append(e.split())
i.close
i=0
ap=[]
for i in range(len(a)):
	#取第三欄
	ap.append(a[i][2])
print(ap)
for _ in ap:
	if float(_) < 8000:
		print(_)
		ap.remove(_)
print(ap)
y=[]
#取得x 座標
for z in range(len(ap)):

	y.append(z)
plt.xlabel("i am x label")
plt.ylabel("i am y label")
plt.plot(y,ap,label='performance走勢圖') #marker='^'
plt.show()