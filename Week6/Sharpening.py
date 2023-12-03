from tkinter import *
from tkinter import filedialog
import DerivativeSignal as tst

dialog = Tk()
dialog.geometry("250x250")
dialog.title("Sharpening")


def Sharpening():
  
    tst.DerivativeSignal()


btn = Button(dialog, text="Sharpen", width=20, height=4, command=Sharpening)


btn.pack(pady=40)
dialog.mainloop()
