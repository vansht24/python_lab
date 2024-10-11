"""Write a Python program to compute the sum of elements of an array of integers. Use the map() function."""
def sum_of_elements(numbers):
    return sum(map(int, numbers))

numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print(result) 
 # Output: 15
