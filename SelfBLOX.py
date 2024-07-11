
import os, sys

os.system("title SelfBLOX")

def rerun():
    cwd = os.getcwd()
    file_path = os.path.realpath(__file__)
    os.system(f"python {file_path}")
    
try:
    import base64
    from colorama import *
    import datetime
    import json
    import logging
    import mediafire_dl
    from PIL import Image, ImageDraw
    import random
    import requests
    import rblxopencloud
    import subprocess
    import webbrowser
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import string
    import time
    from time import gmtime, strftime
    import urllib3
    import uuid
    import zipfile
    from rblxopencloud import *

except ModuleNotFoundError as f:
    if "rblxopencloud" in str(f):
        os.system(f'python -m pip install rblx-open-cloud')
    elif "mediafire" in str(f):
        os.system(f'python -m pip install git+https://github.com/Juvenal-Yescas/mediafire-dl')
    else: 
        os.system(f'python -m pip install {f.name}')
    rerun()
    
try:
    from ChromedriverDownloader import * # type: ignore
    from PyTokio import * # type: ignore
except ModuleNotFoundError as f:
    print("No Modules Called:\nPyTokio and\nChromedriver Were Found.")
    print("For your safety we have to provide from which sources we are gonna download.")
    print()
    print("ChromeDriverDownloader = https://github.com/Damix-hash/ChromedriveDownloader")
    print("PyTokio = https://github.com/DaFrenchTokio/PyTokio")
    print("These projects are open-sourced so check them out!")
    print()
    input("Press ENTER To Download These Projects And Continue.")

    if not os.path.exists("PyTokio"):
        os.mkdir("PyTokio")

        response = requests.get("https://raw.githubusercontent.com/DaFrenchTokio/PyTokio/main/PyTokio/__init__.py")
        with open("Pytokio/__init__.py", "w", encoding="utf-8") as pytokio_source:
            pytokio_source.write(response.text)

    if not os.path.exists("ChromedriverDownloader"):
        os.mkdir("ChromedriverDownloader")

        response = requests.get("https://raw.githubusercontent.com/Damix-hash/ChromedriveDownloader/main/ChromedriverDownloader/__init__.py")
        with open("ChromedriverDownloader/__init__.py", "w", encoding="utf-8") as ChromedriverDownloader_source:
            ChromedriverDownloader_source.write(response.text)
        
    rerun()
    
init()

global ver
ver = 0.1

response = requests.get("https://raw.githubusercontent.com/Damix-hash/roblox-stuff/main/version")
if response.ok:
    if not str(response.text) != ver:
        input(f"Invalid Version. Latest Version {response.text} Press ENTER To Leave")
        exit()
else:
    input("Couldn't Fetch Version. Press ENTER To Leave.")
    exit()

os.system(f"title SelfBLOX [{ver}] - StartUp")
os.system('mode con: cols=130 lines=25')
path = os.getcwd()



user_agents = []

response = requests.get("https://raw.githubusercontent.com/Damix-hash/roblox-stuff/main/user-agents")

if response.ok:
    for user_agent in response.text.split("\n"):
        user_agents.append(user_agent)

def random_useragent():
    return str(random.choice(user_agents))

def cprint(color=None, sign=None, msg=None, width=None):
    if msg is not None:
        if color is not None:
            color = color.lower()
            if color == "red":
                print("["+ Fore.RED + sign + Fore.RESET + "]", msg)
            elif color == "yellow":
                print("["+ Fore.YELLOW + sign + Fore.RESET + "]", msg)
            elif color == "green":
                print("["+ Fore.GREEN + sign + Fore.RESET + "]", msg)
        else:
            if width is not None:
                print(msg.center(int(width)))
            else:
                print(msg)
    else:
        print()

warning_tag = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
banner = Fore.RED + """
                       ::::::::  :::::::::: :::        :::::::::: :::::::::  :::        ::::::::  :::    ::: 
                      :+:    :+: :+:        :+:        :+:        :+:    :+: :+:       :+:    :+: :+:    :+: 
                      +:+        +:+        +:+        +:+        +:+    +:+ +:+       +:+    +:+  +:+  +:+  
                      +#++:++#++ +#++:++#   +#+        :#::+::#   +#++:++#+  +#+       +#+    +:+   +#++:+   
                             +#+ +#+        +#+        +#+        +#+    +#+ +#+       +#+    +#+  +#+  +#+  
                      #+#    #+# #+#        #+#        #+#        #+#    #+# #+#       #+#    #+# #+#    #+# 
                       ########  ########## ########## ###        #########  ########## ########  ###    ### 
""" + Fore.RESET

def welcome_print(width=None):    
    cprint(msg="Welcome to " + Fore.RED + "SELFBLOX" + Fore.RESET + "!", width=width)

def separator():
    print("\n===========================================================[" + Fore.RED + "SelfBLOX" + Fore.RESET + "]===========================================================\n")

global headers

headers = {
    "User-Agent": random_useragent(),
    "Accept": "application/json",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "referrer": "https://roblox.com/",
}



def base64_decode(base64_string):
    if not base64_string.startswith(warning_tag):
        base64_bytes = base64_string.encode("ascii") 
        base64_decode = base64.b64decode(base64_bytes) 
        return base64_decode.decode("ascii")


def base64_encode(normal_string):
    normal_string_bytes = normal_string.encode("ascii")
    normal_string_encode = base64.b64encode(normal_string_bytes) 
    return normal_string_encode.decode("ascii") 


def custom_random_string(amount):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(int(amount)))
    return str(result_str)


def makedir(path):
    if not os.path.exists(str(path)):
        os.mkdir(str(path))


