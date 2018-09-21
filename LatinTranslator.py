from tkinter import *

root = Tk()

root.title("Zach's Latin Lab")

top = Frame(root)
middle = Frame(root)
bottom = Frame(root)

header = Label(top, text="Little Latin Translator:")
header.pack()

exitButton = Button(bottom, text="Close Translator", command=root.destroy)
exitButton.pack()

top.pack(padx=3, pady=2)
middle.pack(padx=3, pady=2)
bottom.pack(padx=3, pady=2)

latinWord1 = "sinister"
latinWord2 = "dexter"
latinWord3 = "medium"

englishWord1 = "left"
englishWord2 = "right"
englishWord3 = "center"

def translate1():
    translateBtn1.configure(text=englishWord1, command=translate4)

def translate2():
    translateBtn2.configure(text=englishWord2, command=translate5)

def translate3():
    translateBtn3.configure(text=englishWord3, command=translate6)

def translate4():
    translateBtn1.configure(text=latinWord1, command=translate1)

def translate5():
    translateBtn2.configure(text=latinWord2, command=translate2)

def translate6():
    translateBtn3.configure(text=latinWord3, command=translate3)

translateBtn1 = Button(middle, text=latinWord1, command=translate1)
translateBtn2 = Button(middle, text=latinWord2, command=translate2)
translateBtn3 = Button(middle, text=latinWord3, command=translate3)

translateBtn1.grid(row=0, column=0, padx=(15, 15), pady=(5,15))
translateBtn2.grid(row=1, column=0, padx=(15, 15), pady=(5,15))
translateBtn3.grid(row=2, column=0, padx=(15, 15), pady=(5,15))

root.mainloop()