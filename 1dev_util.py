from main import R
from random import *

temp1 = []
f = open("E.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    temp1.append(line)
f.close()
for i in range(len(temp1)) :
    if temp1[i][-1:] == "\n" :
        temp1[i] = temp1[i][:-1]

E_codes = []
for i in range(len(temp1)) :
    E_codes.append(temp1[i].split(","))
print("E_codes :",E_codes)

c = 0
for i in range(len(E_codes)) :
    for j in range(len(E_codes[i])) :
        c += 1
print("c :",c)   




count = 1
a = "PC2_key"+str(count)+".txt"
print("a :",a)

cr = []
for i in range(64) :
    i = randint(0,1)
    cr.append(i)
print()
print("len(cr) :",len(cr))
for i in range(len(cr)) :
    print(cr[i],end="")