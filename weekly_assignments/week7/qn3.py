"""
Write a program that manages a list of countries and their capital cities. 
It should prompt the user to enter the name of a country. If the program already 
"knows" the name of the capital city, it should display it. Otherwise it should 
ask the user to enter it. This should carry on until the user terminates the
 program (how this happens is up to you).
"""

countries_capitals = {
    "england": "London",
    "USA": "WashingtonDc",
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "China": "Beijing",
    "Germany": "Berlin",
    "Spain": "Madrid"
}

def get_capital(country):
    if country.capitalize() in countries_capitals:
        return countries_capitals[country.capitalize()]
    else:
        return "IDK the capital"

get_country = input("Enter a country to get capital: ")
print(get_capital(get_country))