from tkinter import *
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual

root = Tk()
root.title("Accumulation")
root.geometry("300x200")


def accumulation():
    xSignal = []
    ySignal = []
    yAccumulated = []

    signal = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Signal 2",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            xSignal.append(float(parts[0]))
            ySignal.append(float(parts[1]))

    y = 0

    for i in range(0, len(ySignal)):
        y += ySignal[i]
        yAccumulated.append(y)

    # test accumulation
    SignalSamplesAreEqual(
        "Lab 2/output/accumulation for signal1.txt",
        xSignal,
        yAccumulated,
    )

    fig, acc = plt.subplots(2, 1, figsize=(6, 8))

    acc[0].plot(xSignal, ySignal)
    acc[0].set_title("Original signal")
    acc[1].plot(xSignal, yAccumulated)
    acc[1].set_title("Accumulated signal")

    plt.show()


button = Button(
    root,
    command=accumulation,
    text="Upload",
    width="15",
    height="2",
    font="30",
    bg="white",
    fg="black",
)
button.pack()

root.mainloop()
