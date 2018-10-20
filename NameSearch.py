#Imported modules
from tkinter import *
from tkinter import messagebox
import re

#Program window with title & background
root = Tk()
root.title("Find popular names")
root.configure(background='black')

#Function finds name
def find_name():
    try:
        #Retreive name entry from user
        name = nameEntry.get()
        numbers = re.search(r'\d+', name)

        #Validation if entry is a number
        if numbers is not None:
            messagebox.showerror("Invalid Entry", "Please no numbers.")
        else:
            #Opening both files and putting list into one variable list
            girl_names = open(r"GirlNames.txt")
            boys_name = open(r"BoyNames.txt")
            contents = boys_name.read() + girl_names.read()
            contents = contents.split()

            #If statement to see if name was in list
            if name in contents:
                messagebox.showinfo(f"Information", f'{name} is in the list')
            else:
                messagebox.showinfo(f"Information", f'{name} is not a popular name based on that list.')
    #Message box if unable to read file names
    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to read the names file.")

#destroy function
def destroy():
    root.destroy()

#Binding alt + key
root.bind('<Alt_L><F>', lambda e: find_name())
root.bind('<Alt_L><f>', lambda e: find_name())
root.bind('<Alt_L><X>', lambda f: destroy())
root.bind('<Alt_L><x>', lambda f: destroy())

#Intro Label
nameEntryLabel = Label(root, text="Enter name to find out if it is a popular name: ", bg="black", fg="cyan",
                       font="Helvetica 12",)
#Entry for name
nameEntry = Entry(root)

#Find button to search name
findButton = Button(root, text="Find out!", bg="seashell3", highlightbackground="black",
                    fg="blue", font="Helvetica 8 bold", underline=0, command=find_name)
#Exit button
exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 8 bold", underline=1)

#Packing program widgets
nameEntryLabel.pack(padx=5, pady=5)
nameEntry.pack(padx=5, pady=5)
findButton.pack(padx=5, pady=5)
exitButton.pack(padx=5, pady=5)

#Keep program running
root.mainloop()
