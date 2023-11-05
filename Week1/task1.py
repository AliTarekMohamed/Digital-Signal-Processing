from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import os
from comparesignals import SignalSamplesAreEqual


class Signalplotter:
    def __init__(self, root):
        self.dialog = root
        self.dialog.geometry("500x400")
        self.dialog.title("Signals")

        self.x_value = []
        self.y_value = []

        self.options = ['Continuous', 'Discrete', 'both']
        self.selectedoptions = IntVar()

        self.createWidgets()

    def createWidgets(self):
        for i in range(len(self.options)):
            rbutton = Radiobutton(
                self.dialog,
                text=self.options[i],
                variable=self.selectedoptions,
                value=i,
            )
            rbutton.place(x=200, y=50 + (i * 50))

        btn1 = Button(
            self.dialog,
            command=self.openFile,
            text="UPLOAD",
            width="10",
            height="2",
            font="30",
            bg="white",
            fg="black",
        )
        btn1.pack(side="bottom", pady="50")

    def openFile(self):
        Filepath = filedialog.askopenfilename(
            initialdir="A:\\Programming\\Python dsp tasks\\Task 1",
            title="Which signal?",
        )
        if not Filepath:
            return
        filename = os.path.basename(Filepath)
        self.loadData(Filepath)

        if self.selectedoptions.get() == 0:
            self.plotcontinuous()
        elif self.selectedoptions.get() == 1:
            self.plotdiscrete()
        else:
            self.plotcontinuous()
            self.plotdiscrete()

        self.showplot()

    def loadData(self, filepath):
        self.x_value = []
        self.y_value = []

        with open(filepath, "r") as f:
            for _ in range(3):
                next(f)

            for line in f:
                parts = line.strip().split()
                self.x_value.append(float(parts[0]))
                self.y_value.append(float(parts[1]))

    def plotcontinuous(self):
        plt.plot(
            self.x_value, self.y_value, marker="o", linestyle="-", label="Continuous"
        )

    def plotdiscrete(self):
        plt.stem(
            self.x_value,
            self.y_value,
            linefmt="-b",
            markerfmt="ob",
            basefmt="r",
            label="Discrete",
        )

    def showplot(self):
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.title("Discrete Time Signal")
        plt.legend()
        plt.grid()
        plt.show()


def main():
    root = Tk()
    app = Signalplotter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
