# Design an algorithm that finds the maximum positive integer input by a user. 
# The user repeatedly inputs numbers until a negative value is entered.

# While the number that is imputed is positive the algorithm will compare
# two numbers, num_int (that is imputed) and max_int (that starts as 0).
# If the imputed number is larger that the recorded max_int the algorithm
# will change max_int so that the value of max_int becomes the last inputed
# number.
# This will continue until the user inputs a negative number. When a negative
# number is inputed the algorithm will break and print the maximum number.

num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0         # Counter for max_int is set at 0

while num_int >= 0:         # Loop will continue while inputed num_int is a positive number.
    if num_int > max_int:   # If the new input is larger than max_int we will assign a new number to max_int
        max_int = num_int
    
    num_int = int(input("Input a number: "))    # Do not change this line

    if num_int < 0:         # To stop the loop we insert a negative number.
        break

print("The maximum is", max_int)    # Do not change this line