#!/usr/bin/python3
import tkinter as tk
import picamera
from time import sleep
def press():
	pass
def preview():
	pass


camera=picamera.PiCamera()
win=tk.Tk()
win=configure(background="yellow")
takePIC=tk.Button(win,text="take",command=press)
takePreview=tk.Button(win,text="preview",command=preview)
takePIC.pack()
takePreview.pack()
win.mainloop()
