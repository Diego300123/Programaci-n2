annual = int(input("Enter your annual income: "))



final = int(0)

porcentages = [0.19, 0.24, 0.30, 0.37, 0.45, 0.47]

irpf = [2365.5, 1860, 4440, 9250, 10800]

if annual < 12450:
    a = "19% section (Less than 12450)"
    b = 0
    num = annual
    
elif annual >= 12450 and annual < 20200: 
    a = "24% section (From 12450 to 20200)"
    b = 1
    num = annual - 12450

elif annual >= 20200 and annual < 35000: 
    a = "30% section (From 20200 to 35000)"
    b = 2
    num = annual - 20200

elif annual >= 35000 and annual < 60000: 
    a = "37% section (From 35000 to 60000)"
    b = 3
    num = annual - 35000

elif annual >= 60000 and annual < 300000: 
    a = "45% section (From 60000 to 300000)"
    b = 4
    num = annual - 60000

elif annual >= 300000: 
    a = "47% section (Over 300000)"
    b = 5
    num = annual - 300000

for i in range(0, b):
    final = float(irpf[i]) + final

final = num * float(porcentages[b]) + final

c = annual - final

print(a)
print("The amount to be paid is: ", final)
print("The net amount recieved is: ", c)