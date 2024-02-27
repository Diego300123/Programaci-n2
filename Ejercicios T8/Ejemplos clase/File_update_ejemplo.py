with open("test.txt", 'r+') as myfile:
 
    lines = myfile.readlines()
    myfile.seek(0) # Posicionamos el puntero al principio
    myfile.truncate()

    for number, line in enumerate(lines):
        if number not in [4, 7]:
            myfile.write(line)