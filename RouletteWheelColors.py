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
# We are importing all of the tkinter library
from tkinter import *
import tkinter.messagebox
import logging

# Getting the GUI going.
root = Tk()
root.title("Roulette Wheel Colors")
root.geometry("300x350")
root.configure(background="black")

# Default Colors for text and backgrounds
black = "black"
black_back = "seashell3"
blue = "cyan"
green = "green"
red = "red"
red_back = "black"

# Setting of values for corresponding Radio and Check buttons
numbersRadioVar = IntVar()
numbersRadioVar.set(1)
colorBlind = IntVar()
colorBlind.set(0)

# Defining the labels, entry box, checkbox, radio buttons and button.
labelNumberEntry = Label(root, text="Please pick a pocket: ", bg=black, fg=blue, font="Helvetica 10")
numberEntry = Entry(root, bd=2, justify="center")
finalPocketOutput = Label(root, text="Pick a number between 0-36.", bg=black, fg=blue, font="Helvetica 10")
buttonToPickAPocket = Button(root, text=" Pick a Pocket! ", bg="seashell3", fg="black", font="Helvetica 8 bold")
redNumbersRadio = Radiobutton(root, bg=black, fg=blue, selectcolor="black", text="Show me all RED numbers.",
                              value=3, variable=numbersRadioVar, highlightbackground=black, activebackground="black",
                              highlightthickness=6, font="Helvetica 8 bold")
blackNumbersRadio = Radiobutton(root, bg=black, fg=blue, selectcolor="black", text="Show me all BLACK numbers.",
                                value=2, variable=numbersRadioVar, highlightbackground=black, activebackground="black",
                                highlightthickness=6, font="Helvetica 8 bold")
greenNumbersRadio = Radiobutton(root, bg=black, fg=blue, selectcolor="black", text="Show me all GREEN numbers.",
                                value=1, variable=numbersRadioVar, highlightbackground=black, activebackground="black",
                                highlightthickness=6, font="Helvetica 8 bold")
colorBlindCheck = Checkbutton(root,  bg=black, fg=blue, selectcolor="black", text="Colorblind?",
                              variable=colorBlind, highlightbackground=black, activebackground="black",
                              highlightthickness=6, font="Helvetica 8 bold")
exitButton = Button(root, text=" Exit ", command=root.destroy, bg="seashell3", fg=black, font="Helvetica 7 bold")

# The packing order.
labelNumberEntry.pack(fill=X, ipady=5)
numberEntry.pack(expand=10, padx=5)
finalPocketOutput.pack(fill=X, pady=2)
buttonToPickAPocket.pack(expand=10, padx=5, pady=5)
redNumbersRadio.pack(padx=15)
blackNumbersRadio.pack(padx=15)
greenNumbersRadio.pack(padx=15)
colorBlindCheck.pack(padx=5, pady=2)
exitButton.pack(expand=8)


