import Functions as fc
import F
import Key_Scheduling as ks
import copy as c
ks.ks_main()
IP_1_key = fc.get_txt_file_contents("Keys/IP-1.txt")
IP_1_key = fc.set_2_dim_arr(IP_1_key)

inputs = fc.get_txt_file_contents("input.txt")
#fc.print_funcs.print_var_with_number("inputs :"+inputs)
#fc.print_funcs.print_var_with_number("inputs : {}".format(inputs),6)

IP_1ed_inputs = fc.DEC_apply_arr_to_cry(IP_1_key,inputs)

fc.print_funcs.print_var_with_number("IP_1ed_inputs : {}".format(IP_1ed_inputs),5)
fc.write_txt_file("Log_rerounds/R{}.txt".format(16),IP_1ed_inputs)


cry = c.deepcopy(IP_1ed_inputs)
R16 = fc.get_cry_left(cry)
L16_R15 = fc.get_cry_right(cry)
Fed_L16_R15 = F.F_main(L16_R15,16)
L15 = fc.CAL.Rebuild_XOR(R16,Fed_L16_R15)
result = ''.join([L15,L16_R15])
print("result :",result)
fc.write_txt_file("Log_rerounds/R{}.txt".format(15),result)



for i in range(14,-1,-1) :

    cry = fc.get_txt_file_contents("Log_rerounds/R{}.txt".format(i+1))
    R1L2 = fc.get_cry_left(cry)
    R2 = fc.get_cry_right(cry)
    Fed_R1L2 = F.F_main(R1L2,i+1)
    L1 = fc.CAL.Rebuild_XOR(R2,Fed_R1L2)
    result = ''.join([L1,R1L2])
    fc.write_txt_file("Log_rerounds/R{}.txt".format(i),result)

IP1_key = fc.get_txt_file_contents("Keys/IP.txt")
IP1_key = fc.set_2_dim_arr(IP1_key)

r0 = fc.get_txt_file_contents("Log_rerounds/R0.txt")
IP1ed_result = fc.DEC_apply_arr_to_cry(IP1_key,r0)
print("IP1ed_result :",IP1ed_result)
fc.CRY2STR(IP1ed_result,8)
#ENC : 1100111110100011001001110111111000011000011101011111001111100110
#DEC : 1100111110100011001001110111111000011000011101011111001111100110
