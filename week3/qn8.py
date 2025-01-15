number = int(input("Enter a number to get the times table for: "))
if 0 < number < 12:

    for i in range(13):
        print(f"{i} X {number} = {i * number}")

elif number < 0:
    for j in range(12, -1, -1):
        print(f"{j} X {number} = {j * number}")

else: 
    print("Please enter number between 0 to 12")