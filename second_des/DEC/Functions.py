import copy as c
from typing import NoReturn

def get_txt_file_contents(file_target) :
    res = []

    f = open(file_target, 'r')
    while True :
        line = f.readline()
        if not line : break
        res.append(line)
    f.close()

    if len(res) == 1:
        print("이번 목표인 {}에는 문장이 하나밖에 없었습니다. str형태로 반환합니다.".format(file_target))
        res = "".join(res)

    print("res :",res)
    print("len(res) :",len(res))
    return res
def write_txt_file(file_target,contents) :
    f = open(file_target, 'w')
    if type(contents) == str :
        f.write(contents)
    else :
        print("전달받은 contents의 값이 str 형식이 아닙니다. 전달받은 contents는 정상적으로 쓰여지지 않았으며, 목표는\n",file_target,"이였고\n contents는\n",contents,"\n였습니다.")
    f.close()

def set_2_dim_arr(arr) :
    print("arr :",arr)
    for i in range(len(arr)) :
        if arr[i][-1:] == "\n" :
            arr[i] = arr[i][:-1]
    print()
    print("arr :",arr)

    res = []
    for i in range(len(arr)) :
        res.append(arr[i].split(","))
    print("res :",res)

    '''이 밑의 코드는 res변수의 실질적인 전체 길이를 알기 위한 간단코드
    count = 0
    for i in range(len(res)) :
        for j in range(len(res[i])) :
            count += 1
    print("count :",count)
    '''
    return res

def apply_arr_to_key(arr,cry) :
    res = []
    print("apply_arr_to_key에 진입하였습니다.")
    print("arr :",arr)
    print("cry :",cry)
    print("len(cry) :",len(cry))
    #print("key[{}] : {}".format(3,cry[3]))
    
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            res.append(cry[int(arr[i][j])-1])

    '''암호화의 의미와는 맞지 않아 폐기한 코드.
    for i in range(len(cry)) :
        for j in range(len(arr)) :
            for k in range(len(arr[j])) :
                if arr[j][k] == str(i) :
                    res.append(str(cry[i]))
    '''
    res = "".join(res)
    print("apply_arr_to_key에서의 연산이 끝났습니다. 결과는 다음과 같습니다.")
    print_funcs.print_list_nicly(res)
    print("\n")
    print("len(res) :",len(res))
    
    #print(res)
    return res

def DEC_apply_arr_to_cry(arr1,cry) :
    
    print("DEC_apply_arr_to_cry에 진입하였습니다.")
    print("arr1 :")
    print_funcs.print_list_nicly(arr1)
    print()
    print("cry :",cry)
    arr2 = []
    arr3 = [""]
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            arr2.append(arr1[i][j])
            arr3.append("")
    print("arr2 :",arr2)
    for i in range(len(cry)) :
        arr3[int(arr2[i])] = cry[i]
    print("arr3 :",arr3)

    '''
    res = set_arr_DEC(len(arr),len(arr[0]))
    print("res :",res)
    #print(res[4][6])
    for i in range(len(cry)) :
        x1 = i//cut
        y1 = i%cut
        #print("{} : [{}][{}]".format(arr[x1][y1],x1,y1))
        target = int(arr[x1][y1])-1
        print("{} , {}".format((x1*8)+y1,target))
        y2 = target//cut
        x2 = target%cut
        print("\t\t{} : [{}][{}] , {}".format(i,y2,x2,target))
        res[y2][x2] = cry[i]
    print(res)
    res = DEC_2DIMARR_to_STR(res)
    return res
    '''
    return "".join(arr3)


def DEC_2DIMARR_to_STR(arr) :
    res = []
    for i in range(len(arr)) :
        temp = "".join(arr[i])
        res.append(temp)
    return "".join(res)





def set_arr_DEC(x,y) :
    res = []
    for i in range(x) :
        temp = []
        for j in range(y) :
            temp.append("")
        res.append(temp)
    return res

