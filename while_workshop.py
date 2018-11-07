#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 30, 2018
#
#######################################################################################
# # While loop asking for two numbers
#
# exit_code = "go"
#
# while exit_code == "go":
#     int_input1 = int(input("Please enter the first number:"))
#     int_input2 = int(input("Please enter the second number:"))
#
#     total = int_input1 + int_input2
#
#     print(f"Total of two numbers added together: {total}")
#
#     exit_code = input("Type go to go again.")
# For loop that displays 0, 10, 20, 30, 40, 50 ... 1000
# for number in range(0, 1010, 10):
#     print("The number: " + f"{number}")
#     number += 10

# Loop that asks user to enter number 10 times and adds them all
# int_total = 0
#
# for number in range(1, 11):
#     int_input = int(input(f"Please enter number {number}:"))
#     int_total += int_input
#
# print(f"The total is: {int_total}")
# Augmented assignment operators.
#
# x += 1
# x *= 2
# x /= 10
# x -= 200
# int_input = int(input("Please enter a number between 1 through 100"))
#
# if int_input in range(1, 101):
#     print("Number in range.")
# else:
#     print("Number not in range")
# def times_ten(input_number, b, c):
#     output = input_number
#     print(f"{output}")
#     print(f"{b}")
#     print(f"{c}")
#
#     return output
#
# times_ten(3, 2, 1)
# def main():
#     x = 1
#     y =3.4
#     print(x, y)
#     change_us(x, y)
#     print(x, y)
#
# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
# main()

# def my_function(a, b, c):
# # #     d = (a + c) / b
# # #     print(d)
# # #
# # # my_function(2, 4, 6)

# name = open("my_name.txt", "w")
# name.write("Zach Dorow")
# name.close()
#
# name = open("my_name.txt", "r")
# print(name.read())
# name.close()

# try:
#     x = float('abc123')
#     print(x)
# except IOError:
#     print("This is a fucking error")
# except ZeroDivisionError:
#     print("There is nothing to divide here.")
# except:
#     print("Generally something is always wrong")
# print('This is the end, beautiful friend. The end.')
#
# list_dict_test = {'key1': 'test1', 'key2': [{'key2.1': 'test2.1', 'key2.2':'test2.2'}]}
# for key, value in list_dict_test.items(): # iterate through key and values in a dictionary
#     if isinstance(value, list): # if value is a list
#         for index_of_value in range(len(value[0].items())): # grabs index values in the list
#             print(index_of_value)
#             if index_of_value == 0:
#                 index_of_value + 1
#             for i in range(index_of_value): # iterate index from above
#                     print("x") # should print x twice
#         else:
#             print(key)
#             print(value)

# list_dict_test = {'key1': 'test1', 'key2': [{'key2.1': 'test2.1', 'key2.2': 'test2.2', 'key2.3': 'test2.3'}], 'key3': 'test3'}
# desired_list = list_dict_test['key2'][0].items()
#
# for range_of_value in range(len(list(desired_list))):
#
#     print(desired_list[range_of_value])

# list_dict_test = {'key1': 'test1', 'key2':[{'key2.1': 'test2.1', 'key2.2':'test2.2', 'key2.3':'test2.3'}], 'key3': 'test3'}
#
#
# def famj(my_value):
#     for key, value in list_dict_test.items():
#         if isinstance(value, list):
#             nested_dict = value[0]
#             for key, value in nested_dict.items():
#                 if value == 'test2.2':
#                     print(f"nested value: {value}")
#                     for key, value in nested_dict.items():
#                         if key == 'key2.3':
#                             print(f"nested value: {value}")
#
#
# famj(list_dict_test)
# # random sales dictionary
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
#
# items = sales.items()
# print('Original items:', items)
#
# # delete an item from dictionary
# add[sales['apple']]
# print('Updated items:', items)

# for key,value in list_dict_test.items():
#     if isinstance(value, list):
#         #print(value)#[{'key2.1': 'test2.1', 'key2.2': 'test2.2', 'key2.3': 'test2.3'}]
#         for range_of_value in range(len(value[0].items())):
#             #num_index = range_of_value #0,1,2
#             for x in range(range_of_value):
#             #print(x) #0,1,2
#                 for nested_dict_key_pairs in (list_dict_test['key2'][0].items()):
#                     print(nested_dict_key_pairs)
#
#     else:
#         print(key)
#         print(value)
# namesList = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
# numbers = [2] * 5
#
# print(numbers)
# list = [1,2,3,4,5,6,67,78,65]
#
# def sum_of_list(list):
#     return sum(list)
#
# print(sum_of_list(list))

