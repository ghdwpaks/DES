import copy as c
import Functions as fc
import IP
import F
main_cry = "ghdwpakss" #cryptogram 크립토그램, DES를 관통하는 암호문
main_cry = fc.STR2CRY(main_cry)
print("\n\n")


fc.print_funcs.print_ops_of_var(main_cry,"main_cry")
ip1ed_cry = IP.IP1(main_cry)
print("main2")
fc.print_funcs.print_ops_of_var(ip1ed_cry,"ip1ed_cry")


cry = c.deepcopy(ip1ed_cry)
L = fc.get_cry_left(cry)
R = fc.get_cry_right(cry)

this_round = 1
Fed_R = F.F_main(cry,this_round)
XORED_L_with_Fed_R = fc.CAL.XOR(L,Fed_R)

print("\n\n\n")
print("XORED_L_with_Fed_R :",XORED_L_with_Fed_R)
print("len(XORED_L_with_Fed_R) :",len(XORED_L_with_Fed_R))
print("\n\n\n")

res = "".join([R,XORED_L_with_Fed_R])
target_write_log = "Log_rounds/R{}.txt".format(this_round)
fc.write_txt_file(target_write_log,res)