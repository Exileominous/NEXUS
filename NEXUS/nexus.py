import os
import sys
import time
import subprocess
from module.l7 import *
from module.l4 import *
from module.l3 import *

nexus = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nexus}
          
███╗░░██╗███████╗██╗░░██╗██╗░░░██╗░██████╗
████╗░██║██╔════╝╚██╗██╔╝██║░░░██║██╔════╝
██╔██╗██║█████╗░░░╚███╔╝░██║░░░██║╚█████╗░
██║╚████║██╔══╝░░░██╔██╗░██║░░░██║░╚═══██╗
██║░╚███║███████╗██╔╝╚██╗╚██████╔╝██████╔╝
╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░       
{clear}""")
    
    print(f"[{nexus}NEXUS{clear}] {white}Welcome NEXUS DDoS Attack Tools{clear}")
    print(f"[{nexus}NEXUS{clear}] {white}Join DoxGroup !! https://rvlt.gg/PnjMbQwH{clear}")
    os.system("pip install aiohttp --break-system-packages")
    input(f"[{nexus}NEXUS{clear}] {white}Enter the continue...{clear}")
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nexus}

███╗░░██╗███████╗██╗░░██╗██╗░░░██╗░██████╗
████╗░██║██╔════╝╚██╗██╔╝██║░░░██║██╔════╝
██╔██╗██║█████╗░░░╚███╔╝░██║░░░██║╚█████╗░
██║╚████║██╔══╝░░░██╔██╗░██║░░░██║░╚═══██╗
██║░╚███║███████╗██╔╝╚██╗╚██████╔╝██████╔╝
╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░ {clear}
          
╔═════════════════════════════════════════════════════╗
║ {nexus}*{clear} Github    {nexus}:{clear}   https://github.com/Exileominous     ║
║ {nexus}*{clear} version   {nexus}:{clear}   https://app.revolt.chat/channe/NEXUS║
║ {nexus}*{clear} Created   {nexus}:{clear}   IE.INTERNET EXPLORE                 ║
╚═════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════╗
║ {nexus}[{clear}1{nexus}]{clear} Update NEXUS                                    ║
║ {nexus}[{clear}2{nexus}]{clear} Layer3 Attack Methods                           ║     
║ {nexus}[{clear}3{nexus}]{clear} Layer4 Attack Methods                           ║               
║ {nexus}[{clear}4{nexus}]{clear} Layer7 Attack Methods                           ║
║ {nexus}[{clear}5{nexus}]{clear} nmap                                            ║                                    
║ {nexus}[{clear}6{nexus}]{clear} Exit NEXUS                                      ║          
╚═════════════════════════════════════════════════════╝                              
""")


def main():
    while True:
        logo()
        select = input(f"""
╔═══[{nexus}root{clear}@{nexus}NEXUS{clear}]
╚══{nexus}>{clear} """)
                                        
        if select == "1" or select.lower() == "u":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{nexus}
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                  {clear}""")
            subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
            print(f"[{nexus}NEXUS{clear}] Update Success!")
            input(f"[{nexus}NEXUS{clear}] Enter the continue...")

        elif select == "6" or select.lower() == "e":
            sys.exit()

        elif select == "5" or select.lower() == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{zoic}
███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
                {clear}""")
            
            target = input(f"[{nexus}NEXUS{clear}] IP       {zoic}>{clear} ")
            
            os.system(f"nmap {target}")
            input(f"[{zoic}NEXUS{clear}] Enter the continue...")

        elif select == "2" or select.lower() == "2":
            layer3()

        elif select == "3" or select.lower() == "3":
            layer4()

        elif select == "4" or select.lower() == "4":
            layer7()
            
    
             


if __name__ == "__main__":
    check_main()
    main()
