#! /usr/bin/python3
# -*- coding: utf8 -*-
import pyautogui
import time
import tkinter as tk
from subprocess import call
import sys
from os import mkdir
IP='192.8.1.79'
tstTime=time.strftime("%Y%m%d%H%M",time.localtime())
folder='/home/roger/Desktop/ExpPHY_'+tstTime
log=' | tee '+ folder + '/expander_'
pyautogui.FAILSAFE = True
commands=['fwinfo','counters','phyinfo','showpost','disk']
cmdRt=call('ping ' + IP + ' -c 5',shell=True)
mkdir(folder)
if cmdRt == 0:
	pyautogui.hotkey('ctrl','alt','t')
	time.sleep(2)
	pyautogui.press('enter')
	x=1
	for i in range(4):
		expander='ipmitool -H ' + IP + ' -U admin -P admin -I lanplus raw 0x30 0x81 ' + str(x)
		sol='ipmitool -H ' + IP + ' -U admin -P admin -I lanplus sol activate '+ log + str(x) +'.log'
		pyautogui.typewrite(expander)
		pyautogui.press('enter')
		pyautogui.typewrite(sol)
		pyautogui.press('enter')
		time.sleep(3)
		pyautogui.press('enter')
		for j in commands:
			pyautogui.typewrite(j)
			pyautogui.press('enter')
			time.sleep(4)
		pyautogui.press(['~','.'])
		time.sleep(2)
		x+=1
	win=tk.Tk()
	win.title("Expander PHY check")
	label=tk.Label(win,text="Done")
	label.pack()
	win.mainloop()
else:
	print('ping not available')
	sys.exit(1)