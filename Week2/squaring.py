from tkinter import *
from tkinter import filedialog, messagebox
import numpy as np
from matplotlib import pyplot as plt
from comparesignals import SignalSamplesAreEqual

root = Tk()
root.title("Squaring")
root.geometry("300x200")


def square():
    xSignal = []
    ySignal = []
    ySquared = []

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

    ySquared = np.power(ySignal, 2)

    # test squaring
    SignalSamplesAreEqual("Lab 2/output/squaring signal1.txt", xSignal, ySquared)

    fig, sqr = plt.subplots(2, 1, figsize=(6, 8))

    sqr[0].plot(xSignal, ySignal)
    sqr[0].set_title("Original Signal")
    sqr[1].plot(xSignal, ySquared)
    sqr[1].set_title("Squared Signal")

    plt.show()


button = Button(
    root,
    command=square,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
)
button.pack()


root.mainloop()
