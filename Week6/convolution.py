from tkinter import *
from tkinter import filedialog
import ConvTest as tst


dialog = Tk()
dialog.geometry("250x250")
dialog.title("Convolution")


def Convolution():
    index1 = []
    index2 = []
    ysignal1 = []
    ysignal2 = []
    indeices = []
    convsignal = []

    signal1 = filedialog.askopenfilename(
        initialdir="Lab 6\Convolution", title="Which Signal")

    signal2 = filedialog.askopenfilename(
        initialdir="Lab 6\Convolution", title="Which Signal")

    with open(signal1, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            index1.append(int(parts[0]))
            ysignal1.append(float(parts[1]))

    with open(signal2, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            index2.append(int(parts[0]))
            ysignal2.append(float(parts[1]))

    min = index1[0]+index2[0]
    max = index1[len(index1)-1]+index2[len(index2)-1]

    for n in range(min, max+1):
        value = 0
        for k in range(min, max+1):  # max+1
            if ((n-k) < 0):
                continue

            if (k > index1[len(index1) - 1]):
                xOfn = 0
            else:
                xOfn = ysignal1[index1.index(k)]

            if ((n - k) > index2[len(index2) - 1]):
                hOfn = 0
            else:
                hOfn = ysignal2[index2.index(n-k)]

            value += xOfn * hOfn

        indeices.append(n)
        convsignal.append(value)

    for i in convsignal:
        print(i)
    tst.ConvTest(indeices, convsignal)


btn = Button(dialog, text="Convolve", width=20, height=4, command=Convolution)


btn.pack(pady=40)
dialog.mainloop()
