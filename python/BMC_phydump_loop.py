#! /usr/bin/python3
# -*- coding: utf8 -*-
import pyautogui
import time
import tkinter as tk
from subprocess import call
import sys
from os import mkdir
tstTime=time.strftime("%Y%m%d%H%M",time.localtime())
folder='/home/roger/Desktop/ExpPHY_'+tstTime
def finish():
	weight,height = pyautogui.size()
	wt=int(weight/2)
	hg=int(height/2)
	folder
	win=tk.Tk()
	win.title("ExpanderPHYcheck")
	label=tk.Label(win,text="Done !! log save to" + folder)
	p="270x60+"+ str(wt)+"+"+str(hg)
	win.geometry(p)
	label.pack()
	win.mainloop()

def run(IP,TIME):
	pyautogui.FAILSAFE = True
	IPMITOOL='ipmitool -H '
	ipmiPara=' -U admin -P admin -I lanplus'
	commands=['fwinfo','counters','phyinfo','showpost','disk']
	log=' | tee '+ folder +'/expander_'
	cmdRt=mkdir(folder)
	if cmdRt==0:
		print("Create test log to folder path :" + folder)
	pwrStat=IPMITOOL + IP + ipmiPara + ' power status | grep on'
	startTime=time.time()
	endTime=time.time()
	cmdRt=call('ping ' + IP + ' -c 3', shell=True)
	if cmdRt == 0:
		pyautogui.hotkey('ctrl','alt','t')
		while (endTime-startTime) < int(TIME):
			time.sleep(2)
			pyautogui.press('enter')
			x=1
			logtime=time.strftime("%Y%m%d%H%M",time.localtime())
			for i in range(4):
				#ipmi 切換expander
				expander = IPMITOOL + IP + ipmiPara + ' raw 0x30 0x81 ' + str(x)
				#切換sol console
				sol = IPMITOOL + IP + ipmiPara + ' sol activate' + log + str(x) + '_'+ str(logtime) + '.log'
				pyautogui.typewrite(expander)
				pyautogui.press('enter')
				pyautogui.typewrite(sol)
				pyautogui.press('enter')
				time.sleep(3)
				pyautogui.press('enter')
				for j in commands:
					pyautogui.typewrite(j)
					pyautogui.press('enter')
					time.sleep(3)
				pyautogui.press(['~','.'])
				time.sleep(2)
				x+=1
				endTime=time.time()
			while not call(pwrStat,shell=True):
				print("Wait for JBOD power off")
				endTime=time.time()
				if (endTime-startTime) > int(TIME):
					time.sleep(2)
					pyautogui.typewrite('exit')
					pyautogui.press('enter')
					break
				#等power off再跳出
				time.sleep(30)
			print("Test running over " + str(endTime-startTime) + "seconds !")
			while call(pwrStat,shell=True):
				print("Wait for JBOD power on")
				endTime=time.time()
				if (endTime-startTime) > int(TIME):
					time.sleep(2)
					pyautogui.typewrite('exit')
					pyautogui.press('enter')
					break
				#等待Exp醒來
				time.sleep(90)
			print("Test running over " + str(endTime-startTime) + "seconds !")
	else:
		print('No JBOD connected')
		sys.exit(1)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("\033[31m" + "\
	Input JBOD expanderIP! and test total seconds.\n \
	such as : python3 BMC_phydump_loop.py 192.168.0.1 3600" + "\033[0m")
		sys.exit(1)
	print("\033[31m" + "Warning don't touch keyboard and mouce that will be cause that script not under controll" + "\033[0m")
	run(sys.argv[1],sys.argv[2])
	finish()

