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
for number in range(0, 1010, 10):
    print("The number: " + f"{number}")
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
