
'''
Key scheduling 키 스케쥴링 기능 파일
'''
class KS :
    def get_Key_scheduling_cryptogram() :
        Key_scheduling_cryptogram = ""
        f = open("PC_key.txt", 'r')
        Key_scheduling_cryptogram = f.readline()
        f.close()
        print(Key_scheduling_cryptogram)
        print("len(PCcryptogram) :",len(Key_scheduling_cryptogram))
        return Key_scheduling_cryptogram