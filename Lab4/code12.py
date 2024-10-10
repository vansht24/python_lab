"""Write a program to display the following pattern: 1
22
333
4444
55555"""
def print_pattern_2(n):

    for i in range(1, n + 1):
        print(str(i) * i)

# Example usage:
n = 5
print_pattern_2(n)