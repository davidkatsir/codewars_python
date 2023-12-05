# ****************************************************************************************************
print("****************************************************************************************************")


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
print("****************************************************************************************************")


# Multiply
# This code does not execute properly. Try to figure out why.
def multiply(a, b):
    return a * b


multiply_result = multiply(7, 3)
print(multiply_result)

# ****************************************************************************************************
print("****************************************************************************************************")


# Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.
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
print("****************************************************************************************************")

# ****************************************************************************************************
print("****************************************************************************************************")
