from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual


root = Tk()
root.title("Shifting")
root.geometry("300x200")


def shifting():
    xSignal = []
    ySignal = []
    xShifted = []

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

    const = int(txt.get(1.0, "end"))

    for i in range(0, len(xSignal)):
        xShifted.append(xSignal[i] - const)

    # test shifting by add 500
    # SignalSamplesAreEqual("Lab 2/output/shifting by add 500.txt", xShifted, ySignal)

    # test shifting by minus 500
    # SignalSamplesAreEqual("Lab 2/output/shifting by minus 500.txt", xShifted, ySignal)

    figure, shift = plt.subplots(2, 1, figsize=(6, 8))

    shift[0].plot(xSignal, ySignal)
    shift[0].set_title("Original signal")
    shift[1].plot(xShifted, ySignal)
    shift[1].set_title("Shifted signal")

    plt.show()


frame = Frame(root)
lf = LabelFrame(frame, text="Constant")
txt = Text(lf, width="50", height="2")
button = Button(
    frame,
    command=shifting,
    text="Upload",
    width="10",
    height="2",
    font="30",
    bg="white",
    fg="black",
)
lf.pack()
txt.pack()
frame.pack()
button.pack()


root.mainloop()
