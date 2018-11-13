# from tkinter import *
#
# def donothing():
# 	filewin = Toplevel(root)
# 	button = Button(filewin, text="Do nothing button")
# 	button.pack()
#
# root = Tk()
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)
#
# filemenu.add_separator()
#
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
#
# editmenu.add_separator()
#
# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)
#
# menubar.add_cascade(label="Edit", menu=editmenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)
#
# root.config(menu=menubar)
# root.mainloop()

from tkinter import *

def NewFile():
	print ("New File!")
def OpenFile():
	name = "Fuck"
	print (name)
def About():
	print ("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()