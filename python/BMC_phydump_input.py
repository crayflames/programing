#! /usr/bin/python3
# -*- coding: utf8 -*-
import pyautogui
import time
import tkinter as tk
from subprocess import call
import sys
import re
import os
def run(IP):
	tstTime=time.strftime("%Y%m%d%H%M",time.localtime())
	folder='/home/roger/Desktop/ExpPHY_'+tstTime
	log=' | tee '+ folder + '/expander_'
	os.mkdir(folder)
	pyautogui.FAILSAFE = True
	commands=['fwinfo','counters','phyinfo','showpost','disk']
	cmdRt=call('ping ' + IP + ' -c 5',shell=True)
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
	else:
		print('ping not available')
		sys.exit(1)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Input JBOD expanderIP!")
		sys.exit(1)
	x=re.match(r'\d.\d.\d.\d',sys.argv[1])
	if not x:
		sys.exit()
	run(sys.argv[1])
	win=tk.Tk()
	win.title("tk title")
	label=tk.Label(win,text="Done")
	label.pack()
	win.mainloop()