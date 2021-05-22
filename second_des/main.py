import Functions as f
first_cry = "ghdwpakss" #cryptogram 크립토그램, DES를 관통하는 암호문

bined_cry = [] #2진법으로 변환된 암호문
for i in range(len(first_cry)) :
    bined_cry.append(str(bin(ord(first_cry[i])))[2:])
bined_cry = "".join(bined_cry)
#f.print_funcs.print_ops_of_var(bined_cry,"bined_cry")
bined_cry = f.fill_up_zero_to_end(bined_cry,64)
print("\n\n")
print("main_1")
f.print_funcs.print_ops_of_var(bined_cry,"bined_cry")