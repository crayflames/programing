#! /usr/bin/python3
# -*- coding: utf8 -*-
#from openpyxl import Workbook
import datetime
import requests
import time
from bs4 import BeautifulSoup
#想要找的股票
stockList=['2317', '2887', '2354', '3209']
#持有成本
stockCost=['78.01','12.8','78.91','20.39']
#爬出來的股價
stockValue=[]
#存入訊息裡
content=[]
for _ in stockList:
	res=requests.get('https://tw.stock.yahoo.com/q/q?s='+ _ )
	wes=BeautifulSoup(res.text,"html.parser")
	ss=wes.select("b")
	stockValue.append(ss[0].text)
stockTime=time.strftime("%H:%M:%S", time.localtime())
 
msgs='=搜尋股價='+ '\n' \
 '搜尋時間: '+ stockTime + '\n'
for i in range(len(stockList)):
	profit= ("%.2f"%(float(stockValue[i]) - float(stockCost[i])))
	msgs = msgs + stockList[i] + ' 目前股價為： ' + stockValue[i] + ' 損益： ' + str(profit) + '\n'
 ## Line Notify
 
lineUrl = "https://notify-api.line.me/api/notify"
token = "RNeFGMxis9g8JTmOQHDBovWR87elsHCzm8Udb2Kvhtr"
headers = {
 "Authorization": "Bearer " + token, 
 "Content-Type" : "application/x-www-form-urlencoded"
 }

payload = {'message':msgs}
r = requests.post(lineUrl, headers = headers, params = payload)