n = int(83)

n1 = int(n / 10)
n2 = int(n % 10)

if n1 == 3:
    n1=str("E")
elif n1 == 4:
    n1=str("A")
elif n1 < 1:
    n1=str("0")

if n2 == 3:
    n2=str("E")
elif n2 == 4:
    n2=str("A")

n1 = str(n1)
n2 = str(n2)

print(n1 + n2)