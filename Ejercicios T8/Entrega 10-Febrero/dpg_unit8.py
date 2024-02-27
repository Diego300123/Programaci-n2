from sys import argv
import dpg_library

if len(argv) < 3:
    print("Use the next syntax:")
    print(argv[0], "p", "<name of the file>", "<Parameter (if you need)>")
    exit()

option = argv[1]

file = argv[2]

if len(argv) > 3:
    parameter = argv[3]

if option == "r":
    dpg_library.r(file)

if option == "s":
    try:
        print(dpg_library.s(file, parameter))
    except NameError:
        print("Please enter a student's name to search for in the file")
        print("Use the next syntax:")
        print(argv[0], "p", "<name of the file>", "<student name>")

if option == "m":
    print(dpg_library.m(file))

if option == "p":
    try:
        print(dpg_library.p(file, parameter))
    except NameError:
        print("Please, enter a value to compare with student grades")
        print("Use the next syntax:")
        print(argv[0], "p", "<name of the file>", "<value to compare>")

if option == "a":
    print("The average of grades is:", dpg_library.a(file)) 

if option == "o":
    print("Students with the grade over the average:", dpg_library.o(file))
