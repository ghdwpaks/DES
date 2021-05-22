import copy as c
import Functions as f
import IP
main_cry = "ghdwpakss" #cryptogram 크립토그램, DES를 관통하는 암호문
main_cry = f.STR2CRY(main_cry)
print("\n\n")


f.print_funcs.print_ops_of_var(main_cry,"main_cry")
ip1ed_cry = IP.IP1(main_cry)
print("main2")
f.print_funcs.print_ops_of_var(ip1ed_cry,"ip1ed_cry")


cry = c.deepcopy(ip1ed_cry)
L = f.get_cry_left(cry)
R = f.get_cry_right(cry)

