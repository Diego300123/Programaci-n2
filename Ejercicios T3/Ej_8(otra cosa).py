#Exercice 8, Write a program to calculate the value of the following formula, provided the number n as an input: ∑(j=1..n) ∑(i=1..j) j · i2
n = int(input("Enter a number:"))
result = None

j = int((n / 2) * (n + 1))

i = int((j / 2) * (j + 1))

result = j * (i ** 2)

print("The first value is:", j)
print("The second value is:", i)
print("The final value is:", result)