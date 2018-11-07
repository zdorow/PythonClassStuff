#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Nov 3, 2018
#
#     Description: The program function is to manage e-mail addresses.
#
#######################################################################################
# Getting needed imports.
from tkinter import messagebox
from tkinter import *
import pickle
import re

# Making a default dict if nothing is there initially
try:
    names_and_email_dict = pickle.load(open("saved_names_and_addresses.dat", "rb"))
except FileNotFoundError:
    names_and_email_dict = {"Joe Johnson": "joe.johnson@gmail.com", "John Joeson": "john.joeson@outlook.com",
                            "Jane Doe": "jane.doe@hotmail.com"}
    pickle.dump(names_and_email_dict, open("saved_names_and_addresses.dat", "wb"))
print(names_and_email_dict)


# Creating a name and e-mail address entry with basic validation.
def create(name, emailAddress):

    if all_blank_check(name, emailAddress) is False and is_valid_name(name) is True and\
            is_valid_email(emailAddress) is True:
        if name in names_and_email_dict:
            messagebox.showerror("Failure to Add", "That name is already in use.")
        else:
            names_and_email_dict[name] = emailAddress
            pickle.dump(names_and_email_dict, open("saved_names_and_addresses.dat", "wb"))
            messagebox.showinfo("Success", name + " and " + emailAddress + " has been successfully added.")
            clear()
    else:
        messagebox.showerror("Entry blank", "Please enter a valid name and  valid e-mail address to add.\n"
                                            "This function requires both fields to be filled out.")


# The read function allows searching by name or e-mail address also with basic validation.
def read(name, emailAddress):

    # Count for the e-mail search for loop to make it so it only displays after the search has been exhausted.
    bad_match_count = 0
    if one_blank_check(name, emailAddress) is False and is_valid_name(name) is True or \
            is_valid_email(emailAddress) is True:
        if emailAddress == "" and name != "":
            if name in names_and_email_dict:
                messagebox.showinfo("E-mail", "The e-mail address of " + name + " is: " + names_and_email_dict[name])
                clear()
            else:
                messagebox.showerror("E-mail not found.", "The e-mail address of " + name + " is not found.")
        elif name == "" and emailAddress != "" and is_valid_name(name) is True and \
                is_valid_email(emailAddress) is True:
            for names, email_addresses in names_and_email_dict.items():
                if emailAddress == email_addresses:
                    messagebox.showinfo("Name", "The name of " + emailAddress + " is: " + names)
                    clear()
                    break
                else:
                    bad_match_count += 1
                    if bad_match_count >= len(names_and_email_dict):
                        messagebox.showerror("Name not found.", "The name of " + emailAddress + " is not found.")
        else:
            messagebox.showerror("Entry Error", "Please enter a valid name or a valid e-mail address to find. \n"
                                                "Searches can only be done for a valid stored name or e-mail address.")
    else:
        messagebox.showerror("Entry blank", "Please enter a valid value to search for. ")


# Updates a current e-mail address based on the name put in.
def update(name, emailAddress):
    if all_blank_check(name, emailAddress) is False:
        if name in names_and_email_dict and is_valid_email(emailAddress) is True:
            names_and_email_dict[name] = emailAddress
            pickle.dump(names_and_email_dict, open("saved_names_and_addresses.dat", "wb"))
            messagebox.showinfo("Success",  name + " and " + emailAddress + " has been successfully updated.")
            clear()
            print(names_and_email_dict)
        elif is_valid_email(emailAddress) is False:
            messagebox.showerror("Failed to Update",  emailAddress + " is not a valid e-mail address. ")
        elif is_valid_name(name) is False:
            messagebox.showerror("Failed to Update",  name + " is not a valid name address. ")
        else:
            messagebox.showerror("Failed to Update",  name + " is not a currently known name. ")
    else:
        messagebox.showerror("Entry blank", "Please enter a name or e-mail address to update.\n"
                                            "This function requires both fields to be filled out.")


