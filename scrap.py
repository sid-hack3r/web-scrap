
import re
from traceback import print_tb
import requests
import sys
import time
from colorama import Fore
from bs4 import BeautifulSoup as bs

print()
print(Fore.GREEN+' AUTHOR: S I D '+Fore.WHITE)
print(Fore.LIGHTYELLOW_EX+' Version: 1.0.0'+Fore.WHITE)
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
        print(Fore.BLUE+'[~]'+Fore.RED+' Finding phone numbers...'+Fore.WHITE)
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
            print(Fore.BLUE+'[~]'+Fore.LIGHTYELLOW_EX+' Phone Numbers Not Found'+Fore.WHITE)
            print()
        print(Fore.BLUE+'[~]'+Fore.RED+' Finding Server...'+Fore.WHITE)
        print()
        header = r.headers
        
        time.sleep(5)
        print(Fore.BLUE+'[~]'+Fore.GREEN+' Found Server: '+header['Server']+Fore.WHITE)
        print()
        time.sleep(3)
        print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Finding Technology...'+Fore.WHITE)
        print()
        try:
            print(Fore.BLUE+'[~]'+Fore.GREEN+f' Found Technology: '+header['X-Powered-By']+Fore.WHITE)
            print()
        except Exception as e:
             print(Fore.BLUE+'[~]'+Fore.LIGHTYELLOW_EX+f' Not Found '+Fore.WHITE)
             print()
        print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Finding Cookies...'+Fore.WHITE)
        print()
        time.sleep(3)
        try:
            print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Found Cookie: '+Fore.GREEN+header['Set-Cookie']+Fore.WHITE)
            print()
        except Exception as e:
             print(Fore.BLUE+'[~]'+Fore.LIGHTYELLOW_EX+' Not Found '+Fore.WHITE)
             print()
        print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+' Finding Robots.txt...'+Fore.WHITE)
        print()
        time.sleep(3)
        robotfile = url+'/robots.txt'
        u = robotfile.replace('//r','/r')
        res = requests.get(u)
        if res.status_code == 200:
            print(Fore.BLUE+'[~]'+Fore.LIGHTGREEN_EX+f' Found Robot.txt: {robotfile}'+Fore.WHITE)
            print()
            time.sleep(3)
        else:
             print(Fore.BLUE+'[~]'+Fore.LIGHTYELLOW_EX+f' Not Found  '+Fore.WHITE)
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
            print(Fore.BLUE+'[~]'+' Forbidden error status: 403 '+Fore.WHITE)
            print()
            exit()
        elif status == 503:
            print(Fore.BLUE+'[~]'+' Internal server error status: 503 '+Fore.WHITE)
            print()
            exit()
        else:
            print(Fore.BLUE+'[~]'+f' Error Status: {status}'+Fore.WHITE)

    if status == 200:
        with open('wordlist/wordlist.txt') as file:
                  word = file.read()
                  l = word.split('\n')
                  num = len(l)
                  for i in range(num+1):
                      urls = url+'/'+str(l[i])
                      resp = requests.get(urls).status_code
                      if resp == 200 or resp == 302:
                        print(Fore.BLUE+'[~]'+Fore.LIGHTGREEN_EX+f'Found Url: {urls}  Code:{resp}'+Fore.WHITE)
                        print()
                      else:
                          print(Fore.BLUE+'[~]'+Fore.LIGHTRED_EX+f' Not Found: {urls}  Code: {resp}'+Fore.WHITE,end='')
                          print()
                          
                          
                      
except NameError:
    pass

