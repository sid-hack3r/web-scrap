import re
from traceback import print_tb
import requests
import sys
import time
from colorama import Fore
from bs4 import BeautifulSoup as bs

print()
print(Fore.GREEN+' AUTHOR: S I D '+Fore.WHITE)
print(Fore.LIGHTYELLOW_EX+' Contact: sidghule123@gmail.com'+Fore.WHITE)
print()
print('################################################')
print()
time.sleep(3)
print(Fore.LIGHTMAGENTA_EX+'Checking Input...'+Fore.WHITE)
print()
time.sleep(3)
try:  
    url = sys.argv[1]
    print(Fore.BLUE+'[~]'+' Target: '+Fore.LIGHTYELLOW_EX+url+Fore.WHITE)
    print()
except IndexError:
    print(Fore.BLUE+'[~]'+Fore.RED+' usegs:'+Fore.WHITE+Fore.GREEN+' python scrap.py https://example.com'+Fore.WHITE)
    exit()
try:
    r = requests.get(url)
    status = r.status_code
    html = r.text
    txt = bs(html,'lxml')
    search = str(txt)
    pattern  = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
    pattern2  = re.compile(r'\+\d\d\s\d\d\d\d\d\d\d\d\d\d')
    match = pattern.finditer(search)
    match2 = pattern2.finditer(search)
    
    index = []
    numbers = []
    for i in match,match2:
        for j in i:
            index.append(j.span())
    for n in range(len(index)):
        numbers.append(search[list(index[0])[0]:list(index[0])[1]])    
except Exception as e:
    print(Fore.BLUE+'[~]'+' Status code: 404 Not Found')
    print()
    print(Fore.BLUE+'[~]'+Fore.RED+f' Something is wrong please check url {url}'+Fore.WHITE)
    print()
    print(Fore.BLUE+'[~]'+Fore.RED+' usegs:'+Fore.WHITE+Fore.GREEN+' python scrap.py https://example.com'+Fore.WHITE)
    print()
    exit()
try:
    print(Fore.BLUE+'[~]'+Fore.RED+' Checking status...')
    print()
    time.sleep(3)
    
    if status == 200:
        print(Fore.BLUE+'[~]'+Fore.GREEN+f' Status: {status} ok'+Fore.WHITE)
        print()
        print(Fore.BLUE+'[~]'+Fore.RED+' Finding phone numbers...')
        print()
        time.sleep(5)
         
        if numbers != []:
            print(Fore.BLUE+'[~]'+Fore.GREEN+f' Phone Numbers: Found {len(numbers)}'+Fore.WHITE)
            print()
            time.sleep(3)
            num = 0
            for i in numbers:
                num+=1
                print(Fore.BLUE+'[~]'+Fore.GREEN+f' Found:{num} '+i+Fore.WHITE)
                time.sleep(2)
                print()   
        else:
            print(Fore.BLUE+'[~]'+Fore.RED+' Phone Numbers Not Found')
            print()
        print(Fore.BLUE+'[~]'+Fore.RED+' Finding Server...'+Fore.WHITE)
        print()
        header = r.headers
        
        time.sleep(5)
        print(Fore.BLUE+'[~]'+Fore.GREEN+' Found Server: '+header['Server']+Fore.WHITE)
        print()
        print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Finding Technology...'+Fore.WHITE)
        print()
        print(Fore.BLUE+'[~]'+Fore.GREEN+f' Found Technology: '+header['X-Powered-By']+Fore.WHITE)
        print()
        print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Finding Cookies...'+Fore.WHITE)
        print()
        time.sleep(3)
        print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Found Cookie: '+Fore.GREEN+header['Set-Cookie']+Fore.WHITE)
        print()
    else:
        if status == 404:
            print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+f' Status Code: 404 Not Found '+Fore.WHITE)
            print()
            exit()
        elif status == 406:
            print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+f' Status Code: 406 Not Acceptable '+Fore.WHITE)
            print()
            exit()
        elif status == 403:
            print(Fore.BLUE+'[~]'+' forbidden error status: 403 '+Fore.WHITE)
            print()
            exit()
        else:
            print(Fore.BLUE+'[~]'+f' Error Status: {status}'+Fore.WHITE)

        
except NameError:
    pass