from time import sleep
from random import random

myfile = open(__file__)
mytext = myfile.read()

while True:
	child = open(str(random())+'.py', 'w')
	child.write(mytext)
	child.close()
	sleep(random()*10)
