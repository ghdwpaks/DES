sbox1 = []
sbox2 = []
sbox3 = []
sbox4 = []
sbox5 = []
sbox6 = []
sbox7 = []
sbox8 = []
def setting_sbox(target) :
    temp1 = []
    temp2 = []
    f = open("SBOXES/SBOX"+str(target)+".txt", 'r')
    while True:
        line = f.readline()
        if not line: break
        temp1.append(line)
    f.close()
    for i in range(len(temp1)) :
        if temp1[i][-1:] == "\n" :
            temp1[i] = temp1[i][:-1]
    temp2 = []
    for i in range(len(temp1)) :
        temp2.append(temp1[i].split(","))
    return temp2

def show_list(a) :
    a = str(a)
    for i in range(len(a)) :
        print(a[i],end='')
        if a[i] == "," and a[i-1] == "]":
            print("")

sbox1 = setting_sbox(1)
sbox2 = setting_sbox(2)
sbox3 = setting_sbox(3)
sbox4 = setting_sbox(4)
sbox5 = setting_sbox(5)
sbox6 = setting_sbox(6)
sbox7 = setting_sbox(7)
sbox8 = setting_sbox(8)
'''
print(1)
show_list(sbox1)
print()
print(2)
show_list(sbox2)
print()
print(3)
show_list(sbox3)
print()
print(4)
show_list(sbox4)
print()
print(5)
show_list(sbox5)
print()
print(6)
show_list(sbox6)
print()
print(7)
show_list(sbox7)
print()
print(8)
show_list(sbox8)
print()
'''
code = "110110100101100011011100101101000010110111110100"
div_code = []
fir1 = 1
for i in range(len(code)+1) :
    #print(i)
    
    if i%6 == 0 and i != 0 :
        if fir1 == 1 :
            print(i)
            print("code[{}:{}] : {}".format(i-6,i,code[i-6:i]))
            print()
            div_code.append(code[i-6:i+1])
            fir1 = 0
        else :
            print(i)
            print("code[{}:{}] : {}".format(i-5,i+1,code[i-5:i+1]))
            print()
            div_code.append(code[i-5:i+1])
print("div_code :",div_code)
print(code)
for i in range(len(div_code)) :
    print(div_code[i],end="")

