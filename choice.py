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
import datetime

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
      with open("halaman2.txt", 'w') as f:
       f.write(str(e2))
       f.close()
       
def halaman2 ():
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
      with open("halaman144.txt", 'w') as f:
       f.write(str(e2))
       f.close()
       
def halaman3 ():
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
    with open('issuenumber2.txt', 'w') as f:
        f.write(str(d))
        f.close()
       
halaman1()
halaman2()
halaman3()
gameissue()

TZ="GMT+7"

os.environ['TZ'] = 'Asia/Jakarta'
        
GOLD = '\033[2;93;40m'
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
print("")
print("")
print("")
os.system("git pull")
os.system('clear')
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"""{PT}
    ███████╗███████╗███████╗            {GR}[INFORMASI]{L}
    {PT}██╔════╝██╔════╝██╔════╝         
    {PT}██████╗░██████╗░█████╗       {PT}🔹AUTOR   = {H} Racknarock {L}
    {PT}╚════██╗╚════██╗██╔══╝       {PT}🔹RNGv?   = {GRY}Searching..
    {PT}██████╔╝██████╔╗██║░░░██     {PT}🔹LOGIN   = OWNER
    {PT}╚═════╝░╚═════╝░╚═╝          {PT}🔹SERVER  = {H}OFFLINE{L}
""")
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print("")
print(f" {H}OWNER WHATSAPP 085796297189{L}{PT}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•{L}")
print(f"•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•{PTH} Your Device is Registered {L}")
print(f"{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"                    {H} List SC {L}-{WW} 55FIVE• {L} \n{PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L}\n       {WW2} NEW {L}               {WW2} OLD {L}             {WW2} ULTIMATE {L} \n{PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L}")
print(f"{PTH}┃1. Super Sonic   ┃{L} {PTH}┃#. RevoX         ┃{L} {PTH}┃21.{L}{PT1}{BO}Aurora Mystic {L}{PTH}┃{L}")
print(f"{PTH}┃2. Sonic         ┃{L} {PTH}┃A. Devilz4       ┃{L} {PTH}┃25.{L}{PT1}{BO}Follow - N V2 {L}{PTH}┃{L}")
print(f"{PTH}┃3. Magic         ┃{L} {PTH}┃B. Eagle4        ┃{L} {PTH}┃28.{L}{PT1}{BO}Ripper Forex  {L}{PTH}┃{L}")
print(f"{PTH}┃4. Prime         ┃{L} {PTH}┃C. Electra       ┃{L} {PTH}┃26.{L}{PT1}{BO}Hack Mode v6  {L}{PTH}┃{L}")
print(f"{PTH}┃5. Regulator     ┃{L} {PTH}┃D. Nebula2       ┃{L} {PTH}┃39.{L}{PT1}{BO}IRON-MAN™     {L}{PTH}┃{L}")
print(f"{PTH}┃6. Ultra Insting ┃{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PTH}┃42.{L}{PT1}{BO}Time-Stop™    {L}{PTH}┃{L}")
print(f"{PTH}┃7. Black Hole    ┃{L}      {WW2} Limited {L}      {PTH}┃47.{L}{PT1}{BO}Black-panther {L}{PTH}┃{L}")
print(f"{PTH}┃8. Evo-X         ┃{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PTH}┃92.{L}{PT1}{BO}Risk-X        {L}{PTH}┃{L}")
print(f"{PTH}┃9. Cool-Down     ┃{L} {PTH}┃51.{L}{PT1}{BO}kompen-Searah {L}{PTH}┃{L} {PTH}┃76.{L}{PT1}{BO}Risk-X_v2     {L}{PTH}┃{L}")
print(f"{PTH}┃10.Fast-X        ┃{L} {PTH}┃69.{L}{PT1}Hack Mode {L}{PTH}    ┃{L} {PTH}┃67.{L}{PT1}{BO}{B}X-VVIP{L}{PT1}{BO}        {L}{PTH}┃{L}")
print(f"{PTH}┃11.Super-Magic   ┃{L} {PTH}┃99.{L}{PT1}Hack Mode v2 {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃12.Elipse        ┃{L} {PTH}┃88.{L}{PT1}Hack Mode v3 {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃13.Prisma        ┃{L} {PTH}┃77.{L}{PT1}Hack Mode v4 {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃14.Glizer        ┃{L} {PTH}┃55.{L}{PT1}Hack Mode v5 {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃15.Golden_Frezee {L}{PTH}┃{L} {PTH}┃44.{L}{PT1}HM Circle𓆩♡𓆪 {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃16.Gatotkaca     {L}{PTH}┃{L} {PTH}┃33.{L}{PT1}{BO}•Gladiator•  {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃17.{L}{PT1}VIP      {L}{PTH}     ┃{L} {PTH}┃90.{L}{PT1}{BO}Master Trend {L}{PTH} ┃{L} {PTH}┃                 ┃{L}")
print(f"{PTH}┃18.{L}{PT1}VVIP      {L}{PTH}    ┃{L} {PTH}┃30.{L}{PT1}{BO}Follow - N {L}{PTH}   ┃{L} {PTH}┃                 ┃{L}")
print(f"{RED}▬▬▬▬▬▬▬▬▬{G}•{RED}▬▬▬▬▬▬▬▬▬{L} {RED}▬▬▬▬▬▬▬▬▬{G}•{RED}▬▬▬▬▬▬▬▬▬{L} {RED}▬▬▬▬▬▬▬▬▬{G}•{RED}▬▬▬▬▬▬▬▬▬{L}")
print(f"{PT1} Auto Update :{L} {WW1} ON {L} {PTH}┃56.{L}{PT1}Turn-Back-X   {L}{PTH}┃{L} {PTH}┃                 ┃{L}")
print(f"{PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L} {PT}▬▬▬▬▬▬▬▬▬{G}•{PT}▬▬▬▬▬▬▬▬▬{L}")
print("")
print(f"{RED}{BO}Rilis SC{L} {RED}{UNDER}X-VVIP{L} {RED}{BO}ADDED..{L}")
print("")
pilih = input(f"{PTH} Pilih {L}{H} Nomor {L} : ")
if pilih == '1':
    os.system("python smain2.py")
elif pilih == '2':
    os.system("python main2.py")
elif pilih == '3':
    os.system("python md1.py")
elif pilih == '4':
    os.system("python prime.py")
elif pilih == '5':
    os.system("python mulai.py")
elif pilih == '6':
    os.system("python SX.py")
elif pilih == '7':
    os.system("python BH.py")
elif pilih == '8':
    os.system("python Evo-X.py")
elif pilih == '9':
    os.system("python CD.py")
elif pilih == '10':
    os.system("python FX.py")
elif pilih == '11':
    os.system("python smd1.py")
elif pilih == '12':
    os.system("python ep1.py")
elif pilih == '13':
    os.system("python PR1.py")
elif pilih == '14':
    os.system("python G1.py")
elif pilih == '15':
    os.system("python GF.py")
elif pilih == '16':
    os.system("python GK.py")
elif pilih == '17':
    os.system("python V.py")
elif pilih == '18':
    os.system("python VV.py")
elif pilih == '#':
    os.system("python RX.py")
elif pilih == 'A':
    os.system("python DV.py")
elif pilih == 'B':
    os.system("python eagle4.py")
elif pilih == 'C':
    os.system("python electra.py")
elif pilih == 'D':
    os.system("python NB2.py")
elif pilih == '69':
    os.system("python HM1.py")
elif pilih == '99':
    os.system("python HMv2L.py")
elif pilih == '88':
    os.system("python HMv3L.py")
elif pilih == '77':
    os.system("python HMv4L.py")
elif pilih == '55':
    os.system("python HMv5L.py")
elif pilih == '44':
    os.system("python HMvLc.py")
elif pilih == '33':
    os.system("python GL.py")
elif pilih == '90':
    os.system("python MT.py")
elif pilih == '51':
    os.system("python KS.py")
elif pilih == '30':
    os.system("python FN.py")
elif pilih == '21':
    os.system("python AU.py")
elif pilih == '25':
    os.system("python FN2.py")
elif pilih == '28':
    os.system("python RP.py")
elif pilih == '26':
    os.system("python HM6.py")
elif pilih == '39':
    os.system("python iMc.py")
elif pilih == '42':
    os.system("python TSC.py")
elif pilih == '47':
    os.system("python BP.py")
elif pilih == '56':
    os.system("python KBc.py")
elif pilih == '92':
    os.system("python RK.py")
elif pilih == '76':
    os.system("python RS.py")
elif pilih == '67':
    os.system("python XVV.py")
else :
	os.system("python choice.py")