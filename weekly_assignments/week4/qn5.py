def fahrenheit_to_celsius(fahr):
    cels = (fahr - 32) / 1.8
    return cels

def celsius_to_fahrenheit(cels):
    fahr = (cels * 1.8) + 32
    return fahr


print(f"{fahrenheit_to_celsius(100)}")
print(f"{celsius_to_fahrenheit(25)}")