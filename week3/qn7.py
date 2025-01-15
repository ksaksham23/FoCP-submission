number = int(input("Enter a number to get the times table for: "))
if 0 < number < 12:

    for i in range(13):
        print(f"{i} X {number} = {i * number}")

else: 
    print("Please enter number between 0 to 12")