<<<<<<< HEAD
#! /usr/bin/env python3
=======
#! /usr/bin/python3
>>>>>>> a72756bf9dc1e38b2e1f5f5dd848a3219769d4a7
# -*- coding: utf8 -*-
import pyautogui
import time
import tkinter as tk
<<<<<<< HEAD
from subprocess import call
import sys
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
		sol='ipmitool -H 192.8.1.180 -U admin -P admin -I lanplus sol activate | tee expander_' + str(x) +'.log'
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
else:
	print('ping not available')
	sys.exit(1)
=======
import subprocess
import sys
IP='192.8.1.180'
IPMITOOL='ipmitool -H '
ipmiPara=' -U admin -P admin -I lanplus'
log=' | tee expander_'
pyautogui.FAILSAFE = True
array=['fwinfo','counters','phyinfo','showpost']
cmdRt=subprocess.call('ping ' + IP + ' -c 3', shell=True)
startTime=time.time()
endTime=time.time()
while (endTime-startTime) < 1000:
	if cmdRt == 0:
		pyautogui.hotkey('ctrl','alt','t')
		time.sleep(2)
		pyautogui.press('enter')
		x=1
		for i in range(4):
			expander = IPMITOOL + IP + ipmiPara + ' raw 0x30 0x81 ' + str(x)
			sol = IPMITOOL + IP + ipmiPara + ' sol activate' + str(x) + log + '.log'
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
			endTime=time.time()
	else:
		print('Network unavailable')
		#sys.exit(1)
		endTime=time.time()

win=tk.Tk()
win.title("tk title")
label=tk.Label(win,text="Done")
label.pack()
win.mainloop()
>>>>>>> a72756bf9dc1e38b2e1f5f5dd848a3219769d4a7
