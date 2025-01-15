def remove_last_char(string):
    if len(string) > 1:
        return string[-1]
    else:
        return string
    

print(remove_last_char("hello"))       # Expected: "hell"
print(remove_last_char("Python!"))    # Expected: "Python"
print(remove_last_char("A"))          # Expected: "A"
print(remove_last_char(""))           # Expected: ""