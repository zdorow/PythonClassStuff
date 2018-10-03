from tkinter import *

root = Tk()
root.title("Future Value Calculator")
root.configure(background='black')
root.geometry("395x275")

labelOutput = Label(root, text="Enter the numbers in their respective fields.\n"
                               "Press Calculate or Alt-c to calculate future value\n "
                               "Press Exit or Alt-x to kill the program\n",
                    bg="black", fg="cyan", font="Helvetica 12", wraplength=400)
labelOutput.pack(padx=5, pady=5)

presentValueEntry = Entry(root, bd=2, justify="center")
presentValueEntry.pack(padx=5, pady=5)

monthlyInterestEntry = Entry(root, bd=2, justify="center")
monthlyInterestEntry.pack(padx=5, pady=5)

monthsLeftEntry = Entry(root, bd=2, justify="center")
monthsLeftEntry.pack(padx=5, pady=5)

calculateButton = Button(root, text="Calculate", bg="seashell3", highlightbackground="black",
                         fg="blue", font="Helvetica 7 bold", underline=0)
calculateButton.pack(padx=5, pady=5)

exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold", underline=0)

exitButton.pack(padx=5, pady=5)


def future_value():
    labelOutput.configure(text="Welcome to the world of tomorrow!")


def destroy():
    root.destroy()


root.bind('<Alt_L><c>', lambda e: future_value())
root.bind('<Alt_L><x>', lambda f: destroy())

calculateButton.configure(command=future_value)
root.mainloop()
