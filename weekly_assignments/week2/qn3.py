students = int(input("Enter the number of students: "))
group_size = int(input("Required group size: "))

groups = students // group_size
leftover = students % group_size

print(f"There will be {groups} with {leftover} students left over.\n")
