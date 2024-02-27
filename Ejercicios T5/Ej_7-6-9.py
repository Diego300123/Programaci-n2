def wrap(values):
    """Counnt how many times a number appears

    values (list): collection of values
    output (list): collection of tuples, values and repetitions
    """
    previous = None
    result = []
    counter = None
    for elem in values:
        if previous != elem:
            counter += 1
        else:
            my_tuple = (previous, counter)
            if previous != None:
                result.append(my_tuple)
            counter = 1

        previous = elem
    my_tuple = (previous, counter)
    result.append(my_tuple)
    
    return result

print(wrap([1, 1, 1, 3, 5, 1, 1, 3, 3]))