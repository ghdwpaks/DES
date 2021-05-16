
'''
Key scheduling 키 스케쥴링 기능 파일
'''
class KS :
    def get_Key_scheduling_cryptogram() :
        Key_scheduling_cryptogram = ""
        f = open("PC_key.txt", 'r')
        Key_scheduling_cryptogram = f.readline()
        f.close()
        print(Key_scheduling_cryptogram)
        print("len(PCcryptogram) :",len(Key_scheduling_cryptogram))
        return Key_scheduling_cryptogram

    def get_pc1() :
        pc1_temp1 = []
        f = open("PC1.txt", 'r')
        while True:
            line = f.readline()
            if not line: break
            pc1_temp1.append(line)
        f.close()
        print("pc1_temp1 :",pc1_temp1)
        for i in range(len(pc1_temp1)) :
            if pc1_temp1[i][-1:] == "\n" :
                pc1_temp1[i] = pc1_temp1[i][:-1]
        print()
        print("pc1_temp1 :",pc1_temp1)
        pc1_temp2 = []
        for i in range(len(pc1_temp1)) :
            pc1_temp2.append(pc1_temp1[i].split(","))
        print("pc1_temp2 :",pc1_temp2)
        count = 0
        for i in range(len(pc1_temp2)) :
            for j in range(len(pc1_temp2[i])) :
                count += 1
        print("count :",count)
        return pc1_temp2
    
    def apply_ks_cry_by_pc1() :
        key = KS.get_Key_scheduling_cryptogram()
        pc1 = KS.get_pc1()
        print("key :",key)
        print("pc1 :",pc1)
        Refined_key = []
        for i in range(len(pc1)) :
            for j in range(len(pc1[i])) :
                Refined_key.append(key[int(pc1[i][j])])
        print(Refined_key)
        res = "".join(Refined_key)
        print("res :",res)
        print("len(res) :",len(res))
        return res
    
KS.get_pc1()
KS.apply_ks_cry_by_pc1()
