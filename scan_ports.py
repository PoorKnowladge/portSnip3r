from main import main
import sys, random, re, threading
from time import sleep
from warna.color import Color
import os

print_lock = threading.Lock()
def clearX():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

clearX()

# def banner():
#     banner = f"""{Color.BOLD}{Color.OKGREEN}
# ██████╗  ██████╗ ██████╗ ████████╗███████╗███╗   ██╗██╗██████╗ ██████╗ ██████╗ 
# ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝████╗  ██║██║██╔══██╗╚════██╗██╔══██╗
# ██████╔╝██║   ██║██████╔╝   ██║   ███████╗██╔██╗ ██║██║██████╔╝ █████╔╝██████╔╝
# ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║╚██╗██║██║██╔═══╝  ╚═══██╗██╔══██╗
# ██║     ╚██████╔╝██║  ██║   ██║   ███████║██║ ╚████║██║██║     ██████╔╝██║  ██║
# ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝

#     {Color.BOLD}{Color.ENDC}"""
#     print(banner)

def banner():
    banner = f"""{Color.BOLD}{Color.FAIL}
{Color.FAIL}██████╗  ██████╗ ██████╗ ████████╗{Color.ENDC}{Color.ENDC}███████╗███╗   ██╗██╗██████╗ ██████╗ ██████╗{Color.ENDC}
{Color.FAIL}██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝{Color.ENDC}{Color.ENDC}██╔════╝████╗  ██║██║██╔══██╗╚════██╗██╔══██╗{Color.ENDC}
{Color.FAIL}██████╔╝██║   ██║██████╔╝   ██║   {Color.ENDC}{Color.ENDC}███████╗██╔██╗ ██║██║██████╔╝ █████╔╝██████╔╝{Color.ENDC}
{Color.ENDC}██╔═══╝ ██║   ██║██╔══██╗   ██║   {Color.ENDC}{Color.FAIL}╚════██║██║╚██╗██║██║██╔═══╝  ╚═══██╗██╔══██╗{Color.ENDC}
{Color.ENDC}██║     ╚██████╔╝██║  ██║   ██║   {Color.ENDC}{Color.FAIL}███████║██║ ╚████║██║██║     ██████╔╝██║  ██║{Color.ENDC}
{Color.ENDC}╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   {Color.ENDC}{Color.FAIL}╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝{Color.ENDC}

 Author:
_________

{Color.OKGREEN}-----------------------{Color.ENDC}+------------------------------------------------+
{Color.OKGREEN}| Email                {Color.ENDC}| Informasi                                      |
{Color.OKGREEN}+======================{Color.ENDC}+================================================+
{Color.OKGREEN}| gojoeath63@gmail.com {Color.ENDC}| Nama: grimEnigma                               |
{Color.OKGREEN}|                      {Color.ENDC}| Instagram: bitswif                             |
{Color.OKGREEN}|                      {Color.ENDC}| Channel WhatsApp: https://bit.ly/cyberShade    |
{Color.OKGREEN}+----------------------{Color.ENDC}+------------------------------------------------+
    {Color.BOLD}{Color.ENDC}"""
    print(banner)

def printX(text):
    for char in text:
        print(f"{Color.BOLD}{Color.WARNING}{char}{Color.BOLD}{Color.ENDC}", end='', flush=True)  # Mencetak karakter tanpa newline dan langsung ke output
        sleep(random.uniform(0.1, 0.3))

def is_valid_target(target):
    return bool(re.match(r'^[a-zA-Z0-9.]+$', target))

if __name__ == "__main__":
    try:
        while True:
            sleep(1.0)
            banner()
            print("")
            target = input(Color.HEADER + "[+] Input target : " + Color.ENDC).strip();print("")
            if not is_valid_target(target):
                print(f"{Color.FAIL}[-] Target tidak valid. Masukan target yang valid")
                break
            start_port = int(input(Color.HEADER + "[+] Input port awal : " + Color.ENDC));print("")
            end_port = int(input(Color.HEADER + "[+] Input port akhir : " + Color.ENDC));print("")
            interval = float(input(Color.HEADER + "[+] Tentukan berapa lama waktu yang akan Anda alokasikan untuk pemindaian : " + Color.ENDC))
            print("")
            host = main.ScanPortsVulnerable(target, ["Scan Port"], [])
            host.scan_open_ports(target, start_port, end_port, interval)
            host.report_vulnerabilities()
            printX(f"[!] Report / Laporan scan ada di direktori reports")
            print("")
            sleep(3.0)
            clearX()
    except KeyboardInterrupt:
        choise = input('\n' + Color.FAIL + '[!] Yakin Ingin Berhenti [Y/n]: ' + Color.ENDC)
        print("")
        if choise == 'y' or choise == 'Y':
            print(Color.FAIL + "[-] Program Di Hentikan ...!" + Color.ENDC)
            sys.exit()
        elif choise == 'n' or choise == 'N':
            print(Color.OKBLUE + "[!] Program Di Lanjutkan ...!" + Color.ENDC)
        else:
            print(Color.FAIL + "[-] Pilihan tidak valid!" + Color.ENDC)
            # system('clear')
            sys.exit()

