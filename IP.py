import copy as c
import csv

class IP :
    def get_first_ans(ans) :
        ans1 = ans
        ans2 = []
        #print("ans1 길이 :",len(ans1))
        for i in range(len(ans1)) :
            ans2.append(str(bin(ord(ans1[i])))[2:])
        #print(ans2)
        ans3 = "".join(ans2)
        #print("ans3 :",ans3)
        #print("ans3 길이 :",len(ans3))
        ans4 = ans3 + '0'
        #print("ans4 :",ans4)
        #print("ans4 길이 :",len(ans4))
        return ans4

    def get_IP_arr() :
        l1 = []
        l2 = []
        l3 = []
        for i in range(8) :
            l3.append([])
        for i in range(8) :
            for j in range(8) :
                l3[i].append([])
        #print(l3)
        return l3

    def get_IP_data() :
        table = []
        temp = []
        data = ""
        f = open("IP.txt",'r')
        while True :
            line = f.readline()
            if not line : break
            data = c.deepcopy(data + line)
        #print(data)
        #print("\n\n")
        temp = data.split("\n")
        #print("temp :",temp)
        #print("\n\n")
        for i in range(len(temp)) :
            table.append(str(temp[i]).split(','))
        #print(table)
        for i in range(len(table)) :
            for j in range(len(table[i])) :
                table[i][j] = int(table[i][j])
        #print(table)
        return table

    def print_IP_data(print1) :
        print1 = str(print1)
        for i in range(len(print1)) :
            if print1[i-1] == "]" and print1[i] == "," :
                print()
            print(print1[i],end="")
        print()

    def IP_func(fir_code) :
        #fir_code = get_first_ans()
        #print("location 58 :",fir_code[58])
        res_IP = IP.get_IP_arr()
        #print("IP.IP_func.fir_code :",fir_code)
        IP_data = IP.get_IP_data()

        for i in range(len(IP_data)) :
            for j in range(len(IP_data[i])) :
                location = c.deepcopy(int(IP_data[i][j])-1)
                '''
                print("i :",i)
                print("j :",j)
                print("location :",location)
                '''
                temp_bin_code = c.deepcopy(fir_code[location])
                res_IP[i][j] = c.deepcopy(temp_bin_code)

        #print_IP_data(res_IP)
        res = ""
        for i in range(len(res_IP)) :
            temp_res = "".join(res_IP[i])
            res = res + temp_res
        return res

    def IP_main(self,string1) :
        print("IP main 진입 및 string1 :",string1)
        #print("원문 :",string1)
        code = IP.get_first_ans(string1)
        #print("2진수 ㅇ원문 :",code)
        res = IP.IP_func(code)
        #print("2진수 암호문 :",res)
        return res

