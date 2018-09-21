from tkinter import *

root = Tk()
root.title("Newtons")
root.geometry("275x150")
root.configure(background='black')
labelMass = Label(root, text=" Please enter the values for mass: ", bg="black", fg="cyan", font="Helvetica 10")
massEntry = Entry(root, bd=2, justify="center")
buttonToCalculateNewtons = Button(root, text=" Judge Weight ", bg="white", fg="black", font="Helvetica 8 bold")
weightTotalOutput = Label(root, text=" Press the button to perform weight calculation ", bg="black", fg="cyan", font="Helvetica 10")

def weightcalculator():
    try:
        mass = float(massEntry.get())
        newtons = mass * 9.8
        if newtons > 500:
            weightTotalOutput.configure(text="   Please try again! That is much too heavy!    ", bg="black", fg="cyan", font="Helvetica 10")
        elif newtons < 100:
            weightTotalOutput.configure(text="   Please try again! That is much too light!    ", bg="black", fg="cyan", font="Helvetica 10")
        else:
            weightTotalOutput.configure(text=f"That is juuuuust right at {newtons:.1f} newtons ", bg="black", fg="cyan", font="Helvetica 10")
    except:
        weightTotalOutput.configure(text="     Invalid Entry. Please enter a number.      ", bg="yellow",  fg="red", font="Helvetica 10 bold")

buttonToCalculateNewtons.configure(command=weightcalculator)
exitButton = Button(root, text="Exit", command=root.destroy, bg="white", fg="blue", font="Helvetica 7 bold")

labelMass.grid(row=0, column=0, columnspan=4, padx=15, pady=5)
massEntry.grid(row=1, column=0, columnspan=4, padx=15, pady=5)
buttonToCalculateNewtons.grid(row=2, column=0, columnspan=4, padx=15, pady=5)
weightTotalOutput.grid(row=3, column=0, columnspan=4, padx=15, pady=0)
exitButton.grid(row=4, column=0, columnspan=4, padx=15, pady=5)

root.mainloop()