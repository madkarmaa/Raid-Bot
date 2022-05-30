import requests
import os
import urllib.request
import colorama
from colorama import Fore
import time

colorama.init()


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


linkBot = "https://raw.githubusercontent.com/madkarmaa/Raid-Bot/main/bot.py"
linkAuto = "https://raw.githubusercontent.com/madkarmaa/Raid-Bot/main/auto-update.py"
f = requests.get(linkBot)
f2 = requests.get(linkAuto)
onlineResult = f.text
onlineResult2 = f2.text

with open("bot.py", "r") as original:
    originalResult = original.read()
    original.close()

with open("auto-update.py", "r") as original2:
    originalResult2 = original2.read()
    original2.close()

if onlineResult == originalResult and onlineResult2 == originalResult2:
    exit()
if onlineResult != originalResult:
    print(Fore.YELLOW +
          'An update for "bot.py" has been found. Do you want to download it?' + Fore.RESET)
    confirm = input("(Y/N): ")
    if confirm.lower() in ["yes", "y", "true"]:
        urllib.request.urlretrieve(linkBot, "bot.py")
        print(Fore.GREEN + "Update successfully downloaded." + Fore.RESET)
        time.sleep(3.0)
        os.system("python auto-update.py")
        clearConsole()
        exit()
    elif confirm.lower() in ["no", "n", "false"]:
        clearConsole()
        exit()
    else:
        print(Fore.RED + "Error. Loading current version..." + Fore.RESET)
        time.sleep(3.0)
        clearConsole()
        exit()
if onlineResult2 != originalResult2:
    print(Fore.YELLOW +
          'An update for "auto-update.py" has been found. Do you want to download it?' + Fore.RESET)
    confirm = input("(Y/N): ")
    if confirm.lower() in ["yes", "y", "true"]:
        urllib.request.urlretrieve(linkAuto, "auto-update.py")
        print(Fore.GREEN + "Update successfully downloaded." + Fore.RESET)
        time.sleep(3.0)
        os.system("python auto-update.py")
        clearConsole()
        exit()
    elif confirm.lower() in ["no", "n", "false"]:
        clearConsole()
        exit()
    else:
        print(Fore.RED + "Error. Loading current version..." + Fore.RESET)
        time.sleep(3.0)
        clearConsole()
        exit()
