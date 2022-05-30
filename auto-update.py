import requests
import os
import urllib.request
import colorama
from colorama import Fore
import time

colorama.init()


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


link = "https://raw.githubusercontent.com/madkarmaa/Raid-Bot/main/bot.py"
f = requests.get(link)
onlineResult = f.text

with open("bot.py", "r") as original:
    originalResult = original.read()
    original.close()

if onlineResult == originalResult:
    exit()
else:
    print(Fore.YELLOW +
          'An update for "bot.py" has been found. Do you want to download it?' + Fore.RESET)
    confirm = input("(Y/N): ")
    if confirm.lower() in ["yes", "y", "true"]:
        urllib.request.urlretrieve(link, "bot.py")
        print(Fore.GREEN + "Update successfully downloaded.")
        time.sleep(3.0)
        clearConsole()
        exit()
    elif confirm.lower() in ["no", "n", "false"]:
        clearConsole()
        exit()
    else:
        print(Fore.RED + "Error. Loading current version...")
        time.sleep(3.0)
        clearConsole()
        exit()
