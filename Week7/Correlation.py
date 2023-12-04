from tkinter import *
from tkinter import filedialog
import comparesignal2 as tst
import numpy as np


dialog = Tk()
dialog.title("Correlation")
dialog.geometry("300x200")


def correlation(ysignal1, ysignal2):
    r = []
    correlationsignal = []

    N = len(ysignal1)
    r.clear()

    for j in range(0, N):
        value = 0
        for n in range(0, N):
            d = n + j
            if (d >= N):
                d -= N
            value += (ysignal1[n] * ysignal2[d])
        r.append(value / N)

    denominator = 0
    y1square = 0
    y2square = 0

    for i in range(0, N):
        y1square += np.power(ysignal1[i], 2)
        y2square += np.power(ysignal2[i], 2)

    denominator = (np.sqrt(y1square * y2square)) / N

    correlationsignal.clear()
    for i in r:
        correlationsignal.append(i / denominator)

    return correlationsignal

def perpare_signal():
    ysignal1 = []
    ysignal2 = []

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 7\Point1 Correlation", title="Which Signal")

    signal2 = filedialog.askopenfilename(
        initialdir="Lab 7\Point1 Correlation", title="Which Signal")

    with open(signal1, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ysignal1.append(float(parts[1]))

    with open(signal2, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ysignal2.append(float(parts[1]))

    correlationsignal = correlation(ysignal1, ysignal2)

    tst.SignalSamplesAreEqual("Lab 7\Point1 Correlation\CorrOutput.txt", correlationsignal)

Corrbutton = Button(dialog, width=17, height=3, text="Correlation", command=perpare_signal)
Corrbutton.pack(pady=50)
dialog.mainloop()