#Exercice 9,Write a program to guess a number. To do this, ask for a number N, and then ask for numbers pointing out either “greater” or “lesser” (depending on whether the given number it is greater or not as regards to N). The process ends when the user gets it right.
import random

n = int(input("Enter a number:"))
secretN = random.randint(1,100)

while n != secretN:
    if n > secretN:
        print("The secret number is lesser")
        n = int(input("Try again:"))
    else:
        print("The secret number is greater")
        n = int(input("Try again:"))

print("You have guessed the secret number!! It was:", secretN)

"""
import random

n = None
secretN = random.randint(1,100)

while n != secretN:
    n = int(input("Type a number: "))

    if n > secretN:
        print("The secret number is lesser")
    elif n < secretN:
        print("The secret number is greater")

print("You have guessed the secret number!! It was:", secretN)"""