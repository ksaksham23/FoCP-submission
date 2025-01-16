def capitalize_name(name):
    # print(f"Hello, {name.capitalize()}")
    proper = name[0].upper() + name[1:len(name)].lower()
    print(f"Hello, {proper}")

capitalize_name("SAKSHAM")