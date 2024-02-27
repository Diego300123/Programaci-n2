import sys

def head(filename, n):
    """Print the first n lines for printing them.

        my_file: (str) the name of an existing text file to show the lines from.
        n: (int) number of the first lines to be printed out (n > 0)"""
    myfile = open(filename)
    for i in range(n):
        line = myfile.readline()
        print(line)
    myfile.close()


head(sys.argv[1], int(sys.argv[2]))