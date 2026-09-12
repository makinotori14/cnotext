# `coordinate-system`

Координатный рисунок, где главные объекты — оси, точки, векторы, области или
геометрические ограничения. Для точного графика функции используйте
`function-plot`; для евклидовой конструкции с углами и длинами — `geometry`.

## Зависимости

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta,patterns}
\input{lib/tex/bricks/coordinate-system/commands.tex}
```

`coordinate axes` оформляет оси со стрелками. Масштаб и диапазон должны
показывать все значимые объекты без лишнего пустого пространства. Подписи
точек смещайте относительно узлов, а не ручными пробелами.

## Примеры

- [`points.tex`](examples/points.tex) — точки и вектор;
- [`region.tex`](examples/region.tex) — заштрихованная область неравенств.
