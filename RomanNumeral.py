#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Nov 17, 2018
#
#     Description: The program function is to use a spinbox to output a roman numeral
#
#
#######################################################################################
import tkinter as tk
from tkinter import *
import logging


class RomanNumeralGuide:

    def __init__(self, master):
        # Getting the GUI going.
        self.master = master
        # Change title of GUI.
        master.title("Roman Numeral Guide")
        # Set background color of GUI.
        master.configure(background='black')
        # Set size of the GUI window.
        master.geometry("425x150")

        # Create label for when program starts to instruct user on how to start.
        self.numeral_output = Label(root, text="Press the arrows to select a numeral", bg="black", fg="cyan", font="Helvetica 18")

        # Create spinbox widget.
        self.spin_box = tk.Spinbox(root, state='readonly', from_=1, to=3999, bg="black", highlightbackground="black",
                                   buttonbackground="cyan", command=self.callback)

        # This button is for the Exit button.
        self.exit_button = Button(root, text="Exit", command=master.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                                  font="Helvetica 7 bold")

        # Add widgets to main window.
        self.spin_box.pack(padx=5, pady=15)
        self.numeral_output.pack(padx=5, pady=5)
        self.exit_button.pack(padx=5, pady=5)

    # Function converts integer input to roman numeral.
    @staticmethod
    def int_to_roman(int_input: object) -> object:
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
    def callback(self):
        try:
            # Get value from spinner box and call function to convert number
            selection = self.int_to_roman(int(self.spin_box.get()))
            # Set output font
            self.numeral_output.configure(font="Helvetica 24")
        except Exception as nex:
            # Display error message if number is out of range
            self.numeral_output.configure(text='Exception Error!')
            # Log error
            logging.exception("User tried to go to a value that is not present." + nex)
        # Output result
        self.numeral_output.configure(text=selection)


root = Tk()
romanNumeralGuide = RomanNumeralGuide(root)
# Run main loop for displaying window
root.mainloop()
