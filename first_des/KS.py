import copy as c
from io import open_code
from random import randrange
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
        f = open("PC_key/PC2_key.txt", 'r')
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

    def key_dvice_by_two_and_shift_in_ks_and_shift_in_ks(key,round_count) :
        shift_len = 0
        if round_count == 1 or 2 or 9 or 16 :
            shift_len = 1
        else :
            shift_len = 2
        c = key[:len(key)//2]
        d = key[len(key)//2:]
        print("1c :",c)
        print("1d :",d)
        print()
        ks_cal = CAL.CAL()
        c = ks_cal.shift_cal(c,shift_len)
        print("2c :",c)
        d = ks_cal.shift_cal(d,shift_len)
        print("2d :",d)
        res = []
        res.append(c)
        res.append(d)
        res = "".join(res)
        return res

    def main_pc1(round_count) :
        pc1 = KS.apply_ks_cry_by_pc1()
        pc1_code = KS.key_dvice_by_two_and_shift_in_ks_and_shift_in_ks(pc1,round_count)
        f = open("PC_key/PC2_key0.txt", 'w')
        f.write(pc1_code)
        f.close()
        

    def middle_section_pc2(count,round_count) :
        code = []
        get_file_target = "PC_key/PC2_key"+str(count)+".txt"
        f = open(get_file_target, 'r')
        line = f.readline()
        code.append(line)
        f.close()
        code = "".join(code)
        print("middle_section_pc2.code :",code)
        new_key = KS.key_dvice_by_two_and_shift_in_ks_and_shift_in_ks(code,round_count)
        write_file_target = "PC_key/PC2_key"+str(count+1)+".txt"
        f = open(write_file_target, 'w')
        f.write(new_key)
        f.close()

        code = []
        get_file_target = "PC_key/PC2_key"+str(count)+".txt"
        f = open(get_file_target, 'r')
        line = f.readline()
        code.append(line)
        f.close()

        count += 1

        pc2_key = KS.get_pc2s() #pc2를 가져온 객체, list 형식이다.
        res = []
        new_key = list(new_key)
        
        print("pc2 :",pc2_key)
        print("ney_key :",new_key)
        count_pc2 = 0
        for i in range(len(pc2_key)) :
            for j in range(len(pc2_key[i])) :
                count_pc2 += 1
        
        print("count_pc2 :",count_pc2)
        print("len(new_key) :",len(new_key))
        for i in range(len(pc2_key)) :
            for j in range(len(pc2_key[i])) :
                print("i :",i)
                print("j :",j)
                print("int(pc2_key[i][j]) :",int(pc2_key[i][j]))
                res.append(new_key[int(pc2_key[i][j])-1])
        res = "".join(res)
        print("KS.main_ks_pc2.res =",res)
        print("len(res) :",res)

        write_file_target = "PC_key/PC2_key2"+str(count+1)+".txt"
        f = open(write_file_target, 'w')
        f.write(res)
        f.close()





    def main_ks(self) :
        round_count = 1
        KS.main_pc1(round_count)
        for i in range(16) :
            round_count = i + 1
            KS.middle_section_pc2(i,round_count)
        
        
        
        




    def handover_key(self,key_number) :
        print("entered handover_key, key_number :",key_number)

        get_file_target = "PC_key/PC2_key2"+str(key_number)+".txt"

        KS_key = []

        f = open(get_file_target, 'r')
        line = f.readline()
        KS_key.append(line)
        f.close()
        KS_key = "".join(KS_key)
        return KS_key


#KS.main_ks()



            


        

    



