class P :
    def P_main(self,key) :
        t1 = []
        f = open("P.txt", 'r')
        while True:
            line = f.readline()
            if not line: break
            t1.append(line)
        f.close()
        print("t1 :",t1)
        for i in range(len(t1)) :
            if t1[i][-1:] == "\n" :
                t1[i] = t1[i][:-1]
        print()
        print("t1 :",t1)
        t2 = []
        for i in range(len(t1)) :
            t2.append(t1[i].split(","))
        print("t2 :",t2)
        count = 0
        for i in range(len(t2)) :
            for j in range(len(t2[i])) :
                count += 1
        print("count :",count)

        
        pc1 = t2
        print("key :",key)
        print("pc1 :",pc1)
        Refined_key = []
        for i in range(len(pc1)) :
            for j in range(len(pc1[i])) :
                Refined_key.append(key[int(pc1[i][j])-1])
        print(Refined_key)
        res = "".join(Refined_key)
        print("res :",res)
        print("len(res) :",len(res))
        return res