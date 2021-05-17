import copy as c
from io import open_code
import CAL

'''
Key scheduling 키 스케쥴링 기능 파일
'''
class KS :
    def get_Key_scheduling_cryptogram() :
        Key_scheduling_cryptogram = ""
        f = open("PC_key/PC1_key.txt", 'r')
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

    def get_pc2s() :
        pc1_temp1 = []
        f = open("PC2.txt", 'r')
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

    def key_dvice_by_two_and_shift_in_ks_and_shift_in_ks(key) :

        c = key[:len(key)//2]
        d = key[len(key)//2:]
        print("1c :",c)
        print("1d :",d)
        print()
        ks_cal = CAL.CAL()
        c = ks_cal.shift_cal(c,10)
        print("2c :",c)
        d = ks_cal.shift_cal(d,10)
        print("2d :",d)
        res = []
        res.append(c)
        res.append(d)
        res = "".join(res)
        return res

    def main_pc1() :
        pc1 = KS.apply_ks_cry_by_pc1()
        pc1_code = KS.key_dvice_by_two_and_shift_in_ks_and_shift_in_ks(pc1)
        f = open("PC_key/PC2_key0.txt", 'w')
        f.write(pc1_code)
        f.close()

    def middle_section_pc2(count) :
        code = []
        get_file_target = "PC_key/PC2_key"+str(count)+".txt"
        f = open(get_file_target, 'r')
        line = f.readline()
        code.append(line)
        f.close()
        code = "".join(code)
        print("middle_section_pc2.code :",code)
        new_key = KS.key_dvice_by_two_and_shift_in_ks_and_shift_in_ks(code)
        write_file_target = "PC_key/PC2_key"+str(count+1)+".txt"
        f = open(write_file_target, 'w')
        f.write(new_key)
        f.close()


    def main_ks() :
        KS.main_pc1()
        for i in range(16) :
            KS.middle_section_pc2(i)
KS.main_ks()
#KS.middle_section_pc2()


            


        

    



