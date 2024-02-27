import sys

if len(sys.argv) < 2:
    print("Syntax:")
    print(sys.argv[0], "<matrix text filename>")
    sys.exit

try:
    with open(sys.argv[1]) as my_file:
        lines = my_file.readlines()
        matrix = [] #Lista que va a conetener otras listas
        values = lines[0].split()
        num_rows = int(values[0])
        num_cols = int(values[1])
        for line in lines[1:]:
            values = line.split()
            int_values = []
            for value in values:
                int_values.append(int(value))
            matrix.append(int_values)
        print("Number of rows:", num_rows)
        print("Number of cols:", num_cols)
        print("Matrix values:", matrix)
except FileNotFoundError:
    print("The file does not exits.")

