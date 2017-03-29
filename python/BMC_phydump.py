#! /usr/bin/python3
# -*- coding: utf8 -*-
import pyautogui
import time
import tkinter as tk
import subprocess
pyautogui.FAILSAFE = True
array=['fwinfo','counters','phyinfo','showpost']
cmdRt=subprocess.call('ping 192.8.1.180 -c 5',shell=True)
if cmdRt == 0:
	pyautogui.hotkey('ctrl','alt','t')
	time.sleep(2)
	pyautogui.press('enter')
	x=1
	for i in range(4):
		expander='ipmitool -H 192.8.1.180 -U admin -P admin -I lanplus raw 0x30 0x81 ' + str(x)
		sol='ipmitool -H 192.8.1.180 -U admin -P admin -I lanplus sol activate'
		pyautogui.typewrite(expander)
		pyautogui.press('enter')
		pyautogui.typewrite(sol)
		pyautogui.press('enter')
		time.sleep(3)
		pyautogui.press('enter')
		for j in array:
			pyautogui.typewrite(j)
			pyautogui.press('enter')
			time.sleep(4)
		pyautogui.press(['~','.'])
		time.sleep(2)
		x+=1
	win=tk.Tk()
	win.title("tk title")
	label=tk.Label(win,text="Done")
	label.pack()
	win.mainloop()
