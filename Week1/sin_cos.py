from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual

root = Tk()
root.title("Digital Signal Processing")
root.geometry("550x300")


def generate_signal():
    a = float(amplitude.get(1.0, "end"))
    f = float(analog_frequency.get(1.0, "end"))
    fs = float(discrete_frequency.get(1.0, "end"))
    theta = float(Theta.get(1.0, "end"))
    var = str(List.get(ACTIVE))

    if (fs < (2 * f)) and (fs != 0):
        messagebox.showwarning("Warning", "Invalid discrete frequency")
    else:
        if var == "sin wave":
            if fs == 0:
                t = np.arange(0, 2 * np.pi, 0.01)
                x = a * np.sin((2 * np.pi * f * t) + theta)
            else:
                t = np.arange(0, 2 * np.pi, 1)
                x = a * np.sin((2 * np.pi * (f / fs) * t) + theta)
        elif var == "cos wave":
            if fs == 0:
                t = np.arange(0, 2 * np.pi, 0.01)
                x = a * np.cos((2 * np.pi * f * t) + theta)
            else:
                t = np.arange(0, 2 * np.pi, 1)
                x = a * np.cos((2 * np.pi * (f / fs) * t) + theta)

    plt.plot(t, x)
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.title("Digital Signal Processing")
    plt.show()


frame1 = Frame(root)
frame1.grid(column=1, row=1)

lbfr1 = LabelFrame(frame1, text="Signal Generation")
lbfr1.pack()

List = Listbox(lbfr1)
List.insert(0, "sin wave")
List.insert(1, "cos wave")
List.pack()


frame2 = Frame(root)
frame2.grid(column=2, row=1)

lbfr2 = LabelFrame(frame2, text="Data of Signal")
lbfr2.pack(side=LEFT)

amp_frame = LabelFrame(lbfr2, text="Amplitude")
amp_frame.pack()
amplitude = Text(amp_frame, width="50", height="2", fg="black")
amplitude.pack()

analog_frame = LabelFrame(lbfr2, text="Analog Frequency")
analog_frame.pack()
analog_frequency = Text(analog_frame, width="50", height="2", fg="black")
analog_frequency.pack()

discrete_frame = LabelFrame(lbfr2, text="Discrete Frequency")
discrete_frame.pack()
discrete_frequency = Text(discrete_frame, width="50", height="2", fg="black")
discrete_frequency.pack()

theta_frame = LabelFrame(lbfr2, text="Theta")
theta_frame.pack()
Theta = Text(theta_frame, width="50", height="2", fg="black")
Theta.pack()

gen_sig = Button(
    lbfr2,
    text="Generate Signal",
    width="13",
    height="2",
    bg="black",
    fg="white",
    command=generate_signal,
)
gen_sig.pack()
root.mainloop()
