"""
Write and test a function that takes an integer as its parameter and 
returns the factors of that integer. (A factor is an integer which can
 be multiplied by another to yield the original).
"""

def get_factors(number):
    factors = []
    for i in range(1, number+1):   
        if number % i == 0:
            factors.append(i)
    print("List of factors are: ")
    for i in factors:
        print(i)

num = int(input("Enter a number: "))
get_factors(num)
