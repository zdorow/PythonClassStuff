#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Oct 27, 2018
#
#     Description: The program function is to take english users input and convert it
#       to Pig latin which is just the first letter taken to the end and ay added
#       in this case. Does not handle underscores since they are used to get single
#       quotes to be recognized by regex.
#
#######################################################################################
from tkinter import messagebox
from tkinter import *
import re

# GUI setup.
root = Tk()
root.title("Pig Latin Translator")
root.configure(background='black')


# This function takes one phrase and converts it to pig latin.
def alpha_to_igpay(alpha_input):

    # Splitting up the words with regex. Then adjusting and appending accordingly.
    word_split = re.split("(\W+)", alpha_input)

    # This goes through each element and if not alphanumeric then leave it alone. Else pig latin it.
    sentence = map(lambda word: word if not re.search('\w', word) else word[1:].lower() + word[0].lower() + 'ay',
                   word_split)
    return ''.join(sentence)


# This is the callback for the Translate button.
def callback():

        # Getting user input and changing the single quotes to underscores so regex will see them as a whole word.
        # Without this it's would be split into two words.
        user_input = english_entry.get().replace("'", "_")

        # Checking if numbers are input. They really should not be a part of the Pig Latin translation.
        number_check = re.search(r'\d', user_input)
        if user_input == "":
            messagebox.showerror("Invalid Entry", "Please enter a phrase.")
        # If this is commented out the numbers go through fine, but they are treated like normal characters.
        # It would be easy to get rid of them or treat them like punctuation, however no one talks in numbers.
        elif number_check:
            pig_latin_output.configure(text='\nPlease no numbers. They do not translate.\n')
        else:

            # Splitting the sentences with regex by punctuation.
            sentence_split = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", user_input)
            final_sentence_list = []

            # Looping through all the entered sentences split by punctuation.
            for sentences in sentence_split:

                # Capitalize the first letter in the sentence and put back all the single quotes.
                latin = alpha_to_igpay(sentences).lstrip().capitalize().replace("_", "'")
                # Append the final sentence output.
                final_sentence_list.append(latin)

            # Combining it all as a string for output.
            final_sentence = ' '.join(map(str, final_sentence_list))
            pig_latin_output.configure(text=final_sentence)


def destroy():
    root.destroy()


# GUI widgets setup and definition.
pig_latin_output = Label(root, text="\n Enter a phrase to translate. \n", bg="black", fg="cyan",
                         font="Helvetica 12", wraplength=400)

english_entry = Entry(root, bg="white", width=55)
english_entry.focus_set()

translate_button = Button(root, text=" Translate! ", command=callback, bg="seashell3", highlightbackground="black", fg="blue",
                          font="Helvetica 7 bold", underline=1)

exit_button = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                     font="Helvetica 7 bold", underline=1)

# Layout setup.
pig_latin_output.pack(padx=5, pady=15)
english_entry.pack(padx=15, pady=5)
translate_button.pack(padx=5, pady=5)
exit_button.pack(padx=5, pady=5)

# Key bindings.
root.bind('<Alt_L><t>', lambda e: callback())
root.bind('<Alt_L><T>', lambda e: callback())
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

root.mainloop()
