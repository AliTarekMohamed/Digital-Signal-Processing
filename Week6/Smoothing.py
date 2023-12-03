from tkinter import *
from tkinter import filedialog
import comparesignals as tst
import matplotlib.pyplot as plt


dialog = Tk()
dialog.geometry("250x250")
dialog.title("Smoothing")

# 1,3,5,7,9,11,13,15,17,19

def Smoothing():
    xsignal = []
    ysignal = []
    smoothedsignal = []

    signal = filedialog.askopenfilename(
        initialdir="Lab 2\input", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            xsignal.append(float(parts[0]))
            ysignal.append(float(parts[1]))

    windowsize = int(Nofstrides.get("1.0", END))

    for i in range(0, len(ysignal)-windowsize + 1):
        Smoothedvalue = 0
        for j in range(i, i+windowsize):
            Smoothedvalue += ysignal[j]

        smoothedsignal.append(Smoothedvalue/windowsize)

    tst.SignalSamplesAreEqual(
        "Lab 6\Moving Average\OutMovAvgTest1.txt", xsignal, smoothedsignal)
    tst.SignalSamplesAreEqual(
        "Lab 6\Moving Average\OutMovAvgTest2.txt", xsignal, smoothedsignal)


frm = Frame(dialog)
txtLabel = LabelFrame(frm, text="Enter the Window Size")
Nofstrides = Text(txtLabel, width=50, height=2)
btn = Button(dialog, text="Smooth", width=20, height=4, command=Smoothing)

frm.pack()
txtLabel.pack()
Nofstrides.pack()
btn.pack(pady=40)
dialog.mainloop()
