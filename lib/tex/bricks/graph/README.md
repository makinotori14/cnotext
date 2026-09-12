# `graph`

Граф в математическом смысле: вершины и рёбра, возможно ориентированные,
взвешенные или помеченные. Если блок описывает процесс, выбирайте `flowchart`;
если связи не являются рёбрами графа — `diagram`.

## Зависимости

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning}
\input{lib/tex/bricks/graph/commands.tex}
```

`graph vertex` задаёт единый вид вершин, `graph edge` — рёбер. Размещайте
вершины относительными координатами, если точное положение не кодирует смысл.
Для петель указывайте `loop above/left/...`; вес ребра ставьте узлом на ребре.

## Примеры

- [`undirected.tex`](examples/undirected.tex) — неориентированный граф;
- [`directed.tex`](examples/directed.tex) — ориентированный граф;
- [`weighted.tex`](examples/weighted.tex) — веса и петля.
