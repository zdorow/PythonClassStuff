#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 20, 2018
#
#     Description: The program function is to take a list of World Series winners and
#       output how many times they have won.
#
#######################################################################################
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("World Series Winners")
root.configure(background='black')


# Function to find the number of times a team has won
def find_number_of_times_won(event):

        # Getting the active selection.
        team_name = winnersListBox.get(ACTIVE)

        # Resetting the value because sometimes it seemed to add them.
        number_won = None
        number_won = split_up_winners_list.count(team_name)
        worldSeriesWonOutput.configure(text=f'They have won {number_won} of times')


# Function to kill the program.
def destroy():
    root.destroy()


# Loading up the list for the initial loading of the list. Show message box if we cannot find the file.
try:
    teams_text_file = open(r"C:\Users\ZD\IdeaProjects\PythonClassStuff\WorldSeriesWinners.txt")
    winners_list = teams_text_file.read()
    split_up_winners_list = winners_list.splitlines()
except IOError:
    messagebox.showerror("Invalid File Path", "Unable to read the team names file.")
    destroy()

# Bind access keys for EXIT.
root.bind('<Alt_L><X>', lambda f: destroy())
root.bind('<Alt_L><x>', lambda f: destroy())

# Labels for directing user.
worldSeriesLabel = Label(root, text="Click through the list of World Series Winners\n from 1903 through 2009. ",
                         bg="seashell3", fg="black", font="Helvetica 12 bold")

# Listbox creation.
winnersListBox = Listbox(root, bg="white", fg="black", font="Helvetica 12 bold")

# Making a winners list removing duplicates.
for winners in set(split_up_winners_list):
    winnersListBox.insert(END, winners)

# Binding the find_number_of_times_won to a various number of events to make sure the GUI updates.
# Still kinda buggy IMO. Maybe a scroll box would be better?
winnersListBox.bind("<<ListboxSelect>>", find_number_of_times_won)
winnersListBox.bind("<Double-Button-1>", find_number_of_times_won)
winnersListBox.bind("<Button-1>", find_number_of_times_won)

# Outputting the total times won once something is selected.
worldSeriesWonOutput = Label(root, text="No Team Selected",
                             bg="seashell3", fg="black", font="Helvetica 12 bold")

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="black",
                    font="Helvetica 8 bold", underline=1)

# Layout Setup.
worldSeriesLabel.pack(padx=5, pady=5)
winnersListBox.pack(padx=5, pady=5)
worldSeriesWonOutput.pack(padx=5, pady=5)
exitButton.pack(padx=5, pady=5)

root.mainloop()
