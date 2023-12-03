from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Delaying or Advancing")

def Delay_or_Advance():
    xSignal = []
    ySignal = []
    yFolded = []
    xShFo = []

    signal = filedialog.askopenfilename(
        initialdir="Lab 6/Shifting and Folding",
        title="Which Signal ?",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            xSignal.append(float(parts[0]))
            ySignal.append(float(parts[1]))


    def folding():
        for i in range(len(ySignal) - 1, -1, -1):
            yFolded.append(ySignal[i])

    fow = var1.get()

    if (fow == 'Only Folding'):
        folding()
        figure, shift = plt.subplots(2, 1, figsize=(6, 8))
        shift[0].plot(xSignal, ySignal)
        shift[0].set_title("Original signal")
        shift[1].plot(xSignal, yFolded)
        shift[1].set_title("Shifted signal")
        plt.show()

    const = int(txt.get(1.0, 'end'))

    if (fow == 'Shifting With Folding'):
        folding()
        for i in range(len(xSignal)):
            xShFo.append(xSignal[i] + const)
        figure, shift = plt.subplots(2, 1, figsize=(6, 8))
        shift[0].plot(xSignal, ySignal)
        shift[0].set_title("Original signal")
        shift[1].plot(xShFo, yFolded)
        shift[1].set_title("Shifted signal")
        plt.show()

    elif(fow == 'Shifting Without Folding'):
        for i in range(len(xSignal)):
            xShFo.append(xSignal[i] - const)
        figure, shift = plt.subplots(2, 1, figsize=(6, 8))
        shift[0].plot(xSignal, ySignal)
        shift[0].set_title("Original signal")
        shift[1].plot(xShFo, ySignal)
        shift[1].set_title("Shifted signal")
        plt.show()

frame = Frame(root)
lf = LabelFrame(frame, text="Constant")
txt = Text(lf, width="50", height="2")
var1 = StringVar()
fold = Radiobutton(frame, width="50", height="2", text="Only Folding", value="Only Folding", variable=var1)
swf = Radiobutton(frame, width="50", height="2", text="Shifting With Folding", value="Shifting With Folding", variable=var1)
swof = Radiobutton(frame, width="50", height="2", text="Shifting Without Folding", value="Shifting Without Folding", variable=var1)
button = Button(
    frame,
    command=Delay_or_Advance,
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
fold.pack()
swf.pack()
swof.pack()
root.mainloop()