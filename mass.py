from tkinter import *

# Create root window
root = Tk()

# Set the title of the window
root.title("Newtons")

# Set the size of the window
# Adjusted the window size to center the content - Chris Carmody 21 Sep
root.geometry("225x175")

# Set the backgroud color of the window
root.configure(background='black')

# Create the mass label
labelMass = Label(root, text="Please enter the values for mass:", bg="black", fg="cyan", font="Helvetica 10")

# Create the entry widget
massEntry = Entry(root, bd=2, justify="center")

# Create a button to calculate weight
buttonToCalculateNewtons = Button(root, text=" Judge Weight ", bg="white", fg="black", font="Helvetica 8 bold")

# Create a label for weight total
# Added wraplenght to keep this line from changing the column widths - Chris Carmody 21 Sep
weightTotalOutput = Label(root, text="Press the button to perform weight calculation", bg="black", fg="cyan", font="Helvetica 10", wraplength=200)

# Create a function to calculate weight
def weightcalculator():

    # Create a try block
    try:
        # Convert the mass entry to a float
        mass = float(massEntry.get())

        # Calcualte newtons
        newtons = mass * 9.8

        # Check if the newtons is greater than 500 and write a message to a label
        if newtons > 500:
            weightTotalOutput.configure(text="Please try again! That is much too heavy!", bg="black", fg="cyan", font="Helvetica 10")

        # Check if the newtons is less than 100 and write s message to a label
        elif newtons < 100:
            weightTotalOutput.configure(text="Please try again! That is much too light!", bg="black", fg="cyan", font="Helvetica 10")

        # If its not to heavy or too light, write a newtons to a label
        else:
            weightTotalOutput.configure(text=f"That is juuuuust right at {newtons:.1f} newtons", bg="black", fg="cyan", font="Helvetica 10")

    # Catch any exception and write to a label
    except:
        weightTotalOutput.configure(text="Invalid Entry. Please enter a number.", bg="yellow",  fg="red", font="Helvetica 10 bold")

# Configure button to execute weightcalculator() function
buttonToCalculateNewtons.configure(command=weightcalculator)

# Create a button that exiets the program
exitButton = Button(root, text="Exit", command=root.destroy, bg="white", fg="blue", font="Helvetica 7 bold")

# Set the mass label on the grid
labelMass.grid(row=0, column=0, columnspan=4, padx=15, pady=5)

# Set the mass entry on the grid
massEntry.grid(row=1, column=0, columnspan=4, padx=15, pady=5)

# Set the calculate button on the grid
buttonToCalculateNewtons.grid(row=2, column=0, columnspan=4, padx=15, pady=5)

# Set the total weight on the grid
weightTotalOutput.grid(row=3, column=0, columnspan=4, padx=15, pady=0)

# Set the exit button on the grid
exitButton.grid(row=4, column=0, columnspan=4, padx=15, pady=5)

# Execute the main loop
root.mainloop()
