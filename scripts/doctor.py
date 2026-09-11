from shutil import which
import time
import subprocess

from packages import SRC

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

def main():
    exit_code = 0

    missing = []

    for command in SRC:
        if which(command):
            print_status(command, 0)
        else:
            download_process = subprocess.Popen(
                SRC[command].split(),
                stdout=subprocess.PIPE,
            )
            install_process = subprocess.Popen(
                ["bash"],
                stdin=download_process.stdout,
            )
            download_process.stdout.close()

            while (install_process.poll() is None):
                print_status(command, 1)

            download_process.wait()

            if download_process.returncode or install_process.returncode or not which(command):
                print(f"[-] {command}")
                missing.append(command)
            else:
                print_status(command, 1)
    
    if len(missing) > 0:
        print(f"Не удалось установить:", *missing)
        exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
