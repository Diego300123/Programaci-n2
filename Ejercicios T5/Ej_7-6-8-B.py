def reverse_list(my_list):
    '''Turn around a list.
    my_list: (list)
    output: (list) reversed previous list values.
    '''
    length = len(my_list)
    limit = length // 2

    for i in range(0, limit):
        aux = my_list[i]
        my_list[i] = my_list[length -i -1]
        my_list[length -i -1] = aux

    return my_list

"""example = [14, "Pepe", 3.8, True, 7]
result = reverse_list(example)

print(result)"""

def reverse_list_V2(my_list):
    '''Turn around a list.
    my_list: (list)
    output: (list) reversed previous list values.
    '''
    length = len(my_list)
    for i in range(length):
        aux = my_list.pop()
        my_list.insert(0, aux)
    return my_list

example = [14, "Pepe", 3.8, True, 7]
result = reverse_list_V2(example)

print(result)