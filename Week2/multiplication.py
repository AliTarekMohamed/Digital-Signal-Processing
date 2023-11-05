from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual


root = Tk()
root.title("Multiplication")
root.geometry("300x200")


def multiplication():
    x_value = []
    y_value = []
    y_multi = []

    signal = filedialog.askopenfilename(
        initialdir="Lab 2/input",
        title="Which Signal?",
    )

    with open(signal, "r") as f:
        for _ in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            x_value.append(float(parts[0]))
            y_value.append(float(parts[1]))

    const = float(txt1.get(1.0, "end"))

    for i in range(0, len(y_value)):
        y_multi.append(y_value[i] * const)

    # test multiplication signal1 by 5
    # SignalSamplesAreEqual("Lab 2/output/multiply signa1 by 5.txt", x_value, y_multi)

    # test multiplication signal2 by 10
    # SignalSamplesAreEqual("Lab 2/output/multiply signal2 by 10.txt", x_value, y_multi)

    fig, multi = plt.subplots(2, 1, figsize=(6, 8))

    multi[0].plot(x_value, y_value)
    multi[0].set_title("Original Signal")
    multi[1].plot(x_value, y_multi)
    multi[1].set_title("Multiplied signal")

    plt.plot()
    plt.show()


frame1 = Frame(root)
lf1 = LabelFrame(frame1, text="Constant")
txt1 = Text(lf1, width=50, height=2)

button = Button(
    frame1,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=multiplication,
)

frame1.pack()
lf1.pack()
txt1.pack()
button.pack()
root.mainloop()
