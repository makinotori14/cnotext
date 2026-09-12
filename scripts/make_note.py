from pathlib import Path
import subprocess
import sys

def get_img():
    num = 1
    while True:
        answer = input(
            "Хотите ли вы вставить фото из буфера обмена? (y/n, def=y): "
        ).strip().lower()

        if answer in ("", "y"):
            TEMP_DIR = Path(__file__).resolve().parents[1] / "temp"
            TEMP_DIR.mkdir(exist_ok=True)

            subprocess.run(["pngpaste", TEMP_DIR / f"{num:02d}.png"])
            num += 1
            continue
        return


def main():
    get_img()
    
    project_root = Path(__file__).resolve().parents[1]
    logic_script = project_root / "src" / "logic.py"
    subprocess.run(
        [sys.executable, str(logic_script)],
        check=True,
        cwd=project_root,
    )

if __name__ == "__main__":
    main()
