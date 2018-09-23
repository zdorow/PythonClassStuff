#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 23, 2018
#
#     Description: The program function is to take user input and validate then
#       determine which pocket the number falls into. Roulette Wheel Colors.
#
#######################################################################################
# We are importing all of the tkinter library.
from tkinter import messagebox
from tkinter import *
import logging

# Getting the GUI going.
root = Tk()
root.title("Roulette Wheel Colors")
root.geometry("225x175")
root.configure(background='black')

# Defining the labels, entry box and button.
labelNumberEntry = Label(root, text="Please pick a pocket: ", bg="black", fg="cyan", font="Helvetica 10")
labelNumberEntry.pack(fill=X, ipady=10)
numberEntry = Entry(root, bd=2, justify="center")
numberEntry.pack(fill=X, padx=10)
buttonToPickAPocket = Button(root, text=" Pick a Pocket! ", bg="blue", fg="black", font="Helvetica 8 bold")
buttonToPickAPocket.pack(fill=X, padx=10)
exitButton = Button(root, text="Exit", command=root.destroy, bg="blue", fg="red", font="Helvetica 7 bold")
exitButton.pack(fill=X, padx=10)

# Initial informational message.
finalPocketOutput = Label(root, text="Welcome to Roulette Wheel Colors! Press the button to pick a pocket!"
                          " Please pick a number between 0-36.", bg="black", fg="cyan", font="Helvetica 10",
                          wraplength=200)
finalPocketOutput.pack(fill=X)

# The function that does all the calculation and error handing for the tax.
def pick_a_pocket():

    # This is where we want to get a int number.
    # All others will throw an exception.
    try:
        pocket_picked = int(numberEntry.get())
    # What the user sees when they input invalid data.

    except Exception as nex:
        messagebox.showwarning("Error!", "Invalid Entry. Please enter a number for the pocket.")
        logging.exception("User entered a non-numeric value" + nex)

    if pocket_picked == 0:
        finalPocketOutput.configure(text="You have picked the GREEN", bg="black", fg="green",
                                    font="Helvetica 10 bold")
    elif pocket_picked in range(1, 11) or pocket_picked in range(19, 29):
        if pocket_picked % 2 == 0:
            finalPocketOutput.configure(text="You have picked BLACK", bg="white", fg="black",
                                        font="Helvetica 10 bold")

        else:
            finalPocketOutput.configure(text="You have picked RED", bg="black", fg="red",
                                        font="Helvetica 10 bold")
    elif pocket_picked in range(11, 19) or pocket_picked in range(29, 37):
        if pocket_picked % 2 == 0:
            finalPocketOutput.configure(text="You have picked RED", bg="black", fg="red",
                                        font="Helvetica 10 bold")

        else:
            finalPocketOutput.configure(text="You have picked BLACK", bg="white", fg="black",
                                        font="Helvetica 10 bold")
    else:
        messagebox.showwarning("Out of Range!", "Entry out of range. Please enter a number from 0-36.")


buttonToPickAPocket.configure(command=pick_a_pocket)


# The layout is defined here.
# labelNumberEntry.grid(row=0, columnspan=4, padx=5, pady=5)
# numberEntry.grid(row=1, columnspan=4, padx=5, pady=5)
# buttonToPickAPocket.grid(row=2, columnspan=4, padx=5, pady=5)
# finalPocketOutput.grid(row=3, columnspan=4, padx=5, pady=0)
# exitButton.grid(row=4, columnspan=4, padx=5, pady=5)

# Continue running program
root.mainloop()
