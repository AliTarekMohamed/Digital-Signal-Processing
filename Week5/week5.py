from tkinter import *
import tkinter.font as font
import subprocess

root = Tk()
root.title("Week 5")
root.geometry("300x200")

def dct():
    subprocess.run(["python", "Week5\dct.py"], check=True)

def dc_remove():
    subprocess.run(["python", "Week5\dc_remove.py"], check=True)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

DCT_Button = Button(root, text="DCT", width="15", height="3", command=dct, font=buttonFont)
DC_remove_Button = Button(root, text="Remove DC", width="15", height="3", command=dc_remove, font=buttonFont)

DCT_Button.pack(pady=(20,20))
DC_remove_Button.pack(pady=(20,20))

root.mainloop()