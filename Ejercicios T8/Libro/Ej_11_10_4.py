from sys import argv

def grep(filename, string):
    """Look for a given string in a text file.

    filename: (str) A given text file
    string: (str) A given string 
    """
    with open(filename) as my_file:
        for line in my_file:
            if string in line:
                print(line)

if len(argv) < 3:
    print("Syntax:")
    print(argv[0], "<file> <string to search>")
    exit

grep(argv[1], argv[2])