# shortest arguments question

import sys

arguments = sys.argv[1:] 
print(arguments)
shortest = arguments[0]
for i in arguments:
    if len(str(i)) < len(shortest):
        shortest = i

print(f"Shortest argument= {shortest}")