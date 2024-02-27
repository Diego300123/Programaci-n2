import sys

print(sys.argv)
print(type(sys.argv))

if len(sys.argv) == 1:
    print("You must write at least one argument")

else:
    for elem in sys.argv:
        print(elem, type(elem))