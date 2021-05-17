
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

'''
main_ks = KS.KS()
key = main_ks.KS_m()
'''