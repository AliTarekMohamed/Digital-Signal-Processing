from tkinter import *
from tkinter import filedialog
import numpy as np
import ConvTest as tst

root = Tk()
root.title("Fast Convolution")
root.geometry("300x150")

def fast_convolution():
    index1 = []
    index2 = []
    indices = []
    ySignal1 = []
    ySignal2 = []
    xOfk1 = []
    xOfk2 = []
    yOfk = []
    convsignal = []

    # READ SIGNALS
    signal1 = filedialog.askopenfilename(
        initialdir="Lab 8/Fast Convolution", title="Which Signal")

    signal2 = filedialog.askopenfilename(
        initialdir="Lab 8/Fast Convolution", title="Which Signal")

    with open(signal1, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            index1.append(int(parts[0]))
            ySignal1.append(int(parts[1]))

    with open(signal2, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            index2.append(int(parts[0]))
            ySignal2.append(int(parts[1]))

    min = index1[0] + index2[0]
    max = index1[len(index1) - 1] + index2[len(index2) - 1]

    for i in range(min, max+1):
        indices.append(i)

    N1 = len(ySignal1)
    N2 = len(ySignal2)
    new_len = N1 + N2 - 1

    for i in range(new_len - len(ySignal1)):
        ySignal1.append(0)
    for i in range(new_len - len(ySignal2)):
        ySignal2.append(0)

    j =1j
    
    #DFT
    for k in range (0, new_len):
        harmonic_value = 0
        for n in range (0, new_len):
            harmonic_value += (ySignal1[n] * np.exp((-j * 2 * np.pi * k * n) / new_len))
        xOfk1.append(harmonic_value)

    for k in range (0, new_len):
        harmonic_value = 0
        for n in range (0, new_len):
            harmonic_value += (ySignal2[n] * np.exp((-j * 2 * np.pi * k * n) / new_len))
        xOfk2.append(harmonic_value)

    #CONVOLUTION
    for i in range(new_len):
        yOfk.append(xOfk1[i] * xOfk2[i])

    #IDFT
    for n in range(0, new_len):
        harmonic_value = 0
        for k in range(0, new_len):
            harmonic_value += (1 / new_len) * (yOfk[k] * np.exp((j * 2 * np.pi * n * k) / new_len))
        convsignal.append(round(np.real(harmonic_value)))

    print(convsignal)

    #TST
    tst.ConvTest(indices, convsignal)

Convbutton = Button(root, width="17", height="3", text="Fast Convolution", command=fast_convolution)

Convbutton.pack()
root.mainloop()
