import sys

def head(my_file, n):
    """Print the first n lines for printing them.

        my_file: (str) the name of an existing text file to show the lines from.
        n: (int) number of the first lines to be printed out (n > 0)"""
    lines = my_file.readlines()
    i = 0
    while i < n:
        print(lines[i])
        i += 1

if len(sys.argv) < 3:
    print("Syntax:")
    print(sys.argv[0], "<file> <number of lines to read>")
    sys.exit

myfile = open(sys.argv[1])
number = int(sys.argv[2])

result = head(myfile, number)

myfile.close()