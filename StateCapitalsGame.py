#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 30, 2018
#
#     Description: The program function is to have users guess the state capitals.
#
#######################################################################################
from tkinter import messagebox
from tkinter import *
import random
import time
import re

# GUI setup.
root = Tk()
root.title("State Capital Quiz Machine")
root.configure(background='black')

state_capitals_dic = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
    'Indiana': 'Indianapolis', 'Iowa': 'Des Monies', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
    'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

correct_answer_count = []
incorrect_answer_count = []


def callback(state_chosen):

    user_input = guess_entry.get().lower()
    number_check = re.search(r'\d', user_input)
    new_state = pick_a_state()
    guess_button.configure(command=lambda: callback(new_state))
    if user_input == "":
        messagebox.showerror("Invalid Entry", "Please enter a guess.")
    elif number_check:
        messagebox.showerror("Invalid Entry", "State capital names do not have numbers.")
    else:
        if user_input == state_capitals_dic[state_chosen].lower():
            correct_answer_count.append(user_input)
            count_output.configure(text=" Correct for: \n" + state_chosen + "\n---\nPlease guess for: \n" + new_state +
                                        f"\n\nCorrect: {len(correct_answer_count)}\n" +
                                        f"Incorrect: {len(incorrect_answer_count)}")
        else:
            incorrect_answer_count.append(user_input)
            count_output.configure(text=" Incorrect for: \n" + state_chosen + "\n---\nPlease guess for: \n" + new_state
                                        + f"\n\nCorrect: {len(correct_answer_count)}\n" +
                                        f"Incorrect: {len(incorrect_answer_count)}")
    root.bind('<Return>', lambda e: callback(new_state))
    root.bind('<Alt_L><s>', lambda e: callback(new_state))
    root.bind('<Alt_L><S>', lambda e: callback(new_state))


def pick_a_state():
    all_states = list(state_capitals_dic.keys())
    state_chosen = random.choice(all_states)
    return state_chosen


def destroy():
    root.destroy()


first_state = pick_a_state()

count_output = Label(root, text=" Enter the capital of:\n" + first_state + "\n\nCorrect: 0\n" +
                     "Incorrect: 0",
                     bg="black", fg="cyan", font="Helvetica 12", wraplength=400)

guess_entry = Entry(root, bg="white", width=35)
guess_entry.focus_set()

guess_button = Button(root, text=" Submit Guess! ", command=lambda: callback(first_state),
                      bg="seashell3", highlightbackground="black", fg="blue", font="Helvetica 7 bold", underline=1)

exit_button = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                     font="Helvetica 7 bold", underline=1)

count_output.pack(padx=5, pady=15)
guess_entry.pack(padx=15, pady=5)
guess_button.pack(padx=5, pady=5)
exit_button.pack(padx=5, pady=5)

root.bind('<Return>', lambda e: callback(first_state))
root.bind('<Alt_L><s>', lambda e: callback(first_state))
root.bind('<Alt_L><S>', lambda e: callback(first_state))
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

root.mainloop()
