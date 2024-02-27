import sys

MAX_VALUE = 10
FILENAME = "table-" + sys.argv[1] + ".txt"

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
myfile = open(fname, "wt")

for i in range(1, MAX_VALUE + 1):
    result = number * i
    line = "{0} x {1} = {2}\n".format(number, i, result) #En el format se ponen los valores que vamos a poner en los {}
    myfile.write(line)
myfile.close()