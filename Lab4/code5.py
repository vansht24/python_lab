"""Write a program to Calculate the value of nCr. """
def calculate_ncr(n, r):
    """Calculates the value of nCr."""

    from math import factorial

    ncr = factorial(n) / (factorial(r) * factorial(n - r))
    return ncr

# Example usage:
n = 5
r = 2
result = calculate_ncr(n, r)
print(f"5C2 = {result}")