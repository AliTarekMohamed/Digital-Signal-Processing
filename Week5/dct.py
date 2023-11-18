from tkinter import *
from tkinter import filedialog
import numpy as np
import comparesignal2 as tst

root = Tk()
root.title("DCT")

def DCT():
    ySignal = []
    amplitude = []
    phase = []
    
    
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

    N = len(ySignal)

    for k in range(len(ySignal)):
        dct_values = 0
        for n in range(len(ySignal)):
            dct_values += float(ySignal[n] * np.cos((np.pi / (4 * N)) * ((2 * n) - 1) * ((2 * k) - 1)))
        dct_values *= float(np.sqrt(2 / N))
        amplitude.append(np.sqrt(np.power(np.real(dct_values), 2) + np.power(np.imag(dct_values), 2)))
        phase.append(np.arctan2(np.imag(dct_values), np.real(dct_values)))
    
    m = int(numOfCoeff.get(1.0, "end"))
    with open("Week5\coefficient.txt", mode="wt") as file:
        for i in range(m):
            file.write(f"{phase[i]} {amplitude[i]}\n") # Handle the first 3 lines
        file.close()

    # Testing
    tst.SignalSamplesAreEqual("Lab 5\DCT\DCT_output.txt", amplitude)


frame = Frame(root)
lf = LabelFrame(frame, text="Number of coefficients to save")
numOfCoeff = Text(lf, width="50", height="2")
button = Button(
    frame,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=DCT,
)
frame.pack()
lf.pack()
numOfCoeff.pack()
button.pack()
root.mainloop()