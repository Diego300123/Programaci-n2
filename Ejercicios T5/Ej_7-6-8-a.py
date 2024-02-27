def reverse_list(my_list):
    '''Turn around a list.
    my_list: (list)
    output: (list) reversed previous list values.
    '''

    reversed_list = []
    for value in my_list:
        reversed_list.insert(0, value)
    return reversed_list

list_example = [1,2,3,4,5,6]
print ((reverse_list) (list_example))
