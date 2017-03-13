#! /usr/bin/python3
# -*- coding: utf8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html,"lxml")
print(bs0bj.html.body.h1.text)