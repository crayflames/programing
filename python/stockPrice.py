#! /usr/bin/python3
# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
def SP(a):
	res=requests.get('https://tw.stock.yahoo.com/q/q?s='+ a )
	wes=BeautifulSoup(res.text,"html.parser")
	ss=wes.select("b")
	return ss[0].text