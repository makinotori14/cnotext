import argparse
from shutil import which
import time
import subprocess

from packages import SRC, TEX, TEX_PACKAGES

def print_status(command, status):
    CLEAR = "\r\033[2K"
    LOADING_SLEEP = 0.2

    if status == 0:
        print(f"[✔] {command}")
    elif status == 1:
        print(f"[\] {command}", end="", flush=True)
        time.sleep(LOADING_SLEEP)
        print(CLEAR, end="")
        print(f"[|] {command}", end="", flush=True)
        time.sleep(LOADING_SLEEP)
        print(CLEAR, end="")
        print(f"[/] {command}", end="", flush=True)
        time.sleep(LOADING_SLEEP)
        print(CLEAR, end="")
        print(f"[-] {command}", end="", flush=True)
        time.sleep(LOADING_SLEEP)
        print(CLEAR, end="")
    elif status == 2:
        print(f"[✘] {command}")

def check_core_packages():
    exit_code = 0
    missing = []

    for command, install_command in SRC.items():
        if which(command):
            print_status(command, 0)
        else:
            install_process = subprocess.Popen(
                install_command.split(),
            )

            install_process.wait()

            if install_process.returncode or not which(command):
                print_status(command, 2)
                missing.append(command)
            else:
                print_status(command, 0)
    
    if len(missing) > 0:
        print(f"Не удалось установить:", *missing)
        exit_code = 1

    return exit_code


def is_tex_file_installed(filename):
    result = subprocess.run(
        ["kpsewhich", filename],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def check_tex_packages():
    if not which("kpsewhich"):
        print("Не найдена команда kpsewhich. Сначала установите BasicTeX.")
        return 1

    exit_code = 0
    missing = []

    for filename, package in TEX_PACKAGES.items():
        if is_tex_file_installed(filename):
            print_status(filename, 0)
            continue

        install_command = TEX.get(package)
        if install_command is None:
            print_status(filename, 2)
            print(f"Не найдена команда установки для пакета {package}.")
            missing.append(filename)
            continue

        install_process = subprocess.Popen(install_command.split())
        install_process.wait()

        if install_process.returncode or not is_tex_file_installed(filename):
            print_status(filename, 2)
            missing.append(filename)
        else:
            print_status(filename, 0)

    if missing:
        print("Не удалось установить:", *missing)
        exit_code = 1

    return exit_code


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--core",
        action="store_true",
        help="проверить и установить основные зависимости",
    )
    parser.add_argument(
        "--tex",
        action="store_true",
        help="проверить и установить TeX-зависимости",
    )
    
    args = parser.parse_args()

    exit_code = 0
    if args.core:
        exit_code |= check_core_packages()
    if args.tex:
        exit_code |= check_tex_packages()

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
