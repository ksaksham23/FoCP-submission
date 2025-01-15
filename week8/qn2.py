import sys

try:
    f1 = open(f"{sys.argv[1]}")
    f2 = open(f"{sys.argv[2]}")

    if f1.read() == f2.read():
        print(f"{sys.argv[1]} and {sys.argv[2]} contain the same contents")
    else:
        print("Different")
except: 
    print("File not found")