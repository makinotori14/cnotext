# `remark`

Замечание, уточнение, ограничение применимости или предупреждение, которое не
является новым определением или доказываемым результатом. По умолчанию блок
ненумерованный: это уменьшает визуальный шум в конспекте.

## Зависимости и подключение

```latex
\usepackage{amsthm}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
\input{lib/tex/bricks/remark/commands.tex}
```

Определены `remark` и более заметное `warning`. Заголовок `remark` можно
заменить необязательным аргументом.

## Примеры

- [`simple.tex`](examples/simple.tex) — обычное замечание;
- [`warning.tex`](examples/warning.tex) — существенное предостережение.
