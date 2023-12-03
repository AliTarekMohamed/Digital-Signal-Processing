from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import signalcompare as tst

root = Tk()
root.title("Week 4")
root.geometry("500x400")

def Fourier_transform():
    xValues = []
    yValues = []
    xOfn = []
    xOfk = []
    amplitude = []
    phase = []
    sigma = []

    tst_amp1 = [64, 20.9050074380220, 11.3137084989848, 8.65913760233915, 8, -3.14159265358979, 8.65913760233915, 11.3137084989848, 20.9050074380220]
    tst_phase = [0, 1.96349540849362, 2.35619449019235, 2.74889357189107, -3.14159265358979, -2.74889357189107, -2.35619449019235, -1.96349540849362]
    tst_amp2 = [1, 3, 5, 7, 9, 11, 13, 15]

    signal = filedialog.askopenfilename(
        initialdir="Lab 4",
        title="Which Signal ?",
    )

    chk = int(np.loadtxt(signal, skiprows = 1, max_rows = 1))

    with open(signal, "r") as f:
        for i in range(3): 
            next(f)

        for line in f:
            line=line.replace('f',' ')
            line=line.replace(',',' ')
            parts = line.strip().split()
            xValues.append(float(parts[0]))
            yValues.append(float(parts[1]))

    N = len(yValues)

    def writeToTxtFile():
        with open("Week4\polarform.txt", mode="wt") as file:
            for i in range(0, len(amplitude)):
                file.write(f"{amplitude[i]} {phase[i]}\n") # Handle the first 3 lines
            file.close()
    
    def DFT():
        xOfn = yValues
        j = 1j

        for k in range (0, N):
            harmonic_value = 0
            for n in range (0, N):
                harmonic_value += xOfn[n] * np.exp((-j * 2 * np.pi * k * n) / N)
            xOfk.append(harmonic_value)
            amplitude.append(np.sqrt(np.power(np.real(harmonic_value), 2) + np.power(np.imag(harmonic_value), 2)))
            phase.append(np.arctan2(np.imag(harmonic_value), np.real(harmonic_value)))

        fund_freq = 0
        fs = int(freq.get(1.0, "end"))

        for i in range(0, len(amplitude)):
            fund_freq += (2 * np.pi * fs) / N
            sigma.append(fund_freq)

        if (tst.SignalComapreAmplitude(amplitude, tst_amp1)):
            print("Test case passed successfully")
        if (tst.SignalComaprePhaseShift(tst_phase, phase)):
            print("Test case passed successfully")

    def new_amp_phase():

        new_amp = amp_mod.get(1.0, "end").split()
        new_phase = phase_mod.get(1.0, "end").split()

        amplitude.clear()
        phase.clear()

        for i in range(len(new_amp)):
            amplitude.append(float(new_amp[i]))
            phase.append(float(new_phase[i]))

        writeToTxtFile()
        plot()
        
    def plot():
        figure, dft = plt.subplots(2, 1, figsize=(6, 8))
        dft[0].bar(sigma, amplitude)
        dft[0].set_title("Frequency / Amplitude")
        dft[1].bar(sigma, phase)
        dft[1].set_title("Frequency / Phase")
        plt.show()

    if (chk == 0): # Time Domain (DFT)
        DFT()

        # This is a window to allow modification on amplitude and phase shift
        modWindow = Toplevel(root)
        modWindow.title("Modification")
        modWindow.geometry("500x400")
        frame = Frame(modWindow)
        lf1 = LabelFrame(frame, text="Modify Amplitude")
        lf2 = LabelFrame(frame, text="Modify Phase Shift")
        amp_mod = Text(lf1, wrap=WORD, width=20, height=8)
        amp_mod.insert(1.0, amplitude)
        phase_mod = Text(lf2, wrap=WORD, width=20, height=8)
        phase_mod.insert(1.0, phase)
        update = Button(frame, text="Update", width="12", height="2", font="30", bg="white", fg="black", command=new_amp_phase)
        frame.pack()
        lf1.pack()
        lf2.pack()
        amp_mod.pack()
        phase_mod.pack()
        update.pack()

        writeToTxtFile()
        plot()

    else: # else chk = 1 that means frequency domain (IDFT)
        real = []
        img = []
        j = 1j

        for i in range(N):
            real.append(xValues[i] * np.cos(yValues[i]))
            img.append(xValues[i] * np.sin(yValues[i]))
            xOfk.append(real[i] + img[i] * j)

        for n in range (0, N):
            harmonic_value = 0
            for k in range (0, N):
                harmonic_value += xOfk[k] * np.exp((j * 2 * np.pi * n * k) / N)
            harmonic_value *= (1 / N)
            xOfn.append(round(np.real(harmonic_value)))

        if (tst.SignalComapreAmplitude(tst_amp2, xOfn)):
            print("Test case passed successfully")

        plt.plot(xOfn)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.title("IDFT")
        plt.show()

freq_label = Label(root, text="Enter the Sampling Frequency in HZ", pady=40)
freq = Text(root, width=20, height=2)
upload = Button(root, text="Upload", width=12, height=2, command=Fourier_transform)

freq_label.pack()
freq.pack()
upload.pack()
root.mainloop()