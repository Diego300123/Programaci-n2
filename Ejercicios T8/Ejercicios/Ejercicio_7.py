import sys

MAX_VALUE = 10
FILENAME = "table-{0}"

if len(sys.argv) < 2:
    print("Syntax:")
    print(sys.argv[0], "<number between 1 and 10>")
    sys.exit

try:
    number = int(sys.argv[1])
except ValueError:
    print("Please, enter an integer number")
    sys.exit()

if number > 10 or number < 1:
    print("The number must be between 1 and 10")
    sys.exit()

fname = FILENAME.format(number)
myfile = open(fname)

data = myfile.read()
print(data)

myfile.close()