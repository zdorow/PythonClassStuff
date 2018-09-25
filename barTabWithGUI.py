#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 14, 2018
#
#     Description: The program function is to take user input and validate then
#       calculate tip,tax and then the total of the meal.
#
#######################################################################################
# We are importing all of the tkinter library.
from tkinter import *

# Static variable definition.
tip = 0.18
tax = 0.07

# Getting the GUI going.
root = Tk()
root.title("Bar Tab Calculator")
root.configure(background='black')

# Defining the labels, entry box and button.
labelMealCost = Label(root, text="Please enter the total charge for the food and drinks: ", bg="black", fg="cyan", font="Helvetica 10")
mealCostEntry = Entry(root, bd=2, justify="center")
buttonToCalculateTax = Button(root, text=" Calculate Tax ", bg="white", fg="black", font="Helvetica 8 bold")
buttonToCalculateTotal = Button(root, text="Calculate Total", bg="white", fg="black", font="Helvetica 8 bold")

# Initial informational message.
mealTotalOutput = Label(root, text="Press the button to select and perform calcuation", bg="black", fg="cyan", font="Helvetica 10")


# The function that does all the calculation and error handing for the tax.
def bar_tab_tax_calculator():

    # This is where we want to get a int number. Integers will be turned into int.
    # All others will throw an exception.
    try:
        meal = float(mealCostEntry.get())

        # Calculations needed for output.
        tax_total = meal * tax

        # Printing the output with formatting for expected output when handling money.
        mealTotalOutput.configure(text=f"Tax Total: ${tax_total:,.2f}", bg="black", fg="cyan", font="Helvetica 10")

    # What the user sees when they input invalid data.
    except:
        mealTotalOutput.configure(text="Invalid Entry. Please enter the dollars and cents.", bg="yellow",  fg="red", font="Helvetica 10 bold")


# The function that does all the calculation and error handing for the tab total.
# Pretty much the same as the Tax function.
def bar_tab_total_calculator():

    try:
        meal = float(mealCostEntry.get())

        tipTotal = meal * tip
        taxTotal = meal * tax
        mealTotal = meal + tipTotal + taxTotal

        mealTotalOutput.configure(text=f"Tip Total: ${tipTotal:,.2f} Meal Total: ${mealTotal:,.2f}", bg="black",
                                  fg="cyan", font="Helvetica 10")

    except:
        mealTotalOutput.configure(text="Invalid Entry. Please enter the dollars and cents.", bg="yellow",  fg="red", font="Helvetica 10 bold")


# Configuring the button to use the barTabCalculator function.
buttonToCalculateTax.configure(command=bar_tab_tax_calculator)


buttonToCalculateTotal.configure(command=bar_tab_total_calculator)


# This button is for the Exit button.
exitButton = Button(root, text="Exit", command=root.destroy, bg="white", fg="blue", font="Helvetica 7 bold")

# The layout is defined here.
labelMealCost.grid(row=0, padx=5, pady=5)
mealCostEntry.grid(row=1, padx=5, pady=5)
buttonToCalculateTax.grid(row=2, padx=5, pady=5)
buttonToCalculateTotal.grid(row=3, padx=5, pady=5)
mealTotalOutput.grid(row=4, padx=5, pady=0)
exitButton.grid(row=5, padx=5, pady=5)

# Continue running program
root.mainloop()
