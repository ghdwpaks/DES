import Functions as fc
IP_1_key = fc.get_txt_file_contents("Keys/IP-1.txt")
IP_1_key = fc.set_2_dim_arr(IP_1_key)

inputs = fc.get_txt_file_contents("input.txt")
IP_1ed_inputs = fc.DEC_apply_arr_to_cry(IP_1_key,inputs)

R16 = fc.get_cry_left(IP_1ed_inputs)
L16 = fc.get_cry_right(IP_1ed_inputs)


