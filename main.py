#!/usr/bin/env python3

from colorama import Fore, init
import subprocess
import sys
import os

init(autoreset=True)

Warning = Fore.RED + "[!]" + Fore.RESET
Success = Fore.GREEN + "[+]" + Fore.RESET
Error = Fore.RED + "[-]" + Fore.RESET
Info = Fore.BLUE + "[*]" + Fore.RESET


def display_banner() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.CYAN + f"""
    ██████   ██████ █████ ███████████ ██████   ██████              █████████   ███████████ ███████████   █████████     █████████  █████   ████ 
    ░░██████ ██████ ░░███ ░█░░░███░░░█░░██████ ██████              ███░░░░░███ ░█░░░███░░░█░█░░░███░░░█  ███░░░░░███   ███░░░░░███░░███   ███░ 
    ░███░█████░███  ░███ ░   ░███  ░  ░███░█████░███             ░███    ░███ ░   ░███  ░ ░   ░███  ░  ░███    ░███  ███     ░░░  ░███  ███    
    ░███░░███ ░███  ░███     ░███     ░███░░███ ░███  ██████████ ░███████████     ░███        ░███     ░███████████ ░███          ░███████     
    ░███ ░░░  ░███  ░███     ░███     ░███ ░░░  ░███ ░░░░░░░░░░  ░███░░░░░███     ░███        ░███     ░███░░░░░███ ░███          ░███░░███    
    ░███      ░███  ░███     ░███     ░███      ░███             ░███    ░███     ░███        ░███     ░███    ░███ ░░███     ███ ░███ ░░███   
    █████     █████ █████    █████    █████     █████            █████   █████    █████       █████    █████   █████ ░░█████████  █████ ░░████ 
    ░░░░░     ░░░░░ ░░░░░    ░░░░░    ░░░░░     ░░░░░            ░░░░░   ░░░░░    ░░░░░       ░░░░░    ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░ 
    
        ╔═════════════════════════════════════════════════════╗
        ║ Github: https://github.com/DenisEx8l0it             ║
        ║ Created: DenisEx8l0it                               ║
        ║ version: 2.0                                        ║
        ╚═════════════════════════════════════════════════════╝
    """)


def check_sudo() -> None:
    if os.geteuid() != 0:
        print(f"{Error} Этот скрипт требует права root!")
        sys.exit(1)


def show_menu() -> None:
    print(f"\n{Info} ВЫБЕРИТЕ ТИП АТАКИ:")
    print(f"{Warning} 1 - ARP Spoofing")
    print(f"{Warning} 2 - Denial Of Service (DoS)") 
    print(f"{Warning} 0 - Выход")
    
    print(f"{Info} <-- Только для образовательных целей! -->")


def launch_arp_spoofing() -> None:
    if os.path.exists('ARP-Spoofing/ARP.py'):
        print(f"{Success} Запуск ARP Spoofing...")
        subprocess.run([sys.executable, 'ARP-Spoofing/ARP.py'])
    else:
        print(f"{Error} Файл arp-spoofing.py не найден!")
        print(f"{Info} Создайте файл arp-spoofing.py для ARP атак")


def launch_dos_attack() -> None:
    if os.path.exists('DoS-Attack/DoS.py'):
        print(f"{Success} Запуск DoS Attack...")
        subprocess.run([sys.executable, 'DoS-Attack/DoS.py'])
    else:
        print(f"{Error} Файл DoS.py не найден!")
        print(f"{Info} Создайте файл DoS.py для Denial Of Service атак...")


def main() -> None:
    check_sudo()
    
    while True:
        display_banner()
        show_menu()
        
        choice = input(f"\n{Info} Выберите опцию [0-2]: ").strip()
        
        if choice == '1':
            launch_arp_spoofing()
        elif choice == '2':
            launch_dos_attack()
        elif choice == '0':
            print(f"\n{Success} Выход из программы...")
            break
        else:
            print(f"{Error} Неверный выбор! Введите 0, 1 или 2")
        
        input(f"\n{Info} Нажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"{Error} Ошибка: {e}")