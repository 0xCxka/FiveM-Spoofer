import os
import time
from random import choice
from colorama import Fore

def loading():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "+", end="")
    print(Fore.RESET + " Press Enter to start spoofing FiveM...")
    input()

def spoof():
    os.system("cmd /c netsh advfirewall firewall add rule name='FiveM Spoof' dir=in action=allow protocol=TCP localport=30120")
    os.system("cmd /c netsh advfirewall firewall add rule name='FiveM Spoof' dir=out action=allow protocol=TCP localport=30120")
    print(Fore.GREEN + "\nSpoofing FiveM... Success")

    os.system('cls' if os.name == 'nt' else 'clear')
    start_time = time.time()
    progress = 0
    while progress <= 100:
        bar_length = 30
        filled_length = int(bar_length * progress / 100)
        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        print(f"{Fore.WHITE} Spoofing... [{bar}] {progress}%", end="\r") # WE LOVE CXKA <3
        progress += choice([3, 5, 7, 10])
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(Fore.RED + "+", end="")
    print(Fore.RESET + " Spoofing Complete, Thx for using !")

loading()
spoof()

while True:
    pass
