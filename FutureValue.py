#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 05, 2018
#
#     Description: The program function is to take user input and validate then
#
#######################################################################################
from tkinter import *
from tkinter import messagebox


# Function to calculate future value output upon the button being pressed.
def future_value_calc():
    try:
        present_value = float(presentValueEntry.get())
        monthly_interest = float(monthlyInterestEntry.get())
        months_entry = float(monthsEntry.get())

        future_value = present_value * (1 + monthly_interest) ** months_entry
        labelOutput.configure(text=f"\nThe future value is: {future_value:,.2f}\n")

    except ValueError:
        messagebox.showerror("Invalid Entry", "Please enter a valid number")


# Function to exit the program.
def destroy():
    root.destroy()


# Getting the GUI started. Setting the background, size and title.
root = Tk()
root.title("Future Value Calculator")
root.configure(background='black')
root.geometry("395x355")

# Initial message in GUI.
labelOutput = Label(root, text="Enter the numbers in their respective fields.\n"
                               "Press Calculate or Alt-c to calculate future value\n "
                               "Press Exit or Alt-x to kill the program",
                    bg="black", fg="cyan", font="Helvetica 12", wraplength=400)
labelOutput.pack(padx=5, pady=5)

# Present value label and entry field.
presentValueLabel = Label(root, text="Please enter the present value:", bg="black", fg="cyan", font="Helvetica 12")
presentValueLabel.pack(padx=5, pady=5)
presentValueEntry = Entry(root, bd=2, justify="center")
presentValueEntry.pack(padx=5, pady=5)

# Monthly Interest label and entry field.
monthlyInterestLabel = Label(root, text="Please enter the monthly interest rate: ", bg="black", fg="cyan",
                             font="Helvetica 12")
monthlyInterestLabel.pack(padx=5, pady=5)
monthlyInterestEntry = Entry(root, bd=2, justify="center")
monthlyInterestEntry.pack(padx=5, pady=5)

# Months label and entry field.
monthsLabel = Label(root, text="Please enter the number of months: ", bg="black", fg="cyan", font="Helvetica 12")
monthsLabel.pack(padx=5, pady=5)
monthsEntry = Entry(root, bd=2, justify="center")
monthsEntry.pack(padx=5, pady=5)

# Buttons definitions.
calculateButton = Button(root, text=" Calculate ", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 9 bold", underline=1, command=future_value_calc)
calculateButton.pack(padx=5, pady=5)

exitButton = Button(root, text=" Exit ", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 9 bold", underline=2)
exitButton.pack(padx=5, pady=5)

# Key bindings.
root.bind('<Alt_L><c>', lambda e: future_value_calc())
root.bind('<Alt_L><x>', lambda f: destroy())

root.mainloop()
