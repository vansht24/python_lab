"""Write a program to count the sum of digits in the entered number.
"""
def sum_of_digits(num):

    sum_of_digits = sum(map(int, str(num)))
    return sum_of_digits

# Example usage:
number = 12345
result = sum_of_digits(number)
print(f"Sum of digits in 12345: {result}")