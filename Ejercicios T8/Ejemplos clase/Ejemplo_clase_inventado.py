import sys

myfile = open(sys.argv[1], "w")
while True:
    typed_text = input("Type some text")
    if typed_text == "0":
        break
    myfile.write(typed_text + "\n")
myfile.close()
