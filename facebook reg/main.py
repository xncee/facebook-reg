import os, random, subprocess, uuid, string
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    xrblue = f"\n{blueplus} Facebook Reg {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
class Xnce():
    def __init__(self):
        print(f"\n{DESIGN.blueplus} Email: ", end="")
        email = input()
        self.facebook_register(email)
        self.inex()
    def inex(self):
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        exit()
    def facebook_register(self, email):
        head = {
            "Host": "www.facebook.com",
            "Cookie": "sb=vf8lYoDVW8wyNpJgiZLEcEBx; datr=vf8lYsPP_n9JMtenehAO1SpF; locale=ar_AR; wd=1365x961; fr=0rhqNQIV1Z4KcyhbT.AWV_nc_6WlK6A0KJrsoSsoLepuk.BiKI3M.9n.AAA.0.0.BiKI4L.AWUZDuIZgko",
            "Content-Length": "1269",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Fb-Lsd": "AVrHhyt2bfA",
            "Accept": "*/*",
            "Origin": "https://www.facebook.com",
            "Referer": "https://www.facebook.com/index.php?next=https%3A%2F%2Fwww.facebook.com%2Fconfirmemail.php%3Fnext%3Dhttps%253A%252F%252Ffacebook.com%252F",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9"
        }
        data = {
            "jazoest": "2993",
            "lsd": "AVrHhyt2bfA",
            "firstname": "ahmad",
            "lastname": "ak",
            "reg_email__": email,
            "reg_email_confirmation__": email,
            "reg_passwd__": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=15)),
            "birthday_month": "2",
            "birthday_day": "21",
            "birthday_year": "2000",
            "birthday_age": "",
            "did_use_age": "false",
            "sex": "2",
            "preferred_pronoun": "",
            "custom_gender": "",
            "referrer":"",
            "asked_to_login": "0",
            "use_custom_gender": "",
            "terms": "on",
            "ns": "0",
            "ri": uuid.uuid4(),
            "action_dialog_shown": "",
            "ignore": "captcha",
            "locale": "en_US",
            "reg_instance": "tFUnYqo_rpslNVpCvxLITZl9",
            "captcha_persist_data": "AZml18M-LU8rx1iFbY0mNEYD4cmA1-I6Ld7XySb9TLhBR66ttv1F2iQThTyjl1UMjXw-dg_q0DauFjH8llsJ_9Oybdcf7XGiWai-AIkzkvU50bmFac5O8PV9eFTo4xXdkbUalElBlscMQl-BpkYzxk5ibpZ5_ijopdLlJ9ep4dqIE4LMIez9SGIc0hzhllwWvW9OM8BNvIoiEDDDKeki_vke4jLQJdITRXVMBOLaGEAdK-NODIb5YPzP6UXgCvKZOaxO7Q2Un5FM4MJn4CHLwvy3cf9gtqZy_KdrPHrfZsbSoFvqoCOHF5_DQY64BtJUqWP7IYmeDVF8VRuiT26nX3NzA0Rmul_n3IzvoAogYJT-p8cM97jQfIFBSGBe3b-GIiE",
            "captcha_response": "",
            "__user": "0",
            "__a": "1",
            "__dyn": "7xe6FomK36Q5E5ObwKBWo5O12wAxu13wqovzEdEc8uw9-3K4o1j8hwem0nCq1ewcG0KEswaq0yE5ufz81sbzo5-0me2218w5uwbO7E2swdq0Ho2ewnE3fw5rwSyE1582Zw",
            "__csr": "",
            "__req": "a",
            "__hs": "19059.BP%3ADEFAULT.2.0.0.0.dpr=1",
            "__ccg": "MODERATE",
            "__rev": "1005163005",
            "__s": "jggw25%3A5xex56%3Azntftb",
            "__hsi": "7072717098373465848-0",
            "__comet_req": "0",
            "__spin_r": "1005163005",
            "__spin_b": "trunk",
            "__spin_t": "1646745274"
        }
        req = requests.post("https://www.facebook.com/ajax/register.php", headers=head, data=data)
        #print(req.text, req.status_code)
        if '"registration_succeeded":true' in req.text:
            print(f"\n{DESIGN.blueplus} Done {DESIGN.BLUE}{email}")
            print(f"\n{DESIGN.blueplus} Wait 5-10 Minutes")
        elif '"email_claiming_skip_to_recovery":true' in req.text:
            print(f"\n{DESIGN.redminus} Email Is Already Registered")
        else:
            print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
print(DESIGN.xrblue)
Xnce()
