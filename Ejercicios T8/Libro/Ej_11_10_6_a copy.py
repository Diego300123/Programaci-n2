from sys import argv
from pickle import loads

def load_data(filename):
    """Loads  file with data and converts them into a dictionary of keys and values.

    filename: (filename) A text file with a collection of key adn values separated by ":"
    Output: (dict) Get te file content as key-value pairs
    """
    my_dict = None 
    with open (filename) as my_file:
        encoded_data = my_file.read()
        my_dict = loads(encoded_data)
    return my_dict

result = load_data(argv[1])
print(result, type (result))