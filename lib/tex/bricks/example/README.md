# `example`

Разобранный пример, иллюстрация правила или контрпример. Он не заменяет
`problem`: пример объясняет идею, а задача формулирует действие для решения.

## Зависимости и подключение

```latex
\usepackage{amsthm}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\input{lib/tex/bricks/example/commands.tex}
```

Окружения `example` и `counterexample` принимают необязательный заголовок и
могут разрываться между страницами. Если внутри есть длинное решение,
используйте отдельный `solution`.

## Примеры

- [`worked.tex`](examples/worked.tex) — вычислительный пример;
- [`counterexample.tex`](examples/counterexample.tex) — контрпример.
