import sys

if len(sys.argv) < 2:
    print("Syntax:")
    print(sys.argv[0], "<matrix text filename>")
    sys.exit

matrix = [
    [2, 0, 3, -1],
    [3, -2, 10, 9],
    [5, 1, 7, 7]
]

with open(sys.argv[1], "wt") as my_file:
    data = "{0} {1}\n".format(len(matrix), len(matrix[0]))
    my_file.write(data)
    for row in matrix:
        line = ""
        for number in row:
            line += str(number) + " "
        my_file.write(line + "\n")
