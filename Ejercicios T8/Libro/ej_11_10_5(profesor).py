from sys import argv

LOWERCASE_A = 'a'
LOWERCASE_Z = 'z'
UPPERCASE_A = 'A'
UPPERCASE_Z = 'Z'
BASE_VALUE = 13
MOD_VALUE = 26

def is_letter(char):
    '''
    Checks whether a given character is alphabetic.

    char: (str) a single character.
    Output: (bool) True if char is a letter, False otherwise
    '''
    is_lower_letter = char >= LOWERCASE_A and char <= LOWERCASE_Z
    is_upper_letter = char >= UPPERCASE_A and char <= UPPERCASE_A
    return is_lower_letter or is_upper_letter
    # if char >= 'a' and char <= 'z':
    #     return True
    # else:
    #     return False

def encode_char(char):
    '''
    Transforms the given character in another encoded.

    char: (str) a single character.
    Output: (str) single encoded character.
    '''
    if not is_letter(char):
        return char
    value = ord(char)
    value += BASE_VALUE
    value = value % MOD_VALUE
    #value += ord(LOWERCASE_A) if char >= LOWERCASE_A else ord(UPPERCASE_A)
    encoded_char = chr(value)
    return encoded_char

def encode_line(line):
    '''
    Transforms the given line in another encoded.

    line: (str) a sequence of characters ending in \n
    Output: (str) encoded line.
    '''
    encoded_line = ''
    for my_char in line:
        encoded_line += encode_char(my_char)
    return encoded_line

def rot13(orig_fname, enc_fname):
    '''
    Encodes a given file and saves the result in another file.

    orig_fname: (str) name of the original source text file.
    enc_fname: (str) name of the file to be created with encoded data.
    '''
    orig_file = open(orig_fname)
    enc_file = open(enc_fname, 'wt')
    for my_line in orig_file:
        encoded_line = encode_line(my_line)
        enc_file.write(encoded_line)
    orig_file.close()
    enc_file.close()

rot13(argv[1], argv[2])
