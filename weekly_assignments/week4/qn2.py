def check_case(string):
    upper_count = 0 
    lower_count = 0

    for i in string:
        if i.upper() == i:
            upper_count += 1
        else:
            lower_count += 1
    
    return upper_count, lower_count


upper_C, lower_C = check_case("RiWaZ")
print(f"UPPERCASE = {upper_C}\n LOWERCASE = {lower_C}\n")