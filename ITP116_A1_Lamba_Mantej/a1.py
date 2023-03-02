# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-09-04
# DESCRIPTION: this is assignment one that teaches us the basics of functions, variables and user input

import math


# Task 1
# Complete function double so that it takes a number and returns twice its value
# according to the examples in the docstring. Use a return statement; note that
# this function does not have a print statement.
def double(num: float) -> float:
    # multiplying the input by 2 to reach a final answer
    return num * 2.0


# Task 2
# Function our_maximum takes two numbers and returns the larger of the two.
# Complete the function.
def our_maximum(num1: float, num2: float) -> float:
    # checking if num1 is greater, if it is then we print num1
    if num1 > num2:
        return num1
    # checking if num2 is greater, if it is then we print num2
    elif num2 > num1:
        return num2
    else:
    # if they are equal then return None
        return None


# Task 3
# Complete the following function.
def max_of_min(num1: float, num2: float, value1: float, value2: float) -> float:
    # creating a list of the first two numbers
    numbers = [num1, num2]
    # creating a list of the second values
    values = [value1, value2]
    # finding the minimum of the first numbers
    min1 = min(numbers)
    # finding the minimum of the second values
    min2 = min(values)
    # returning the max of the numbers and values
    if (min1 > min2):
        return min1
    else:
        return min2


# Task 4
# Function format_name receives two parameters.
# The first parameter represents a first name and the second represents a last name.
# It returns a string in the format: last_name, first_name
# where last_name and first_name are replaced by the given last and first names.
def format_name(first_name: str, last_name: str) -> str:
    # printing out the last name, with string concatenation and a comma
    return last_name + ", " + first_name


# Task 5
# Complete the following function circle_area.
# It receives the radius and returns the area of the circle.
# Add proper comments.
def circle_area(radius: float) -> float:
    # using the math library to get pi and multiplying it by radius squared
    return math.pi * (radius**2)


# Task 6
# Function sum_to receives one parameter
# the parameter is a number
# returns an integer value: the sum of all integers from 1 to that number
# Add proper comments.
def sum_to(n: int) -> int:
    # creating num = 0
    num = 0
    # creating count = 1 for the sum of integers
    count = 1
    # while loop to run through count to n
    while count <= n:
        # adding count to num
        num += count
        # incrementing count
        count+=1
    # returning num
    return num


# Task 7
# Complete function is_odd which receives one parameter.
# the parameter is a number.
# returns a boolean value True if the number is odd and False otherwise.
# Add proper comments.
def is_odd(n: int) -> bool:
    # checking if the remainder of n/2 is not 0 to return True
    if n % 2 != 0:
        return True
    else:
        return False


# Task 8
# Complete function is_even which receives one parameter.
# the parameter is a number.
# returns a boolean value True if the number is even and False otherwise.
def is_even(n: int) -> bool:
    # checking if the remainder of n/2 is 0 to return True
    if n % 2 == 0:
        return True
    else:
        return False


# Complete calling
def main():
    print("Starting task 1, doubling a number.")
    num_to_double = input("Please enter the number you would like to duplicate: ")
    print("Double of", num_to_double, "is", double(float(num_to_double)))
    input("Press any key to continue...\n")

    print("Starting task 2, finding maximum.")
    first_num = input("Please enter the first number: ")
    second_num = input("Please enter the second number: ")
    print("Max of", first_num, "and", second_num, "is", our_maximum(float(first_num), float(second_num)))
    input("Press any key to continue...\n")

    print("Starting task 3, finding max of min.")
    user_num1 = input("Please enter the a value for num1: ")
    user_num2 = input("Please enter the a value for num2: ")
    user_value1 = input("Please enter the a value for value1: ")
    user_value2 = input("Please enter the a value for value2: ")
    print("Max of min of pairs (" + user_num1 + "," + user_num2 + ") and (" +
          user_value1 + "," + user_value2 + ") is ",
          max_of_min(float(user_num1), float(user_num2), float(user_value1), float(user_value2)))
    input("Press any key to continue...\n")

    print("Starting task 4, format name.")
    first_num = input("Please enter the first name: ")
    second_num = input("Please enter the last name: ")
    print(format_name(first_num, second_num))
    input("Press any key to continue...\n")

    print("Starting task 5, finding area of circle.")
    # Task 9
    # provide the code for calling function circle_area
    radius_input = input("Please enter a number for the radius: ")
    print("The area of the circle is ", circle_area(float(radius_input)))
    input("Press any key to continue...\n")

    print("Starting task 6, finding Summation of n.")
    to_sum_up_to = input("Please enter the number you'd like to sum up to: ")
    print("Summing up to ", to_sum_up_to, "yields", sum_to(int(to_sum_up_to)))
    input("Press any key to continue...\n")

    print("Starting task 7 checking odd:")
    user_input = input("Please enter the number you'd like to check: ")
    print("It is", is_odd(float(user_input)), "that", user_input, "is odd.")
    input("Press any key to continue...\n")

    print("Starting task 8 checking even:")
    # Task 10
    # provide the code for calling function is_even
    user_input = input("Please enter the number you'd like to check: ")
    print("It is", is_even(float(user_input)), "that", user_input, "is even.")

# Do not change
if __name__ == "__main__":
    main()
