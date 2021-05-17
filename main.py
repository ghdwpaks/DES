from KS import KS
import IP
import KS

main_ip = IP.IP()
cryptogram = main_ip.IP_main() #크립토그램, IP단계 암호문
print(cryptogram)

main_ks = KS.KS()
main_ks.main_ks() #PC_key 하위 폴더에 있는 키들 세팅함.
