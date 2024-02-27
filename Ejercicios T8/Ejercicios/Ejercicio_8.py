import sys

MAX_VALUE = 10
FILENAME = "table-{0}.txt"

def validate_number(value):
    """
    Checks that the user provide value is a number between 1 and 10.
    Throws ValueError otherwise.
    
    value: (str) user provided value
    Output: (int) 1 < number < 10"""

    number = int(value)
    if number > 10 or number < 1:
        raise ValueError("The number must be between 1 and 10")
    return number

def check_parameter(param):
    """
    Converts a given param into a valid number. 
    Reports potential errors to end user and exits the program.
   
    param: (str) user provided value
    Output: (int) 1 < number < 10"""

    try:
        number = validate_number(param)
    except ValueError as ex:
        print("Error in firts parameter:", param)
        print(ex)
        sys.exit()
    return number


if (len(sys.argv)) < 3:
    print("Syntax:")
    print(sys.argv[0], "<number between 1 and 10> <number between 1 and 10>")
    sys.exit

n = check_parameter(sys.argv[1])
m = check_parameter(sys.argv[2])

fname = FILENAME.format(n)
myfile = open(fname)

lines = myfile.readlines()
print(lines[m-1])

myfile.close()