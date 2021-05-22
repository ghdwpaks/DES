import Functions as f
import E
this_round = 1
cry = "11000011111011100001100111001111"
cry = E.Expand_cry(cry)

PC_key = f.get_txt_file_contents("PC_keys/PC2_2{}.txt".format(this_round))

res = f.CAL.XOR(cry,PC_key)
f.print_funcs.print_ops_of_var(res,"res")


