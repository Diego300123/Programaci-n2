import sys 

if len(sys.argv) < 3:
    print("Syntax:")
    print(sys.argv[0], "<original file> <new file in uppercase>")
    sys.exit

original_file = open(sys.argv[1])
new_file = open(sys.argv[2], "w")

"""mytext = original_file.read()
text_to_upper = mytext.upper()
new_file.write(text_to_upper)"""

for line in original_file:
    line_to_upper = line.upper
    new_file.write(line_to_upper)

original_file.close()
new_file.close()