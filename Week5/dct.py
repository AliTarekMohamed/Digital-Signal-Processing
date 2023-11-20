from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import comparesignal2 as tst

root = Tk()
root.title("DCT")

def DCT():
    ySignal = []
    dct = []
    
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

    for k in range(N):
        dct_values = 0
        for n in range(N):
            dct_values += float(ySignal[n] * np.cos((np.pi / (4 * N)) * ((2 * n) - 1) * ((2 * k) - 1)))
        dct_values *= float(np.sqrt(2 / N))
        dct.append(dct_values)
    
    table_window = Toplevel(root)
    table_window.title("DCT")
    table = ttk.Treeview(table_window, columns=("DCT"))
    table.heading("#1", text="DCT")
    table.column("#1", width=100)
    for i in range(N):
        table.insert("", "end", values=(dct[i]))
    table.pack()

    # Testing
    tst.SignalSamplesAreEqual("Lab 5\DCT\DCT_output.txt", dct)

    m = int(numOfCoeff.get(1.0, "end"))
    with open("Week5\coefficient.txt", mode="wt") as file:
        for i in range(m):
            file.write(f"{dct[i]}\n")
        file.close()

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