#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Nov 19, 2018
#
#     Description: The program function is to demonstrate recursive versus a loop to
#       raise a number to a power.
#
#######################################################################################
from tkinter import *


class RecursiveAndLoopPower:

    def __init__(self, master):

        # Getting the GUI going.
        self.master = master
        master.title("Power Calculator")
        master.configure(background='black')

        # Defining the labels, entry box and button.
        self.labelNumberEntry = Label(master, text="Please enter the number to raise by a power: ", bg="black",
                                      fg="cyan", font="Helvetica 10")

        self.numberEntry = Entry(master, bd=2, justify="center")
        self.labelPowerEntry = Label(master, text="Please enter the power: ", bg="black", fg="cyan",
                                     font="Helvetica 10")

        self.powerEntry = Entry(master, bd=2, justify="center")
        self.buttonRecursiveCalculate = Button(master, text="Calculate Recursively", bg="white", fg="black",
                                               font="Helvetica 8 bold",
                                               command=lambda: self.recursive_power(self.numberEntry.get(),
                                                                                    self.powerEntry.get()))

        self.buttonLoopCalculate = Button(master, text="Calculate with Loop", bg="white", fg="black",
                                          font="Helvetica 8 bold",
                                          command=lambda: self.loop_power(self.numberEntry.get(),
                                                                          self.powerEntry.get()))
        
        # Initial informational message.
        self.totalOutput = Label(master, text="Press the button to select and perform calculation", bg="black",
                                     fg="cyan", font="Helvetica 10")

        # This button is for the Exit button.
        self.exitButton = Button(master, text="Exit", command=master.destroy, bg="white", fg="blue",
                                 font="Helvetica 7 bold")

        # The layout is defined here.
        self.labelNumberEntry.grid(row=0, padx=5, pady=5)
        self.numberEntry.grid(row=1, padx=5, pady=5)
        self.labelPowerEntry.grid(row=2, padx=5, pady=5)
        self.powerEntry.grid(row=3, padx=5, pady=5)
        self.buttonRecursiveCalculate.grid(row=4, padx=5, pady=5)
        self.buttonLoopCalculate.grid(row=5, padx=5, pady=5)
        self.totalOutput.grid(row=6, padx=5, pady=0)
        self.exitButton.grid(row=7, padx=5, pady=5)

    # The recursive power function that calls the recursion function to raise the powers of the entered numbers and
    #  change the output accordingly.
    def recursive_power(self, number, power):
    
        try:
            if float(power) < 0:
                total = -(self.recursion(float(number), float(power)))
            else:
                total = self.recursion(float(number), float(power))
            self.totalOutput.configure(text=f"Total: {total}", bg="black", fg="cyan", font="Helvetica 10")

        except ValueError:
            self.totalOutput.configure(text="Invalid Entry. Please enter numbers only.", bg="yellow",
                                       fg="red", font="Helvetica 10 bold")

    # The loop power function that calls the loop function to raise the powers of the entered numbers and
    #  change the output accordingly.
    def loop_power(self, number, power):
    
        try:
            if float(power) < 0:
                total = -(self.loop(float(number), float(power)))
            else:
                total = self.loop(float(number), float(power))
            self.totalOutput.configure(text=f"Total: {total}", bg="black", fg="cyan", font="Helvetica 10")
        except ValueError:
            self.totalOutput.configure(text="Invalid Entry. Please enter numbers only.", bg="yellow",
                                       fg="red", font="Helvetica 10 bold")

    # Recursion function and loop function that behave the same way. Handles negative and positive bases and powers.
    #   Negative bases return negative correctly on odd numbers and flipped positive because of the way they are called
    #   in the base function. Handles decimal bases but not decimal powers. Since this is out of scope for the
    #   assignment, it was decided it was fine as-is.

    def recursion(self, number, power):
        if power == 1:
            return number
        elif power == 0:
            return 1
        elif power < 0:
            return self.recursion(number, power + 1) / number
        else:
            return number * self.recursion(number, (power - 1))

    def loop(self, number, power):
        total = 1
        if power == 1:
            return number
        elif power == 0:
            return 1
        elif power < 0:
            for _ in range(int(power) * -1):
                total /= number
        else:
            for _ in range(int(power)):
                total *= number
        return total


root = Tk()
recursive_and_loop_power = RecursiveAndLoopPower(root)
root.mainloop()