# names_list = ["Joe"]
#
# name = "Ruby"
#
# if name in names_list:
#     print("Hello Ruby")
# else:
#     print("No Ruby")

# from tkinter import *
#
# root = Tk()
#
# canvas = Canvas(root, width=400, height=400)
# canvas.pack()
#
# canvas.create_rectangle(50, 50, 100, 100, fill='red')
# canvas.create_polygon(70, 80, 125, 100, 12, 23, fill='black')
# canvas.create_arc(20, 75, 150, 150, start=0, extent=180, fill='blue')
#
# root.mainloop()

# xml="<note><date>2015-09-01</date><hour>08:30</hour><to>Tove</to><from>Jani</from><body>Don't forget me this weekend!</body></note>"
#
# cleaner_xml = str.maketrans("<>/", "   ")
# cleaned_up_xml = xml.translate(cleaner_xml)
#
# print(cleaned_up_xml)

# mystr = 'yes'
# mystr += 'no'
# mystr += 'yes'
#
# mystr = 'abc' * 3
# print(mystr)

# mystr = 'abcdefg'
#
# print(mystr[2:5])

# numbers = [1, 2, 3, 4, 5, 6, 7]
# # print(numbers[4:6])
# if choice.upper() == 'Y':
#     name = 'joe'
#
# print(name.lower())
# print(name.upper())
# print(name)

# def email_check(string_input):
#     if string_input.endswith(".com"):
#         return True
#     else:
#         return False
#
# print(email_check("test"))

# def reverse(string_input):
#     return string_input[::-1]
#
# print(reverse("test"))

# mystring = 'cookies>milk>fude>cake>ice cream'
#
# string_list = mystring.split(">")
#
# print(string_list)

# Allowing the widget to take the full space of the window.
# self.pack(fill=BOTH, expand=1)
#
# # Creating a menu instance.
# menu = Menu(self.master)
# self.master.config(menu=menu)
#
# # Create the File object.
# file = Menu(menu)
#
# # Adds a command to the File option
# file.add_command(label="Save", command=self.client_exit)
# file.add_command(label="Save As", command=self.client_exit)
# file.add_command(label="Open", command=self.client_exit)
# file.add_command(label="Exit", command=self.client_exit)
#
# # Added "file" label to the menu.
# menu.add_cascade(label="File", menu=file)
#
# # Create the Edit object.
# edit = Menu(menu)
#
# # Adds a command to the Edit option.
# edit.add_command(label="Undo")
# edit.add_command(label="Redo")
#
# # Added "Edit" to our menu bar.
# menu.add_cascade(label="Edit", menu=edit)

# dct = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}
# print(dct.get("Friday", 'Not Found'))

# stuff = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}
# print(stuff["Tuesday"])

# dct = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
# for k in dct:
#     print(k)

# myset = set('1 2 3')
#
# print(myset)
#
# set1 = set([100, 200, 300, 400, 500])
# set2 = set([200, 400, 500])
# # set3 = set1.symmetric_difference(set2)
#
# print(set1.issuperset(set2))

# set1 = set(['d', 'e', 'f'])
# set2 = set(['a', 'b', 'c', 'd', 'e'])
# set3 = set2.symmetric_difference(set1)
#
# print(set3)

# print(dct.get('James', 'Not Found'))

# import pickle
#
# dct = {1: "a", 2: "b"}
#
# pickle.dump(dct, open("my_data.dat", "wb"))
#
# imported_dct = pickle.load(open("my_data.dat", "rb"))
#
# print(imported_dct)
# from tkinter import Tk, Frame, Menu
#
# class Example(Frame):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.master.title("Simple menu")
#
#         menubar = Menu(self.master)
#         self.master.config(menu=menubar)
#
#         fileMenu = Menu(menubar)
#         fileMenu.add_command(label="Exit", command=self.onExit)
#         menubar.add_cascade(label="File", menu=fileMenu)
#
#
#     def onExit(self):
#
#         self.quit()
# Simple enough, just import everything from tkinter.
from tkinter import *


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)


    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()