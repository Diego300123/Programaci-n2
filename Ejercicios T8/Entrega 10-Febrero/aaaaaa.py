from sys import argv
from statistics import mean

SEPARATOR = ","
file = argv[1]



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

def grades_to_float_cgpt(my_list):
    """Convert a given list of grades into float values list.

    my_list: (list) List with the grades as strings
    Output: (list or str) List with the grades as float values or a message error
    """
    float_list = []
    try:
        for elem in my_list:
            grade = float(elem)
            if grade < 0 or grade > 10:
                raise ValueError(f"La nota de un alumno es igual a {elem}. Las notas deben estar entre 0 y 10.")
            float_list.append(grade)
        return float_list
    except ValueError as e:
        return str(e)
    
def s2(fname, name):
    """Checks if a given name matches a student's name. 
    If it matches it returns all the data for that student.

    fname: (str) The file with the students data
    name: (str) The given name
    Output: (str) The data of the students with that name
    """
    result = ""
    try:
        with open (fname) as my_file:
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
                result = "The student name does not match with anyone in the file."
    except FileNotFoundError:
        result = "The file does not exist."
    return result


# print(s2(file, argv[2]))
print(grades_to_float_cgpt(save_grades(file)))