def makefile(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass


def webdriver_check(setpath):
    if not os.path.exists(f"{setpath}/chromedriver.exe"):
        version = latest_chromedriver() # type: ignore
        download_chromedriver(setpath, "", version, False) # type: ignore
        rerun()


def cmd(command):
    os.system(str(command))


def clr():
    cmd("cls" if os.name == "nt" else "clear")


def title_message(msg):
    cmd(f"title SelfBLOX [{ver}] - {msg}")

def help():
    numbers = {
        1: "Check Account Information",
        2: "Check What User Has Played",
        3: "Check Users Location",
        4: "Join Game",
        5: "Friend List Cleaner",
        6: "Redeem All Promocodes",
        7: "Purchase Everything That's Free",
        8: "Scrape Group Clothes",
        9: "Avatar Fun",
        10: "Chat Bypass Checker",
        11: "Pin Cracker",
        12: "Spam Friends",
        13: "Mass Uploader",
        14: "Robux Calculator",
        15: "Robux History",
        16: "Mass Group Exile",
        17: "Nuke Account",
        18: "Join Our Discord",
        19: "Switch Accounts",
        20: "Exit",
    }

    print(f"[{Fore.RED}1{Fore.RESET}]", f"{numbers[1]:<30}", f"[{Fore.RED}6{Fore.RESET}]", f"{numbers[6]:<30}", f" [{Fore.RED}11{Fore.RESET}]", f"{numbers[11]:<30}", f"[{Fore.RED}16{Fore.RESET}]", f"{numbers[16]}")
    print(f"[{Fore.RED}2{Fore.RESET}]", f"{numbers[2]:<30}", f"[{Fore.RED}7{Fore.RESET}]", f"{numbers[7]:<30}", f"[{Fore.RED}12{Fore.RESET}]", f"{numbers[12]:<30}", f"[{Fore.RED}17{Fore.RESET}]", f"{numbers[17]}")
    print(f"[{Fore.RED}3{Fore.RESET}]", f"{numbers[3]:<30}", f"[{Fore.RED}8{Fore.RESET}]", f"{numbers[8]:<30}", f" [{Fore.RED}13{Fore.RESET}]", f"{numbers[13]:<30}", f"[{Fore.RED}18{Fore.RESET}]", f"{numbers[18]}")
    print(f"[{Fore.RED}4{Fore.RESET}]", f"{numbers[4]:<30}", f"[{Fore.RED}9{Fore.RESET}]", f"{numbers[9]:<30}", f" [{Fore.RED}14{Fore.RESET}]", f"{numbers[14]:<30}", f"[{Fore.RED}19{Fore.RESET}]", f"{numbers[19]}")
    print(f"[{Fore.RED}5{Fore.RESET}]", f"{numbers[5]:<30}", f"[{Fore.RED}10{Fore.RESET}]", f"{numbers[10]:<30}", f"[{Fore.RED}15{Fore.RESET}]", f"{numbers[15]:<30}", f"[{Fore.RED}20{Fore.RESET}]", f"{numbers[20]}")


def setup_files():
    makedir("SelfBLOX")
    makedir("SelfBLOX/WebDriver")
    webdriver_check("SelfBLOX/WebDriver")
    makedir("SelfBLOX/Accounts")
    makefile("SelfBLOX/session-logs.txt")
    makefile("SelfBLOX/previous-cookie.txt")
    makefile("SelfBLOX/cookie.txt")
    makedir("SelfBLOX/Logs")
    makefile("SelfBLOX/Logs/run-time.log")

def unban(session, token, cookie):
    cprint("red", "!", "Checking If You Are Banned.")
    
    ban_check = requests.get("https://roblox.com/home", allow_redirects=True, cookies={".ROBLOSECURITY":cookie})
    if "not-approved" in str(ban_check.url):
        unban_url = "https://usermoderation.roblox.com/v1/not-approved/reactivate"

        unban_headers = {
            "User-Agent": random_useragent(),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
            "x-csrf-token": token,
            "Alt-Used": "usermoderation.roblox.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site"
        }

        response = session.post(unban_url, headers=unban_headers, proxies=GetProxy())
        print(response.content)

def option_picker(session, userid, username, cookie):

    token = ""
    token_response = session.post("https://auth.roblox.com/v2/logout", headers=headers)
    token = token_response.headers["x-csrf-token"]

    clr()
    title_message("Home")
    print(banner)
    welcome_print(137)
    cprint(msg="Your Are Logged In As: " + Style.BRIGHT + username + Style.NORMAL, width=135)
    cprint(msg="What would you like to do today?\n", width=130)
    separator()
    help()
    print()
    option = int(input("-> "))

    main(option, session, token, userid, username, cookie)

global cookie
global driver
cookie = None
cookies = {".ROBLOSECURITY": cookie}

setup_files()

logging.basicConfig(filename=str(os.path.join(path, "SelfBLOX", "logs", "run-time.log")), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(str(os.path.join(path, "SelfBLOX", "logs", "run-time.log")))

if os.path.getsize("SelfBLOX/cookie.txt") > 0:
    with open("SelfBLOX/cookie.txt", "r", encoding="utf-8") as read_cookie:
            base_cookie = read_cookie.read()
            unobf_cookie = base64_decode(base_cookie)
            if not unobf_cookie.startswith(warning_tag):
                cookie = warning_tag + unobf_cookie
            else:
                silly_cookie = unobf_cookie.replace(warning_tag, "")
                encoded_cookie = base64_encode(silly_cookie)

                with open("SelfBLOX/cookie.txt", "w", encoding="utf-8") as login_cookie:
                    login_cookie.write(encoded_cookie)
                
                cookie = unobf_cookie

def main(option, session, token, userid, username, cookie):
    '''
    So hello there programmer!
    This is creator of the script speaking

    So this is the MAIN function of the program
    Do not edit anything... Not even the "Unless you know what you are doing"
    Because the script should be 100% perfect and does not require any optimatizations or anything like that
    '''

    
    __RequestVerificationToken = ''


    def get__RequestVerificationToken(session, userid): # Not Being Used
        # will be used next time
        response = session.get(f'https://www.roblox.com/abusereport/userprofile?id={userid}', proxies=GetProxy())
        if response.ok:
            site_data = response.text
            site_data = site_data.split('<input name="__RequestVerificationToken" type="hidden" value="')[1]
            __RequestVerificationToken = site_data.split('" />')[0]

    func_headers = {
        "User-Agent": random_useragent(),
        "Accept": "application/json",
        "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
        "Content-Type": "application/json;charset=utf-8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "x-csrf-token": token,
    }

    if option == 1:
        clr()
        print(banner)
        separator()
        title_message("Account Information")
        cprint("green", ">", "Getting Account Information.")
        separator()

        response = session.get("https://users.roblox.com/v1/users/authenticated", proxies=GetProxy())

        if response.ok:
            data = response.json()
            username = data["name"]
            userID = data["id"]
            displayName = data["displayName"]

        response = session.get("https://users.roblox.com/v1/birthdate", proxies=GetProxy()) # type: ignore
                               
        if response.ok:
            data = response.json()
            birthMonth = data["birthMonth"]
            birthDay = str(data["birthDay"])
            birthYear = str(data["birthYear"])
            if birthMonth < 10:
                birthMonth = "0" + str(birthMonth)
            formatted = "[DD-MM-YYYY] "+ str(birthDay)+ "-" + str(birthMonth) + "-" + str(birthYear)

        response = session.get("https://users.roblox.com/v1/description", proxies=GetProxy())
        if response.ok:
            data = response.json()
            if data["description"] == "":
                description = " "
            else:
                description = data["description"]

        response = session.get("https://users.roblox.com/v1/gender", proxies=GetProxy()) # type: ignore
        if response.ok:
            data = response.json()
            gender_data = data["gender"]
            if gender_data == "1":
                gender = "Male"
            else:
                gender = "Female"

        response = session.get("https://www.roblox.com/my/settings/json", proxies=GetProxy()) # type: ignore
        
        if response.ok:
            data = response.json()
            aboveThirdteen = data["UserAbove13"]
            accountAge = data["AccountAgeInDays"]
            premium = data["IsPremium"]
            IsEmailVerified = data["IsEmailVerified"]

        response = session.get("https://accountinformation.roblox.com/v1/promotion-channels", proxies=GetProxy()) # type: ignore
        
        if response.ok:
            data = response.json()
            facebook = data["facebook"]
            twitter = data["twitter"]
            youtube = data["youtube"]
            twitch = data["twitch"]
            guilded = data["guilded"]

        response = session.get("https://economy.roblox.com/v1/user/currency", proxies=GetProxy()) # type: ignore
        
        if response.ok:
            data = response.json()
            robux = data["robux"]

        cprint(msg=f"Username: {username}\nUserID: {userID}\nDisplay Name: {displayName}\nBirthdate: {formatted}\nDescription: {description}\nGender: {gender}\nUser Above 13: {aboveThirdteen}\nAccount Age in Days: {accountAge}\nPremium: {premium}\nEmail Verified: {IsEmailVerified}\nFacebook: {facebook}\nTwitter: {twitter}\nYoutube: {youtube}\nTwitch: {twitch}\nGuilded: {guilded}\nRobux: {robux}")
        separator()
        input("Press ENTER To Continue")
        option_picker(session, userid, username, cookie)

    elif option == 2:
        clr()
        print(banner)
        separator()
        title_message("Games User Has Played")
        userid = int(userid)
        cursor = ""
        game_IDs = []
        game_Names = []
        places = []

        cprint("green", ">", "Getting Badges")

        while cursor != None:
            badges_api = f"https://badges.roblox.com/v1/users/{userid}/badges?limit=100&sortOrder=Asc&cursor={cursor}"
            response = requests.get(badges_api, proxies=GetProxy()) # type: ignore
            if response.ok: 
                data = response.json()["data"]
                if data != []:
                    for item in data:
                        if item["awarder"] != None:
                            if item["awarder"]["id"] not in game_IDs:
                                game_IDs.append(item["awarder"]["id"])
                    cursor = response.json()["nextPageCursor"]
                else:
                    cprint("red", "!", "User Has No Badges. (Can't Check What Games He Played)")
                    input("Press ENTER To Continue")
                    option_picker(session, userid, username, cookie)

        cprint("green", ">", "Decoding Names")

        for universeids in game_IDs:
            universeData = f"https://www.roblox.com/games/{universeids}"
            response = requests.get(universeData, proxies=GetProxy()) # type: ignore
            for line in response.text.split("\n"):
                if "<title>" in line:
                    title = line
                    title = title.strip()
                    game_Name = title[7:-17]
                    if game_Name not in game_Names:
                        game_Names.append(game_Name)

        separator()
        print("Games that the person played:")
        for game in game_Names:
            cprint("green", ">", str(game))

        input("Press ENTER To Continue")
        option_picker(session, userid, username, cookie)
    elif option == 3:
        clr()
        print(banner)
        separator()
        title_message("Session Log")
        cprint("green", ">", "Grabbing Information")
        response = session.get(
            "https://apis.roblox.com/token-metadata-service/v1/sessions?nextCursor=&desiredLimit=500",
            proxies=GetProxy(), # type: ignore
        )
        if response.ok:
            global n
            city = []
            subdivision = []
            country = []
            roblox_type = []
            browser = []
            oos = []
            ip = []
            date = []
            data = response.json()
            sessions = data["sessions"]
            for acc_session in sessions:
                if acc_session["isCurrentSession"] == False:
                    location = acc_session["location"]
                    city.append(location["city"])
                    subdivision.append(location["subdivision"])
                    country.append(location["country"])
                    agent = acc_session["agent"]
                    roblox_type.append(agent["type"])
                    browser.append(agent["value"])
                    oos.append(agent["os"])
                    ip.append(acc_session["lastAccessedIp"])
                    miliseconds = acc_session["lastAccessedTimestampEpochMilliseconds"]
                    miliseconds = int(miliseconds)
                    ms_to_date = datetime.datetime.fromtimestamp(
                        miliseconds / 1000, tz=datetime.timezone.utc
                    )
                    date.append(str(ms_to_date))

            if (
                city != None
                and subdivision != None
                and country != None
                and roblox_type != None
                and browser != None
                and oos != None
                and ip != None
                and date != None
            ):
                with open(
                    "SelfBLOX/session-logs.txt", "w", encoding="utf-8"
                ) as session_logs:
                    sessions_logged = 0
                    for n in range(
                        max(
                            len(city),
                            len(subdivision),
                            len(country),
                            len(roblox_type),
                            len(browser),
                            len(oos),
                            len(ip),
                            len(date),
                        )
                    ):
                        formatted_data = ""
                        if n < len(city):
                            city_data = city[n]
                        else:
                            city_data = ""

                        if n < len(subdivision):
                            subdivision_data = subdivision[n]
                        else:
                            subdivision_data = ""

                        if n < len(country):
                            country_data = country[n]
                        else:
                            country_data = ""

                        if n < len(roblox_type):
                            roblox_type_data = roblox_type[n]
                        else:
                            roblox_type_data = ""

                        if n < len(browser):
                            browser_data = browser[n]
                        else:
                            browser_data = ""

                        if n < len(oos):
                            oos_data = oos[n]
                        else:
                            oos_data = ""

                        if n < len(ip):
                            ip_data = ip[n]
                        else:
                            ip_data = ""

                        if n < len(date):
                            date_data = date[n]
                        else:
                            date_data = ""
                        sessions_logged += 1
                        formatted_data = f"[{username}:{sessions_logged}]\nCity: {city_data}\nSubdivision: {subdivision_data}\nCountry: {country_data}\nRoblox Type: {roblox_type_data}\nBrowser: {browser_data}\nOs: {oos_data}\nIP: {ip_data}\nDate: {date_data}"
                        with open(
                            "SelfBLOX/session-logs.txt", "a", encoding="utf-8"
                        ) as session_logs:
                            session_logs.write(formatted_data + "\n")

            subprocess.Popen(f"notepad {path}/SelfBLOX/session-logs.txt")
            cprint("red", "!", f"Logged {sessions_logged} Sessions!")
            input("Press ENTER To Continue")
            option_picker(session, userid, username, cookie)

    elif option == 4:
        clr()
        print(banner)
        separator()
        title_message("Game Joiner")
        cprint(msg="Hello! Welcome To Game Joiner!")
        cprint(msg="Before Using This Make Sure You Have A WebDriver Installed.")
        cprint(msg="So How Would You Like To Join A Game?")

        cprint("red", "1", "GameID")
        cprint("red", "2", "GameID and JobID")
        cprint("red", "3", "Return")

        join_option = int(input("> "))
        if join_option == 1:
            clr()
            print(banner)
            separator()
            cprint(msg="Please Provide GameID.")
            gameid = int(input("> "))
            driver = webdriver.Chrome("SelfBLOX/WebDriver/chromedriver.exe")
            driver.get(f"https://www.roblox.com/games/{gameid}")
            driver_cookies = {
                "name": ".ROBLOSECURITY",
                "value": str(cookie),
                "domain": ".roblox.com",
            }
            driver.add_cookie(driver_cookies)
            driver.refresh()
            script = f"Roblox.GameLauncher.joinGameInstance({gameid})"
            driver.execute_script(script)
            driver.quit()
            input("Press ENTER To Continue")
            option_picker(session, userid, username, cookie)
        elif join_option == 2:
            clr()
            print(banner)
            separator()
            cprint(msg="Please Provide GameID.")
            gameid = int(input("> "))
            cprint(msg="Please Provide JobID.")
            jobid = str(input("> "))
            driver = webdriver.Chrome("SelfBLOX/WebDriver/chromedriver.exe")
            driver.get(f"https://www.roblox.com/games/{gameid}")
            driver_cookies = {
                "name": ".ROBLOSECURITY",
                "value": str(cookie),
                "domain": ".roblox.com",
            }
            driver.add_cookie(driver_cookies)
            driver.refresh()
            script = f"Roblox.GameLauncher.joinGameInstance({gameid}, {jobid})"
            driver.execute_script(script)
            driver.quit()
            input("Press ENTER To Continue")
            option_picker(session, userid, username, cookie)
        elif join_option == 3:
            option_picker(session, userid, username, cookie)

    elif option == 5:
        clr()
        print(banner)
        separator()
        title_message("Friend List Cleaner")
        friend_ids = []
        cprint("green", ">", "Declining All Friend Requests")
        session.post(
            "https://friends.roblox.com/v1/user/friend-requests/decline-all",
            proxies=GetProxy(), # type: ignore
        )
        response = session.get(
            f"https://friends.roblox.com/v1/users/{userid}/friends", proxies=GetProxy() # type: ignore
        )

        if response.ok:
            cprint("green", ">", "Getting All Friends")
            data = response.json()["data"]
            for friend in data:
                friend_ids.append(friend["id"])

        for friend in friend_ids:
            response = session.get(
                f"https://friends.roblox.com/v1/users/{friend}/unfriend",
                proxies=GetProxy(), # type: ignore
                headers=func_headers,
            )
            cprint("green", ">", f"Removed {friend}")

        input("Press ENTER To Continue")
        option_picker(session, userid, username, cookie)
    elif option == 6:
        clr()
        print(banner)
        separator()
        title_message("Promocode Redeemer")

        codes = []
        response = requests.get("https://raw.githubusercontent.com/Damix-hash/roblox-stuff/main/promocodes")
        if response.ok:
            data = response.text
            for code in data.split("\n"):
                codes.append(code)

        for code in codes:
            body = {"code": code}
            response = session.post(
                "https://billing.roblox.com/v1/promocodes/redeem",
                json=body,
                headers=func_headers,
                proxies=GetProxy(), # type: ignore
            )
            if response.ok:

                data = response.json()
                if "Code already redeemed." in data["errorMsg"]:
                    cprint("red", "!", f"{code} Is Already Redeemed.")
                elif "Invalid promo code." in data["errorMsg"]:
                    cprint("red", "!", f"{code} Is Invalid.")
                else:
                    cprint("green", ">", f"{code} Is Valid!")

        input("Press ENTER To Continue")
        option_picker(session, userid, username, cookie)
    elif option == 7:
        clr()
        print(banner)
        separator()
        title_message("Free Items Buyer")
        ids = []
        cursor = ""
        count = 1
        while cursor != None:
            response = session.get(
                f"https://catalog.roblox.com/v1/search/items/details?category=All&limit=30&maxPrice=0&cursor={cursor}",
                proxies=GetProxy(), # type: ignore
            )
            if response.ok:
                data = response.json()["data"]
                for items in data:
                    if "productId" in items:
                        ids.append(items["productId"])
                cprint("red", str(count), f"Scraped {len(data)} Ids!")
                count += 1
                cursor = response.json()["nextPageCursor"]

        separator()
        count = 0
        for assetid in ids:
            response = session.post(
                f"https://economy.roblox.com/v1/purchases/products/{assetid}",
                json={"expectedCurrency": 1, "expectedPrice": 0, "expectedSellerId": 1},
                headers={"X-CSRF-TOKEN": token},
                proxies=GetProxy(), # type: ignore
            )
            if response.ok:
                data = response.json()
                if data["purchased"] == True:
                    cprint("green", str(count), f"Successfully purchased: {data['assetName']} || Id: {assetid}")
                else:
                    cprint("red", str(count), f"Failed to purchase: {data['assetName']}: {data['errorMsg']}")
                count += 1
            elif "TooManyRequests" in response.text or response.status_code == 429:
                cprint("yellow", str(count), "Rate Limit! Waiting 60 Seconds.")
                time.sleep(60)

        separator()
        cprint("green", "!", "Finished Purchasing Free Items!")
        input("Press ENTER To Continue")
        option_picker(session, userid, username, cookie)
    elif option == 8:
        clr()
        print(banner)
        separator()
        title_message("Group Scraper")
        global pos
        pos = 0

        try:
            groupID = int(input("Provide GroupID: "))
        except:
            pass

        if groupID == None or groupID == 0:
                cprint("red", "!", "Please put only the ID of the group.")
                input("Press ENTER To Continue")
                option_picker(session, userid, username, cookie)

        if not os.path.exists("SelfBLOX/Templates"):
            os.mkdir("SelfBLOX/Templates")

        def check_group_exists(group_id):
            cprint(msg="Checking If ROBLOX Group Exists")
            url = f"https://groups.roblox.com/v2/groups?groupIds={group_id}"
            response = requests.get(url, proxies=GetProxy()) # type: ignore
            if response.ok:
                data = response.json()
                groups = data["data"]
                for group in groups:
                    if group["id"] == group_id:
                        return True
                    return False

        def get_group_name(group_id):
            cprint(msg="Getting GroupName")
            url = f"https://groups.roblox.com/v2/groups?groupIds={group_id}"
            response = requests.get(url, proxies=GetProxy()) # type: ignore
            if response.ok:
                data = response.json()
                groups = data["data"]
                for group in groups:
                    if group["name"]:
                        return str(group["name"])

        def get_ids(groupid):
            cprint(msg="Getting IDS")
            global amount
            global clothes
            amount = 1
            clothes = []
            cursor = ""
            while cursor != None:
                url = f"https://catalog.roblox.com/v1/search/items?category=All&creatorTargetId={groupid}&creatorType=Group&cursor={cursor}&limit=100&sortOrder=Desc"
                response = requests.get(url, proxies=GetProxy()) # type: ignore
                if response.ok:
                    data = response.json()["data"]
                    if data != []:
                        for item in data:
                            if item["itemType"] == "Asset":
                                clothes.append(item["id"])
                                clothing_id = item["id"]
                                cprint("green", str(amount), f"ID: {clothing_id}")
                                amount += 1
                        cursor = response.json()["nextPageCursor"]
                    else:
                        cprint("red", "!", "No Clothes Found!")
                        input("Press ENTER To Continue")
                        option_picker(session, userid, username, cookie)

            return clothes

        def check_for_XML(folder):
            global func_amount
            global remove_ids
            remove_ids = []
            func_amount = 0
            if os.path.exists(folder):
                for assetid in clothes:
                    for file in os.listdir(folder):
                        if file.startswith(str(assetid)):
                            cprint("green", ">", f"AssetID {assetid} Already Exists!, Ignoring.")
                            remove_ids.append(assetid)
                            func_amount += 1
                for assetid in remove_ids:
                    if remove_ids != None:
                        clothes.remove(assetid)

        def assetXML(asset_id, folder):
            cprint("green", ">", f"Scraping assetXML from: {asset_id}")
            random_string = custom_random_string(25)
            url = f"https://assetdelivery.roblox.com/v1/asset?id={asset_id}"
            save_path = f"{folder}/{asset_id}-{random_string}.xml"

            response = requests.get(url, proxies=GetProxy()) # type: ignore
            if response.ok:
                with open(save_path, "wb") as file:
                    try:
                        file.write(response.content)
                    except Exception as e:
                        cprint("red", "!", f"Fatal Error: {str(e)}")
                        logger.error(str(e))
                        input("Press ENTER To Continue")
                        option_picker(session, userid, username, cookie)

            cprint("green", ">", f"Saved XML As: {asset_id}-{random_string}.xml")

        def scrape_templates(folder):
            global template_ids
            editing_string = ""
            template_ids = []
            if os.path.exists(folder):
                for XML in os.listdir(folder):
                    with open(f"{folder}/{XML}", "r", encoding="utf-8") as XMLfile:
                        for line in XMLfile:
                            if "<url>" in line:
                                editing_string = line.replace(
                                    "<url>http://www.roblox.com/asset/?id=", ""
                                )
                                editing_string = editing_string.replace("</url>", "")
                                editing_string = editing_string.strip()
                                template_ids.append(editing_string)

                for XML in os.listdir(folder):
                    cprint("green", ">", f"Removing: {XML}")
                    try:
                        os.remove(f"{folder}/{XML}")
                    except Exception as e:
                        cprint("red", "!", f"Fatal Error: {str(e)}")
                        logger.error(str(e))
                        input("Press ENTER To Continue")
                        option_picker(session, userid, username, cookie)

        def download_templates(folder_to_save):
            if os.path.exists(folder_to_save):
                for template_id in template_ids:
                    cprint(msg=f"Downloading TemplateID: {template_id}")
                    url = f"https://assetdelivery.roblox.com/v1/asset/?id={template_id}"
                    random_string = custom_random_string(25)
                    save_path = f"{folder_to_save}/{template_id}-{random_string}.png"
                    response = requests.get(url, proxies=GetProxy()) # type: ignore
                    if response.ok:
                        with open(save_path, "wb") as file:
                            try:
                                file.write(response.content)
                            except Exception as e:
                                cprint("red", "!", f"Fatal Error: {str(e)}")
                                logger.error(str(e))
                                input("Press ENTER To Continue")
                                option_picker(session, userid, username, cookie)
                        cprint("green", ">", f"Finished Downloading: {template_id}-{random_string}.png")

        if check_group_exists(groupID):
            group_name = str(get_group_name(groupID))
            cprint(msg=f"Group Name: {group_name}")
            get_ids(groupID)
            group_name_folder = group_name

            if " " in group_name_folder:
                group_name_folder = group_name.replace(" ", "-")
            if "." in group_name_folder:
                group_name_folder = group_name_folder.replace(".", "(dot)")
            if ":" in group_name_folder:
                group_name_folder = group_name_folder.replace(":", "(double-colon)")
            if '"' in group_name_folder:
                group_name_folder = group_name_folder.replace('"', "")
            if "/" in group_name_folder:
                group_name_folder = group_name_folder.replace("/", "(slash-left)")
            if "?" in group_name_folder:
                group_name_folder = group_name_folder.replace("/", "(question)")
            if "*" in group_name_folder:
                group_name_folder = group_name_folder.replace("*", "(star)")
            if "|" in group_name_folder:
                group_name_folder = group_name_folder.replace("|", "I")
            if "<" in group_name_folder:
                group_name_folder = group_name_folder.replace("<", "(arrow-left)")
            if ">" in group_name_folder:
                group_name_folder = group_name_folder.replace(">", "(arrow-right)")

            group_name_folder = group_name_folder.replace("\\", "")
            group_folder = f"SelfBLOX/Templates/{group_name_folder}"

            if not os.path.exists(group_folder):
                os.mkdir(group_folder)
            else:
                check_for_XML(group_folder)

            if clothes != None:
                for clothing_id in clothes:
                    assetXML(clothing_id, group_folder)
                cprint("green", ">", f"Saved everything to XML!")
                scrape_templates(str(group_folder))
                download_templates(str(group_folder))
            else:
                cprint("red", "!", f"No Clothes Found!")
                input("Press ENTER To Continue")
                option_picker(session, userid, username, cookie)
        else:
            cprint("red", "!", f"No Group Found!")
            input("Press ENTER To Continue")
            option_picker(session, userid, username, cookie)

        separator()
        cprint(msg="Finished!")
        cprint(msg="Check SelfBLOX/Templates For Templates.")
        webbrowser.open(os.path.realpath("SelfBLOX/Templates"))
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 9:

        def body_colors(head, torso, right_arm, left_arm, right_leg, left_leg):
            response = session.post("https://avatar.roblox.com/v2/avatar/set-wearing-assets", headers=func_headers, json={"assets":[]}, proxies=GetProxy())
            if response.ok:
                cprint(msg="Removed All Items!")

            body = {
                "headColorId": head,
                "torsoColorId": torso,
                "rightArmColorId": right_arm,
                "leftArmColorId": left_arm,
                "rightLegColorId": right_leg,
                "leftLegColorId": left_leg,
            }
            response = session.post("https://avatar.roblox.com/v1/avatar/set-body-colors", json=body, headers=func_headers, proxies=GetProxy()) # type: ignore
            
            if response.ok:
                cprint("green", ">", "Success")
            else:
                cprint(msg=str(response.status_code))
                cprint(msg=str(response.text))

        clr()
        print(banner)
        separator()
        title_message("Avatar Fun")
        cprint("red", ">", "Hello! Welcome to Avatar Fun! Here you can set pre-made avatar skin colors!")
        cprint("red", ">", "For example 'Noob' will make your avatar look like noob!")
        cprint("red", "!", "Also it automatically removes all of your accessories.")
        cprint("red", ">", "Avaible Options Are:\n")
        
        options = ["Noob", "Zombie", "Erik Cassel", "Naked", "Old-School", "Guest", "Default", "Randomized"]
        amount = 1
        for option in options:
            cprint("red", str(amount), option)
            amount += 1

        avaible_body_colors = [
            364,
            217,
            359,
            18,
            125,
            361,
            192,
            351,
            352,
            5,
            153,
            1007,
            101,
            1025,
            330,
            135,
            305,
            11,
            1026,
            321,
            107,
            310,
            317,
            29,
            105,
            24,
            334,
            199,
            1002,
            1001,
        ]

        avatar_option = int(input("> "))
        if avatar_option == 1:
            body_colors(334, 23, 334, 334, 119, 119)
        elif avatar_option == 2:
            body_colors(317, 38, 317, 317, 26, 26)
        elif avatar_option == 3:
            body_colors(1001, 105, 1001, 1001, 1011, 1011)
        elif avatar_option == 4:
            body_colors(125, 1030, 125, 125, 125, 125)
        elif avatar_option == 5:
            body_colors(334, 199, 334, 334, 1003, 1003)
        elif avatar_option == 6:
            body_colors(1001, 1003, 1003, 1003, 26, 26)
        elif avatar_option == 7:
            body_colors(1001, 194, 1001, 1001, 102, 102)
        elif avatar_option == 8:
            body_colors(
                random.choice(avaible_body_colors),
                random.choice(avaible_body_colors),
                random.choice(avaible_body_colors),
                random.choice(avaible_body_colors),
                random.choice(avaible_body_colors),
                random.choice(avaible_body_colors),
            )
        else:
            cprint("red", "!","This Option Isn't Avaible.")
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)
    elif option == 10:
        clr()
        print(banner)
        separator()
        title_message("Chat Bypass Checker")
        cprint("red", "!", "Check if your message will possibly get tagged or not.")
        message = str(input("> "))
        if message != "" or message != " ":
            response = requests.get(
                f"https://catalog.roblox.com/v1/search/items?category=All&keyword={message}"
            )
            if response.json()["keyword"] == "###":
                cprint(msg=f"{message} Is Tagged.")
            else:
                cprint(msg=f"{message} Isn't  Tagged!")
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 11:
        clr()
        print(banner)
        separator()
        title_message("Pin Cracker")
        avaible_pins = []

        makedir(f"SelfBLOX/Accounts/{username}")
        makedir(f"SelfBLOX/Accounts/{username}/Pins")
        makefile(f"SelfBLOX/Accounts/{username}/Pins/invalid.txt")
        makefile(f"SelfBLOX/Accounts/{username}/Pins/valid.txt")

        with open(
            f"SelfBLOX/Accounts/{username}/Pins/invalid.txt", "r", encoding="utf-8"
        ) as invalid_pins:
            the_invalid_pins = invalid_pins.read()
            common_pins = requests.get(
                "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv"
            ).text
            for common_pin in common_pins.split("\n"):
                avaible_pins.append(str(common_pin.split(",")[0].strip()))

            pins_to_remove = []
            for pins in avaible_pins:
                if pins in the_invalid_pins.split(",")[0]:
                    pins_to_remove.append(pins)

            for pin in pins_to_remove:
                avaible_pins.remove(pin)
        cprint("green", "!", f"Scraped {str(len(avaible_pins))} Pins.")

        global break_loop
        break_loop = False

        def postPin(pin):
            headers = {
                "User-Agent": random_useragent(),
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
                "Content-Type": "application/json;charset=utf-8",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            }
            global break_loop
            while True:
                pin = str(pin)
                if break_loop:
                    break
                try:
                    response = requests.post(
                        "https://auth.roblox.com/v1/account/pin/unlock",
                        headers={"x-csrf-token": getToken()},
                        json={"pin": str(pin)},
                        cookies=cookies,
                    )
                    data = response.json()

                    if data:
                        if "unlockedUntil" in data:
                            cprint("green", ">", f"Valid Pin For User {username}: {pin}")
                            with open(
                                f"SelfBLOX/Accounts/{username}/Pins/valid.txt",
                                "w",
                                encoding="utf-8",
                            ) as valid_pin:
                                valid_pin.write(f"{username}:{pin}")
                            break_loop = True
                            break

                        elif data["errors"][0]["message"] == "Too many requests":
                            cprint("yellow", "!", f"Rate Limit Reached. Cooling For 5 Minutes")
                            time.sleep(60 * 5)

                        elif data["errors"][0]["code"] == 4:
                            cprint("red", "!", f"Invalid Pin: {pin}")
                            with open(
                                f"SelfBLOX/Accounts/{username}/Pins/invalid.txt",
                                "a",
                                encoding="utf-8",
                            ) as invalid_pin:
                                with open(
                                    f"SelfBLOX/Accounts/{username}/Pins/invalid.txt",
                                    "r",
                                    encoding="utf-8",
                                ) as check_invalid_pin:
                                    if not f"{username}:{pin}" in check_invalid_pin:
                                        invalid_pin.write(f"{username}:{pin}\n")
                            break

                except Exception as e:
                    cprint("red", "!", f"An Error Just  Occured: {e}")
                    logger.error(str(e))

        for pin in avaible_pins:
            if break_loop == True:
                break
            else:
                cprint(msg=f"Trying: {pin}")
                postPin(pin)

        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 12:
        clr()
        print(banner)
        separator()
        title_message("Spammer")
        cprint(msg="Which method would you like to use?")
        cprint("red", "1", f"DM everyone (With Spam)")
        cprint("red", "2", f"GroupChat Target")
        spam_option = int(input("> "))
        if spam_option == 1:
            title_message("Chat Spammer")

            def send_message(conversationID, message):
                body = {"conversationID": conversationID, "message": str(message)}
                response = session.post(
                    "https://chat.roblox.com/v2/send-message",
                    json=body,
                    headers=func_headers,
                    proxies=GetProxy(), # type: ignore
                )
                if response.ok:
                    cprint(msg=f"Posted Message: {str(message)} To ConversationID: {conversationID}")

            users_friends = []
            response = session.get(
                f"https://friends.roblox.com/v1/users/{userid}/friends",
                headers=func_headers,
                proxies=GetProxy(), # type: ignore
            )
            if response.ok:
                data = response.json()["data"]
                for friend in data:
                    users_friends.append(friend["id"])

            conversations = []
            response = session.get(
                "https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=10000",
                headers=func_headers,
                proxies=GetProxy(), # type: ignore
            )
            if response.ok:
                data = response.json()
                for item in data:
                    conversations.append(item["id"])
                    cprint(msg=f"Added {str(len(data))} Conversations!")

                cprint(msg=f"Choose Message Option:")
                random_numbers = False
                random_strings = False
                random_binary = False
                custom_message = ""

                cprint("red", "1", f"Random Numbers")
                cprint("red", "2", f"Random Strings")
                cprint("red", "3", f"Custom Message")

                message_option = int(input("> "))
                if message_option == 1:
                    random_numbers = True
                    random_strings = False

                elif message_option == 2:
                    random_strings = True
                    random_numbers = False

                elif message_option == 3:
                    random_numbers = False
                    random_strings = False
                    custom_message = str(input("Message: "))

                cprint(msg="How many times do you want to spam it?")
                amount = int(input("> "))
                separator()
                for spam in range(0, amount):
                    if random_numbers:
                        custom_message = random.randint(0, 100)
                    elif random_strings:
                        custom_message = custom_random_string(50)
                    for conversation in conversations:
                        send_message(conversation, f"SelfBLOX - {custom_message}")

        elif spam_option == 2:
            clr()
            print(banner)
            separator()
            title_message("Group Chat Spammer")
            groupchat_conversationId = 0

            def leave_group_chat(participantUserId, conversationId):
                body = {
                    "participantUserId": participantUserId,
                    "conversationId": conversationId,
                }
                response = session.post(
                    "https://chat.roblox.com/v2/remove-from-conversation",
                    json=body,
                    headers=func_headers,
                    proxies=GetProxy(), # type: ignore
                )
                if response.ok:
                    cprint(msg="Left the group")

            def create_group_chat(participantUserIds):
                random_text = custom_random_string(10)
                body = {
                    "participantUserIds": participantUserIds,
                    "title": f"SelfBLOX - {random_text}",
                }
                response = session.post(
                    "https://chat.roblox.com/v2/start-group-conversation",
                    json=body,
                    headers=func_headers,
                    proxies=GetProxy(), # type: ignore
                )
                if response.ok:
                    cprint(msg="Successfully started a new group conversation")
                    data = response.json()
                    if (
                        data["conversation"]["id"] is not None
                        and data["conversation"]["id"] != ""
                    ):
                        return data["conversation"]["id"]

            target_userids = []
            cprint(msg="Input UserID/s For Group Chat Spammer (Split with : For Multiple Users In One Group!)\nOnly up to 5 users for safety but you could try 9-10 (max)")
            userIds = input("> ")
            if ":" in userIds:
                for usersId in userIds.split(":"):
                    target_userids.append(int(usersId))
            else:
                target_userids.append(int(userIds))
            amount = int(input("How Many Times do you want to spam with group chat?\n> "))
            separator()

            for i in range(0, amount):
                groupchat_conversationId = create_group_chat(target_userids)
                leave_group_chat(userid, groupchat_conversationId)

        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)
    elif option == 13:
        clr()
        print(banner)
        separator()
        title_message("Mass Uploader")

        # Please may god forgive for this sin of the code.
        
        makedir(f"SelfBLOX/Accounts/{username}")
        makefile(f"SelfBLOX/Accounts/{username}/api_key.txt")

        makedir("SelfBLOX/Mass-Uploader")
        makedir(f"SelfBLOX/Mass-Uploader/Baits")
        date = strftime("%Y-%m-%d %H;%M;%S", gmtime())
        path_script = f"{path}/SelfBLOX/Mass-Uploader/{date}"
        path_script2 = f"{path}\SelfBLOX\Mass-Uploader\{date}"
        open_path_script = f"{path}\\SelfBLOX\\Mass-Uploader\\{date}"
        makedir(path_script)
        makedir(f"{path_script}/Image")
        makedir(f"{path_script}/Audio")
        cprint(msg="Pick option for what do you want to mass upload.")
        cprint("red", "1", f"Images/Decals")
        cprint("red", "2", f"Audio")
        mass_uploader_option = int(input("> "))

        ###########[For Audio MassUpload]###########
        ffmpeg_avaible = True
        duration = 0
        upload_account = None # None means to the account
        ###########[For Audio MassUpload]###########

        ###########[API]###########
        api_key = ''
        ###########[API]###########

        names = [
        "Happy",   
        "Sunshine",
        "Summer",  
        "Pencil",
        "Notebook",
        "Desk",
        "Bookshelf",
        "Rainbow",
        "Adventure",
        "Hiking",
        "Forest",
        "Ocean",
        "Campfire",
        "Marshmallow",
        "Tent",
        "Backpack",
        "Map",
        "Trail",
        "Ecosystem",
        "Wildlife",
        "Conservation",
        "Recycling",
        "Gardening",
        "Flowers",
        "Pollination",
        "Butterfly",
        "Caterpillar",
        "Ladybug",
        "Dragonfly",
        "Waterfall",
        "River",
        "Creek",
        "Lake",
        "Island",
        "Paradise",
        "Desert",
        "Oasis",
        "Cactus",
        "Sunflower",
        "Daisy",
        "Tulip",
        "Rose",
        "Peony",
        "Lily",
        "Orchid",
        "Violets",
        "Pansies",
        "Daffodil",
        "Hyacinth",
        "Lilac",
        "Iris",
        "Chrysanthemum",
        "Aster",
        "Cosmo",
        "Marigold",
        "Zinnia",
        "Snapdragon",
        "Petunia",
        "Begonia",
        "Caladium",
        "Bleeding heart",
        "Shasta daisy",
        "Hosta",
        "Echinacea",
        "Phlox",
        "Coneflower",
        "Daylily",
        "Black-eyed Susan",
        "Mexican petunia",
        "Forget-me-not",
        "Coral bells",
        "Hellebore",
        "Goat's beard",
        "Fuchsia",
        "Asters",
        "Bleeding heart",
        "Calla lily",
        "Columbine",
        "Delphinium",
        "Foxglove",
        "Gerbera daisy",
        "Hydrangea",
        "Iris",
        "Lavender",
        "Lupine",
        "Milkweed",
        "Moonflower",
        "Morning glory",
        "Nasturtium",
        "Orchid",
        "Peony",
        "Periwinkle",
        "Primrose",
        "Rhododendron",
        "Sunflower",
        "Trillium",
        "Tulip",
        "Violet",
        ]

        
        ###########[IMAGE MANIPULATION]############
        def get_valid_color():
            return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        mass_upload_headers = {
            "User-Agent": "RobloxStudio/WinInet RobloxApp/0.601.0.6010507 (GlobalDist; RobloxDirectDownload)", # ROBLOX Studio.
            'Requester': 'Client',
            "x-csrf-token": token,
        }
        
        def create_api_key(api_name, api_description):
            name = api_name
            description = api_description
            
            url = "https://apis.roblox.com/cloud-authentication/v1/apiKey"

            api_key_headers = {
                "User-Agent": random_useragent(),
                "Accept": "*/*",
                "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
                "Content-Type": "application/json",
                "x-csrf-token": token,
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            }

            body = {"cloudAuthUserConfiguredProperties":{"name":name, "description": description, "isEnabled": True, "allowedCidrs": ["0.0.0.0/0"], "scopes": [{"scopeType": "asset","targetParts": ["U"],"operations": ["read", "write"]}]}}

            response = session.post(url, headers=api_key_headers, json=body, proxies=GetProxy()) # type: ignore
            json = response.json()
            if "Response.DuplicateKey" in response.text or "Response.InvalidNameOrDescription" in response.text:
                    
                cprint(msg="Generating different API Name and Description.")
                    
                name = custom_random_string(5)
                description = custom_random_string(5)
                    
                create_api_key(name, description)
                    
            else:
                global apikey_Secret_Preview
                global apikey_Secret
                
                apikey_Secret_Preview = response.json().get("apikeySecretPreview")
                apikey_Secret = response.json().get('apikeySecret')

                if os.path.exists(f"Selfbot/Accounts/{username}/api_key.txt"):
                    
                    with open(f"Selfbot/Accounts/{username}/api_key.txt", "a", encoding="utf-8") as api_file_key:
                        api_file_key.write(f"[apikey_Secret_Preview:apikey_Secret] > {apikey_Secret_Preview}:{apikey_Secret}\n")
                else:
                    makefile(f"Selfbot/Accounts/{username}/api_key.txt")

                    with open(f"Selfbot/Accounts/{username}/api_key.txt", "a", encoding="utf-8") as api_file_key:
                        api_file_key.write(f"[apikey_Secret_Preview:apikey_Secret] > {apikey_Secret_Preview}:{apikey_Secret}\n")
                    
        def check_for_ffmpeg():
            try:
                subprocess.call(['ffmpeg', '-version'], stdout=subprocess.PIPE)
            except FileNotFoundError:
                cprint(msg="FFMPEG was not found on your device.")
                input("Press ENTER To Continue.")
                ffmpeg_avaible = False
                option_picker(session, userid, username, cookie)

        def join_audios(file_one, file_two, output_file):
            command = ['ffmpeg', '-i', file_one, '-i', file_two, '-filter_complex', '[0:0][1:0]concat=n=2:v=0:a=1[out]', '-map', '[out]', output_file]
            try:
                subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except Exception as e:
                cprint(msg=str(e))
                logger.error(str(e))
                time.sleep(10)

        def get_baits():
            if len(os.listdir(f"SelfBLOX/Mass-Uploader/Baits")) == 0:
                url = 'https://www.mediafire.com/file/p4sxnj6lz0wsfrz/mp3_baits.zip'
                output = "SelfBLOX/Mass-Uploader/Baits/baits.zip"
                mediafire_dl.download(url, output, quiet=False)
                clr()
                print(banner)
                separator()
                cprint(msg="Got zip baits.")
                try:
                    with zipfile.ZipFile("SelfBLOX/Mass-Uploader/Baits/baits.zip", 'r') as zip_ref:
                       zip_ref.extractall("SelfBLOX/Mass-Uploader/Baits")
                    os.remove(output)
                    cprint(msg="Installed baits to: SelfBLOX/Mass-Uploader/Baits")
                except Exception as e:
                    cprint(msg=str(e))
                    logger.error(str(e))
            else:
                cprint(msg="Audio baits are already avaible!")
                   
        if mass_uploader_option == 1:
                create_api_key("S3LFBLOX", "S3LFBLOX")
                creator = User(int(userid), str(apikey_Secret))
                cprint(msg="Place Image into the folder then continue!")
                webbrowser.open(os.path.realpath(f"{open_path_script}\\Image"))
                cprint(msg="Please put name of your file with extension here.")
                image = str(input("> "))
                cprint(msg="How many images do you wanna make for upload?")
                amount = int(input("> "))
                cprint(msg="Which method for mass upload?")
                cprint("red", "1", f"Random squares on corners")
                cprint("red", "2", f"Noise")
                method_option = int(input("> "))
                
                for file in os.listdir(f"{path_script}\\Image"):
                    if file.startswith(image):
                        
                        method_file_path = os.path.join(f"{path_script2}\\Image", file)
                        extension = os.path.splitext(method_file_path)[1]
                        
                makedir(f"{path_script}/Image/UploadImages")

                for _ in range(amount):
                    
                    image = Image.open(method_file_path)
                    width, height = image.size
                    random_string = custom_random_string(25)
                    
                    if method_option == 1:
                        draw = ImageDraw.Draw(image)
                        global corner

                        corner = random.choice(['top-left', 'top-right', 'bottom-left', 'bottom-right'])
                        size = random.randint(10, 100)
                        
                        if corner == 'top-left':
                            draw.rectangle([0, 0, size, size], fill=get_valid_color())
                            draw.line([0, 0, size, size], fill=get_valid_color(), width=5)
                        elif corner == 'top-right':
                            draw.rectangle([image.width - size, 0, image.width, size], fill=get_valid_color())
                            draw.line([image.width - size, 0, image.width, size], fill=get_valid_color(), width=5)
                        elif corner == 'bottom-left':
                            draw.rectangle([0, image.height - size, size, image.height], fill=get_valid_color())
                            draw.line([0, image.height - size, size, image.height], fill=get_valid_color(), width=5)
                        elif corner == 'bottom-right':
                            draw.rectangle([image.width - size, image.height - size, image.width, image.height], fill=get_valid_color())
                            draw.line([image.width - size, image.height - size, image.width, image.height], fill=get_valid_color(), width=5)

                        image.save(f"{path_script}\\Image\\UploadImages\\{random_string}{extension}")
                    elif method_option == 2:
                        image = image.convert('RGBA')
                        static = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                        draw = ImageDraw.Draw(static)

                        for x in range(width):
                            for y in range(height):
                                if random.random() < 0.10:
                                    draw.point(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(10, 50))
                                    
                        result = Image.alpha_composite(image, static)
                        result.save(f"{path_script}\\Image\\UploadImages\\{random_string}{extension}")
                    cprint(msg="Method completed!")
                separator()
                uploaded = 0
                for image in os.listdir(f"{path_script}/Image/UploadImages"):
                    
                    name = random.choice(names) + " " + random.choice(names)
                    description = "This Object Was Uploaded With SelfBLOX! The Best FREE Multi Tool!"
                    with open(f"{path_script}/Image/UploadImages/{image}", "rb") as file:
                        try:
                            asset = creator.upload_asset(file, AssetType.Decal, name, description)
                        except Exception as e:
                            cprint(msg=str(e))
                            logger.error(str(e))
                            pass

                    while True:
                        try:
                            status = asset.fetch_operation()
                            if status:
                                asset = status
                                break
                            else:
                                time.sleep(0.1)
                        except exceptions.RateLimited:
                            time.sleep(0.1)
                        except exceptions.InvalidKey:
                            pass
                        
                    if asset:
                        rblxopencloud_asset = str(asset).replace("rblxopencloud.Asset(", "")
                        rblxopencloud_asset = rblxopencloud_asset.replace('"', "")
                        rblxopencloud_asset = rblxopencloud_asset.replace('name=', "Name: ")
                        rblxopencloud_asset = rblxopencloud_asset.replace("type=AssetType.Decal)", "Type: Decal")
                        rblxopencloud_asset = "ID: https://roblox.com/library/" + rblxopencloud_asset

                        decal_id = str(asset).replace("rblxopencloud.Asset(", "")
                        find_id = decal_id.find("name=")-2
                        decal_id = decal_id[:find_id]

                        with open(f"{path_script}/Image/ids.txt", "a", encoding="utf-8") as avaible_ids:
                            avaible_ids.write(f"{rblxopencloud_asset}\n")
                        cprint("green", ">", f"Uploaded!: https://roblox.com/library/{decal_id}")

        elif mass_uploader_option == 2:
            get_baits()
            check_for_ffmpeg()
            
            if ffmpeg_avaible:
                cprint(msg="Place AudioFile into the folder then continue!")
                webbrowser.open(os.path.realpath(f"{open_path_script}\\Audio"))
                cprint(msg="Please put name of your file with extension here.")
                audio = str(input("> "))
                cprint(msg="Do you wanna upload it to a group? Y/N")
                group_option = str(input("> "))
                if group_option.lower() == "y":
                    cprint(msg="Please put groupID of group you wanna upload audios to.")
                    upload_account = int(input("> "))
                    
                for file in os.listdir(f"{path_script}/Audio"):
                    if file.startswith(audio):
                            file_path = os.path.join(f"{path_script}/Audio", file)
                            extension = os.path.splitext(file_path)[1]
                makedir(f"{path_script}/Audio/UploadAudios")

                count_baits = 0
                for bait in range(len(os.listdir(f"SelfBLOX/Mass-Uploader/Baits"))):
                    mp3_bait = f"SelfBLOX/Mass-Uploader/Baits/bait{count_baits}.mp3"
                    
                    if count_baits < 9:
                        count_baits += 1

                    number_indicator = ''
                    if count_baits == 1:
                        number_indicator = "st"
                    elif count_baits == 2:
                        number_indicator = "nd"
                    elif count_baits == 3:
                        number_indicator = "rd"
                    else:
                        number_indicator = "th"
                        
                    random_string = custom_random_string(25)
                    cprint("red", "!", f"Getting {count_baits}{number_indicator} Upload File! Name: {random_string}{extension}")
                    join_audios(mp3_bait, f"{path_script}/Audio/{audio}", f"{path_script}/Audio/UploadAudios/{random_string}{extension}")
                    
                separator()
                for upload_audio in os.listdir(f"{path_script}/Audio/UploadAudios"):
                    audio_path = f"{path_script}/Audio/UploadAudios/{upload_audio}"
                    
                    with open(audio_path, "rb") as file:
                        audio_base64 = base64.b64encode(file.read()).decode()

                    audio_size = os.path.getsize(audio_path)

                    duration_output = subprocess.run(['ffprobe', '-i', 'example.mp3', '-show_format', '-v quiet'], capture_output=True)
                    duration_output = duration_output.stdout.decode().split('\n')

                    for line in duration_output:
                        if 'duration' in line:
                            duration = float(line.split('=')[1])
                    
                    if duration < 420: # 7 minutes
                        name = random.choice(names) + " " + random.choice(names)
                        cprint("yellow", ">", f'Uploading to ROBLOX file: {upload_audio} as: {name}')
                        data = {
                            "name": name,
                            "file": audio_base64,
                            "groupId": upload_account,
                            "paymentSource": "User",
                            "estimatedFileSize": audio_size,
                            "estimatedDuration": duration,
                            "assetPrivacy": 1
                        }

                        response = session.post("https://publish.roblox.com/v1/audio", json=data, headers=func_headers, proxies=GetProxy())
                        data = response.json()
                        cprint("red", "!", str(response))
                        
                        if 'errors' in data:
                            error = data["errors"]
                            code = error[0]["code"]
                            message = error[0]["message"]

                            if code == 25 and "Audio upload has exceeded user's quota." in message:
                                cprint("red", "!", "Exceeded amount of avaible amount of uploads. (Can't upload more on this account!")
                                break
                            elif code == 8:
                                cprint("red", "!", "Audio is not supported!")
                                break
                            elif code == 9:
                                cprint("red", "!", "Audio is corrupted!")
                                break
                            elif code == 18:
                                cprint("yellow", "!", "Rate Limit Reached! Waiting 1 Minute.")
                                time.sleep(60)
                            else:
                                cprint(msg=data)
                                    
                        elif "Id" in data:
                            get_id = data["Id"]
                            with open(f"{path_script}/Audio/ids.txt", "a", encoding="utf-8") as avaible_ids:
                                avaible_ids.write(f"https://roblox.com/library/{get_id}\n")
                            cprint("green", ">", f"Uploaded!: https://roblox.com/library/{get_id}")
                    else:
                        
                        cprint("red", "!", "Audio is too long. Longer than 7 minutes")
                        break
                if os.path.exists(f"{path_script}/Audio/ids.txt") and os.path.getsize(f"{path_script}/Audio/ids.txt") > 0:
                    cprint("green", ">", f"Ids got saved to: {path_script}/Audio/ids.txt")
                else:
                    cprint("red", "!", "Failed to save Ids.")
                                
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 14:
        clr()
        print(banner)
        separator()
        title_message("Robux Calculator")
        cprint("green", ">", "Input ROBUX Amount:")
        robux_amount = int(input("> "))
        tax = 70
        calc = (tax * robux_amount) / 100.0
        price_it_for = robux_amount / 0.7
        
        separator()
        cprint("green", "!", f"After Tax: {int(calc)}")
        cprint("green", "!", f"Price It For: {int(price_it_for)}")

        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 15:
        clr()
        print(banner)
        separator()
        title_message("Robux History")

        cprint("green", ">", f"Getting Robux History")
        
        amount_of_robux = 0
        cursor = ''
        while cursor != None:
            response = session.get(f"https://economy.roblox.com/v2/users/{userid}/transactions?transactionType=Purchase&limit=100&cursor={cursor}", proxies=GetProxy())
            if response.ok:
                data = response.json()
                if not data["data"] == []:
                    cprint("green", ">", f'Found {len(data["data"])} Purchases!')
                    for robux in data['data']:
                        if robux['currency']['type'] == 'Robux':
                            amount_of_robux += robux['currency']['amount']
                    cursor = data['nextPageCursor']
            else:
                cprint("yellow", "!", f'Rate Limit! Waiting 10 Seconds.')
                time.sleep(10)

        separator()
        cprint(msg=f"User has spent {amount_of_robux} ROBUX since the accounts creation.")

        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)
    elif option == 16:
        clr()
        print(banner)
        separator()
        title_message("Mass Group Excile")
        cprint("green", ">", "Please put groupID here")
        groupid = int(input("> "))

        def check_group_exists(group_id):
            cprint(msg="Checking If ROBLOX Group Exists")
            url = f"https://groups.roblox.com/v2/groups?groupIds={group_id}"
            response = requests.get(url, proxies=GetProxy()) # type: ignore
            if response.ok:
                data = response.json()
                groups = data["data"]
                for group in groups:
                    if group["id"] == group_id:
                        return True
                    return False
                
        def getToken():
            response = requests.post(
                "https://auth.roblox.com/v2/logout", cookies=cookies
            )
            return response.headers["x-csrf-token"]
        
        members = []    
        if check_group_exists(groupid):
            cursor = ''
            while cursor != None:
                response = session.get(f'https://groups.roblox.com/v1/groups/{groupid}/users?cursor={cursor}&limit=100&sortOrder=Desc', proxies=GetProxy())

                if response.ok:
                    data = response.json()
                    target_userid = data['user']['userId']

                    if target_userid != userid:
                        members.append(target_userid)

                    cursor = data['nextPageCursor']
            
            for target_id in members:
                excile_user = session.delete(f'https://groups.roblox.com/v1/groups/{groupid}/users/{target_id}', headers={"x-csrf-token": getToken()}, proxies=GetProxy())
                if excile_user.ok:
                    cprint(msg=f"Kicked User With Id: {target_id}")
        
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)
    elif option == 17:
        clr()
        print(banner)
        separator()
        title_message("Account Nuker")
        cprint("red", "!", "Are you sure you wanna nuke this account?")
        anwser = str(input("Y/N > "))
        if anwser.lower() == "y": 
            session.patch("https://accountsettings.roblox.com/v1/themes/user", headers=func_headers, data={"themeType": "Light"}, proxies=GetProxy())
            session.post("https://locale.roblox.com/v1/locales/set-user-supported-locale", headers=func_headers, data={"supportedLocaleCode": "th_th"}, proxies=GetProxy())
            session.post("https://www.roblox.com/account/settings/account-restrictions?isEnabled=true", headers=func_headers, proxies=GetProxy())
            session.post("https://notifications.roblox.com/v2/notifications/notification-preferences", headers=func_headers, data = {"updatedPreferences": [{"notificationType": "MarketingEmails", "notificationChannel": "Email", "preferenceStatus": "All"}]}, proxies=GetProxy())
            cprint("green", "!", "Finished!")
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 18:
        clr()
        print(banner)
        separator()
        title_message("Discord")

        discord_invites = requests.get("https://raw.githubusercontent.com/Damix-hash/roblox-stuff/main/invites.txt").text

        random_invites = []
        for invites in discord_invites.split("\n"):
            random_invites.append(base64_decode(invites))

        invite = random.choice(random_invites)

        cprint("red", "!", f"Joining selfblox: https://discord.gg/{invite}")

        url = 'http://127.0.0.1:6463/rpc?v=1'

        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://discord.com'
        }

        data = {
            'cmd': 'INVITE_BROWSER',
            'nonce': str(uuid.uuid4()),
            'args': {'code': str(invite)}
        }

        response = requests.post(url, headers=headers, json=data)

        if response.ok:
            cprint("green", ">", "Successfully Requested Invitation")
        else:
            cprint("red", "!", "Could't Request Invitation. Try Joining By Entering Invite Yourself.")
        input("Press ENTER To Continue.")
        option_picker(session, userid, username, cookie)

    elif option == 19:
        clr()
        print(banner)
        separator()
        title_message("Account Switcher")
        cprint("red", "!", "What would you like to do?")
        cprint("red", "1", "Save Cookie")
        cprint("red", "2", "LogOut")
        cprint("red", "3", "Login With Cookie")
        cprint("red", "4", "Changed My Mind")

        acc_option = int(input("> "))
        silly_cookie = cookie.replace(warning_tag, "")
        encoded_cookie = base64_encode(silly_cookie)

        if acc_option == 1:
            if not os.path.exists(f"SelfBLOX/Accounts/{username}"):
                os.mkdir(f"SelfBLOX/Accounts/{username}")
                with open(f"SelfBLOX/Accounts/{username}/{username}.txt", "w", encoding="utf-8") as save_acc_cookie:
                    save_acc_cookie.write(encoded_cookie)
            else:
                with open(f"SelfBLOX/Accounts/{username}/{username}.txt", "w", encoding="utf-8") as save_acc_cookie:
                    save_acc_cookie.write(encoded_cookie)
            cprint(msg=f"Successfully Saved Cookie To: SelfBLOX/Accounts/{username}/{username}.txt")
            input("Press ENTER To Continue.")
            option_picker(session, userid, username, cookie)

        if acc_option == 2:
            cprint("red", "!", "Pick Which account you would like to login to?")
            cprint("red", "!", "Don't write number just username. Can be shortened!")

            acc_num = 1
            for account in os.listdir("SelfBLOX/Accounts"):
                if os.path.exists(f"SelfBLOX/Accounts/{account}/{account}.txt") and os.path.getsize(f"SelfBLOX/Accounts/{account}/{account}.txt") > 0:
                    if account == username:
                            cprint("red", str(acc_num), f"{account} [CURRENT]")
                    else:
                        cprint("red", str(acc_num), account)
                    acc_num += 1
            acc_pick = str(input("> "))

            for account in os.listdir("SelfBLOX/Accounts"):
                if account.startswith(acc_pick.lower()) or account.startswith(acc_pick.upper()):
                    clr()
                    print(banner)
                    separator()
                    cprint("green", "!", f"Logging To: {account}")
                    session.close()
                    with open(f"SelfBLOX/Accounts/{account}/{account}.txt", "r", encoding="utf-8") as read_cookie:
                        base_cookie = read_cookie.read()
                        decoded_cookie = base64_decode(base_cookie)
                        cookie = warning_tag + decoded_cookie

                    with open("SelfBLOX/cookie.txt", "w", encoding="utf-8") as login_cookie:
                        login_cookie.write(encoded_cookie)
                    main_setup(decoded_cookie)

        elif acc_option == 3:
            clr()
            print(banner)
            separator()
            new_input_cookie = str(input("Put new cookie: "))
            if new_input_cookie != '' or new_input_cookie != None:
                session.close()
                new_cookie = new_input_cookie.replace(warning_tag, "")
                encoded_cookie = base64_encode(new_cookie)
                    
                with open("SelfBLOX/cookie.txt", "w", encoding="utf-8") as login_cookie:
                    login_cookie.write(encoded_cookie)
                    
                main_setup(new_input_cookie)
            else:
                option_picker(session, userid, username, cookie)

        elif acc_option == 4:
            option_picker(session, userid, username, cookie)

    elif option == 20:
        cprint("red", "?","Are you sure? Y/N")
        leave_anwser = str(input("> "))
        if leave_anwser.lower() == "y":
            exit()
        else:
            option_picker(session, userid, username, cookie)

    else:
        cprint("red", "!", "Invalid option. Please choose a valid option.\n")
        input("Press ENTER To Continue.")
        
    option_picker(session, userid, username, cookie)

