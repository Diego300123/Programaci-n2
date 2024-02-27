import sys, pickle

SEPARATOR = ":"

def save_data(mydict, filename):
    """
    Save the content of a given dictionary into a tet file.

    mydict: (dict) Anny combination of key-values pairs.
    filename: (str) Destination file to the save the data of the dictionary.
    """
    with open(filename, "wb") as my_file:
        data = pickle.dumps(my_file)
        my_file.write(data)


test_dict = {'primero': '1', 'segundo': '2', 'tercero': '3'}
save_data(test_dict, sys.argv[1])