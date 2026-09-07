import os
import fade
import re
import json
import ipaddress
import requests
import time
import random
from bs4 import BeautifulSoup
from sys import platform
from colorama import Fore, init
from fake_useragent import UserAgent

init()


def logo_main():
    text = """
╔══╗         ╔╗ ╔══╗      ╔╗       
║╔╗║        ╔╝╚╗║╔╗║      ║║       
║╚╝╚╦══╦══╦═╩╗╔╝║╚╝╚╦══╦╗╔╣╚═╦══╦═╗
║╔═╗║ ═╣╔╗║══╣║ ║╔═╗║╔╗║╚╝║╔╗║ ═╣╔╝
║╚═╝║ ═╣╔╗╠══║╚╗║╚═╝║╚╝║║║║╚╝║ ═╣║ 
╚═══╩══╩╝╚╩══╩═╝╚═══╩══╩╩╩╩══╩══╩╝ 
            By un1ucm
 https://t.me/beast_project_team
    """
    print(fade.water(text))


def logo_sms():
    text = """
╔═══╦═╗╔═╦═══╗             
║╔═╗║ ╚╝ ║╔═╗║             
║╚══╣╔╗╔╗║╚══╗╔══╦══╦══╦╗╔╗
╚══╗║║║║║╠══╗║║══╣╔╗║╔╗║╚╝║
║╚═╝║║║║║║╚═╝║╠══║╚╝║╔╗║║║║
╚═══╩╝╚╝╚╩═══╝╚══╣╔═╩╝╚╩╩╩╝
                 ║║        
                 ╚╝        
    """
    print(fade.greenblue(text))


def logo_discord():
    text = """
╔═══╗             ╔╗             
╚╗╔╗║             ║║             
 ║║║╠╦══╦══╦══╦═╦═╝║╔══╦══╦══╦╗╔╗
 ║║║╠╣══╣╔═╣╔╗║╔╣╔╗║║══╣╔╗║╔╗║╚╝║
╔╝╚╝║╠══║╚═╣╚╝║║║╚╝║╠══║╚╝║╔╗║║║║
╚═══╩╩══╩══╩══╩╝╚══╝╚══╣╔═╩╝╚╩╩╩╝
                       ║║        
                       ╚╝        
    """
    print(fade.fire(text))


def logo_email():
    text = """
╔═══╗      ╔╗              
║╔══╝      ║║              
║╚══╦╗╔╦══╦╣║ ╔══╦══╦══╦╗╔╗
║╔══╣╚╝║╔╗╠╣║ ║══╣╔╗║╔╗║╚╝║
║╚══╣║║║╔╗║║╚╗╠══║╚╝║╔╗║║║║
╚═══╩╩╩╩╝╚╩╩═╝╚══╣╔═╩╝╚╩╩╩╝
                 ║║        
                 ╚╝        
    """
    print(fade.purplepink(text))


def logo_ddos():
    text = """
╔═══╦═══╗  ╔═══╗
╚╗╔╗╠╗╔╗║  ║╔═╗║
 ║║║║║║║╠══╣╚══╗
 ║║║║║║║║╔╗╠══╗║
╔╝╚╝╠╝╚╝║╚╝║╚═╝║
╚═══╩═══╩══╩═══╝
    """
    print(fade.brazil(text))


def logo_telegram():
    text = """
╔════╗ ╔╗
║╔╗╔╗║ ║║
╚╝║║╠╩═╣║╔══╦══╦═╦══╦╗╔╗╔══╦══╦══╦╗╔╗
  ║║║ ═╣║║ ═╣╔╗║╔╣╔╗║╚╝║║══╣╔╗║╔╗║╚╝║
  ║║║ ═╣╚╣ ═╣╚╝║║║╔╗║║║║╠══║╚╝║╔╗║║║║
  ╚╝╚══╩═╩══╩═╗╠╝╚╝╚╩╩╩╝╚══╣╔═╩╝╚╩╩╩╝
            ╔═╝║           ║║
            ╚══╝           ╚╝
    """
    print(fade.greenblue(text))


def logo_settings():
    text = """
╔═══╗  ╔╗ ╔╗           
║╔═╗║ ╔╝╚╦╝╚╗          
║╚══╦═╩╗╔╩╗╔╬╦═╗╔══╦══╗
╚══╗║ ═╣║ ║║╠╣╔╗╣╔╗║══╣
║╚═╝║ ═╣╚╗║╚╣║║║║╚╝╠══║
╚═══╩══╩═╝╚═╩╩╝╚╩═╗╠══╝
                ╔═╝║   
                ╚══╝   
    """
    print(fade.greenblue(text))


