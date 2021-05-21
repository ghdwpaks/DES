


code = "110110100101100011011100101101000010110111110100"
string1 = []
for i in range(48) :
    string1.append(str(i%10))
string1 = "".join(string1)
print(string1)
print("string1[0:5] :",string1[0:5])
print(code)
print("code[0:5] :",code[0:5])
for i in range(len(code)) :
    print(i%10,end="")
print()