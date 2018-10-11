#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 10, 2018
#
#     Description: The program function is to calculate the number of names in a file.
#
#
#######################################################################################
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculate number of names in a file.")
root.configure(background='black')
root.geometry("395x175")


def calculate_number_of_names():

    try:
        name_count = 0

        with open("C:/Users/ZD/IdeaProjects/PythonClassStuff/Names.txt", "r") as lines_in_file:

            for line in lines_in_file:
                name_count += 1

        labelOutput.configure(text=f"\nThe number of names in the file is: {name_count}\n\n", pady=0)

    except IOError:
        messagebox.showinfo("Invalid Filepath", "Unable to find or read the file.")


def destroy():
    root.destroy()


root.bind('<Alt_L><c>', lambda e: calculate_number_of_names())
root.bind('<Alt_L><C>', lambda e: calculate_number_of_names())
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

labelOutput = Label(root, text="Press Calculate or Alt-c to read the number of names in the file.\n "
                               "Press Exit or Alt-x to kill the program\n",
                    bg="black", fg="cyan", font="Helvetica 12", wraplength=400)
labelOutput.pack(padx=5, pady=5)

calculateButton = Button(root, text="Calculate Number of names.", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 7 bold", underline=0, command=calculate_number_of_names)
calculateButton.pack(padx=5, pady=5)

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold", underline=1)
exitButton.pack(padx=5, pady=5)

root.mainloop()

