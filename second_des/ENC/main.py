import copy as c
import Functions as fc
import IP
import F
main_cry = "ghdwpakss" #cryptogram 크립토그램, DES를 관통하는 암호문
fir_of_fir_input = c.deepcopy(main_cry)
main_cry = fc.STR2CRY(main_cry)
print("\n\n")


fc.print_funcs.print_ops_of_var(main_cry,"main_cry")
ip1ed_cry = IP.IP1(main_cry)
print("main2")
fc.print_funcs.print_ops_of_var(ip1ed_cry,"ip1ed_cry")

fc.write_txt_file("Log_rounds/R0.txt",ip1ed_cry)


for i in range(1,17):
    fc.get_txt_file_contents("Log_rounds/R{}.txt".format(i-1))
    cry = c.deepcopy(ip1ed_cry)
    L = fc.get_cry_left(cry)
    R = fc.get_cry_right(cry)

    Fed_R = F.F_main(cry,i)
    XORED_L_with_Fed_R = fc.CAL.XOR(L,Fed_R)

    print("\n\n\n")
    print("XORED_L_with_Fed_R :",XORED_L_with_Fed_R)
    print("len(XORED_L_with_Fed_R) :",len(XORED_L_with_Fed_R))
    print("\n\n\n")

    res = "".join([R,XORED_L_with_Fed_R])
    target_write_log = "Log_rounds/R{}.txt".format(i)
    fc.write_txt_file(target_write_log,res)

RESULT = fc.get_txt_file_contents("Log_rounds/R16.txt")
RESULT = IP.IP_1(RESULT)

print("두번째 DES가 전부 끝났습니다.")
print("입력문은 \"{}\"이였으며".format(fir_of_fir_input))
print("결과물은 \"{}\"입니다.".format(RESULT))
