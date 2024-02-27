import sys

if len(sys.argv) < 3:
    print("Syntax:")
    print(sys.argv[0], "<file1> <file2>")
    sys.exit

myfile1 = open(sys.argv[1], "rb")
myfile2 = open(sys.argv[2], "rb")

content1 = myfile1.read()
content2 = myfile2.read()

if content1 == content2:
    print("The files are the same")
else:
    print("The files are different")

myfile1.close()
myfile2.close()