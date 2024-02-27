from sys import argv

LOWERCASE_A = "a"
LOWERCASE_Z = "z"
UPPERCASE_A = "A"
UPPERCASE_Z = "Z"
BASE_VALUE = 13
MOD_VALUE = 26

def is_letter(char): # Es una funcion porque tiene un output
    """Checks if char is a letter between a and z.

    char: (str) a single character
    Output: (bool) True if char is a letter, false otherwise.
    """

    is_lower_letter = char >= LOWERCASE_A and char <= LOWERCASE_Z
    is_upper_letter = char >= UPPERCASE_A and char <= UPPERCASE_Z
    return is_lower_letter or is_upper_letter

def enc_char(char): # Es una funcion porque tiene un output
    """Transform the given character in another encoded.
    
    char: (str) a single character
    Output: (str) encoded character
    """
    if not is_letter(char):
        return char
    value = ord(char)
    value += BASE_VALUE
    value = value % MOD_VALUE
    value += ord(LOWERCASE_A) if char >= LOWERCASE_A else ord(UPPERCASE_A)
    encoded_char = chr(value)

    return encoded_char

def enc_line(line):
    """Transform the given line in another encoded.

    Output: (str) encoded line
    """
    encoded_line = ""
    for my_char in line:
        encoded_line += enc_char(my_char)
    return encoded_line


def rot13(orig_file, dest_file): # Es un procedimiento y no una función porque no tiene un return.
    """Encrypts a file and save the result in another file.

    orig_file: (str) The original file
    dest_file: (str) The new encrypted file
    """
    with open (orig_file) as first_file, open(dest_file, "wt") as sec_file:
        for my_line in first_file:
            encoded_line = enc_line(my_line)
            sec_file.write(encoded_line)

original_file = argv[1]
new_file = argv[2]

rot13(original_file, new_file)