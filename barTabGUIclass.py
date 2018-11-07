#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Nov 6, 2018
#
#     Description: The program function is to take user input and validate then
#       calculate tip,tax and then the total of the meal.
#
#######################################################################################
from tkinter import *


class barTabGUI:

    tip = 0.18
    tax = 0.07

    def __init__(self, master):
        # Getting the GUI going.
        self.master = master
        master.title("Bar Tab Calculator")
        master.configure(background='black')

        # Defining the labels, entry box and button.
        self.labelMealCost = Label(master, text="Please enter the total charge for the food and drinks: ", bg="black",
                                   fg="cyan", font="Helvetica 10")
        self.mealCostEntry = Entry(master, bd=2, justify="center")
        self.buttonToCalculateTax = Button(master, text=" Calculate Tax ", bg="white", fg="black",
                                           font="Helvetica 8 bold", command=lambda: self.bar_tab_tax_calculator(self.tax))
        self.buttonToCalculateTotal = Button(master, text="Calculate Total", bg="white", fg="black",
                                             font="Helvetica 8 bold", command=lambda: self.bar_tab_total_calculator(self.tip, self.tax))

        # Initial informational message.
        self.mealTotalOutput = Label(master, text="Press the button to select and perform calculation", bg="black",
                                     fg="cyan", font="Helvetica 10")

        # This button is for the Exit button.
        self.exitButton = Button(master, text="Exit", command=master.destroy, bg="white", fg="blue",
                                 font="Helvetica 7 bold")

        # The layout is defined here.
        self.labelMealCost.grid(row=0, padx=5, pady=5)
        self.mealCostEntry.grid(row=1, padx=5, pady=5)
        self.buttonToCalculateTax.grid(row=2, padx=5, pady=5)
        self.buttonToCalculateTotal.grid(row=3, padx=5, pady=5)
        self.mealTotalOutput.grid(row=4, padx=5, pady=0)
        self.exitButton.grid(row=5, padx=5, pady=5)
        # Configuring the button to use the barTabCalculator function.

    # The function that does all the calculation and error handing for the tax.
    def bar_tab_tax_calculator(self, tax):
        # This is where we want to get a int number. Integers will be turned into int.
        # All others will throw an exception.
        try:
            meal = float(self.mealCostEntry.get())

            # Calculations needed for output.
            tax_total = meal * tax

            # Printing the output with formatting for expected output when handling money.
            self.mealTotalOutput.configure(text=f"Tax Total: ${tax_total:,.2f}", bg="black", fg="cyan",
                                           font="Helvetica 10")

        # What the user sees when they input invalid data.
        except:
            self.mealTotalOutput.configure(text="Invalid Entry. Please enter the dollars and cents.", bg="yellow",
                                           fg="red", font="Helvetica 10 bold")

    # The function that does all the calculation and error handing for the tab total.
    # Pretty much the same as the Tax function.
    def bar_tab_total_calculator(self, tip, tax):

        try:
            meal = float(self.mealCostEntry.get())

            tipTotal = meal * tip
            taxTotal = meal * tax
            mealTotal = meal + tipTotal + taxTotal

            self.mealTotalOutput.configure(text=f"Tip Total: ${tipTotal:,.2f} Meal Total: ${mealTotal:,.2f}", bg="black",
                                           fg="cyan", font="Helvetica 10")
        except:
            self.mealTotalOutput.configure(text="Invalid Entry. Please enter the dollars and cents.", bg="yellow",
                                           fg="red", font="Helvetica 10 bold")
