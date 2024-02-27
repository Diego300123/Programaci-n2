#Exercice 6, Write a program to calculate the greatest common divisors of two numbers that a user provides as an input.
num1 = int(input("Give me a number"))
num2 = int(input("Give me other number"))

if num1 == num2:
  print("The numbers are the same, it's imposible to calculate the greatest common divisor numbers")
elif num1 > num2:
  limit = num2
else:
  limit = num1

for i in range(1, limit + 1):
    remainder1 = num1 % i
    remainder2 = num2 % i
    if ((remainder1 == 0) and (remainder2 == 0)):
       common = i
print("The greatest common divisor of", num1, "and", num2, "is:", common)