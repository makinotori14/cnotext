# `flowchart`

Алгоритм, процедура или процесс с направлением выполнения. Используйте
стандартные формы: терминатор для начала/конца, прямоугольник для действия,
ромб для решения. Для математического отображения объектов лучше `diagram`
или `commutative-diagram`.

## Зависимости

```latex
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning}
\input{lib/tex/bricks/flowchart/commands.tex}
```

У ромба подписывайте исходящие ветви (`yes`/`no` или текст источника).
Избегайте пересечений и абсолютного позиционирования. Для длинного текста
увеличивайте `text width`, а не уменьшайте весь рисунок.

## Примеры

- [`linear.tex`](examples/linear.tex) — линейный процесс;
- [`decision.tex`](examples/decision.tex) — ветвление и цикл.
