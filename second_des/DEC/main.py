import Functions as fc
import F
IP_1_key = fc.get_txt_file_contents("Keys/IP-1.txt")
IP_1_key = fc.set_2_dim_arr(IP_1_key)

inputs = fc.get_txt_file_contents("input.txt")
#fc.print_funcs.print_var_with_number("inputs :"+inputs)
#fc.print_funcs.print_var_with_number("inputs : {}".format(inputs),6)

IP_1ed_inputs = fc.DEC_apply_arr_to_cry(IP_1_key,inputs)

#fc.print_funcs.print_var_with_number("IP_1ed_inputs : {}".format(IP_1ed_inputs),5)

R16 = fc.get_cry_left(IP_1ed_inputs)
L16_R15 = fc.get_cry_right(IP_1ed_inputs)
Fed_L16_R15 = F.F_main(L16_R15,16)
fc.print_funcs.print_var_with_number("L16_R15 : {}".format(L16_R15),9)
fc.print_funcs.print_var_with_number("Fed_L16_R15 : {}".format(Fed_L16_R15),2)
fc.print_funcs.print_var_with_number("R16 : {}".format(R16),4)
L15 = fc.CAL.Rebuild_XOR(R16,Fed_L16_R15)
fc.print_funcs.print_var_with_number("L15 : {}".format(L15),3)

result = ''.join([L15,R16])
print("result :",result)
