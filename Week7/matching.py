from tkinter import *
from tkinter import filedialog
import Correlationcomponent as corr
import numpy as np

root = Tk()
root.title("Signal Matching")
root.geometry("300x200")


def Matching():
    signal = []
    down_avg = []
    up_avg = []
    down_corr = []
    up_corr = []

    signal_path = filedialog.askopenfilename(
        initialdir="Lab 7/Point3 Files/Test Signals", title="Which Signal")

    signal = np.loadtxt(f"{signal_path}")

    down1 = np.loadtxt("Lab 7/Point3 Files/Class 1/down1.txt")
    down2 = np.loadtxt("Lab 7/Point3 Files/Class 1/down2.txt")
    down3 = np.loadtxt("Lab 7/Point3 Files/Class 1/down3.txt")
    down4 = np.loadtxt("Lab 7/Point3 Files/Class 1/down4.txt")
    down5 = np.loadtxt("Lab 7/Point3 Files/Class 1/down5.txt")

    up1 = np.loadtxt("Lab 7/Point3 Files/Class 2/up1.txt")
    up2 = np.loadtxt("Lab 7/Point3 Files/Class 2/up2.txt")
    up3 = np.loadtxt("Lab 7/Point3 Files/Class 2/up3.txt")
    up4 = np.loadtxt("Lab 7/Point3 Files/Class 2/up4.txt")
    up5 = np.loadtxt("Lab 7/Point3 Files/Class 2/up5.txt")

    for i in range(len(signal)):
        down_avg.append((down1[i] + down2[i] + down3[i] + down4[i] + down5[i]) / 5)
        up_avg.append((up1[i] + up2[i] + up3[i] + up4[i] + up5[i]) / 5)

    down_corr = corr.correlation(signal, down_avg)
    up_corr = corr.correlation(signal, up_avg)

    if (up_corr > down_corr): # up_corr[0] > down_corr[0]
        print("This signal is up movement")
    else:
        print("This signal is down movement")


matching = Button(root, width=17, height=3, text="Matching", command=Matching)
matching.pack(pady=50)
root.mainloop()