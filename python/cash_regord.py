#! /usr/bin/python3
# -*- coding: utf8 -*-
from openpyxl import Workbook
import openpyxl
import datetime
import requests
import time
from bs4 import BeautifulSoup
workbook = openpyxl.load_workbook("/home/roger/Desktop/test_cash.xlsx")
sheet=workbook.get_sheet_by_name('cash')

stockList=['2887', '3209', '1229','2317', '2354']
stockValue=[]

for _ in stockList:
	res=requests.get('https://tw.stock.yahoo.com/q/q?s='+ _ )
	wes=BeautifulSoup(res.text,"html.parser")
	ss=wes.select("b")
	stockValue.append(ss[1].text)

x=4
print(stockValue)
for i in range(len(stockValue)):
	y='C' + str(x)
	sheet[str(y)]=stockValue[i]
	x=x+1

workbook.save("/home/roger/Desktop/test_cash.xlsx")




	
