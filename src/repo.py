from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = PROJECT_ROOT / "notes"

REFERENCE_DIRS = {
    "lec": "lectures",
    "sem": "seminars",
}


def reference_dir(repo_dir, refstr):
    """Return the lectures/seminars directory for a reference prefix."""
    try:
        directory_name = REFERENCE_DIRS[refstr]
    except KeyError as error:
        raise ValueError("refstr должен быть 'lec' или 'sem'") from error

    return repo_dir / directory_name


def note_dir(repo_dir, refstr, number):
    return reference_dir(repo_dir, refstr) / f"{refstr}{number:02d}"


def make_repo(notes_dir=NOTES_DIR):
    """Ask for note parameters, create its directory and return its path."""
    name, refstr, number = ask_info(notes_dir)
    destination = note_dir(Path(notes_dir) / name, refstr, number)

    # exist_ok=False also protects against a directory appearing between the
    # validation in ask_info() and its creation here.
    destination.mkdir(parents=True, exist_ok=False)
    return destination


def find_next(refstr, repo_dir=PROJECT_ROOT):
    """Return one more than the greatest existing lecNN/semNN number."""
    directory = reference_dir(Path(repo_dir), refstr)
    pattern = re.compile(rf"^{re.escape(refstr)}(\d+)$")
    numbers = []

    if directory.is_dir():
        for path in directory.iterdir():
            match = pattern.fullmatch(path.name)
            if path.is_dir() and match:
                numbers.append(int(match.group(1)))

    return max(numbers, default=0) + 1


def ask_name():
    while True:
        name = input("Название репозитория: ").strip()

        # name must be one directory component, otherwise it could escape
        # notes/ or silently create an unexpected nested hierarchy.
        if name and name not in {".", ".."} and Path(name).name == name:
            return name

        print("Название должно быть непустым именем папки без '/'.")


def ask_reference():
    while True:
        reference = input("Тип конспекта — лекция или семинар? (l/s): ").strip().lower()
        if reference in {"l", "s"}:
            return "lec" if reference == "l" else "sem"

        print("Введите 'l' для лекции или 's' для семинара.")


def ask_info(notes_dir=NOTES_DIR):
    """Read and validate repository name, note type and note number."""
    notes_dir = Path(notes_dir)
    name = ask_name()
    refstr = ask_reference()
    repo_dir = notes_dir / name

    while True:
        raw_number = input("Номер (Enter — следующий свободный): ").strip()

        if not raw_number:
            number = find_next(refstr, repo_dir)
        else:
            try:
                number = int(raw_number)
            except ValueError:
                print("Номер должен быть целым положительным числом.")
                continue

            if number <= 0:
                print("Номер должен быть целым положительным числом.")
                continue

        if note_dir(repo_dir, refstr, number).exists():
            print(f"{refstr}{number:02d} уже существует, введите другой номер.")
            continue

        return name, refstr, number
