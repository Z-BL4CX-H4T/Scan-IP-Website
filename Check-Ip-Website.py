# module
from os import system
from time import sleep

# program
def logo():
   print("""

 \33[5;32m__________ _____ _   _    __        _______ ____       ___ ____\33[5;32m  
\33[5;32m|__  / ____|_   _| | | |   \ \      / / ____| __ )     |_ _|  _ \ \33[5;32m
 \33[5;32m / /|  _|   | | | |_| |____\ \ /\ / /|  _| |  _ \ _____| || |_) |\33[5;32m
 \33[5;32m/ /_| |___  | | |  _  |_____\ V  V / | |___| |_) |_____| ||  __/ \33[5;32m 
\33[5;32m/____|_____| |_| |_| |_|      \_/\_/  |_____|____/     |___|_|\33[5;32m     \33[0;31mBy:Mr.ZETH|SAD|BOY\33[0;31m 
""")

   print("""\33[5;32m[+] Author: Mr.ZETH
[+] Team: Ntb Cyber Team
[+] Contact: 087782378275
\33[5;32m""")

logo()

def menu():
   print("""[1] install nslookup
[2] nslookup
[0] keluar
""")

   pil = input("   Masukkan pilihan anda : ")
   if pil =="1":
     sleep(1)
     system("apt install dnsutils")
     print("selesai")
   if pil =="2":
     sleep(1)
     system("nslookup")
     print("selesai")
     sleep(1)

menu()
