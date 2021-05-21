import Functions as f

'''
PC1 START
'''
file_target = "Keys/First_key.txt"
pc1_cry = f.get_txt_file_contents(file_target)

file_target = "PC_keys/PC1.txt"
pc1_key = f.get_txt_file_contents(file_target)
pc1_key = f.set_2_dim_arr(pc1_key)
print("\n\n\n\n")
f.print_funcs.print_list_nicly(pc1_key)
print(pc1_cry)
print("\n\n\n\n")

count = 0
for i in range(len(pc1_cry)) :
    if pc1_cry[i] == "1" :
        count += 1
print("count :",count)
print("len(pc1_cry) :",len(pc1_cry))

print("\n\n\n\n")
applied_pc1 = f.apply_arr_to_key(pc1_key,pc1_cry)
C = f.get_cry_left(applied_pc1)
D = f.get_cry_right(applied_pc1)
temp1 = [C,D]
cry_ready_pc2 = "".join(temp1)
print("\n\n\n\n")
print("Key_Scheduling의 PC1이 끝났습니다. 최종 반환물은 PC2_0.txt에 저장되었으며, 다음과 같습니다.")
f.write_txt_file("PC_keys/PC2_0.txt",cry_ready_pc2)
print(f.get_txt_file_contents("PC_keys/PC2_0.txt"))
print("\n\n\n\n")
'''
PC1 END
'''

'''
PC2 START WIFT 16 ROUNDS
'''


for i in range(1,17) :
    read_file_target = "PC_keys/PC2_{}.txt".format(str(i-1))
    pc2_cry = f.get_txt_file_contents(read_file_target)
    C = f.get_cry_left(pc2_cry)
    D = f.get_cry_right(pc2_cry)
    shift_len = 0
    if (i == 1 or  i == 2 or  i == 9 or  i == 16 ) and (i != 0):
        shift_len = 1
    else :
        shift_len = 2
    C = f.CAL.shift_cal_on_str(C,shift_len)
    D = f.CAL.shift_cal_on_str(D,shift_len)
    temp2 = [C,D]
    res = "".join(temp2)
    write_file_target = "PC_keys/PC2_{}.txt".format(str(i))
    f.write_txt_file(write_file_target,res)

'''
PC2 FINISHED
'''

