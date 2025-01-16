"""
Computers are commonly used in encryption. A very simple form of encryption 
(more accurately "obfuscation") would be to remove the spaces from a message 
and reverse the resulting string. Write, and test, a function that takes a 
string containing a message and "encrypts" it in this way.
"""

def encryption_obfuscation(string):
    withoutspaces = string.split()
    reversed_array = []
    withoutspaces.reverse() 
    for i in withoutspaces:
        print(i)
        rev = ""
        for char in i:
            rev = char + rev
        reversed_array.append(rev)
    
    for  i in reversed_array:
        print(i, end="")

sentence = input("Enter a sentence to encrypt: ")
encryption_obfuscation(sentence)