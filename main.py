

import IP
import KS
import E
import CAL

main_ks = KS.KS()
main_ks.main_ks() #PC_key 하위 폴더에 있는 키들 세팅함.

string1 = "ghdwpakss"
main_ip = IP.IP()
cryptogram = main_ip.IP_main(string1) #크립토그램, IP단계 암호문


print("cryptogram :",cryptogram)

def device_two_for_cry(cryptogram) :
    L = cryptogram[:(len(cryptogram)//2)]
    R = cryptogram[(len(cryptogram)//2):]
    res = []
    res.append(L)
    res.append(R)
    return res




cry_list = device_two_for_cry(cryptogram)
R = cry_list[(len(cry_list)-1)]
#여기서 분할하고 함수로 넘기기
main_e = E.E()
expanded_R = main_e.E_main(R)

this_round = 0
KS_key = main_ks.handover_key(this_round)



main_cal = CAL.CAL()
main_cal.XOR(expanded_R,KS_key)




