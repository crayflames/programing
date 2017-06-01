#! /usr/bin/python3
# -*- coding: utf8 -*-
import pyautogui
import time
pyautogui.FAILSAFE = True

weight,height = pyautogui.position()
print(weight,height )

pyautogui.moveTo(weight,height,duration=2)
pyautogui.click()
pyautogui.press('enter')
pyautogui.hotkey('ctrl','alt','t')
time.sleep(1)
pyautogui.typewrite('ls')
pyautogui.press('enter')
time.sleep(2)
## 找到圖片的位置,回傳圖形的範圍值
print(pyautogui.locateOnScreen('/home/roger/Desktop/close.png'))
a,b,c,d=pyautogui.locateOnScreen('/home/roger/Desktop/close.png')
## 取得中心點
x,y=pyautogui.center((a,b,c,d))
pyautogui.moveTo(x,y)