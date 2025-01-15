import sys

file_name = sys.argv[1]

try:
    file = open(file_name, mode="r")
    data = file.readlines()
    print(data)
    file.close()
    arr = file_name.split('.')
    arr[0] = f"{arr[0]}_copy"
    print(arr)
    backup_filename = '.'.join(arr)
    # open backup file in write mode
    backup = open(backup_filename, mode="w")
    for line in data:
        backup.write(line)
    backup.close()
except: 
    print("File not found ")