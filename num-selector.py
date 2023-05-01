import numpy as np
import random as rand

k=(input('how many times? : '))
print(k)

for j in range(k):
    number=[]
	for i in range(6):
   	    number.append(rand.randint(1,45))
        print(number)
