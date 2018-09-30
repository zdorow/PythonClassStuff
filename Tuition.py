#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 29, 2018
#
#     Description: The program function is to calculate tuition for the next 5 years.
#
#
#######################################################################################
from tkinter import *

# Getting the GUI going.
root = Tk()
root.title("Tuition Calculator")
root.configure(background='black')
root.geometry("395x175")

# Defining the initial label that shows when program starts.
tuitionOutput = Label(root, text="Press Calculate or Alt-c to calculate tuition\n "
                                 "Press Exit or Alt-e to kill the program\n\n\n",
                      bg="black", fg="cyan", font="Helvetica 12", wraplength=400)
tuitionOutput.pack(padx=5, pady=5)

# Making the calculate button.
calculateButton = Button(root, text="Calculate", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 7 bold")
calculateButton.pack(padx=5, pady=5)

# This is for the Exit button.
exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold")

exitButton.pack(padx=5, pady=5)


# Here we do the tuition calculation in a for loop.
def calculate_tuition():
    tuition = 8000
    increase = .03

    for year in range(1, 6):

        # Adding accumulator here
        tuition += tuition * increase

        # Logic to not grab the welcome text and only append the tuition output.
        if year == 1:
            tuitionOutput.configure(text="The tuition for year " + f"{year} " + f"is: ${tuition:.2f}\n")

        else:
            tuitionOutput.configure(text=tuitionOutput.cget("text") + "The tuition for year " + f"{year} " +
                                    f"is: ${tuition:.2f}\n", pady=0)
    calculateButton.configure(pady=0)


# Function used for key bind.
def destroy():
    root.destroy()


# Key stroke bindings.
root.bind('<Alt_L><c>', lambda e: calculate_tuition())
root.bind('<Alt_L><e>', lambda f: destroy())

# Button set to calculate!
calculateButton.configure(command=calculate_tuition)
root.mainloop()
