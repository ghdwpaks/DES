

import IP
import KS
import E
import CAL
import SBOX
import P
main_ks = KS.KS()
main_ks.main_ks() #PC_key 하위 폴더에 있는 키들 세팅함.

string1 = "ghdwpakss"
main_ip = IP.IP()
cryptogram = main_ip.IP_main(string1) #크립토그램, IP단계 암호문

def device_two_for_cry(cryptogram) :
    L = cryptogram[:(len(cryptogram)//2)]
    R = cryptogram[(len(cryptogram)//2):]
    res = []
    res.append(L)
    res.append(R)
    return res

def round_main(cryptogram,round_count) :

    print("cryptogram :",cryptogram)

    cry_list = device_two_for_cry(cryptogram)
    L = cry_list[(len(cry_list)-len(cry_list))]
    R = cry_list[(len(cry_list)-1)]

    #여기서 분할하고 함수로 넘기기
    main_e = E.E()
    expanded_R = main_e.E_main(R)

    this_round = round_count
    KS_key = main_ks.handover_key(this_round)

    main_cal = CAL.CAL()
    xor_expanded_R = main_cal.XOR(expanded_R,KS_key)
    print("xor_expanded_R :",xor_expanded_R)

    main_sbox = SBOX.SBOX()
    xbox_R = main_sbox.main_sbox(xor_expanded_R)
    print(xbox_R)

    main_p = P.P()
    Fed_R = main_p.P_main(xbox_R)
    print("Fed_R :",Fed_R)
    L = main_cal.XOR(Fed_R,L)
    print(L)
    result_main = []
    result_main.append(R)
    result_main.append(L)
    result_main = "".join(result_main)
    return result_main
RESULT = ""
for i in range(1,17) :
    RESULT = round_main(cryptogram,i)
print("RESULT :",RESULT)



 