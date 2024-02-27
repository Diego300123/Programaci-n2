import sys

if len(sys.argv) < 2:
    print("Please, use this syntax:")
    print(sys.argv[0], "<file to read>")
    sys.exit

with open(sys.argv[1]) as myfile:
    lines = myfile.readlines()
    longest_line = ""
    shortest_line = lines[0]
    for line in lines:
        if len(line) > len(longest_line):
            longest_line = line
        if len(line) < len(shortest_line):
            shortest_line = line

print("The longest line in the file is:", longest_line)
print("The shortest line in the file is:", shortest_line)