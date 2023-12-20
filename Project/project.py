from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Project")
dialog.geometry("400x300")

def Filter():
    subprocess.run(["python", "Project/fir.py"], check=True)

def Resampling():
    subprocess.run(["python", "Project/resampling.py"], check=True)

def Task2():
    subprocess.run(["python", "Project/task2.py"], check=True)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

Filterbutton = Button(dialog, text="Filtering", width="13", height="3", command=Filter, font=buttonFont)
Resamplingbutton = Button(dialog, text="Resampling", width="13", height="3", command=Resampling, font=buttonFont)
Task2button = Button(dialog, text="Task2", width="13", height="3", command=Task2, font=buttonFont)

Filterbutton.pack(pady=(20, 20))
Resamplingbutton.pack(pady=(0, 20))
Task2button.pack(pady=(0, 20))

dialog.mainloop()
