#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 27, 2018
#
#     Description: The program function is to calculate tuition for the next 5 years
#
#
#######################################################################################
import tkinter as tk
from tkinter import *
import logging
# Getting the GUI going.
root = tk.Tk()
root.title("Tuition Calculator")
root.configure(background='black')
root.geometry("395x130")

tuitionOutput = Label(root, text="Press Calculate or Alt-c to calculate tuition\n "
                                 "Press Exit or Alt-e to kill the fairy that runs this program",
                      bg="black", fg="cyan", font="Helvetica 12", wraplength=400)

tuitionOutput.pack(padx=5, pady=5)

calculateButton = Button(root, text="Calculate", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 7 bold")
calculateButton.pack(padx=5, pady=5)

# This button is for the Exit button.
exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold")

exitButton.pack(padx=5, pady=5)


def calculate_tuition():

    tuition = 8000
    increase = .03

    tuition_year1 = tuition * increase
    tuition_year2 = tuition * (increase * 2)
    tuition_year3 = tuition * (increase * 3)
    tuition_year4 = tuition * (increase * 4)
    tuition_year5 = tuition * (increase * 5)

    tuitionOutput.configure(text=f"The tuition for year one is: ${tuition_year1:.2f}\n"
                                 f"The tuition for year two is: ${tuition_year2:.2f}\n"
                                 f"The tuition for year three is: ${tuition_year3:.2f}\n"
                                 f"The tuition for year four is: ${tuition_year4:.2f}\n"
                                 f"The tuition for year five is: ${tuition_year5:.2f}")


def destroy():
    root.destroy()


root.bind('<Alt_L><c>', lambda e: calculate_tuition())
root.bind('<Alt_L><e>', lambda f: destroy())


calculateButton.configure(command=calculate_tuition)
root.mainloop()
