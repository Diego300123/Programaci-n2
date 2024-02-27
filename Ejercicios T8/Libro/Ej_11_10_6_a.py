from sys import argv

SEPARATOR = ":"

def load_data(filename):
    """Loads  file with data and converts them into a dictionary of keys and values.

    filename: (filename) A text file with a collection of key adn values separated by ":"
    Output: (dict) Get te file content as key-value pairs
    """
    file_as_dict = {}
    with open (filename) as my_file:
        for line in my_file:
            data = line.split(SEPARATOR)
            key = data[0].strip()
            value = data[1].strip()
            file_as_dict[key] = value
    return file_as_dict

result = load_data(argv[1])
print(result, type (result))