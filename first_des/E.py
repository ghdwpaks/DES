class E:
    def E(codes) :
        print("E 진입함.")
        print("리스트 변환 전 codes :",codes)
        codes = list(codes)
        print("리스트 변환 후 codes :",codes)
        temp1 = []
        f = open("E.txt", 'r')
        while True:
            line = f.readline()
            if not line: break
            temp1.append(line)
        f.close()
        for i in range(len(temp1)) :
            if temp1[i][-1:] == "\n" :
                temp1[i] = temp1[i][:-1]

        E_codes = []
        for i in range(len(temp1)) :
            E_codes.append(temp1[i].split(","))
        print("E_codes :",E_codes)

        res = []
        for i in range(len(E_codes)) :
            for j in range(len(E_codes[i])) :
                print("i :",i)
                print("j :",j)
                print("E_codes[i][j] :",E_codes[i][j])
                res.append(codes[int(E_codes[i][j])-1])
        print("1res :",res)
        res = "".join(res)
        print("2res :",res)
        print("len(res)) :",len(res))
        return res
    

    def E_main(self,code) :
        
        res = E.E(code)
        return res