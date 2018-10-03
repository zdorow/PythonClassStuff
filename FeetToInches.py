
from tkinter import *

root = Tk()
root.title("Feet to Inches Calculator")
root.configure(background='black')
root.geometry("395x175")

labelOutput = Label(root, text="Enter the number in feet to convert to inches\n"
                               "Press Calculate or Alt-c to calculate inches\n "
                               "Press Exit or Alt-x to kill the program\n",
                               bg="black", fg="cyan", font="Helvetica 12", wraplength=400)
labelOutput.pack(padx=5, pady=5)

feetEntry = Entry(root, bd=2, justify="center")
feetEntry.pack(padx=5, pady=5)

calculateButton = Button(root, text="Calculate", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 7 bold", underline=0)
calculateButton.pack(padx=5, pady=5)

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold", underline=0)

exitButton.pack(padx=5, pady=5)


def calculate_inches():
    feet = int(feetEntry.get())
    inches = 12 * feet

    if feet == 1:
        labelOutput.configure(text=f"\n{feet}" + " foot is " + f"{inches}" + " inches.\n\n", pady=0)
    else:
        labelOutput.configure(text=f"\n{feet}" + " feet is " + f"{inches}" + " inches.\n\n", pady=0)

    calculateButton.configure(pady=0)


def destroy():
    root.destroy()


root.bind('<Alt_L><c>', lambda e: calculate_inches())
root.bind('<Alt_L><x>', lambda f: destroy())

calculateButton.configure(command=calculate_inches)
root.mainloop()
