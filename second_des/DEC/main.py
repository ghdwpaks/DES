import Functions as fc
import F
import Key_Scheduling as ks
ks.ks_main()
IP_1_key = fc.get_txt_file_contents("Keys/IP-1.txt")
IP_1_key = fc.set_2_dim_arr(IP_1_key)

inputs = fc.get_txt_file_contents("input.txt")
#fc.print_funcs.print_var_with_number("inputs :"+inputs)
#fc.print_funcs.print_var_with_number("inputs : {}".format(inputs),6)

IP_1ed_inputs = fc.DEC_apply_arr_to_cry(IP_1_key,inputs)

fc.print_funcs.print_var_with_number("IP_1ed_inputs : {}".format(IP_1ed_inputs),5)
fc.write_txt_file("Log_rerounds/R{}.txt".format(16),IP_1ed_inputs)



R16 = fc.get_cry_left(IP_1ed_inputs)
fc.print_funcs.print_var_with_number("R16 : {}".format(R16),4)
L16_R15 = fc.get_cry_right(IP_1ed_inputs)
Fed_L16_R15 = F.F_main(L16_R15,16)
fc.print_funcs.print_var_with_number("Fed_L16_R15 : {}".format(Fed_L16_R15),6)
L15 = fc.CAL.Rebuild_XOR(R16,Fed_L16_R15)

result = ''.join([L15,L16_R15])
print("result :",result)
fc.write_txt_file("Log_rerounds/R{}.txt".format(15),result)

for i in range(14,0,-1) :

    cry = fc.get_txt_file_contents("Log_rerounds/R{}.txt".format(i+1))
    R1L2 = fc.get_cry_left(cry)
    R2 = fc.get_cry_right(cry)
    Fed_R1L2 = F.F_main(R1L2,i+1)
    L1 = fc.CAL.Rebuild_XOR(R2,Fed_R1L2)
    result = ''.join([L1,R1L2])
    fc.write_txt_file("Log_rerounds/R{}.txt".format(i),result)

