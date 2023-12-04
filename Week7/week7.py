from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 7")
dialog.geometry("400x400")


def Correlation():
    subprocess.run(["python", "Week7/Correlation.py"], check=True)


def Time_analysis():
    subprocess.run(["python", "Week7/Time_analysis.py"], check=True)


def Template_Matching():
    subprocess.run(["python", "Week7/matching.py"], check=True)


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

correlationbutton = Button(dialog, text="Correlation", width="13", height="3", command=Correlation, font=buttonFont)
timebutton = Button(dialog, text="Time Analysis", width="13", height="3", command=Time_analysis, font=buttonFont)
matchingbutton = Button(dialog, text="Matching", width="13", height="3", command=Template_Matching, font=buttonFont)

correlationbutton.pack(pady=(20, 20))
timebutton.pack(pady=(0, 20))
matchingbutton.pack(pady=(0, 20))

dialog.mainloop()
