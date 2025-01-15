# Prompt the teacher for input
sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are attending? "))

# Calculate sweets per pupil and leftovers
sweets_per_pupil = sweets // pupils
leftover_sweets = sweets % pupils

# Display the results
print(f"Each pupil will receive {sweets_per_pupil} sweets.")
print(f"There will be {leftover_sweets} sweets left over.")
