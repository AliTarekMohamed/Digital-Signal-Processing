from tkinter import *
from tkinter import filedialog
import comparesignal2 as tst
import Correlationcomponent as corr

dialog = Tk()
dialog.title("Correlation")
dialog.geometry("300x200")


def perpare_signal():
    ysignal1 = []
    ysignal2 = []

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 7\Point1 Correlation", title="Which Signal")

    signal2 = filedialog.askopenfilename(
        initialdir="Lab 7\Point1 Correlation", title="Which Signal")

    with open(signal1, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ysignal1.append(float(parts[1]))

    with open(signal2, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            ysignal2.append(float(parts[1]))

    correlationsignal = corr.correlation(ysignal1, ysignal2)

    tst.SignalSamplesAreEqual(
        "Lab 7\Point1 Correlation\CorrOutput.txt", correlationsignal)


Corrbutton = Button(dialog, width=17, height=3,
                    text="Correlation", command=perpare_signal)
Corrbutton.pack(pady=50)
dialog.mainloop()
