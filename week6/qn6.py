"""
decrypt the same message
"""

import random

interval = random.randint(2, 20)

def generate_random_letters(interval):
    letters = [chr(i) for i in range(97, 127)]
    letter_per_interval = []
    for i in range(interval):
        letter = letters[random.randint(0, 26)]
        letter_per_interval.append(letter)
    
    
    return ''.join(letter_per_interval)


def encryption(msg):
    arr = msg.split()
    total_letters= [] 
    for i in arr:
        for char in i:
            total_letters.append(char)
    
    random_letters = generate_random_letters(2)
    encrypted_msg = random_letters.join(total_letters)
    return encrypted_msg 

sentence = input("Enter a message to encrypt: ")
print(f"Encrypted message: {encryption(sentence)}")
    
def decryption(encrypted_msg, interval):
    decrypted_msg = []
    step = interval + 1
    for i in range(0, len(encrypted_msg), step):
        decrypted_msg.append(encrypted_msg[i])
    
    return ''.join(decrypted_msg)
    
print(decryption(encryption(sentence), 2))