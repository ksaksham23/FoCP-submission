"""
Write a function that accepts a positive integer as a parameter and 
then returns a representation of that number in binary (base 2).
"""

def int_to_binary(number):
    quotient = number // 2
    remainder = number % 2
    binary_string = ""
    binary_string += str(remainder)
    print("First, ", binary_string)
    while quotient != 1:
        # binary_string += str(remainder)
        print("Before ", quotient)
        remainder = quotient % 2
        quotient = quotient // 2
        binary_string += str(remainder)
        print(quotient)
        print(remainder)
    
    binary_string += '1'
    rev = ""
    for i in binary_string:
        rev = i + rev
    return rev 

integer = int(input("Enter a number to convert to binary"))


print(int_to_binary(integer))