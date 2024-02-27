import sys 

SIZE = 2048

if len(sys.argv) < 3:
    print("Syntax:")
    print(sys.argv[0], "<original file> <copy file>")
    sys.exit

original_file = open(sys.argv[1], "rb")
new_file = open(sys.argv[2], "wb")

while True:
    content = original_file.read(SIZE)
    if not content: #Cuando no hay datos, content coge el valor None.
        break
    new_file.write(content)

original_file.close()
new_file.close()