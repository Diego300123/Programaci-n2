n = int(input("Please enter a number between 1 and 99: "))

n1 = int(n / 10)
n2 = int(n % 10)


if n1 > n2:
    maxi = n1
    mini = n2
else:
    maxi = n2
    mini = n1

if mini == 3:
    mini = str("E")
elif mini == 4:
    mini = str("A")
elif mini < 1:
    mini = str("0")

if maxi == 3:
    maxi = str("E")
elif maxi == 4:
    maxi = str("A")

mini = str(mini)
maxi = str(maxi)

print(mini + maxi)