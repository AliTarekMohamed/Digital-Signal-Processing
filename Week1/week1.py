from tkinter import *
import tkinter.font as font
import subprocess

root = Tk()
root.title("Week 1")
root.geometry("300x200")

def signalbutton():
    subprocess.run(["python", "Week1/task1.py"], check=True)
    
def sin_cosbutton():
    subprocess.run(["python", "Week1/sin_cos.py"], check=True)
    
buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

signal = Button(root, text="Task 1", width="13",
                            height="3", command=signalbutton, font=buttonFont)

sin_cos = Button(root, text="Task 2", width="13",
                            height="3", command=sin_cosbutton, font=buttonFont)


signal.pack(pady=(0,20))
sin_cos.pack(pady=(0,20))
root.mainloop()