def logo_bruteforce():
    text = """
╔╦╦═╦╗╔═╗╔═╦═╗
║║║║║║║╔╝║║║║
║║║║║║║╚═╣║║║
╚══╩══╩╝══╩══╝
    """
    print(fade.purplepink(text))


def logo_proxies():
    text = """
╔╗ ╔╗    ╔╗  ╔╗
║║ ║║    ║║ ╔╝╚╗
║║ ║╠══╦═╝╠═╩╗╔╬╦═╗╔══╗╔══╦═╦══╦╗╔╦╦══╦══╗
║║ ║║╔╗║╔╗║╔╗║║╠╣╔╗╣╔╗║║╔╗║╔╣╔╗╠╬╬╬╣ ═╣══╣
║╚═╝║╚╝║╚╝║╔╗║╚╣║║║║╚╝║║╚╝║║║╚╝╠╬╬╣║ ═╬══║
╚═══╣╔═╩══╩╝╚╩═╩╩╝╚╩═╗║║╔═╩╝╚══╩╝╚╩╩══╩══╝
    ║║             ╔═╝║║║
    ╚╝             ╚══╝╚╝
    """
    print(fade.pinkred(text))


def menu_en():
    text = """[0] Exit          
[1] Beast Mode (DDoS)      
[2] Image Logger   
[3] Brute Force
[4] SMS spam
[5] Email spam 
[6] Telegram spam
[7] Discord spam 
[8] Return to Main Menu      
    """
    print(fade.purplepink(text))


def menu_ru():
    text = """[0] Выход        
[1] Beast Mode (DDoS)     
[2] Image Logger   
[3] Брутфорс
[4] СМС спам     
[5] Email спам   
[6] Telegram спам
[7] Discord спам 
[8] Вернуться в главное меню    
    """
    print(fade.purplepink(text))


def settings_menu_ru():
    text = """[0] Назад        
[1] Сменить язык
[2] Очистить кэш
        """
    print(fade.purplepink(text))


def settings_menu_en():
    text = """[0] Back        
[1] Change language
[2] Clear cache
        """
    print(fade.purplepink(text))


def validate_ip(ip):
    try:
        parts = list(map(int, ip.split('.')))
        return len(parts) == 4 and all(0 <= p <= 255 for p in parts)
    except ValueError:
        return False


def validate_port(port):
    return str(port).isdigit() and 1 <= int(port) <= 65535


def update_proxies():
    return


def logo_proxies():
    return


def get_lang():
    try:
        js_file = ''
        with open(os.path.abspath('core/config.json'), 'r') as file:
            for line in file:
                js_file += str(line)

        return json.loads(js_file)["language"]
    except:
        return 'en'


def get_proxies():
    return []


def generate_email():
    lib = 'qwertyuiopasdfhgjklzxcvbnm'
    lib2 = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@yandex.ru']
    email = ''.join(random.choice(lib) for _ in range(random.randint(10, 25))) + random.choice(lib2)
    return email


def randstr(str_len):
    lib = '1234567890qwertyuiopasdfghjklzxcvbnm'
    text = ''.join(random.choices(lib, k=str_len))
    return text


def get_discord_tokens():
    tokens = []
    lang = get_lang()

    try:
        with open(os.path.abspath('core/input/discord_tokens.txt'), 'r') as file:
            for line in file:
                tokens.append(line.replace('\n', ''))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке открыть файл core/input/discord_tokens.txt')
        else:
            print(Fore.RED + '\nError when trying to open a file core/input/discord_tokens.txt')

    return tokens


def get_telegram_accounts():
    lang = get_lang()
    accounts = []

    try:
        accounts = os.listdir(os.path.abspath('core/input/telegram_accounts'))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке получить Telegram аккаунты из core/input/telegram_accounts')
        else:
            print(Fore.RED + '\nError when trying to retrieve Telegram accounts from core/input/telegram_accounts')

    return accounts


def get_email_accounts():
    emails = []
    lang = get_lang()

    try:
        with open(os.path.abspath('core/input/email_accounts.txt'), 'r') as file:
            for line in file:
                emails.append(line.replace('\n', ''))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке открыть файл core/input/email_accounts.txt')
        else:
            print(Fore.RED + '\nError when trying to open a file core/input/email_accounts.txt')

    return emails


def change_language():
    lang = get_lang()
    js_file = os.path.abspath('core/config.json')
    with open(os.path.abspath(js_file)) as file:
        js = json.load(file)

    if lang == "ru":
        js["language"] = "en"
        with open(os.path.abspath('core/config.json'), 'w') as file:
            json.dump(js, ensure_ascii=False, indent=4, fp=file)

    else:
        js["language"] = "ru"
        with open(os.path.abspath('core/config.json'), 'w') as file:
            json.dump(js, ensure_ascii=False, indent=4, fp=file)

