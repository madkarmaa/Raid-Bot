import requests
import urllib.request
import colorama
from colorama import Fore
import time

colorama.init()

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
          'An update for the bot has been found. Do you want to download it?' + Fore.RESET)
    confirm = input("(Y/N): ")
    if confirm.lower() in ["yes", "y", "true"]:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/madkarmaa/Raid-Bot/main/bot.py", "bot.py")
        print(Fore.GREEN + "Update successfully downloaded.")
        exit()
    elif confirm.lower() in ["no", "n", "false"]:
        exit()
    else:
        print(Fore.RED + "Error")
        time.sleep(2.0)
        exit()
