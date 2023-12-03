from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import comparesignal2 as tst

root = Tk()
root.title("Remove DC")
root.geometry("300x200")

def REMOVE_DC():
    ySignal = []
    xOfn = []
    xOfk = []
    
    signal = filedialog.askopenfilename(
    initialdir="Lab 5\Remove DC component",
    title="Which Signal ?",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            ySignal.append(float(parts[1]))

    N = len(ySignal)

    j = 1j

    for k in range (0, N):
        harmonic_value = 0
        for n in range (0, N):
            harmonic_value += ySignal[n] * np.exp((-j * 2 * np.pi * k * n) / N)
        xOfk.append(harmonic_value)

    xOfk[0] = 0

    for n in range (0, N):
        harmonic_value = 0
        for k in range (0, N):
            harmonic_value += (xOfk[k] * np.exp((j * 2 * np.pi * n * k) / N))
        harmonic_value *= (1 / N)
        xOfn.append(np.real(harmonic_value))

    # Testing
    tst.SignalSamplesAreEqual("Lab 5/Remove DC component/DC_component_output.txt", xOfn)

    fig, DC = plt.subplots(2, 1, figsize=(6, 8))
    DC[0].plot(ySignal)
    DC[0].set_title("Before Removing")
    DC[1].plot(xOfn)
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
    command=REMOVE_DC,
)
button.pack()
root.mainloop()