# Delete works with either field.
def delete(name, emailAddress):

    bad_match_count = 0
    if one_blank_check(name, emailAddress) is False:
        if emailAddress == "" and name != "" and is_valid_name(name) is True:
            if name in names_and_email_dict:
                messagebox.showinfo("Name and E-mail Deleted", "The name " + name + " and email address "
                                    + names_and_email_dict[name] + " have successfully been deleted.")
                del names_and_email_dict[name]
                pickle.dump(names_and_email_dict, open("saved_names_and_addresses.dat", "wb"))
                print(names_and_email_dict)
                clear()
            else:
                messagebox.showerror("Name not found.", "The name of " + name + " is not found.")
        elif name == "" and emailAddress != "" and is_valid_email(emailAddress) is True:
            for names, email_addresses in names_and_email_dict.items():
                if emailAddress == email_addresses:

                    messagebox.showinfo("Name and E-mail Deleted", "The name: " + names + " and email address: "
                                        + email_addresses + " have successfully been deleted.")
                    del names_and_email_dict[names]
                    pickle.dump(names_and_email_dict, open("saved_names_and_addresses.dat", "wb"))
                    print(names_and_email_dict)
                    clear()
                    break
                else:
                    bad_match_count += 1
                    if bad_match_count >= len(names_and_email_dict):
                        messagebox.showerror("Name not found.", "The name of " + emailAddress + "is not found.")
        else:
            messagebox.showerror("Entry Error", "Please enter a valid name or a valid e-mail address to delete. \n"
                                                "Deletions can only be done by a valid name or  valid e-mail address.")
    else:
        messagebox.showerror("Entries Blank", "Please enter a name or an e-mail address. ")


# Function to allow us to see all the names in the dict.
def show_all():
    names_and_email_list = []

    for names, emails in names_and_email_dict.items():
        names_and_email_list.append((names, emails))

    names_and_emails = "\n".join(map(str, names_and_email_list))
    messagebox.showinfo("All Names and E-mail Addresses", "These are all the currently stored names and e-mail"
                                                          " addresses:\n" + names_and_emails)


# Validation of the e-mail address. Basically just ensuring the @ symbol is there and that it is bigger than 6 chars.
def is_valid_email(emailAddress):
    if len(emailAddress) <= 6:
        print(len(emailAddress))
        return False
    elif re.search("@", emailAddress) is None:
        print("Regex fail")
        return False
    else:
        return True


# Making sure there are no numbers in the names.
def is_valid_name(name):
    number_check = re.search(r'\d', name)
    if number_check:
        return False
    else:
        return True


# Checking for blank fields.
def one_blank_check(name, emailAddress):
    if name == "" and emailAddress == "":
        return True
    else:
        return False


def all_blank_check(name, emailAddress):
    if name == "" or emailAddress == "":
        return True
    else:
        return False


# Clearing the entry fields.
def clear():
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')


def destroy():
    root.destroy()


# GUI setup.
root = Tk()
root.title(" Names and E-mail Addresses ")
root.configure(background='black')
root.resizable(False, False)

top_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3',
                  highlightthickness=2)

middle_frame = Frame(root, highlightbackground="green", highlightcolor="black", background='seashell3',
                     highlightthickness=2, width=100, height=100, bd=0)

bottom_frame = Frame(root, highlightbackground="green", highlightcolor="black", background='seashell3',
                     highlightthickness=2, width=100, height=100, bd=0)


# Start to widgets definitions.
name_info_output = Label(top_frame, text="Enter a name and press button or select from the menu to perform an "
                                         "action. To add or update both fields are required.",
                         bg="seashell3", fg="black", font="Helvetica 11 bold", wraplength=400)

name_entry = Entry(top_frame, bg="white", width=35)
name_entry.focus_set()

email_info_output = Label(top_frame, text="Enter an e-mail address and press button or select from the menu "
                                          "to perform an action.",
                          bg="seashell3", fg="black", font="Helvetica 11 bold", wraplength=400)

email_entry = Entry(top_frame, bg="white", width=35)

create_button = Button(middle_frame, text=" Add ", command=lambda: create(name_entry.get(), email_entry.get()),
                       bg="seashell3", highlightbackground="black", fg="black", font="Helvetica 8 bold", underline=1)

