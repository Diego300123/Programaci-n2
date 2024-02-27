"""b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario."""

def count_character (my_text):
    """Count the characters in a text and save in a dictionary.

    my_text (str): any text
    output (dict): key -> character, value -> number of matches
    """

    times_by_character = {}

    for character in my_text:
        key = character.lower()

        if key not in times_by_character:
            times_by_character[key] = 1
        else:
            times_by_character[key] += 1

    return times_by_character


text = "Qué lindo día que hace hoy, la verdad que es un espléndido día"

print(count_character(text))