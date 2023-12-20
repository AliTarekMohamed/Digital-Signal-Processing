from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import utils as ut
import CompareSignal as tst

root = Tk()
root.title("Filtering")
root.geometry("500x500")

N = 0
flag1 = 0
flag2 = 0

w = []
h = []
indices = []

def Window_Method():
    global N
    global indices

    N = 0
    w.clear()
    indices.clear()

    samplingfreq = int(samplingfrequencytxt.get(1.0, "end"))
    transition = int(transitiontxt.get(1.0, "end"))
    attenuation = int(stopbandtxt.get(1.0, "end"))

    if (attenuation <= 21):
        N = np.ceil((samplingfreq * 0.9) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(1)

    elif (attenuation <= 44):
        N = np.ceil((samplingfreq * 3.1) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(0.5 + (0.5 * np.cos((2 * np.pi * i) / N)))

    elif (attenuation <= 53):
        N = np.ceil((samplingfreq * 3.3) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(0.54 + (0.46 * np.cos((2 * np.pi * i) / N)))

    elif (attenuation <= 74):
        N = np.ceil((samplingfreq * 5.5) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            indices.append(i)
            w.append(0.42 + (0.5 * np.cos((2 * np.pi * i) / (N - 1))) + (0.08 * np.cos((4 * np.pi * i) / (N - 1))))

    return w


def Filter_Type():
    global flag1
    global N
    N = int(N)
    h.clear()

    samplingfreq = int(samplingfrequencytxt.get(1.0, "end"))
    transition = int(transitiontxt.get(1.0, "end"))
    filtertype = int(Filtertypetxt.get(1.0, "end"))
    f1 = int(F1txt.get(1.0, "end"))
    f2 = int(F2txt.get(1.0, "end"))
    
    Fc1 = 0
    Fc2 = 0

    if (filtertype == 0): # Low Pass Filter
        flag1 = 1
        Fc1 = (f1 + (transition / 2)) / samplingfreq
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(2 * Fc1)
                continue
            h.append(2 * Fc1 * ((np.sin(i * (2 * np.pi * Fc1))) / (i * (2 * np.pi * Fc1))))

    elif (filtertype == 1): # High Pass Filter
        flag1 = 2
        Fc1 = (f1 - (transition / 2)) / samplingfreq
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(1 - (2 * Fc1))
                continue
            h.append(-2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1))))

    elif (filtertype == 2): # Band Pass Filter
        flag1 = 3
        Fc1 = (f1 - (transition / 2)) / samplingfreq
        Fc2 = (f2 + (transition / 2)) / samplingfreq

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(2 * (Fc2 - Fc1))
                continue
            h.append((2 * Fc2 * (np.sin(i * (2 * np.pi * Fc2)) / (i * (2 * np.pi * Fc2)))) - (2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1)))))

    elif (filtertype == 3): # Band Reject Filter
        flag1 = 4
        Fc1 = (f1 + (transition / 2)) / samplingfreq
        Fc2 = (f2 - (transition / 2)) / samplingfreq

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(1 - (2 * (Fc2 - Fc1)))
                continue
            h.append((2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1)))) - (2 * Fc2 * (np.sin(i * (2 * np.pi * Fc2)) / (i * (2 * np.pi * Fc2)))))

    return h


def Filtering():
    global flag2
    flag2 = 0
    w = Window_Method()
    h = Filter_Type()
    result = ut.multiply(w, h)
    test(indices, result)
    plot(h, result)


def Filtering_Uploaded_Signal():
    global flag1
    global flag2
    flag1 = 0
    flag2 = 1

    ySignal = []
    signalresult = []
    result = []

    ySignal.clear()
    result.clear()
    signalresult.clear()

    signal = filedialog.askopenfilename(
        initialdir="Project_Files/Practical task 1/FIR test cases", title="Which Signal")

    with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ySignal.append(int(parts[1]))

    w = Window_Method()
    h = Filter_Type()
    result = ut.multiply(w, h)
    signalresult = ut.fast_convolution(result, ySignal)
    test(indices, signalresult)
    plot(ySignal, signalresult)

def plot(orginal, filtered):
    fig, fir = plt.subplots(2, 1, figsize=(6, 8))
    fir[0].plot(orginal)
    fir[0].set_title("Original Signal")
    fir[1].plot(filtered)
    fir[1].set_title("Filtered Signal")
    plt.show()

def test(indices, signal):
    if (flag2 == 0):
        if(flag1 == 1):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 1/LPFCoefficients.txt", indices, signal)
        if(flag1 == 2):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 3/HPFCoefficients.txt", indices, signal)
        if(flag1 == 3):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 5/BPFCoefficients.txt", indices, signal)
        if(flag1 == 4):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 7/BSFCoefficients.txt", indices, signal)
    else:
        if(flag1 == 1):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 2/ecg_low_pass_filtered.txt", indices, signal)
        if(flag1 == 2):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 4/ecg_high_pass_filtered.txt", indices, signal)
        if(flag1 == 3):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 6/ecg_band_pass_filtered.txt", indices, signal)
        if(flag1 == 4):
            tst.Compare_Signals("Project_Files/Practical task 1/FIR test cases/Testcase 8/ecg_band_stop_filtered.txt", indices, signal)

frame = Frame(root)

lbl = Label(root, text="Low Pass: 0, High Pass: 1, Band Pass: 2, Band Reject: 3")
Filtertypelbl = LabelFrame(frame, text="Filter Type")
Filtertypetxt = Text(Filtertypelbl, width=50, height=2)
Samplingfreqlbl = LabelFrame(frame, text="Sampling Frequency")
samplingfrequencytxt = Text(Samplingfreqlbl, width=50, height=2)
transitionlbl = LabelFrame(frame, text="Transition Band")
transitiontxt = Text(transitionlbl, width=50, height=2)
stopbandlbl = LabelFrame(frame, text="Stop Band Attenuation")
stopbandtxt = Text(stopbandlbl, width=50, height=2)
F1lbl = LabelFrame(frame, text="F1")
F1txt = Text(F1lbl, width=50, height=2)
F2lbl = LabelFrame(frame, text="F2")
F2txt = Text(F2lbl, width=50, height=2)


Filterbutton = Button(frame, width="17", height="3", text="Filter", command=Filtering)

uploadbutton = Button(frame, width="17", height="3", text="Upload Signal", command=Filtering_Uploaded_Signal)

lbl.pack()
frame.pack()
Filtertypelbl.pack()
Filtertypetxt.pack()
Samplingfreqlbl.pack()
samplingfrequencytxt.pack()
transitionlbl.pack()
transitiontxt.pack()
stopbandlbl.pack()
stopbandtxt.pack()
F1lbl.pack()
F1txt.pack()
F2lbl.pack()
F2txt.pack()

Filterbutton.pack()
uploadbutton.pack()
root.mainloop()
