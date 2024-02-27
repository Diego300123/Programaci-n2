def tuples_to_dictionary(tuples_list):
    """Convert a collection of given tuples to a dictionary.
    The fist element on each tuple will be a dictionary key.
    The following elements will be appended to a list linked to their keys.

    tuple_list (list): collection of tuples
    output (dict): input converted as per above description 
    """

    my_dict = {}
    for my_tuple in tuples_list:
        key, *value = my_tuple # Coge el primer elemento como clave del diccionario y el resto (por eso se usa el *) como su valor
        if key not in my_dict:
            my_dict[str(key)] = list(value)
        else:
            my_dict[str(key)].extend(value)
    return my_dict

l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
('Buenos', 'días') ]
print(tuples_to_dictionary(l))