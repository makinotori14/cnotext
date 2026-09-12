# `probability-tree`

Дерево последовательных случайных событий. Ветви подписываются условными
вероятностями, а листья — исходами или совместными вероятностями. Для обычной
иерархии без вероятностей используйте `tree`.

## Зависимости

```latex
\usepackage{tikz}
\usetikzlibrary{trees,positioning}
\input{lib/tex/bricks/probability-tree/commands.tex}
```

У каждого набора исходящих ветвей проверьте, что вероятности суммируются в
единицу, только если это действительно полный набор исходов в источнике.
Стиль `prob branch` рисует рёбра, а `probability label` размещает вероятность
над ребром на белой подложке. Для подписи снизу добавьте `swap` к узлу
`edge from parent node[probability label]`.

## Примеры

- [`simple.tex`](examples/simple.tex) — один эксперимент;
- [`conditional.tex`](examples/conditional.tex) — два зависимых этапа.
