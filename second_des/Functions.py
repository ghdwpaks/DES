import copy as c

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

    #이 밑의 각주는 res변수의 실질적인 전체 길이를 알기 위한 간단코드
    '''
    count = 0
    for i in range(len(res)) :
        for j in range(len(res[i])) :
            count += 1
    print("count :",count)
    '''
    return res

def apply_arr_to_key(arr,cry) :
    res = []
    print("key[{}] : {}".format(3,cry[3]))
    
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

def get_cry_left(cry) :
    L = cry[:len(cry)//2]
    return L

def get_cry_right(cry) :
    R = cry[len(cry)//2:]
    return R

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
