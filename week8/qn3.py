"""
The Unix grep command searches a file and outputs the lines in the 
file that contain a certain pattern. Write an implementation of this. 
It will take two command-line arguments: the first is the string to look for, 
and the second is the file name. The output should be the lines in the file 
that contain the string.
"""
import sys

print(sys.argv)

print(sys.argv[2])


string = sys.argv[1]
filename = sys.argv[2]
print(filename)
f = open(f"{filename}", mode="r")
lines = f.readlines()
print(lines)

# remove new line escape character
new_lines = []
for line in lines:
    if "\n" in line:
        a = line[:-1]
        new_lines.append(a)
    else:
        new_lines.append(line)
# print("A: ", new_lines)
print(string)
if string in new_lines:
    if string == new_lines[-1]:
        line = lines.index(string)
        print(f"{string} appears in line: {line+1}")
    else: 
        line = lines.index(f"{string}\n")
        print(f"{string} appears in line: {line+1}")
