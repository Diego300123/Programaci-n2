#Exercice 8, Write a program to calculate the value of the following formula, provided the number n as an input: ∑(j=1..n) ∑(i=1..j) j · i2
n = int(input("Enter a number:"))
result = 0

for j in range(1, n + 1):
    for i in range(1, j + 1):
        result = int(j * pow(i, 2)) + result

print("The final value is:", result)
