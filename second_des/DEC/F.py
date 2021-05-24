import Functions as f
import E

def F_main(cry,this_round) :
    #cry = "11000011111011100001100111001111"
    #f.print_funcs.print_var_with_1("round{} cry : {}".format(this_round,cry))
    cry = E.Expand_cry(cry)
    #f.print_funcs.print_var_with_1("round{} Ecry : {}".format(this_round,cry))
    PC_key = f.get_txt_file_contents("PC_keys/PC2_2{}.txt".format(this_round))

    key = f.CAL.XOR(cry,PC_key)
    #f.print_funcs.print_ops_of_var(key,"res")
    #f.print_funcs.print_var_with_1("key : {}".format(key))

    div_code = []
    for i in range(len(key)+1) :
        if i == 6 :
            div_code.append(key[0:6])
            fir1 = 0
        elif i == 48 :
            div_code.append(key[42:])
        elif i%6 == 0 and i != 0 :
            div_code.append(key[i-5:i+1])
    #f.print_funcs.print_ops_of_var(div_code,"div_code")
    #f.print_funcs.print_var_with_1("div_code : {}".format(div_code))


    sboxed_cry = []
    for i in range(0,len(div_code)) :
        a = div_code[i][:1] + div_code[i][-1:]
        a = f.CAL.STR2BIN(a)
        b = div_code[i][1:-1]
        b = f.CAL.STR2BIN(b)
        '''
        print("a :",a)
        print("b :",b)
        '''

        read_file_target = "F_keys/SBOX{}.txt".format(i+1)
        SBOX = f.get_txt_file_contents(read_file_target)
        SBOX = f.set_2_dim_arr(SBOX)

        '''
        print("\n\n\n")
        print("i :",i)
        f.print_funcs.print_list_nicly(SBOX)
        print("\n\n\n")
        '''
        res = f.FILL_UP_ZERO(str(bin(int(SBOX[a][b])))[2:],4)
        sboxed_cry.append(res)
    print("\n\n\n")
    print("F1"*10)
    sboxed_cry = "".join(sboxed_cry)
    print(sboxed_cry)
    print("F2"*10)

    P_key = f.get_txt_file_contents("F_keys/P.txt")
    P_key = f.set_2_dim_arr(P_key)
    res = f.apply_arr_to_key(P_key,sboxed_cry)
    #f.print_funcs.print_var_with_1("res : {}".format(res))
    return res



