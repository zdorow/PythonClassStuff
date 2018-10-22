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

from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

canvas.create_rectangle(50, 50, 100, 100, fill='red')
canvas.create_polygon(70, 80, 125, 100, 12, 23, fill='black')
canvas.create_arc(20, 75, 150, 150, start=0, extent=180, fill='blue')

root.mainloop()