# ****************************************************************************************************
print("*" * 100)


# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Example usage:
result = even_or_odd(7)
print(result)  # Output: Odd

# ****************************************************************************************************
print("*" * 100)


# Multiply
# This code does not execute properly. Try to figure out why.
def multiply(a, b):
    return a * b


multiply_result = multiply(7, 3)
print(multiply_result)

# ****************************************************************************************************
print("*" * 100)


# Sum of positive
# You get an array of numbers, return the sum of all the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    total_positive_sum = 0
    if len(arr) == 0:
        return 0
    for num in arr:
        if num > 0:
            total_positive_sum += num
    return total_positive_sum


# Example usage:
positive_sum_result = positive_sum([-8, 9, 9, 2, -7])
print(positive_sum_result)  # Output: 20

# ****************************************************************************************************
print("*" * 100)


# Reversed Strings
# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    string_to_list = list(string)
    reversed_string = []
    for char_in_list in reversed(string_to_list):
        reversed_string.append(char_in_list)
    return ''.join(reversed_string)


# ****************************************************************************************************
# print("*" * 100)


# Convert a Number to a String!
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str(num)


# ****************************************************************************************************
# print("*" * 100)


# Return Negative
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Examples:
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes:
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative(number):
    if number <= 0:
        return number
    elif number > 0:
        return -number


# ****************************************************************************************************
# print("*" * 100)

# Convert boolean values to strings 'Yes' or 'No'.
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Example usage:
boolean_input = bool_to_word(True)
print(boolean_input)  # Output: "Yes"

boolean_input = bool_to_word(False)
print(boolean_input)  # Output: "No"

# ****************************************************************************************************
print("*" * 100)


# Opposite number
# Very simple, given an integer or a floating-point number, find its opposite.
# Examples:
# 1: -1
# 14: -14
# -34: 34
def opposite(number):
    return float(number) * -1


# ****************************************************************************************************
# print("*" * 100)

# Remove First and Last Character
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
def remove_char(s):
    s_to_list = list(s)
    end_s_list = s_to_list[1:-1]
    return ''.join(end_s_list)


# ****************************************************************************************************
# print("*" * 100)

# Square(n) Sum
# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1**2 + 2**2 + 2**2 = 9
def square_sum(numbers):
    pass


# ****************************************************************************************************
print("*" * 100)
