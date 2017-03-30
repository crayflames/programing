#! /usr/bin/python3
# -*- coding: utf8 -*-
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pags/page1.html")
print(html.read())