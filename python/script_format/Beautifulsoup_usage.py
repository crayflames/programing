#! /usr/bin/python3
# -*- coding: utf8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html,"lxml")
for child in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
	print(child)