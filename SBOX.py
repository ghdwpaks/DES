import CAL
main_cal = CAL.CAL()

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
'''
sbox1 = setting_sbox(1)
sbox2 = setting_sbox(2)
sbox3 = setting_sbox(3)
sbox4 = setting_sbox(4)
sbox5 = setting_sbox(5)
sbox6 = setting_sbox(6)
sbox7 = setting_sbox(7)
sbox8 = setting_sbox(8)

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

for i in range(len(code)+1) :
    if i == 6 :
        div_code.append(code[0:6])
        fir1 = 0
    elif i == 48 :
        div_code.append(code[42:])
    elif i%6 == 0 and i != 0 :
        div_code.append(code[i-5:i+1])
print("div_code :",div_code)
print(code)
for i in range(len(div_code)) :
    print(div_code[i],end="")
print("\n\n")

results = []
for i in range(len(div_code)) :
    #print(div_code[i])
    a = div_code[i][:1] + div_code[i][-1:]
    a = main_cal.STR2BIN(a)
    b = div_code[i][1:-1]
    b = main_cal.STR2BIN(b)
    #print("a :",a," , ","b :",b)
    sbox = setting_sbox(i+1)
    '''
    print("sbox :")
    show_list(sbox)
    print()

    print("sbox[a][b] :",sbox[a][b])
    print("int(sbox[a][b]) :",int(sbox[a][b]))
    print("bin(int(sbox[a][b])) :",bin(int(sbox[a][b])))
    print("str(bin(int(sbox[a][b])))[2:] :",str(bin(int(sbox[a][b])))[2:])
    '''
    res = main_cal.FILL_UP_ZERO(str(bin(int(sbox[a][b])))[2:],4)

    #print("res :",res)
    results.append(res)
results = "".join(results)
print("results :",results)
print("len(results) :",len(results))
    



