def check_endswith(cels):
    if 'C' in cels:
        return True
    return False


def extract_value(array):
    actual_array = []
    for i in array:
        new_temp = float(i[:-1])
        actual_array.append(new_temp)
    return actual_array

def maximum(array):
    largest = array[0]
    for i in array:
        if i > largest:
            largest = i
    return largest

def minimum(array):
    smallest = array[0]
    for i in array:
        if i < smallest:
            smallest = i
    return smallest

def mean(array):
    sum = 0
    for i in array:
        sum += i
    
    mean = (sum / len(array))
    return mean

temp_list = []

def main_loop():

    while True:

        for i in range(6):
            temp = (input("Enter temperature in celsius ending with 'C': "))
            if len(temp) == 0:
                print("Please enter a value.")
                return -1
            if check_endswith(temp): 
                temp_list.append(temp)
            else:
                print("Invalid try again")
        break

    values = extract_value(temp_list)

    print(f"MAXIMUM: {maximum(values)} \nMINIMUM: {minimum(values)} \nMEAN: {mean(values)}")


main_loop()