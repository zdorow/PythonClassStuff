from tkinter import *

# Getting the GUI going.
root = Tk()
root.title("Computer Purchase")
root.configure(background='black')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("455x550")

ALL = E+W+N+S

processorRadioVar = IntVar()
processorRadioVar.set(1)

memoryRadioVar = IntVar()
memoryRadioVar.set(1)

hardDriveRadioVar = IntVar()
hardDriveRadioVar.set(1)

opticalDriveRadioVar = IntVar()
opticalDriveRadioVar.set(1)

monitorRadioVar = IntVar()
monitorRadioVar.set(1)


# Here we do the tuition calculation in a for loop.
def calculate_purchase():

    processor = 200
    if processorRadioVar.get() == 2:
        processor = 400

    memory = 150
    if memoryRadioVar.get() == 2:
        memory = 250

    hard_drive = 125
    if hardDriveRadioVar.get() == 2:
        hard_drive = 200

    optical_drive = 50
    if opticalDriveRadioVar.get() == 2:
        optical_drive = 75
    elif opticalDriveRadioVar.get() == 3:
        optical_drive = 100

    monitor = 200
    if monitorRadioVar.get() == 2:
        monitor = 300
    elif monitorRadioVar.get() == 3:
        monitor = 400

    purchase = processor + memory + hard_drive + optical_drive + monitor
    return purchase


def update():
    new_total = calculate_purchase()
    purchasePrice.delete(0, END)
    purchasePrice.insert(0, f"${new_total:,.2f}")


# Function used for key bind.
def destroy():
    root.destroy()


# Defining the initial label that shows when program starts.
directionOutput = Label(root, text="Change options to calculate the cost of the computer\n "
                                   "Press Exit or Alt-e to kill the program",
                        bg="black", fg="cyan", font="Helvetica 12", wraplength=400)

processorLabel = Label(root, text="Processor", bg="black", fg="cyan", font="Helvetica 12")


processorStandardRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="Standard",
                                     value=1, variable=processorRadioVar, highlightbackground="black",
                                     activebackground="black", highlightthickness=6, font="Helvetica 8 bold",
                                     command=update)

processorHighSpeedRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="High Speed",
                                      value=2, variable=processorRadioVar, highlightbackground="black",
                                      activebackground="black", highlightthickness=6, font="Helvetica 8 bold",
                                      command=update)

memoryLabel = Label(root, text="Memory", bg="black", fg="cyan", font="Helvetica 12")


memory2megRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="2 Meg",
                              value=1, variable=memoryRadioVar, highlightbackground="black", activebackground="black",
                              highlightthickness=6, font="Helvetica 8 bold", command=update)


memory4MegRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="4 Meg",
                              value=2, variable=memoryRadioVar, highlightbackground="black", activebackground="black",
                              highlightthickness=6, font="Helvetica 8 bold", command=update)


hardDriveLabel = Label(root, text="Hard Drive", bg="black", fg="cyan", font="Helvetica 12")


hardDrive256Radio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="256 G", value=1,
                                variable=hardDriveRadioVar, highlightbackground="black", activebackground="black",
                                highlightthickness=6, font="Helvetica 8 bold", command=update)

hardDrive512Radio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="512 G",
                                value=2, variable=hardDriveRadioVar, highlightbackground="black",
                                activebackground="black",
                                highlightthickness=6, font="Helvetica 8 bold", command=update)

opticalDriveLabel = Label(root, text="Optical Drive", bg="black", fg="cyan", font="Helvetica 12")

opticalDriveCDRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="CD",
                                  value=1, variable=opticalDriveRadioVar, highlightbackground="black",
                                  activebackground="black", highlightthickness=6, font="Helvetica 8 bold",
                                  command=update)
opticalDriveCD_DVDRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="CD/DVD",
                                      value=2, variable=opticalDriveRadioVar, highlightbackground="black",
                                      activebackground="black", highlightthickness=6, font="Helvetica 8 bold",
                                      command=update)
opticalDriveDVD_RWRadio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="DVD/RW",
                                      value=3, variable=opticalDriveRadioVar, highlightbackground="black",
                                      activebackground="black", highlightthickness=6, font="Helvetica 8 bold",
                                      command=update)

monitorLabel = Label(root, text="Monitor", bg="black", fg="cyan", font="Helvetica 12")

monitor17Radio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="17 inch",
                             value=1, variable=monitorRadioVar, highlightbackground="black", activebackground="black",
                             highlightthickness=6, font="Helvetica 8 bold", command=update)
monitor19Radio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="19 inch",
                             value=2, variable=monitorRadioVar, highlightbackground="black", activebackground="black",
                             highlightthickness=6, font="Helvetica 8 bold", command=update)
monitor21Radio = Radiobutton(root, bg="black", fg="blue", selectcolor="black", text="21 inch",
                             value=3, variable=monitorRadioVar, highlightbackground="black", activebackground="black",
                             highlightthickness=6, font="Helvetica 8 bold", command=update)

totalLabel = Label(root, text="Total:", bg="black", fg="cyan", font="Helvetica 12")
purchasePrice = Entry(root)

total = calculate_purchase()
purchasePrice.insert(0, f"${total:,.2f}")

# Making the calculate button.
# calculateButton = Button(root, text="Calculate", bg="seashell3", highlightbackground="black",
#                          fg="blue", font="Helvetica 7 bold", command=calculate_purchase, underline=0)

# This is for the Exit button.
exitButton = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                    font="Helvetica 7 bold", underline=1)

directionOutput.grid(row=0, columnspan=4, padx=25, pady=5)

processorLabel.grid(row=1, columnspan=4, padx=5, pady=5)
processorStandardRadio.grid(row=2, columnspan=2, column=0, padx=5, pady=5, sticky=ALL)
processorHighSpeedRadio.grid(row=2, columnspan=2, column=1, padx=5, pady=5, sticky=ALL)

memoryLabel.grid(row=3, columnspan=4, padx=5, pady=5)
memory2megRadio.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=ALL)
memory4MegRadio.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky=ALL)

hardDriveLabel.grid(row=5, columnspan=4, padx=5, pady=5)
hardDrive256Radio.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=ALL)
hardDrive512Radio.grid(row=6, column=1, columnspan=2, padx=25, pady=5, sticky=ALL)

opticalDriveLabel.grid(row=7, columnspan=4, padx=5, pady=5)

opticalDriveCDRadio.grid(row=8, column=0, columnspan=2, sticky=ALL, pady=5)
opticalDriveCD_DVDRadio.grid(row=8, column=1, sticky=ALL, padx=5, pady=5)
opticalDriveDVD_RWRadio.grid(row=8, column=2, columnspan=2, sticky=ALL, padx=25, pady=5)

monitorLabel.grid(row=9, columnspan=4, padx=5, pady=5)
monitor17Radio.grid(row=10, column=0, columnspan=2, pady=5, sticky=ALL)
monitor19Radio.grid(row=10, column=1, sticky=ALL)
monitor21Radio.grid(row=10, column=2, columnspan=2, padx=25, pady=5, sticky=ALL)

totalLabel.grid(row=11, column=0, columnspan=2)
purchasePrice.grid(row=11, column=1)
exitButton.grid(row=12, columnspan=4, padx=15, pady=15)

# Key stroke bindings.
# root.bind('<Alt_L><c>', lambda e: calculate_purchase())
# root.bind('<Alt_L><C>', lambda e: calculate_purchase())
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

# Button set to calculate!
root.mainloop()
