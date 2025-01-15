import sys

filename = sys.argv[1]

try:
    f = open(filename)
    no_of_lines = len(f.read())
    print(f.read())
    print(".readlines ", f.readlines())
   
    print(f"NO OF LINES= {no_of_lines}\nNo of characters= ")
except:
    print("File not found")