# `problem`

Условие задачи, упражнения или вопроса. Сохраняйте исходный номер, подпункты,
данные и формулировку; решение размещайте отдельным кирпичиком `solution`.

## Зависимости и подключение

```latex
\usepackage{amsthm}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\usepackage{enumitem}
\input{lib/tex/bricks/problem/commands.tex}
```

`problem` нумеруется внутри раздела и принимает необязательное название.
`taskparts` оформляет подпункты как `(a)`, `(b)`, … . Чтобы сохранить внешний
номер источника, используйте `\tagproblem{<номер>}{<условие>}`.

## Примеры

- [`simple.tex`](examples/simple.tex) — обычная задача;
- [`numbered.tex`](examples/numbered.tex) — исходный номер и подпункты.
