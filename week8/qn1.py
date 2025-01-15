import sys

try: 
    f = open(f"{sys.argv[1]}", mode="r")
    print(f.read())
except:
    print("File not found")