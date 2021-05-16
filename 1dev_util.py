from random import *

cr = []
for i in range(64) :
    i = randint(0,1)
    cr.append(i)
print()
print("len(cr) :",len(cr))
for i in range(len(cr)) :
    print(cr[i],end="")