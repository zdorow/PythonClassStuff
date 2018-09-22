#######################################################################################
#
#     This program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Sept 8, 2018
#
#     Description: The program function is to take user input and validate then calculate
#       tip,tax and then the total of the meal
#
#######################################################################################
# This loop is for validating user input.
while True:
    try:
        # This is where we want to get a float number. Integers will be turned into float.
        meal = float(input("Please enter the total charge for the food and drinks: "))
        break

    # What the user sees when they input invalid data
    except:
        print("Please enter a number with the full dollars and cents of the meal.")

# Static variable definition
tip = 0.18
tax = 0.07

# Calculations needed for output
tipTotal = meal * tip
taxTotal = meal * tax
mealTotal = meal + tipTotal + taxTotal

# Printing the output with formatting for expected output when handling money,
print(f"Tip Total: {tipTotal:.2f}")
print(f"Tax Total: {taxTotal:.2f}")
print(f"Meal Total: {mealTotal:.2f}")