def main_setup(roblox_cookie):
    clr()
    if roblox_cookie and roblox_cookie.strip() and roblox_cookie.lower() != "none":
        title_message("Loading")
        print(banner)
        separator()
        print("Loading...")
        with requests.Session() as session:
            session.cookies.set(".ROBLOSECURITY", roblox_cookie)
            session.headers.update({"referer": "https://www.roblox.com"})

            try:
                response = session.get("https://www.roblox.com/mobileapi/userinfo")
                response.raise_for_status()
            except requests.RequestException as e:
                cprint("red", "!", "ROBLOX Cookie Didn't Work!")
                cprint("red", "!", "Please Check If Cookie Is Correct.")
                with open("SelfBLOX/previous-cookie.txt", "w", encoding="utf-8") as previous_cookie:
                    previous_cookie.write(roblox_cookie)
                cprint(msg="The Old Cookie Was Placed In previous-cookie.txt")
                cprint("red", "!", "Please put new cookie here:")
                new_cookie = str(input("> "))
                main_setup(new_cookie)
            else:
                user_data = response.json()
                username = user_data["UserName"]
                userid = user_data["UserID"]
                option_picker(session, userid, username, roblox_cookie)
                
    else:
        title_message("Login")
        print(banner)
        separator()
        welcome_print()
        cprint(msg="Hello! Please input your ROBLOX cookie below!")
        cookie = str(input("ROBLOX Cookie: "))
        new_cookie = cookie.replace(warning_tag, "")
        base_cookie = base64_encode(new_cookie)
        with open("SelfBLOX/cookie.txt", "w", encoding="utf-8") as save_cookie:
            save_cookie.write(base_cookie)
        main_setup(cookie)

if __name__ == "__main__":
    main_setup(cookie)
else:
    input("Some Unknown Issue Has Happened. Press ENTER To Leave!")
    exit()