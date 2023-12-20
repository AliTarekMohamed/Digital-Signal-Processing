from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb
import numpy as np
import matplotlib.pyplot as plt
import utils as ut

root = Tk()
root.title("Practical Task 2")
root.geometry("500x600")

def Task2():
    result = []
    signal = []
    dct = []

    filter_type = int(Ftypetxt.get(1.0, "end"))
    fs = int(Fstxt.get(1.0, "end"))
    fs_new = int(Fsnewtxt.get(1.0, "end"))
    transition = int(transitiontxt.get(1.0, "end"))
    attenuation = int(stopbandtxt.get(1.0, "end"))
    f_min = int(F1txt.get(1.0, "end"))
    f_max = int(F2txt.get(1.0, "end"))
    m = int(Mtxt.get(1.0, "end"))
    l = int(Ltxt.get(1.0, "end"))
    
    x = filedialog.askopenfilename(
        initialdir="Project_Files/Practical task 2/Test Folder", title="Which Signal")

    with open(x, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            signal.append(float(parts[0]))
    
    # Filtering (Band Pass Filter)
    result = ut.filter(signal, filter_type, fs, transition, attenuation, f_min, f_max)
    plot(signal, result, "Filtered Signal")
    
    result.clear()

    # Resampling
    if (m == 0 and l == 0):
        mb.showwarning("Error", "Invalid M & L values")

    elif (fs_new < (2 * f_max)):
        mb.showwarning("Error", "New Fs is not valid")

    else:
        result = ut.Resampling(signal, m, l, fs, transition, attenuation, f_min, f_max)
        plot(signal, result, "Resampled Signal")

    result.clear()

    # Remove DC Component
    result = ut.Remove_dc(signal)
    plot(signal, result, "DC Removed")

    result.clear()

    # Normalization
    result = ut.Normalization(signal)
    plot(signal, result, "Normalized Signal")

    result.clear()

    # Auto Correlation
    result = ut.Auto_Correlation(signal)
    plot(signal, result, "Auto Correlation")

    result.clear()

    # preserving
    for i in range (200):
        result.append(signal[i])
    plot(signal, result, "Preserved Signal")

    # DCT
    dct = ut.DCT(result)
    N = len(dct)

    table_window = Toplevel(root)
    table_window.title("DCT")
    table = ttk.Treeview(table_window, columns=("DCT"))
    table.heading("#1", text="DCT")
    table.column("#1", width=200)
    for i in range(N):
        table.insert("", "end", values=(dct[i]))
    table.pack()
    plot(result, dct, "DCT")

    # Template Matching
    A_avg = []
    B_avg = []

    A1 = np.loadtxt("Project_Files/Practical task 2/A/ASeg1.txt")
    A2 = np.loadtxt("Project_Files/Practical task 2/A/ASeg2.txt")
    A3 = np.loadtxt("Project_Files/Practical task 2/A/ASeg3.txt")
    A4 = np.loadtxt("Project_Files/Practical task 2/A/ASeg4.txt")
    A5 = np.loadtxt("Project_Files/Practical task 2/A/ASeg5.txt")

    B1 = np.loadtxt("Project_Files/Practical task 2/B/BSeg1.txt")
    B2 = np.loadtxt("Project_Files/Practical task 2/B/BSeg2.txt")
    B3 = np.loadtxt("Project_Files/Practical task 2/B/BSeg3.txt")
    B4 = np.loadtxt("Project_Files/Practical task 2/B/BSeg4.txt")
    B5 = np.loadtxt("Project_Files/Practical task 2/B/BSeg5.txt")

    for i in range(len(A1)):
        A_avg.append((A1[i] + A2[i] + A3[i] + A4[i] + A5[i]) / 5)
        B_avg.append((B1[i] + B2[i] + B3[i] + B4[i] + B5[i]) / 5)

    ut.Matching(signal, A_avg, B_avg)

def plot(orginal, filtered, operation):
    fig, fir = plt.subplots(2, 1, figsize=(6, 8))
    fir[0].plot(orginal)
    fir[0].set_title("Original Signal")
    fir[1].plot(filtered)
    fir[1].set_title(f"{operation}")
    plt.show()

frame = Frame(root)
lable = Label(frame, text="Band Pass = 1, Band Stop = 2")
Ftypelbl = LabelFrame(frame, text="Filter Type")
Ftypetxt = Text(Ftypelbl, width=50, height=2)
Fslbl = LabelFrame(frame, text="Fs")
Fstxt = Text(Fslbl, width=50, height=2)
Fsnewlbl = LabelFrame(frame, text="Fs New")
Fsnewtxt = Text(Fsnewlbl, width=50, height=2)
transitionlbl = LabelFrame(frame, text="Transition Band")
transitiontxt = Text(transitionlbl, width=50, height=2)
stopbandlbl = LabelFrame(frame, text="Stop Band Attenuation")
stopbandtxt = Text(stopbandlbl, width=50, height=2)
F1lbl = LabelFrame(frame, text="F min")
F1txt = Text(F1lbl, width=50, height=2)
F2lbl = LabelFrame(frame, text="F max")
F2txt = Text(F2lbl, width=50, height=2)
Mlbl = LabelFrame(frame, text="M")
Mtxt = Text(Mlbl, width=50, height=2)
Llbl = LabelFrame(frame, text="L")
Ltxt = Text(Llbl, width=50, height=2)

button = Button(frame, width="17", height="3", text="Upload", command=Task2)

frame.pack()
lable.pack()
Ftypelbl.pack()
Ftypetxt.pack()
Fslbl.pack()
Fstxt.pack()
Fsnewlbl.pack()
Fsnewtxt.pack()
transitionlbl.pack()
transitiontxt.pack()
stopbandlbl.pack()
stopbandtxt.pack()
F1lbl.pack()
F1txt.pack()
F2lbl.pack()
F2txt.pack()
Mlbl.pack()
Mtxt.pack()
Llbl.pack()
Ltxt.pack()
button.pack()

root.mainloop()