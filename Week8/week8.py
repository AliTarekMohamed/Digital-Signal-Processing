from tkinter import *
import tkinter.font as font
import subprocess

dialog = Tk()
dialog.title("Week 7")
dialog.geometry("400x400")


def fast_correlation():
    subprocess.run(["python", "Week8/fast_correlation.py"], check=True)


def fast_convolution():
    subprocess.run(["python", "Week8/fast_convolution.py"], check=True)


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

fast_correlation_button = Button(dialog, text="Fast Correlation", width="13", height="3", command=fast_correlation, font=buttonFont)
fast_convolution_button = Button(dialog, text="Fast Convolution", width="13", height="3", command=fast_convolution, font=buttonFont)

fast_correlation_button.pack(pady=(20, 20))
fast_convolution_button.pack(pady=(0, 20))

dialog.mainloop()
