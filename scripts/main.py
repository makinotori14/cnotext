import subprocess
import sys
from pathlib import Path

def print_menu():
    subprocess.run(["clear"])
    logo = """
                                             ██                                       
        ▓████████████████████████          ██████                                █    
      ▓██████████████████████████         ██████                                ██    
    ▓███████                ▓█████████████████████████████████████████████████████████
  ███████                                 ▓████                             █████     
 ▓█████        █████████     █████████    ▓███      ████████  ████    █████ ▓██████   
▓█████       ████████████  ████████████  ▓████   ██████ ▓████   █████████    ▓███     
██████       █████  ▓███  █████  ▓████  ▓████    ████████████    ▓█████     █████     
██████      █████   ▓███  █████  ▓████  █████   █████          ▓███████     █████     
▓███████    ████▒  ████   ██████████   ████████ ▓██████████  █████▒▒████    ▓██████   
▒▒███████████ ▒▒░  █░▒▒   ░▒██████     ░▒████▒  ░▒████████   ▓██▒ ░▒▒█████  ▒▓████▒   
 ░▒█████████   ▒      ▒    ░  ▒▒░       ░▒▒▒ ░  ░░░▒▒▒▒▒     ▒░▒▒   ░▒░░    ░ ▒▒▒ ░   
 ▒   ▒▒░  ▒    ░      ░       ▒ ░       ░░ ▒    ░   ▒  ░       ▒░             ░▒▒ ░   
 ░  ░▒ ░▒ ░                   ░            ░        ░          ░               ░      
    ▒░ ▒                                                                              
     ░                     +--------------------------------+                         
     █████████████████▓▒░  |bby, did u 4get 2 take ur notes?| ░▒▓█████████████████    
                           +--------------------------------+                         
"""
    menu = """
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
.-----------------------.
|0. Install (MacOS only)|
|1. Make Note           |
|2. Settings            |
|3. Exit                |
'-----------------------'
"""
    print(logo)
    print(menu)

def get_cmd():
    while True:
        cmd = input()
        if cmd in ["0", "1", "2", "3"]:
            return int(cmd)

        print("Такой команды нет =)")

def opencode_auth():
    subprocess.run(["opencode", "auth", "login"])

def tex_install():
    subprocess.run(["sudo", "tlmgr", "update", "--self", "--all"])
    doctor_script = Path(__file__).with_name("doctor.py")
    try:
        subprocess.run([sys.executable, doctor_script, "--tex"], check=True)
        print("Все успешно установлено")
        return 0
    except:
        print("Установите вручную не найденные компоненты.")
        input()
        return 1

def core_install():
    doctor_script = Path(__file__).with_name("doctor.py")
    try:
        subprocess.run([sys.executable, doctor_script, "--core"], check=True)
        print("Все успешно установлено")
        return 0
    except:
        print("Установите вручную не найденные компоненты.")
        input()
        return 1

def install():
    if (core_install()):
        return
    
    if (tex_install()):
        return

    opencode_auth()


def make_note():
    note_script = Path(__file__).with_name("make_note.py")
    subprocess.run([sys.executable, note_script], check=True)

def settings():
    pass

def main():
    while True:
        subprocess.run(["clear", ])
        print_menu()
        cmd = get_cmd()
        if cmd == 0:
            install()
        elif cmd == 1:
            make_note()
        elif cmd == 2:
            settings()
        elif cmd == 3:
            break
    

if __name__ == "__main__":
    main()
