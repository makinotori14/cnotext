# `solution`

Решение задачи: ход рассуждения, вычисления и итог. Используйте после
`problem`; не смешивайте условие с решением, если в источнике они разделены.

## Зависимости и подключение

```latex
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\input{lib/tex/bricks/solution/commands.tex}
```

Окружение `solution` ненумерованное и принимает заголовок. Команда `\answer`
выделяет только явно присутствующий итог. Для цепочек формул комбинируйте с
`derivation`.

## Примеры

- [`short.tex`](examples/short.tex) — короткое решение с ответом;
- [`detailed.tex`](examples/detailed.tex) — пошаговое решение.
