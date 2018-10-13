#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 13, 2018
#
#     Description: The program function is to save golf players and scores.
#
#
#######################################################################################
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import date
# Import OS to open file in default program.
import os
# RegEx import
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

        names_and_scores = open("golf.txt", "a+")
        names_and_scores.write(entrySpace.get('1.0', END))
        labelOutput.configure(text="The names and scores have been successfully\n written to the file.")
        entrySpace.delete('1.0', END)

    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to write to the file.")


def read_from_file():
    try:
        os.startfile("golf.txt")
    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to read from the file.")


def calc_scores():
    try:
        line_count = 0
        scores = []

        with open("golf.txt", "r") as lines_in_file:
            line = lines_in_file.readline()
            while line:

                numbers_in_line = re.compile('\d+')
                score = numbers_in_line.findall(line)
                scores.extend(score)

                line_count += 1
                line = lines_in_file.readline()

        for numbers_in_array in range(len(scores)):
            scores[numbers_in_array] = int(scores[numbers_in_array])

        average = statistics.mean(scores)
        highest = max(scores)
        lowest = min(scores)
        top_golfer = ""

        for line in open("golf.txt"):
            if f"{lowest}" in line:
                top_golfer = line
                break
        for line in open("golf.txt"):
            if f"{highest}" in line:
                worst_golfer = line
                break

        messagebox.showinfo("Golf Scores for " + str(date.today()), "Average score is: " + f"{average:.2f}\n"
                            "The top golfer is: " + top_golfer +
                            "Golfer that needs improvement: " + worst_golfer + "\n")

    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to read from the file.")


def destroy():
    root.destroy()


root.bind('<Alt_L><A>', lambda e: write_to_file())
root.bind('<Alt_L><a>', lambda e: write_to_file())
root.bind('<Alt_L><R>', lambda e: read_from_file())
root.bind('<Alt_L><r>', lambda e: read_from_file())
root.bind('<Alt_L><C>', lambda e: calc_scores())
root.bind('<Alt_L><c>', lambda e: calc_scores())
root.bind('<Alt_L><X>', lambda f: destroy())
root.bind('<Alt_L><x>', lambda f: destroy())

labelOutput = Label(root, text="Press Add Button or Alt-A to write the names and scores to the file.\n "
                               "Press Read Button or Alt-R to read the names and scores to the file.\n "
                               "Press Calculate Button or Alt-C to calculate the current standings.\n "
                               "Press Exit or Alt-X to kill the program",
                    bg="black", fg="cyan", font="Helvetica 12", wraplength=500)
labelOutput.pack(padx=5, pady=15)

entrySpace = ScrolledText(root, width=25, height=15)

entrySpace.pack(padx=5, pady=5)

addButton = Button(root, text="Add Names and Scores to file", bg="seashell3", highlightbackground="black",
                   fg="blue", font="Helvetica 8 bold", underline=0, command=write_to_file)
addButton.pack(padx=5, pady=5)

readButton = Button(root, text="Read Names and Scores from file", bg="seashell3", highlightbackground="black",
                    fg="blue", font="Helvetica 8 bold", underline=0, command=read_from_file)
readButton.pack(padx=5, pady=5)

calcButton = Button(root, text="Calculate Average and Top Scores", bg="seashell3", highlightbackground="black",
                    fg="blue", font="Helvetica 8 bold", underline=0, command=calc_scores)
calcButton.pack(padx=5, pady=5)

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 8 bold", underline=1)
exitButton.pack(padx=5, pady=5)

root.mainloop()
