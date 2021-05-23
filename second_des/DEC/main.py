import Functions as fc
import F
IP_1_key = fc.get_txt_file_contents("Keys/IP-1.txt")
IP_1_key = fc.set_2_dim_arr(IP_1_key)

inputs = fc.get_txt_file_contents("input.txt")
fc.print_funcs.print_var_with_1("inputs :"+inputs)
IP_1ed_inputs = fc.DEC_apply_arr_to_cry(IP_1_key,inputs)
fc.print_funcs.print_var_with_1(IP_1ed_inputs)



R16 = fc.get_cry_left(IP_1ed_inputs)
#fc.print_funcs.print_var_with_1(R16)
L16_R15 = fc.get_cry_right(IP_1ed_inputs)
#fc.print_funcs.print_var_with_1("L16_R15 : {}".format(L16_R15))
#ENC : 
#DEC : 

#ENC : 111101010010101111110001010101011010101100001111
#DEC : 111000000111111101011100000011110011111001011111
Fed_L16_R15 = F.F_main(L16_R15,16)
#fc.print_funcs.print_var_with_1(Fed_L16_R15)
L15 = fc.CAL.XOR(R16,Fed_L16_R15)
print(L15)

result = ''.join([L15,R16])
print("result :",result)
