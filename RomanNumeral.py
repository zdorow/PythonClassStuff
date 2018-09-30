#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 25, 2018
#
#     Description: The program function is to use a spinbox to output a roman numeral
#
#
#######################################################################################
import tkinter as tk
from tkinter import *
import logging

# Getting the GUI going.
root = tk.Tk()
# Change title of GUI
root.title("Roman Numeral Guide")
# Set background color of GUI
root.configure(background='black')
# Set size of the GUI window
root.geometry("425x150")

# Create label for when program starts to instruct user on how to start
numeralOutput = Label(root, text="Press the arrows to select a numeral", bg="black", fg="cyan", font="Helvetica 18")


# Function converts integer input to roman numeral
def int_to_roman(int_input):
    # Array storing int numbers to to correspond to roman numerals
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    # Array storing the roman numeral versions of number
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    # Empty array for storing results
    result = []
    # Loop through ints array
    for i in range(len(ints)):
        # Divide input by int value and convert to an int value
        count = int(int_input / ints[i])
        # Append corresponding roman numeral to array by however by the count
        result.append(nums[i] * count)
        # Subtract from original input to find next needed roman numeral
        int_input -= ints[i] * count
    # Return result with blank elements removed
    return ''.join(result)


# Callback function for when spinner arrow's are changed
def callback():
    try:
        # Get value from spinner box and call function to convert number
        selection = int_to_roman(int(spinbox.get()))
        # Set output font
        numeralOutput.configure(font="Helvetica 24")
    except Exception as nex:
        # Display error message if number is out of range
        numeralOutput.configure(text='Exception Error!')
        # Log error
        logging.exception("User tried to go to a value that is not present." + nex)
    # Output result
    numeral_output.configure(text=selection)


# Create spinbox widget
spin_box = tk.Spinbox(root, state='readonly', from_=1, to=3999, bg="black", highlightbackground="black",
                      buttonbackground="cyan", command=callback)

# This button is for the Exit button.
exit_button = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                     font="Helvetica 7 bold")

# Add widgets to main window
spin_box.pack(padx=5, pady=15)
numeral_output.pack(padx=5, pady=5)
exit_button.pack(padx=5, pady=5)

# Run main loop for displaying window
root.mainloop()
