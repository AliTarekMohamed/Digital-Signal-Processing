from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import QuanTest1 as t1
import QuanTest2 as t2

root = Tk()
root.title("Signal Quantization")

def quantize_signal():
    xSignal = []
    ySignal = []
    y_index = []
    mid_points = []
    y_quantized = []
    encoded_x = []
    error = []
    interval_index=[]
    levels_or_bits = var.get()
    
    signal = filedialog.askopenfilename(
    initialdir="Lab 3",
    title="Which Signal ?",
    )

    with open(signal, "r") as f:
        for i in range(3):
            next(f)

        for line in f:
            parts = line.strip().split()
            xSignal.append(float(parts[0]))
            ySignal.append(float(parts[1]))

    if (levels_or_bits == 'levels'):
        levels = float(lvls.get(1.0, "end"))
        
    elif (levels_or_bits == 'bits'):
        bits = int(bts.get(1.0, "end"))
        levels = np.power(2, bits)

    delta = (max(ySignal) - min(ySignal)) / levels

    x = min(ySignal)
    y_index.append(x)
    for i in range (int(levels)):
        x += delta
        y_index.append(round(x, 2))

    for i in range(len(y_index) - 1):
        mid_points.append((y_index[i] + y_index[i + 1]) / 2)

    for i in range(len(mid_points)):
        mid_points[i] = round(mid_points[i], 3)

    for i in range(len(ySignal)):
        for j in range(len(y_index) - 1):
            if (ySignal[i] >= y_index[j] and ySignal[i] <= y_index[j + 1]):
                y_quantized.append((mid_points[j]))
                y_quantized[i] = round(y_quantized[i], 3)
                break

    if (levels_or_bits == 'levels'):

        for i in range(len(y_quantized)):
            interval_index.append(mid_points.index(y_quantized[i]) + 1)
        for i in range(len(y_quantized)):
            encoded_x.append(format(mid_points.index(y_quantized[i]), "02b"))
        for i in range(len(ySignal)):
            error.append(round((y_quantized[i] - ySignal[i]), 3))

        table_window = Toplevel(root)
        table_window.title("Signal Quantization")
        table = ttk.Treeview(table_window, columns=("Interval Index", "Encoded", "Quantized", "error"))

        table.heading("#1", text="Interval Index")
        table.heading("#2", text="Encoded")
        table.heading("#3", text="Quantized")
        table.heading("#4", text="error")
        table.column("#1", width=100)
        table.column("#2", width=100)
        table.column("#3", width=100)
        table.column("#4", width=100)

        for i in range(len(y_quantized)):
            table.insert("", "end", values=(interval_index[i], encoded_x[i], y_quantized[i], error[i]))

        table.pack()
        t2.QuantizationTest2("Lab 3/Test 2/Quan2_Out.txt", interval_index, encoded_x, y_quantized, error)

    elif (levels_or_bits == 'bits'):

        for i in range(len(y_quantized)):
            encoded_x.append(format(mid_points.index(y_quantized[i]), "03b"))

        table_window = Toplevel(root)
        table_window.title("Signal Quantization")
        table = ttk.Treeview(table_window, columns=("Encoded", "Quantized"))

        table.heading("#1", text="Encoded")
        table.heading("#2", text="Quantized")
        table.column("#1", width=100)
        table.column("#2", width=100)

        for i in range(len(y_quantized)):
            table.insert("", "end", values=(encoded_x[i], y_quantized[i]))

        table.pack()
        t1.QuantizationTest1("Lab 3/Test 1/Quan1_Out.txt", encoded_x, y_quantized)

frame = Frame(root)
lf1 = LabelFrame(frame, text="Number of levels")
lf2 = LabelFrame(frame, text="Number of bits")
var = StringVar()
lorb1 = Radiobutton(frame, width="50", height="2", text="levels", value="levels", variable=var)
lorb2 = Radiobutton(frame, width="50", height="2", text="bits", value="bits", variable=var)
lvls = Text(lf1, width="50", height="2")
bts = Text(lf2, width="50", height="2")
button = Button(
    frame,
    text="Upload",
    width="12",
    height="2",
    font="30",
    bg="white",
    fg="black",
    command=quantize_signal,
)

frame.pack()
lf1.pack()
lf2.pack()
lorb1.pack()
lorb2.pack()
lvls.pack()
bts.pack()
button.pack()
root.mainloop()