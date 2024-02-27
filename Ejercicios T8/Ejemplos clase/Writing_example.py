"""lines = ['One', 'Two', 'Three', 1, 2, 3.5, True, False, ]

myfile = open('myfile.txt', 'w')
for line in lines:
    myfile.write(str(line) + "\n") 
myfile.close()"""

lines1 = ['One', 'Two', 'Three', 1, 2, 3.5, True, False, ]
lines2 = ['Four\n', 'Five\n', 'Six\n']

myfile = open('myfile.txt', 'w')
for line in lines1:
    myfile.write(str(line) + "\n") 
myfile.write(lines2)
myfile.close()