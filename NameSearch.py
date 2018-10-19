from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title("Find popular names")
root.configure(background='black')


def find_name():
    try:

        name = nameEntry.get()
        numbers = re.search(r'\d+', name)

        if numbers is not None:
            messagebox.showerror("Invalid Entry", "Please no numbers.")
        else:
            girl_names = open(r"C:\Users\ZD\IdeaProjects\PythonClassStuff\GirlNames.txt")
            boys_name = open(r"C:\Users\ZD\IdeaProjects\PythonClassStuff\BoyNames.txt")
            contents = boys_name.read() + girl_names.read()
            contents = contents.split()

            if name in contents:
                messagebox.showinfo(f"Information", f'{name} is in the list')
            else:
                messagebox.showinfo(f"Information", f'{name} is not a popular name based on that list.')
    except IOError:
        messagebox.showerror("Invalid Entry", "Unable to read the names file.")


def destroy():
    root.destroy()


root.bind('<Alt_L><F>', lambda e: find_name())
root.bind('<Alt_L><f>', lambda e: find_name())
root.bind('<Alt_L><X>', lambda f: destroy())
root.bind('<Alt_L><x>', lambda f: destroy())

nameEntryLabel = Label(root, text="Enter a name to find out if it is a popular name: ", bg="seashell3", fg="black",
                       font="Helvetica 12 bold")

nameEntry = Entry(root)

findButton = Button(root, text="Find out!", bg="seashell3", highlightbackground="black",
                    fg="black", font="Helvetica 8 bold", underline=0, command=find_name)

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="black",
                    font="Helvetica 8 bold", underline=1)

nameEntryLabel.pack(padx=5, pady=5)
nameEntry.pack(padx=5, pady=5)
findButton.pack(padx=5, pady=5)
exitButton.pack(padx=5, pady=5)

root.mainloop()
