#! /usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
import pyautogui
weight,height = pyautogui.size()
wt=int(weight/2)
hg=int(height/2)
print (wt,hg)
win=tk.Tk()

p="270x60+"+ str(wt)+"+"+str(hg)
print(p)
#window size
win.geometry(p)

win.title("tk title")
label=tk.Label(win,text="Done !! log save to00000000000000000000000000000000000")
#label.grid(column=10,row=0)
label.pack()
button=tk.Button(win,text="OK")
button.pack()
win.mainloop()
