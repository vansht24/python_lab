"""Q1.  WAP to find a number is Prime or not."""
number = int(input("Enter a number: "))

if number > 1:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break  
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number.")
#Output -
"""5 is a prime number."""