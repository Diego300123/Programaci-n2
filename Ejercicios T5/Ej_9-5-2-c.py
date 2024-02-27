"""c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados."""

from random import randint
def dices(n):
    """Count the result of throwing two dices.

    n (int): number of times.
    output (dict): key -> result of the throw, value -> number of repetitions
    """
    number_by_result = {}
    for i in range(n):
        result = randint(2, 12)
        result = str(result)
        if result in number_by_result:
            number_by_result[result] += 1
        else:
            number_by_result[result] = 1

    return number_by_result

number = 100
print(dices(number))








"""times different numbers are repeated adding two dice's values"""