#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 13, 2018
#
#     Description: The program function is to save golf players and scores.
#
# These are the 5 names and format I used, however this would work with a fairly
# large list provided the format was something similar.
# Joe Namath, 90
# Bill DiMaggio, 76
# Greg Sanchez, 67
# Nicole Gary, 66
# Sasha Sanchez, 88
#
#######################################################################################
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import date
# Import OS to open file in default program.
import os
# RegEx import.
import re
# Statistics imported for ease of getting the average.
import statistics

root = Tk()
root.title("Add Golf Scores to File")
root.configure(background='black')
root.geometry("595x500")


# Function to take any ScrolledText input and write it to the file.
def write_to_file():
    try:
        # Append the golf text file if data is already there.
        names_and_scores = open("golf.txt", "a+")
        names_and_scores.write(entrySpace.get('1.0', END))
        labelOutput.configure(text="The names and scores have been successfully\n written to the file.\n\n")
        entrySpace.delete('1.0', END)

    # With the file location I doubt this would ever be hit, but not bad to have it.
    # Eventually input validation would want to be added. That would go here.
    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to write to the file.")


# Pop open the file in the default text editor of the OS.
# If the file is not found throw a message box error up.
def read_from_file():
    try:
        os.startfile("golf.txt")
    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to read from the file.")


# Function to calculate average, along with highest and lowest scorers.
def calc_scores():
    try:
        scores = []

        # Open the file as a read and read it line by line.
        with open("golf.txt", "r") as lines_in_file:
            line = lines_in_file.readline()

            # While loop to read all the lines in the file.
            while line:

                # Regex the numbers out of each line in the file.
                numbers_in_line = re.compile('\d+')

                # Find all that match the compiled Regex request.
                score = numbers_in_line.findall(line)

                # Extend the list (not append).
                scores.extend(score)

                # Get that next line.
                line = lines_in_file.readline()

        # Loop to convert all the numbers in the array to int since they are read in as string.
        for numbers_in_array in range(len(scores)):
            scores[numbers_in_array] = int(scores[numbers_in_array])

        # Built-in math functions to get the desired values.
        average = statistics.mean(scores)
        highest = max(scores)
        lowest = min(scores)
        top_golfer = ""

        # Once the highest and lowest score is determined we search the file
        #  for the first line that has that score.
        for line in open("golf.txt"):
            if f"{lowest}" in line:
                top_golfer = line
                break
        for line in open("golf.txt"):
            if f"{highest}" in line:
                worst_golfer = line
                break

        # Messagebox to display output of Calculate Button.
        messagebox.showinfo("Golf Scores for " + str(date.today()), "Average score is: " + f"{average:.2f}\n"
                            "The top golfer is: " + top_golfer +
                            "Golfer that needs improvement: " + worst_golfer + "\n")

    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to read from the file.")


def destroy():
    root.destroy()


# Various key bindings for the button functions.
root.bind('<Alt_L><A>', lambda e: write_to_file())
root.bind('<Alt_L><a>', lambda e: write_to_file())
root.bind('<Alt_L><R>', lambda e: read_from_file())
root.bind('<Alt_L><r>', lambda e: read_from_file())
root.bind('<Alt_L><C>', lambda e: calc_scores())
root.bind('<Alt_L><c>', lambda e: calc_scores())
root.bind('<Alt_L><X>', lambda f: destroy())
root.bind('<Alt_L><x>', lambda f: destroy())


# Button and input portion.
labelOutput = Label(root, text="Press Add Button or Alt-A to write the names and scores to the file.\n "
                               "Press Read Button or Alt-R to read the names and scores to the file.\n "
                               "Press Calculate Button or Alt-C to calculate the current standings.\n "
                               "Press Exit or Alt-X to kill the program",
                    bg="black", fg="cyan", font="Helvetica 12", wraplength=500)

entrySpace = ScrolledText(root, width=25, height=15)

addButton = Button(root, text="Add Names and Scores to file", bg="seashell3", highlightbackground="black",
                   fg="blue", font="Helvetica 8 bold", underline=0, command=write_to_file)

readButton = Button(root, text="Read Names and Scores from file", bg="seashell3", highlightbackground="black",
                    fg="blue", font="Helvetica 8 bold", underline=0, command=read_from_file)

calcButton = Button(root, text="Calculate Average, Top and Poorest Scores", bg="seashell3", highlightbackground="black",
                    fg="blue", font="Helvetica 8 bold", underline=0, command=calc_scores)

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 8 bold", underline=1)

# Layout.
labelOutput.pack(padx=5, pady=15)
entrySpace.pack(padx=5, pady=5)
addButton.pack(padx=5, pady=5)
readButton.pack(padx=5, pady=5)
calcButton.pack(padx=5, pady=5)
exitButton.pack(padx=5, pady=5)

root.mainloop()
