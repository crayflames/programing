#! /usr/bin/env python3
# -*- coding: utf8 -*-
import os
#列出資料夾底下的檔案，清單形式
os.listdir()
#修改檔案目錄
os.chmod('file',stat.S_IWOTH)
#檔案存在
os.path.exists('/sys/class/net/eth0')
#切換路徑
os.chdir(path)
#是目錄回傳true
os.path.isdir('/')
#是否為檔案
os.path.isfile('file')
#回傳當前路徑
os.getcwd()
