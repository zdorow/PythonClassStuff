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
root.title("Roman Numeral Guide")
root.configure(background='black')
root.geometry("325x150")

numeralOutput = Label(root, text="Press the arrows to select a numeral", bg="black", fg="cyan", font="Helvetica 18")


def callback():

	try:
		selection = int(spinbox.get())
		numeralOutput.configure(font="Helvetica 24")
	except Exception as nex:
		numeralOutput.configure(text='Exception Error!')
		logging.exception("User tried to go to a value that is not present." + nex)

	if selection == 1:
		numeralOutput.configure(text='I')
	elif selection == 2:
		numeralOutput.configure(text='II')
	elif selection == 3:
		numeralOutput.configure(text='III')
	elif selection == 4:
		numeralOutput.configure(text='IV')
	elif selection == 5:
		numeralOutput.configure(text='V')
	elif selection == 6:
		numeralOutput.configure(text='VI')
	elif selection == 7:
		numeralOutput.configure(text='VII')
	elif selection == 8:
		numeralOutput.configure(text='VIII')
	elif selection == 9:
		numeralOutput.configure(text='IX')
	elif selection == 10:
		numeralOutput.configure(text='X')

	else:
		numeralOutput.configure(text='Error!')


spinbox = tk.Spinbox(root, state='readonly', from_=1, to=10, bg="black", highlightbackground="black",
                     buttonbackground="black", command=callback)
# This button is for the Exit button.
exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold")

spinbox.pack(padx=5, pady=15)
numeralOutput.pack(padx=5, pady=5)
exitButton.pack(padx=5, pady=5)

root.mainloop()
