
import copy as c


class CAL :
    def shift_cal(self,codes,shift_len) :

        #shift_len = 10
        
        prints1 = codes
        codes = list(codes)
        print("codes :",codes)



        print("CAL 클래스 shift_cal에 진입했습니다.")
        temp = codes[:shift_len]
        for i in range(shift_len,len(codes)) :
            codes[(i-shift_len)] = c.deepcopy(codes[i])
        print("for 문 직후 정제되지 않은 codes :",codes)
        print("temp :",temp)

        for i in range(len(temp)) :
            codes[i-shift_len] = c.deepcopy(temp[i])
        print("완전히 정제된 codes :",codes)
        prints2 = "".join(codes)


        print(prints1)
        print(" " * shift_len,end="")
        print("{}".format(prints2))
        return prints2
    
    def XOR(self,expanded_R,key) :
        print("CAL.XOR.expanded_R :",expanded_R)
        print("CAL.XOR.key :",key)
        print("len(expanded_R) :",len(expanded_R))
        print("len(key) :",len(key))

        expanded_R = list(expanded_R)
        key = list(key)
        res = []
        for i in range(len(expanded_R)) :
            if not expanded_R[i] == key[i] :
                #print("1")
                res.append("1")
            else :
                res.append("0")

        print("res : ",res)
        res = "".join(res)
        print("".join(expanded_R))
        print("".join(key))
        print(res)
        return res
    def STR2BIN(self,code) :
        #print("STR2BIN 진입함")
        #print("code :",code)
        code = list(code)
        t = 0
        for i in range(1,len(code)+1) :
            if code[-i] == "1" :
                t += 2**(i-1)
        #print("t :",t)
        #print("\n\n")
        return t
    def FILL_UP_ZERO(self,t,ins_len) :
        '''
        print("t :",t)
        print("lent :",ins_len)
        '''
        t = list(t)
        lent = len(t)
        for i in range(ins_len-lent) :
            t.insert(0,"0")

        t = "".join(t)
        #print("FILL_UP_ZERO.t :",t)
        return t

            








        



'''
main_ks = KS.KS()
key = main_ks.KS_m()
'''