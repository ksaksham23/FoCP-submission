def check_endswith(cels):
    if 'C' in cels:
        return True
    return False

def celsius_to_fahrenheit(cels):
    if check_endswith(cels):
        numerical = float(cels[:-1])
        print(numerical)
 
        fahr = (numerical * 1.8) + 32
        return fahr
    else:
        return "End with C pls"
    

celsius = input("Enter temperature in celsius ending in 'C' (eg: 25C): ")

print(f"{celsius_to_fahrenheit(celsius)}F")