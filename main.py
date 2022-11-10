import os
import platform
from colorama import Fore

pm = platform.system()
if pm == "Windows":
    os.system("cls")
elif pm == "Linux":
    os.system("clear")
elif pm == "Darwin":
    os.system("clear")
banner = Fore.RED + f"""
                         _____ _         ______ _           _           
                        |_   _| |        |  ___(_)         | |          
                          | | | |__   ___| |_   _ _ __   __| | ___ _ __ 
                          | | | '_ \ / _ \  _| | | '_ \ / _` |/ _ \ '__|
                          | | | | | |  __/ |   | | | | | (_| |  __/ |   
                          \_/ |_| |_|\___\_|   |_|_| |_|\__,_|\___|_|   

                               Github : https://github.com/TanevAZ
"""

print(banner)

def main():
    # ask user for directory to search
    directory = input(f'\n{Fore.RESET}Enter the directory to search : ')
    # ask user for file name to search for
    file = input(f'Enter the file name : {Fore.LIGHTGREEN_EX}')
    # search for file in directory and all subdirectories
    found = False
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name == file:
                print(f'{Fore.RESET}File {Fore.LIGHTGREEN_EX}found(s){Fore.RESET} in : {root}')
                found = True
    if not found:
        print(f'{Fore.RESET}File not {Fore.LIGHTRED_EX}found{Fore.RESET}')
    input(f"\n{Fore.LIGHTGREEN_EX}Scan Terminated. {Fore.WHITE}Press Enter to Exit...")
    exit()

main()