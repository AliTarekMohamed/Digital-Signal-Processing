from tkinter import *
import tkinter.font as font
import subprocess

root = Tk()
root.title("Week 3")
root.geometry("300x200")

def quanButton():
    subprocess.run(["python", "Week3\quantization.py"], check=True)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

quantizationButton = Button(root, text="Quantize", width="13",
                        height="3", command=quanButton, font=buttonFont)

quantizationButton.pack(pady=(20,20))
root.mainloop()