import sys

if len(sys.argv) < 4:
    print("Please, use the next syntax:")
    print(sys.argv[0], "<filename> <word to write> <word to replace>")
    sys.exit

myfile = open(sys.argv[0], "r+")

lines = myfile.readlines()
my_word = sys.argv[1]
for line in lines:
    words = line.split()
    if my_word in words:



myfile.close()