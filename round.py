import copy as c
cryptogram = '1110100101111000101011010110011111000011111011100001100111001111'

l0 = cryptogram[:len(cryptogram)//2]
r0 = cryptogram[len(cryptogram)//2:]
print(cryptogram)
print("{}".format(l0))
'''
print(" "*(len(cryptogram)//2),end="")
print(r0)
'''
print("{}{}".format(" "*(len(cryptogram)//2),r0))
for i in range(32) :
    a = c.deepcopy(i)
    a = str(a)
    print(a[:1],end="")
print()
print("len(cryptogram) :",len(cryptogram))
print("len(l0) :",len(l0))
print("len(r0) :",len(r0))
