import copy as c
import Functions as fc
import IP
import F
import Key_Scheduling as Key_s
Key_s.ks_main()
main_cry = "ghdwpakss" #cryptogram 크립토그램, DES를 관통하는 암호문
fir_of_fir_input = c.deepcopy(main_cry)
main_cry = fc.STR2CRY(main_cry)
print("\n\n")


#fc.print_funcs.print_ops_of_var(main_cry,"main_cry")
ip1ed_cry = IP.IP1(main_cry)
print("main2")
#fc.print_funcs.print_ops_of_var(ip1ed_cry,"ip1ed_cry")

fc.write_txt_file("Log_rounds/R0.txt",ip1ed_cry)


for i in range(1,17):
    cry = fc.get_txt_file_contents("Log_rounds/R{}.txt".format(i-1))
    cry = c.deepcopy(cry)
    #fc.print_funcs.print_var_with_number("cry : {}".format(cry),5)
    L = fc.get_cry_left(cry)
    R = fc.get_cry_right(cry)
    #fc.print_funcs.print_var_with_number("Log_rounds/R{}.txt".format(i-1),415)
    Fed_R = F.F_main(R,i)
    fc.write_txt_file("temps/cry{}.txt".format(i),cry)
    #fc.print_funcs.print_var_with_number("Fed_R : {}".format(Fed_R),2)
    #fc.print_funcs.print_var_with_number("L : {}".format(L),4)
    XORED_L_with_Fed_R = fc.CAL.XOR(L,Fed_R)
    #fc.print_funcs.print_var_with_number("XORED_L_with_Fed_R : {}".format(XORED_L_with_Fed_R),3)
    '''
    print("\n\n\n")
    print("XORED_L_with_Fed_R :",XORED_L_with_Fed_R)
    print("len(XORED_L_with_Fed_R) :",len(XORED_L_with_Fed_R))
    print("\n\n\n")
    fc.print_funcs.print_var_with_number("right : {}".format(Fed_R),10)
    '''
    '''
    if i != 16 :
        print("16"*3000)
        res = "".join([XORED_L_with_Fed_R,R])
        print("res :",res)
    else :
    '''
    res = ""
    print(str(i)*3000)
    
    res = "".join([R,XORED_L_with_Fed_R])
    print("res :",res)
    '''
    print(str(i)*300,"\n\n\n\n\n")
    print(res,"\n\n\n\n\n")
    print(str(i)*300)
    '''

    #fc.print_funcs.print_var_with_number("right : {}".format(res[len(res)//2:]),9)
    #fc.print_funcs.print_var_with_number("left : {}".format(res[:len(res)//2]),8)

    target_write_log = "Log_rounds/R{}.txt".format(i)
    #fc.print_funcs.print_var_with_number("Log_rounds/R{}.txt".format(i),416)
    #fc.print_funcs.print_var_with_number("res : {}".format(res),7.1)
    fc.write_txt_file(target_write_log,res)


RESULT = fc.get_txt_file_contents("Log_rounds/R16.txt")
#fc.print_funcs.print_var_with_number("RESULT : {}".format(RESULT),7)
RESULT = IP.IP_1(RESULT)
#fc.print_funcs.print_var_with_number("RESULT : {}".format(RESULT),6)
print("두번째 DES가 전부 끝났습니다.")
print("입력문은 \"{}\"이였으며".format(fir_of_fir_input))
print("결과물은 \"{}\"입니다.".format(RESULT))

fc.write_txt_file("result.txt",RESULT)