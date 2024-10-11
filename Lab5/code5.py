"""Write a Python program to square the elements of a list using the map() function."""
def square_elements(numbers):
    return list(map(lambda x: x ** 2, numbers))

numbers = [1, 2, 3, 4, 5]
result = square_elements(numbers)
print(result)  
# Output: [1, 4, 9, 16, 25]
