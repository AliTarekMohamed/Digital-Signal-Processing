from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual


root = Tk()
root.title("Normalization")
root.geometry("300x200")


def normalization():
    xSignal = []
    ySignal = []
    yNormalized = []
    
    signal = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Which Signal ?",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            xSignal.append(float(parts[0]))
            ySignal.append(float(parts[1]))

    a = int(txt1.get(1.0, "end"))
    b = int(txt2.get(1.0, "end"))
    yMin = np.min(ySignal)
    yMax = np.max(ySignal)

    for i in range(len(ySignal)):
        yNormalized.append(((ySignal[i] - yMin) * (b - a) / (yMax - yMin)) + a)

    # test normalize signal 1
    # SignalSamplesAreEqual(
    #     "Lab 2/output/normalize of signal1.txt", xSignal, yNormalized
    # )

    # test normalize signal 2
    # SignalSamplesAreEqual(
    #     "Lab 2/output/normalize of signal2.txt", xSignal, yNormalized
    # )

    fig, nrm = plt.subplots(2, 1, figsize=(6, 8))

    nrm[0].plot(xSignal, ySignal)
    nrm[0].set_title("Original signal")
    nrm[1].plot(xSignal, yNormalized)
    nrm[1].set_title("Normalized signal")

    plt.show()


frame = Frame(root)
lf1 = LabelFrame(frame, text="The minimum range")
lf2 = LabelFrame(frame, text="The maximum range")
txt1 = Text(lf1, width="50", height="2")
txt2 = Text(lf2, width="50", height="2")
button = Button(
    frame,
    command=normalization,
    text="Upload",
    width="15",
    height="2",
    font="30",
    bg="white",
    fg="black",
)
txt1.pack()
txt2.pack()
lf1.pack()
lf2.pack()
frame.pack()
button.pack()


root.mainloop()
