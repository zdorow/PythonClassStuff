'''
    Program written by: Zachary Dorow
    Advanced Programing - WK 6 - 2 Oct 2018
    Pg. 281 #10 Feet to Inches
    Comments added by Chris Carmody - 3 Oct 2018
'''

# Import library
from tkinter import *


# Create window and configure
root = Tk()
root.title("Feet to Inches Calculator")
root.configure(background='black')
root.geometry("395x175")


# Create Function to calculate and display results
# Moved the function to the top so the calculate button can fire the function (CC 3 Oct)
def calculate_inches():

    # Create and set variable based on entry box
    feet = feetEntry.get()

    # Validation to ensure the entry is a number (CC 3 Oct)
    try:
        int(feet)

        inches = 12 * int(feet)

        # Logic to update the labelOutput text
        if feet == 1:
            labelOutput.configure(text=f"\n{feet}" + " foot is " + f"{inches}" + " inches.\n\n", pady=0)
        else:
            labelOutput.configure(text=f"\n{feet}" + " feet is " + f"{inches}" + " inches.\n\n", pady=0)

    # On error of the entry, messagebox will be displayed
    except ValueError:
        messagebox.showinfo("Invalid Entry", "Please enter a valid number")


# Function needed to close the window with the access keys
def destroy():
    root.destroy()


# Create and set access keys
root.bind('<Alt_L><c>', lambda e: calculate_inches())
root.bind('<Alt_L><C>', lambda e: calculate_inches()) # Added incase Caps Lock is enabled (CC 3 Oct)
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy()) # Added incase Caps Lock is enabled (CC 3 Oct)

# Create and place Label to display instructions and result
labelOutput = Label(root, text="Enter the number in feet to convert to inches\n"
                               "Press Calculate or Alt-c to calculate inches\n "
                               "Press Exit or Alt-x to kill the program\n",
                    bg="black", fg="cyan", font="Helvetica 12", wraplength=400)
labelOutput.pack(padx=5, pady=5)

# Create and place entry box
feetEntry = Entry(root, bd=2, justify="center")
feetEntry.pack(padx=5, pady=5)

# Create and place calculate button
calculateButton = Button(root, text="Calculate", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 7 bold", underline=0, command=calculate_inches)
calculateButton.pack(padx=5, pady=5)

# Create and place exit button
exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold", underline=1) # Updated the underlined letter to match the access key (CC 3 Oct)
exitButton.pack(padx=5, pady=5)


# Create a loop to keep the window open
root.mainloop()

