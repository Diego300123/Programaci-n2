import sys

try:
    my_file = open(sys.argv[1])
except FileNotFoundError:
    print("The given filename doesn't exist")

else:
    for line in my_file:
            print(line)
"""    filecontent = my_file.read()
    print(filecontent)"""
my_file.close()