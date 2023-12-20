from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import utils as ut
import CompareSignal as tst

root = Tk()
root.title("Resampling")
root.geometry("500x400")

N = 0
indices = []

def Window_Method():
    global N
    global indices
    indices = []
    w = []

    attenutation = int(stopbandtxt.get(1.0, "end"))
    transition = int(transitiontxt.get(1.0, "end"))
    samplingfreq = int(samplingfrequencytxt.get(1.0, "end"))

    if (attenutation <= 21):
        N = np.ceil((samplingfreq * 0.9) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(1)

    elif (attenutation <= 44):
        N = np.ceil((samplingfreq * 3.1) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(0.5 + (0.5 * np.cos((2 * np.pi * i) / N)))

    elif (attenutation <= 53):
        N = np.ceil((samplingfreq * 3.3) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(0.54 + (0.46 * np.cos((2 * np.pi * i) / N)))

    elif (attenutation <= 74):
        N = np.ceil((samplingfreq * 5.5) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(0.42 + (0.5 * np.cos((2 * np.pi * i) / (N - 1))) + (0.08 * np.cos((4 * np.pi * i) / (N - 1))))

    return w

def upsampling(signal, l):
    up_sampled = []
    for i in range(len(signal)):
        up_sampled.append(signal[i])
        if (i == (len(signal) - 1)):
            break
        for j in range(l - 1):
            up_sampled.append(0)

    return up_sampled

def downsampling(signal, m):
    down_sampled = []
    for i in range(len(signal)):
        if ((i % m) == 0):
            down_sampled.append(signal[i])
        else:
            continue

    return down_sampled

def low_pass_filter(signal):
    global N
    w = []
    h = []
    filter = []
    result = []

    w = Window_Method()

    f = int(Ftxt.get(1.0, "end"))
    transition = int(transitiontxt.get(1.0, "end"))
    samplingfreq = int(samplingfrequencytxt.get(1.0, "end"))

    Fc = (f + (transition / 2)) / samplingfreq
    for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
        if (i == 0):
            h.append(2 * Fc)
            continue
        h.append(2 * Fc * ((np.sin(i * (2 * np.pi * Fc))) / (i * (2 * np.pi * Fc))))

    filter = ut.multiply(w, h)
    result = ut.fast_convolution(filter, signal)
    return result

def Resampling():
    global N
    N = int(N)
    M = int(Mtxt.get(1.0, "end"))
    L = int(Ltxt.get(1.0, "end"))

    if (M == 0 and L == 0):
        messagebox.showwarning("Error", "Invalid M & L values")
        return

    ySignal = []
    temp = []
    temp2 = []
    result = []

    signal = filedialog.askopenfilename(initialdir="Project_Files/Practical task 1/Sampling test cases", title="Which Signal")
    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ySignal.append(int(parts[1]))

    if(M == 0 and L != 0):
        temp = upsampling(ySignal, L)
        result = low_pass_filter(temp)

    elif(M != 0 and L == 0):
        temp = low_pass_filter(ySignal)
        result = downsampling(temp, M)

    elif(M != 0 and L != 0):
        temp = upsampling(ySignal, L)
        temp2 = low_pass_filter(temp)
        result = downsampling(temp2, M)

    for i in range(int(((N - 1) / 2) + 1), int(len(result) - ((N - 1) / 2))):
        indices.append(i)

    print(len(indices))
    print(len(result))
    test(M, L, indices, result)
    plot(ySignal, result)

def test(m, l, indices, result):
    if(m == 0 and l != 0):
        tst.Compare_Signals("Project_Files/Practical task 1/Sampling test cases/Testcase 2/Sampling_Up.txt", indices, result)

    elif(m != 0 and l == 0):
        tst.Compare_Signals("Project_Files/Practical task 1/Sampling test cases/Testcase 1/Sampling_Down.txt", indices, result)
        
    elif(m != 0 and l != 0):
        tst.Compare_Signals("Project_Files/Practical task 1/Sampling test cases/Testcase 3/Sampling_Up_Down.txt", indices, result)

def plot(orginal, resampled):
    fig, fir = plt.subplots(2, 1, figsize=(6, 8))
    fir[0].plot(orginal)
    fir[0].set_title("Original Signal")
    fir[1].plot(resampled)
    fir[1].set_title("Resampled Signal")
    plt.show()

frame = Frame(root)
Samplingfreqlbl = LabelFrame(frame, text="Sampling frequency")
samplingfrequencytxt = Text(Samplingfreqlbl, width=50, height=2)
stopbandlbl = LabelFrame(frame, text="StopBand attenuation")
stopbandtxt = Text(stopbandlbl, width=50, height=2)
transitionlbl = LabelFrame(frame, text="Transition width")
transitiontxt = Text(transitionlbl, width=50, height=2)
Flbl = LabelFrame(frame, text="Cut Off Frequency")
Ftxt = Text(Flbl, width=50, height=2)
Mlbl = LabelFrame(frame, text="M")
Mtxt = Text(Mlbl, width=50, height=2)
Llbl = LabelFrame(frame, text="L")
Ltxt = Text(Llbl, width=50, height=2)

frame.pack()
Samplingfreqlbl.pack()
samplingfrequencytxt.pack()
stopbandlbl.pack()
stopbandtxt.pack()
transitionlbl.pack()
transitiontxt.pack()
Flbl.pack()
Ftxt.pack()
Mlbl.pack()
Mtxt.pack()
Llbl.pack()
Ltxt.pack()

Filterbutton = Button(frame, width="17", height="3", text="Filter",command=Resampling)
Filterbutton.pack()

root.mainloop()
