def  cut_a_str(my_text, size):
    """Cut a given string into pieces of given size, always in the spaces.
     
    my_text (str): original text
    size (int): length of the pieces to divide my_text
    Output (list): a collection of the pieces my_text
    """
    left = 0
    right = size - 1
    solution = []
    total_length = len(my_text)

    while right < total_length - 1:
        piece = my_text[left:right + 1]
        while my_text[right] != " " and my_text[right +1] != " ":
            right = 

        solution.append(piece)
        left = right +1
        right = min(left + size -1, total_length -1)
    return solution
