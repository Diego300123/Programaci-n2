from sys import argv
from statistics import mean
from pickle import dumps

SEPARATOR = ","
EQUAL = "="
file = argv[1]

def file_to_dict(fname):
    """
    Convert a given file into a dict


    """
    with open(fname) as my_file:
        data_list = []
        for line in my_file:
            my_dict = {}
            my_line = line.split(SEPARATOR)
            my_dict ["Student"] = my_line[0].strip()
            my_dict ["Mark"] = my_line[1].strip()
            my_dict ["E-mail"] = my_line[2].strip()
            my_dict ["Phone"] = my_line[3].strip()
            data_list.append(my_dict)
    return data_list

def get_bin_file(filename = "students.cfg"):
    """
    """
    with open(filename) as my_file:
        for line in my_file:
            data = line.split(EQUAL)
            bin_file = data[1].strip()
        return bin_file

def write_bin_data(my_dict, bin_file):
    """
    """
    with open(bin_file, "wb") as my_bin_file:
        bin_data = dumps(my_dict)
        my_bin_file.write(bin_data)

def save_names(fname):
    """Save the names are in the first position of a list 
    
    fname: (str) List with all the lines of data
    Output: (list) List with all the names
    """
    names = []
    with open (fname) as my_file:
        for line in my_file:
            line_list = line.split(SEPARATOR)
            names.append(line_list[0].strip())
    return names

def save_grades(fname):
    """Save the grades are in the second position of a list 
    
    fname: (str) List with all the lines of data
    Output: (list) List with all the grades
    """
    marks = []
    with open (fname) as my_file:
        for line in my_file:
            line_list = line.split(SEPARATOR)
            marks.append(line_list[1].strip())
    return marks

def grades_to_float(my_list):
    """Convert a given list of grades into float values list.

    my_list: (list) List with the grades as strings
    Output: (list) List with the grades as float values
    """
    float_list = []
    for elem in my_list:
        try:
            grade = float(elem)
            if grade < 0 or grade > 10:
                raise ValueError(f"La nota de un alumno es igual a {elem}. Las notas deben estar entre 0 y 10.")
            float_list.append(grade)
        except ValueError as e:
            print(e)
            exit()
    return float_list

def comparate_numbers(num_list, name_list, value):
    """Take a grades list and a names list and compare the grades with a given value.
    If the grade is above the value the name in that line will be returned at the final.

    num_list: (list) List with the grades as float values
    name_list: (list) List with the names
    value: (float) Float value acting as a comparator
    Output: (list) List of the names of students whose grades are above the value
    """
    result = []
    x = 0
    for i in num_list:
        if i > value:
            result.append(name_list[x])
            x += 1
        else:
            x += 1
    return result

def lists_to_dict(name_list, grade_list):
    """Convert list with names and list with grades into a dictionary
    The keys wil be the names and the values will be the grades

    name_list: (list) List with students' names
    grade_list: (list) List with students' grades
    Output: (dict) Get key-value pairs from the lists
    """
    keys = name_list
    values = grade_list
    length = len(keys)
    my_dict = {}

    for i in range(length):
        my_dict[keys[i]] = values[i]
    return my_dict


# User options:

def r(fname):
    """
    """
    my_dict = file_to_dict(fname)
    data = get_bin_file()
    write_bin_data(my_dict, data)

def a(fname): 
    """Calculate the average grades for the students.
    
    fname: (str) The file with the students's data
    Output: (float) The average
    """
    marks = save_grades(fname)
    float_list = grades_to_float(marks)
    result = mean(float_list)
    return result

def o(fname): 
    """Return the name of the students with the marks over the average.

    fname: (str) The file with the students' data
    Output: (list) Name of the students who have grades above the average
    """
    avg_grades = a(fname)
    names = save_names(fname)
    grade_list = grades_to_float(save_grades(fname))
    result = comparate_numbers(grade_list, names, avg_grades)
    return result   

def p(fname, value): 
    """Return the name of the students with the marks over the given value.

    fname: (str) The file with the students' data
    value: (str) The user proveded value
    Output: (list) Name of the students who have grades above the given value
    """
    n = float(value)
    names = save_names(fname)
    grade_list = grades_to_float(save_grades(fname))
    result = comparate_numbers(grade_list, names, n)
    return result

def m(fname): 
    """Returns a dict of students' names with their grades, ordered from highest to lowest.

    fname: (str) The file with the students data
    Output: (dict) Ordered list with the names and the grades as key-value pairs
    """
    names = save_names(fname)
    grade_list = grades_to_float(save_grades(fname))
    my_dict = lists_to_dict(names, grade_list)
    values = list(my_dict.keys())
    n = len(values)
    for i in range(n):
        for j in range(0, n - i - 1):
            if my_dict[values[j]] < my_dict[values[j + 1]]:
                values[j], values[j + 1] = values[j + 1], values[j]
    ordered_dict = {}
    for key in values:
        ordered_dict[key] = my_dict[key]
    return ordered_dict

def s(fname, name):
    """Checks if a given name matches a student's name.
    If it matches it returns all the data for that student.

    fname: (str) The file with the students data
    name: (str) The given name
    Output: (str) The data of the students with that name
    """
    result = ""
    try:
        with open(fname) as my_file:
            cap_name = name.capitalize()
            name_found = False
            for line in my_file:
                words = line.split()
                if cap_name in words:
                    name_found = True
                    for elem in line:
                        result += elem.strip()
                    result += "\n"
            if not name_found:
                raise ValueError("Student name not found in file.")
    except Exception as e:
        print(e)
    return result