import sys

def wc(filename):
    """Print the number of lines, words and character of a text file.

    filename: (str) A file's name.
    """
    with open(filename) as myfile:
        num_lines = 0
        num_words = 0
        num_characters = 0
        for line in myfile:
            num_lines += 1
            num_words += len(line.split())
            num_characters += len(line)
        print("The number of lines is:", num_lines)
        print("The number of words is:", num_words)
        print("The number of characters is:", num_characters)

wc(sys.argv[1])