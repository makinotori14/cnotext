# `theorem`

Формальные теоремы, леммы и следствия. Кирпичик нужен, когда утверждение имеет
самостоятельный статус, может иметь имя, номер, доказательство или ссылку.
Для наблюдений без доказательного статуса используйте `remark`.

## Зависимости и интерфейс

```latex
\usepackage{amsthm}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\input{lib/tex/bricks/theorem/commands.tex}
```

Определены окружения `theorem`, `lemma`, `corollary`; они используют общий
счётчик внутри раздела. Необязательный аргумент задаёт имя результата.
Метка располагается после `\begin{...}`.

## Примеры

- [`theorem.tex`](examples/theorem.tex) — именованная теорема;
- [`lemma.tex`](examples/lemma.tex) — лемма с доказательством;
- [`corollary.tex`](examples/corollary.tex) — следствие и ссылка.
