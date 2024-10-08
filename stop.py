import requests
import json
import sys
import os
import time
from requests import session
from random import SystemRandom
import random
import datetime
from sh import whoami
import getpass
import pytz
import datetime

os.environ['TZ'] = 'Asia/Jakarta'

t = time.localtime()
CT = time.strftime("%H:%M", t)

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

def DTS ():
    g = ['5','6','7','8','9']
    m = ['5','6','7','8','9']
    j = ['🟢','🟢','🔴','🟢','🔴']
    v = ['BESAR','KECIL','BESAR','KECIL']
    p = [' 🎲🎲',' 🎲🎲']
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
        print(f'[{CYAN}Countdown{L}] : {PT}-{secs:02d} ', end='\r')
        time.sleep(1)
        total_second -= 1
        
TZ="GMT+7"

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

print(f"{H}{UNDER} Stop Bermain 15 Menit {L}")