# Building the colorblind color check function to convert the colors as determined by the checkbox.
def color_blind_check():
    if colorBlind.get() == 1:
        black = "black"
        black_back = "white"
        blue = "black"
        green = "black"
        red = "black"
        red_back = "white"

        root.configure(background="white")
        labelNumberEntry.configure(bg="white", fg=black, highlightbackground="white", activebackground="white")
        buttonToPickAPocket.configure(fg=black, highlightbackground="white", activebackground="white")
        finalPocketOutput.configure(bg="white", fg=black, highlightbackground="white", activebackground="white")
        redNumbersRadio.configure(bg="white", fg=black,  selectcolor="white", highlightbackground="white",
                                  activebackground="white")
        blackNumbersRadio.configure(bg="white", fg=black,  selectcolor="white", highlightbackground="white",
                                    activebackground="white")
        greenNumbersRadio.configure(bg="white", fg=black,  selectcolor="white", highlightbackground="white",
                                    activebackground="white")
        colorBlindCheck.configure(bg="white", fg=black,  selectcolor="white", highlightbackground="white",
                                  activebackground="white")

    else:
        black = "black"
        black_back = "seashell3"
        blue = "cyan"
        green = "green"
        red = "red"
        red_back = "black"

        root.configure(background="black")
        labelNumberEntry.configure(bg="black", fg=blue, highlightbackground="black",
                                   activebackground="white")
        finalPocketOutput.configure(bg="black", fg=blue, highlightbackground="black",
                                    activebackground="white")
        buttonToPickAPocket.configure(highlightbackground="black", activebackground="black")
        redNumbersRadio.configure(bg="black", fg=blue,  selectcolor="black", highlightbackground="black",
                                  activebackground="black")
        blackNumbersRadio.configure(bg="black", fg=blue,  selectcolor="black", highlightbackground="black",
                                    activebackground="black")
        greenNumbersRadio.configure(bg="black", fg=blue,  selectcolor="black", highlightbackground="black",
                                    activebackground="white")
        colorBlindCheck.configure(bg="black", fg=blue,  selectcolor="black", highlightbackground="black",
                                  activebackground="white")


# Making the check box have it's own function.
colorBlindCheck.configure(command=color_blind_check)


# The function that does all the logic and error handing for the picking of the pocket.
def pick_a_pocket():
    # This is where we want to get a int number.
    # All others will throw an exception.
    try:
        pocket_picked = int(numberEntry.get())

        # Additional color evaluation to convert the colors to the checkbox selected.
        if colorBlind.get() == 1:
            black = "black"
            black_back = "white"
            blue = "black"
            green = "black"
            red = "black"
            red_back = "white"
        else:
            black = "black"
            black_back = "seashell3"
            blue = "cyan"
            green = "green"
            red = "red"
            red_back = "black"

        # Output from Radio button selections.
        if numbersRadioVar.get() == 3:
            desired_color = "\n RED is 1, 3, 5, 7, 9, 12, 14, 16, 18, 19 ,21, 23, 25, 27, 30, 32, 34, 36"

        elif numbersRadioVar.get() == 2:
            desired_color = "\n BLACK is 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35"

        else:
            desired_color = "\n GREEN is 0"

    # What the user sees when they input invalid data.
    except Exception as nex:
        tkinter.messagebox.showwarning("Error!", "Invalid Entry. Please enter a number for the pocket.")
        logging.exception("User entered a non-numeric value" + nex)

    # Logic for the number entered and the corresponding pocket.
    if pocket_picked == 0:
        finalPocketOutput.configure(text="You have picked GREEN " + desired_color, bg=black_back, fg=green,
                                    font="Helvetica 10 bold", wraplength=225)
    elif pocket_picked in range(1, 11) or pocket_picked in range(19, 29):
        if pocket_picked % 2 == 0:
            finalPocketOutput.configure(text="You have picked BLACK " + desired_color, bg=black_back, fg=black,
                                        font="Helvetica 10 bold", wraplength=225)

        else:
            finalPocketOutput.configure(text="You have picked RED " + desired_color, bg=red_back, fg=red,
                                        font="Helvetica 10 bold", wraplength=225)
    elif pocket_picked in range(11, 19) or pocket_picked in range(29, 37):
        if pocket_picked % 2 == 0:
            finalPocketOutput.configure(text="You have picked RED" + desired_color, bg=red_back, fg=red,
                                        font="Helvetica 10 bold", wraplength=225)

        else:
            finalPocketOutput.configure(text="You have picked BLACK " + desired_color, bg=black_back, fg=black,
                                        font="Helvetica 10 bold", wraplength=225)
    else:
        tkinter.messagebox.showwarning("Out of Range!", "Entry out of range. Please enter a number from 0-36.")


# Setting the button to use the pick_a_pocket function.
buttonToPickAPocket.configure(command=pick_a_pocket)

# Continue running program
root.mainloop()
