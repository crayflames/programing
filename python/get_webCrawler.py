#! /usr/bin/python3
# -*- coding: utf8 -*-
from openpyxl import Workbook
import datetime
import requests
from bs4 import BeautifulSoup
res=requests.get('https://sites.google.com/a/crayflames.co.cc/crayflames/linux-about')
wes=BeautifulSoup(res.text,"html.parser")
ss=wes.select(".sites-announcement-embed-post-title")
xx=wes.select(".sites-text-secondary")
num=len(ss)
wb=Workbook()
ws=wb.active
ws.title='blogtitle'
for i in range(1,num):
	content=ss[i-1].text.strip()
	time=xx[i-1].text.strip()
	ws.cell(row=i, column=1, value=content)
	ws.cell(row=i, column=2, value=time)
wb.save("/home/roger/Desktop/example2.xlsx")

print(wes.title)
print(wes.title.string)
print(wes.title.parent.name)
print(wes.p)
print(wes.find_all('a'))
for link in wes.find_all('a'):
	print(link.get('href'))