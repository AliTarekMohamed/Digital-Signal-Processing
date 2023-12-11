from tkinter import *
from tkinter import filedialog
import numpy as np
import comparesignal2 as tst

root = Tk()
root.title("Fast Correlation")
root.geometry("300x200")

def dft(xOfn):
    xOfk = []
    j = 1j
    N = len(xOfn)

    for k in range (0, N):
        harmonic_value = 0
        for n in range (0, N):
            harmonic_value += (xOfn[n] * np.exp((-j * 2 * np.pi * k * n) / N))
        xOfk.append(harmonic_value)

    return xOfk

def idft(yOfk):
    yOfn = []
    j = 1j
    N = len(yOfk)

    for n in range(0, N):
        harmonic_value = 0
        for k in range(0, N):
            harmonic_value += (1 / N) * (yOfk[k] * np.exp((j * 2 * np.pi * n * k) / N))
        yOfn.append(round(np.real(harmonic_value)))
    
    return yOfn

def read_signal():
    ySignal = []
    signal = filedialog.askopenfilename(
        initialdir="Lab 8/Fast Correlation", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ySignal.append(float(parts[1]))

    return ySignal

def fast_correlation():
    ySignal1 = []
    ySignal2 = []
    xOfk = []
    hOfk = []
    yOfk = []
    yOfn = []

    aoc = var.get()

    if (aoc == 'Auto Correlation'):
        ySignal1 = read_signal()
        N = len(ySignal1)

        # DFT
        xOfk = dft(ySignal1)

        # CORRELATION
        for i in range(0, N):
            yOfk.append(np.conj(xOfk[i]) * xOfk[i])

        # IDFT
        tmp = idft(yOfk)

        yOfn.clear()
        for i in tmp:
            yOfn.append(i / N)

    elif (aoc == 'Cross Correlation'):
        ySignal1 = read_signal()
        ySignal2 = read_signal()
        N = len(ySignal1)

        #DFT
        xOfk = dft(ySignal1)
        hOfk = dft(ySignal2)

        # CORRELATION
        for i in range(len(xOfk)):
            yOfk.append(np.conj(xOfk[i]) * hOfk[i])

        # IDFT
        tmp = idft(yOfk)
    
        yOfn.clear()
        for i in tmp:
            yOfn.append(i / N)

        tst.SignalSamplesAreEqual("Lab 8/Fast Correlation/Corr_Output.txt", yOfn)
        
    print(yOfn)

frame = Frame(root)

var = StringVar()
auto = Radiobutton(frame, width="50", height="2", text="Auto Correlation", value="Auto Correlation", variable=var)
cross = Radiobutton(frame, width="50", height="2", text="Cross Correlation", value="Cross Correlation", variable=var)
Corrbutton = Button(frame, width="17", height="3", text="Fast Correlation", command=fast_correlation)

frame.pack()
auto.pack()
cross.pack()
Corrbutton.pack()
root.mainloop()
