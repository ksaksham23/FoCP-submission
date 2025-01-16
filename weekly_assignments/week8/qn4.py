import sys

def wc(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_chars = sum(len(line) for line in lines)

            print(f"Lines: {num_lines}")
            print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

name_file = sys.argv[1]
wc(name_file)