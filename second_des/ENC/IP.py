import Functions as f

def IP1(none_ip_cry) :

    IP1 = f.get_txt_file_contents("Keys/IP.txt")
    IP1 = f.set_2_dim_arr(IP1)
    print("\n\n")
    f.print_funcs.print_list_nicly(IP1)
    ip1ed_cry = f.apply_arr_to_key(IP1,none_ip_cry)
    f.print_funcs.print_ops_of_var(ip1ed_cry,"ip1ed_cry")
    return ip1ed_cry

def IP_1(none_ip_cry) :
    IP_1 = f.get_txt_file_contents("Keys/IP-1.txt")
    IP_1 = f.set_2_dim_arr(IP_1)
    ip_1ed_cry = f.apply_arr_to_key(IP_1,none_ip_cry)
    return ip_1ed_cry

