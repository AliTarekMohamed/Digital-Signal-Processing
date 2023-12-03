from tkinter import *
import tkinter.font as font
import subprocess

root = Tk()
root.title("Week 6")
root.geometry("400x400")

def Smoothing():
    subprocess.run(["python", "Week6/Smoothing.py"], check=True)

def Sharpening():
    subprocess.run(["python", "Week6/Sharpening.py"], check=True)

def Delay_or_Advance():
    subprocess.run(["python", "Week6/delay&advance.py"], check=True)

def remove_dc():
    subprocess.run(["python", "Week6/remove_dc.py"], check=True)

def Convolution():
    subprocess.run(["python", "Week6\convolution.py"], check=True)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

smottingbutton = Button(root, text="Smoothing", width="17", height="3", command=Smoothing, font=buttonFont)
Sharpeningbutton = Button(root, text="Sharpening", width="17", height="3", command=Sharpening, font=buttonFont)
DoA_Button = Button(root, text="Delaying & Advancing", width="17", height="3", command=Delay_or_Advance, font=buttonFont)
DC_remove_Button = Button(root, text="Remove DC", width="17", height="3", command=remove_dc, font=buttonFont)
Convolutionbutton = Button(root, text="Convolution", width="17", height="3", command=Convolution, font=buttonFont)

smottingbutton.pack(pady=(0, 20))
Sharpeningbutton.pack(pady=(0, 20))
DoA_Button.pack(pady=(0,20))
DC_remove_Button.pack(pady=(0,20))
Convolutionbutton.pack(pady=(0, 20))

root.mainloop()