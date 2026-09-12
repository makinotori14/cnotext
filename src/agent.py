import subprocess

def make_query(repo_path):
    PROMPT = f"""
Создай LaTeX-конспект по предоставленным исходным материалам.

Следуй инструкциям проекта.
Используй lib/tex/lectures или lib/tex/seminars только как
структурный референс, а конкретные элементы выбирай из bricks.

Изображения хранятся temp/
.tex и .pdf должны быть в {repo_path}
"""
    subprocess.run([
        "opencode",
        "run",
        PROMPT,
    ], check=True)