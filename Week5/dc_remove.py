from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import comparesignal2 as tst

root = Tk()
root.title("DC Remove")
root.geometry("300x200")

def DC_REMOVE():
    ySignal = []
    dc = []
    
    signal = filedialog.askopenfilename(
    initialdir="Lab 5",
    title="Which Signal ?",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            ySignal.append(float(parts[1]))

    mean = 0

    for i in ySignal:
        mean += i
    mean /= len(ySignal)

    for i in ySignal:
        dc.append(i - mean)

    # Testing
    tst.SignalSamplesAreEqual("Lab 5\Remove DC component\DC_component_output.txt", dc)

    fig, DC = plt.subplots(2, 1, figsize=(6, 8))
    DC[0].plot(ySignal)
    DC[0].set_title("Before Removing")
    DC[1].plot(dc)
    DC[1].set_title("After Removing")
    plt.show()

button = Button(
    root,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=DC_REMOVE,
)
button.pack()
root.mainloop()