read_button = Button(middle_frame, text=" Find ", command=lambda: read(name_entry.get(), email_entry.get()),
                     bg="seashell3", highlightbackground="black", fg="black", font="Helvetica 8 bold", underline=1)

update_button = Button(middle_frame, text=" Update ", command=lambda: update(name_entry.get(), email_entry.get()),
                       bg="seashell3", highlightbackground="black", fg="black", font="Helvetica 8 bold", underline=1)

delete_button = Button(middle_frame, text=" Delete ", command=lambda: delete(name_entry.get(), email_entry.get()),
                       bg="seashell3", highlightbackground="black", fg="black", font="Helvetica 8 bold", underline=1)

clear_button = Button(bottom_frame, text=" Clear ", command=lambda: clear(),
                      bg="seashell3", highlightbackground="black", fg="black", font="Helvetica 8 bold", underline=1)

exit_button = Button(bottom_frame, text=" Exit ", command=lambda: destroy(), bg="seashell3",
                     highlightbackground="black", fg="black", font="Helvetica 8 bold", underline=2)

# Getting the menu bar in the GUI.
menu_bar = Menu(root)

# Create the file menu dropdown.
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Add", command=lambda: create(name_entry.get(), email_entry.get()), accelerator="Alt+A")
file_menu.add_command(label="Find", command=lambda: read(name_entry.get(), email_entry.get()), accelerator="Alt+F")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=destroy, accelerator="Alt+X")
menu_bar.add_cascade(label="File", menu=file_menu)

# Create edit menu.
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Update", command=lambda: update(name_entry.get(), email_entry.get()), accelerator="Alt+U")
edit_menu.add_command(label="Delete", command=lambda: delete(name_entry.get(), email_entry.get()), accelerator="Alt+D")
edit_menu.add_command(label="Clear", command=clear, accelerator="Alt+C")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu dropdown.
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About Program",
                                                                         "This program allows for managing a persistent"
                                                                         " \nName and E-mail list.\n\n"
                                                                         "Functions that require both fields:\n\n"
                                                                         " - Create\n - Update\n\n"
                                                                         "Functions that use one field or the other:\n\n"
                                                                         " - Find\n - Delete\n\n"))
help_menu.add_separator()
help_menu.add_command(label="List All", command=show_all)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Display the menu.
root.config(menu=menu_bar)

# Layout definition.
top_frame.pack(padx=6, pady=6, fill="both", expand="yes")
name_info_output.pack(padx=5, pady=5)
name_entry.pack(padx=15, pady=5)
email_info_output.pack(padx=5, pady=5)
email_entry.pack(padx=15, pady=5)

middle_frame.pack(padx=6, pady=0, fill="both", expand="yes")
create_button.pack(side=LEFT, padx=35, pady=5)
read_button.pack(side=LEFT, padx=35, pady=5)
update_button.pack(side=LEFT, padx=35, pady=5)
delete_button.pack(side=LEFT, padx=35, pady=5)

bottom_frame.pack(padx=6, pady=1, fill="both")
clear_button.pack(side=LEFT, padx=35, pady=5)
exit_button.pack(side=RIGHT, padx=35, pady=5)


# Key binding stuff.
root.bind('<Alt_L><a>', lambda a: create(name_entry.get(), email_entry.get()))
root.bind('<Alt_L><A>', lambda a: create(name_entry.get(), email_entry.get()))

root.bind('<Alt_L><f>', lambda b: read(name_entry.get(), email_entry.get()))
root.bind('<Alt_L><F>', lambda b: read(name_entry.get(), email_entry.get()))

root.bind('<Alt_L><u>', lambda c: update(name_entry.get(), email_entry.get()))
root.bind('<Alt_L><U>', lambda c: update(name_entry.get(), email_entry.get()))

root.bind('<Alt_L><d>', lambda d: delete(name_entry.get(), email_entry.get()))
root.bind('<Alt_L><D>', lambda d: delete(name_entry.get(), email_entry.get()))

root.bind('<Alt_L><c>', lambda e: clear())
root.bind('<Alt_L><C>', lambda e: clear())

root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

root.mainloop()
