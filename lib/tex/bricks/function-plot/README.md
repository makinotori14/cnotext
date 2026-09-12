# `function-plot`

График функции по формуле или точкам с математически значимыми осями,
масштабом и областью определения. Используйте `pgfplots`, когда нужна система
координат и корректное преобразование данных; для схематичной кривой без
числового масштаба подходит `coordinate-system` на чистом TikZ.

## Зависимости

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\input{lib/tex/bricks/function-plot/commands.tex}
```

`function axis` задаёт нейтральные оси и сетку. Всегда задавайте разумные
`domain`, `xmin/xmax`, `ymin/ymax`; у разрывов рисуйте отдельные участки, чтобы
PGFPlots не соединял их ложной линией.

## Примеры

- [`function.tex`](examples/function.tex) — гладкая функция;
- [`piecewise.tex`](examples/piecewise.tex) — кусочный график;
- [`points.tex`](examples/points.tex) — экспериментальные точки.
