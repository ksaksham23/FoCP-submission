import sys

def nl():
    filename = sys.argv[1]
    f = open(f"{filename}", "r")
    data = f.readlines()
    count = 1
    for i in range(1, len(data)):
        print(f"{count}. {data[i]}")
        count += 1


nl()