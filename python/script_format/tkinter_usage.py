#! /usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
win=tk.Tk()
win.title("tk title")
label=tk.Label(win,text="Hello World")
#label.grid(column=10,row=0)
label.pack()
button=tk.Button(win,text="OK")
button.grid(column=1,row=10)
button.pack()
win.mainloop()