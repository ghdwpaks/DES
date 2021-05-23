import Functions as f

def Expand_cry(cry) :
    E_key = f.get_txt_file_contents("F_keys/E.txt")
    E_key = f.set_2_dim_arr(E_key)
    #f.print_funcs.print_2_dim_arr_counts(E_key,"E_key")
    res = f.apply_arr_to_key(E_key,cry)
    return res
