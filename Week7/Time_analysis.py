from tkinter import *
from tkinter import filedialog
import numpy as np

root = Tk()
root.title("Time Analysis")

def Time_Analysis():
    ysignal1 = []
    ysignal2 = []
    correlationsignal = []
    TimeDelay = 0

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 7/Point2 Time analysis", title="Which Signal")

    signal2 = filedialog.askopenfilename(
        initialdir="Lab 7/Point2 Time analysis", title="Which Signal")

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

    N = len(ysignal1)

    for j in range(0, N):
        value = 0
        for n in range(0, N):
            d = n + j
            if (n + j) >= N:
                d -= N
            value += ysignal1[n] * ysignal2[d]
        correlationsignal.append(value / N)

    maxvalue = np.max(correlationsignal)
    maxindex = correlationsignal.index(maxvalue)
    TimeDelay = maxindex / int(Fs.get(1.0, "end"))
    print(TimeDelay)

Corrbutton = Button(root, width=17, height=3, text="Time Delay", command=Time_Analysis)
f = Frame(root)
lbl = LabelFrame(f, text="Enter Sampling frequency")
Fs = Text(lbl, width=50, height=2)

f.pack(pady=10)
Fs.pack()
lbl.pack()
Corrbutton.pack(pady=50)
root.mainloop()
