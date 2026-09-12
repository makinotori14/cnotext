# `tree`

Корневое иерархическое дерево: классификация, разбор случаев, структура
объекта. В отличие от `graph`, здесь важны корень, уровни и отношение
«родитель—потомок». Для вероятностей на ветвях используйте
`probability-tree`.

## Зависимости

```latex
\usepackage{tikz}
\usetikzlibrary{trees,positioning}
\input{lib/tex/bricks/tree/commands.tex}
```

Используйте синтаксис `child` и задавайте расстояния уровнями, а не отдельными
абсолютными координатами. `tree node` подходит для содержательных узлов,
`edge from parent` задаёт связи.

## Примеры

- [`classification.tex`](examples/classification.tex) — дерево классификации;
- [`binary.tex`](examples/binary.tex) — компактное бинарное дерево.
