from tkinter import *
import tkinter.font as font
import subprocess

root = Tk()
root.title("Week 4")
root.geometry("300x200")

def FourierTransform():
    subprocess.run(["python", "Week4\Fouriertransform.py"], check=True)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')
FourierButton = Button(root, text="Fourier Transfrom", width="15", height="3", command=FourierTransform, font=buttonFont)

FourierButton.pack(pady=(20,20))
root.mainloop()