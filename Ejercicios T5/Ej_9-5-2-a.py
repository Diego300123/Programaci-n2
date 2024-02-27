"""a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}."""

def count_word(my_text):
    """Count the words in a text and save in a dictionary.

    my_text (str): any text
    output (dict): key -> word, value -> number of matches
    """
    times_by_word = {}
    word_list = my_text.split()

    for word in word_list:
        key = word.lower()
        if key not in times_by_word:
            times_by_word[key] = 1
        else:
            times_by_word[key] += 1

    return times_by_word

text = "Qué lindo día que hace hoy, la verdad que es un espléndido día hoy"
print(count_word(text))