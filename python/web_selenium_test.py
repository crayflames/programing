#! /usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
web = webdriver.Chrome("/home/roger/Downloads/chromedriver")
web.get('http://www.books.com.tw/')
inputElement = web.find_element_by_name("key")
inputElement.send_keys("python")
inputElement.submit()
web2=web.current_url
res=urlopen(web2)
wes=BeautifulSoup(res,"html.parser")
#s=wes.findAll("li",{"class":"item"})
ss=wes.findAll("li",attrs={"class":"item"})
print(ss)
web.close()
'''


#xx=BeautifulSoup(str(ss),"html.parser")
for _ in range(len(xx)):
	print(xx[_].text.strip())
web.find_element_by_class_name('nxt').click() 
#web.close()
'''
