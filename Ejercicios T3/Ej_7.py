#Exercice 7, Write a program to calculate the minimum common multiple of two numbers that a user provides as an input.
num1 = int(input("Give me a number:"))
num2 = int(input("Give me other number:"))
sart = max(num1, num2)

for i in range(sart, num1*num2 + 1):
  remainder1 = i % num1
  remainder2 = i % num2
  if ((remainder1 == 0) and (remainder2 == 0)):
    print("The minimum common multiple of", num1, "and", num2, "is:", i)
    break