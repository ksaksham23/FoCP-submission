"""
Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!
"""
import sys

temperature_readings = sys.argv[1:]

def endswith_C(temperature):
    if temperature.endswith('C'):
        return True
    return False

def extract_value(array):
    actual_array = []
    for i in array:
        new_temp = int(i[:-1])
        actual_array.append(new_temp)
    return actual_array

def maximum(temperature_values):
    largest = temperature_values[0]
    print(type(largest))
    print(temperature_values)
    for i in temperature_values:
        if i > largest:
            largest = i
    return largest

def minimum(temperature_values):
    smallest = temperature_values[0]
    for i in temperature_values:
        if i < smallest:
            smallest = i
    return smallest

def mean(temperature_values):
    result = sum(temperature_values) / len(temperature_values)
    return result


def main():   
    if len(temperature_readings) < 2:
        print("Not enough arguments")
        return "INSUFFICIENT ARGUMENTS"
    for i in temperature_readings:
        if not endswith_C(i):
            print("Temperature must end with C")
            return "Must end with C" 
    actual_array = extract_value(temperature_readings)
    greatest = maximum(actual_array)
    smallest = minimum(actual_array)
    average = mean(actual_array)

    print(f"MAXIMUM: {greatest}\nMINIMUM: {smallest}\nAVERAGE: {average}")

main()