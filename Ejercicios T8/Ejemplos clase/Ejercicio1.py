import sys

if len(sys.argv) < 2:
    print("Please enter a valid text filename.")
    sys.exit

myfile = open(sys.argv[1], "r")

lines = myfile.readlines()

longest_line = lines[0]
shortest_line = lines[0]

for line in lines:
    if len(line) > len(longest_line):
            longest_line = line
    if None or len(line) < len(shortest_line):
            shortest_line = line

myfile.close()
print("The longest line is:", longest_line)
print("The shortest line is:", shortest_line)