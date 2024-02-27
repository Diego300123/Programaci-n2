import sys

SEPARATOR = ":"

def save_data(mydict, filename):
    """
    Save the content of a given dictionary into a tet file.

    mydict: (dict) Anny combination of key-values pairs.
    filename: (str) Destination file to the save the data of the dictionary.
    """
    with open(filename, "wt") as my_file:
        for key in mydict:
            value = mydict[key]
            line = key + SEPARATOR + value + "\n"
            my_file.write(line)


test_dict = {'primero': '1', 'segundo': '2', 'tercero': '3'}
save_data(test_dict, sys.argv[1])