def get_cry_left(cry) :
    L = cry[:len(cry)//2]
    return L

def get_cry_right(cry) :
    R = cry[len(cry)//2:]
    return R

def fill_up_zero_to_end(cry,wants_len) :
    print("fill_up_zero_to_end에 진입하였습니다.")
    #print_funcs.print_ops_of_var(cry,"cry")
    cry = list(cry)
    #print_funcs.print_ops_of_var(cry,"cry")
    if len(cry) < wants_len :
        fill_up_len = wants_len - len(cry)
        for i in range(fill_up_len) :
            cry.insert(len(cry),"0")
    #print_funcs.print_ops_of_var(cry,"cry")
    cry = "".join(cry)
    print("fill_up_zero_to_end 함수가 종료되었습니다. 0을 채워넣은 목표는",cry,"이며, 현재 길이는",len(cry),"입니다.")
    return cry

def STR2CRY(cry) :
    bined_cry = [] #2진법으로 변환된 암호문
    for i in range(len(cry)) :
        bined_cry.append(str(bin(ord(cry[i])))[2:])
    bined_cry = "".join(bined_cry)
    bined_cry = fill_up_zero_to_end(bined_cry,64)
    return bined_cry

def CRY2STR(cry,div_len) :
    print("\n\n\n")
    print(cry)
    cry = list(cry)
    temp1 = [cry[i * div_len:(i + 1) * div_len] for i in range((len(cry) + div_len - 1) // div_len )] 
    #print(temp1)
    temp2 = []
    for i in range(len(temp1)) :
        temp2.append("".join(temp1[i]))
    #print("temp2 :",temp2)
    print("".join(temp2))
    print("\n\n\n")
    temp3 = []
    for i in range(len(temp2)) :
        temp3.append(CAL.STR2BIN(temp2[i]))
    print("temp3 :",temp3)


def FILL_UP_ZERO(s,limit_len) :
    s = list(s)
    lens = len(s)
    for i in range(limit_len-lens) :
        s.insert(0,"0")
    return "".join(s)

class print_funcs :
    def print_list_nicly(arr) :
        arr = str(arr)
        for i in range(len(arr)) :
            if arr[i-1] == "]" and arr[i] == "," :
                print()
            print(arr[i],end="")
        print()

    def print_str_div(div_num,prints) :
        #div num 은 몇번 출력 당 줄을 넘을건지 미리 알려주는 변수.
        for i in range(len(prints)) :
            if i % div_num == 0 :
                print()
            print(prints[i],end="")
    
    def print_ops_of_var(var,var_name):
        print("{} : {}".format(var_name,var))
        t_var = type(var)
        print("{} : {}".format("type({})".format(var_name),type(var)))
        if t_var == str or t_var == list :
            print("{} : {}".format("len({})".format(var_name),len(var)))
    def print_2_dim_arr_counts(arr,arr_name) :
        c = 0
        for i in range(len(arr)) :
            for j in range(len(arr[i])) :
                c += 1
        print("{}의 실질적인 갯수 : {}".format(arr_name,c))
    def print_var_with_number(var,number=1) :
        print(str(number)*300)
        print("\n\n\n\n",var,"\n\n\n\n")
        print(str(number)*300)
class CAL :
    def shift_cal_on_str(code_str,shift_len) :
        code_str = list(code_str)
        temp = code_str[:shift_len]
        for i in range(shift_len,len(code_str)) :
            code_str[(i-shift_len)] = c.deepcopy(code_str[i])
        for i in range(len(temp)) :
            code_str[i-shift_len] = c.deepcopy(temp[i])
        code_str = "".join(code_str)
        return code_str
    
    def XOR(cry,key) :
        cry = list(cry)
        key = list(key)
        res = []
        for i in range(len(cry)) :
            if not cry[i] == key[i] :
                res.append("1")
            else :
                res.append("0")
        res = "".join(res)
        return res
    
    def STR2BIN(code) :
        code = list(code)
        t = 0
        for i in range(1,len(code)+1) :
            if code[-i] == "1" :
                t += 2**(i-1)
        return t
    def Rebuild_XOR(res_cry,fed_cry) :
        res = []
        for i in range(len(res_cry)) :
            if res_cry[i] == '0' and fed_cry[i] == '0' :
                res.append("0")
            elif res_cry[i] == '1' and fed_cry[i] == "1" :
                res.append('0')
            elif res_cry[i] == '0' and fed_cry[i] == "1" :
                res.append('1')
            elif res_cry[i] == '1' and fed_cry[i] == "0" :
                res.append('1')
        return "".join(res)
