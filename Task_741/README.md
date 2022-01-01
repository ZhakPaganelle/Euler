##Binary grid colouring


Let $f(n)$ be the number of ways an $n\times n$ square grid can be coloured, each cell either black or white, such that each row and each column contains exactly two black cells.
For example, $f(4)=90$, $f(7) = 3110940$ and $f(8) = 187530840$.


Let $g(n)$ be the number of colourings in $f(n)$ that are unique up to rotations and reflections.
You are given $g(4)=20$, $g(7) = 390816$ and $g(8) = 23462347$ giving $g(7)+g(8) = 23853163$.


Find $g(7^7) + g(8^8)$. Give your answer modulo $1\,000\,000\,007$.

##Раскрашивание двоичной сетки


Пусть $f(n)$ будет количеством способов, как можно раскрасить каждую ячейку квадратной сетки $n\times n$ в белый или черный цвет, так чтобы каждый ряд и столбец содержали ровно две черные ячейки.
Например, $f(4)=90$, $f(7) = 3110940$ и $f(8) = 187530840$.


Пусть $g(n)$ будет количеством способов раскраски в $f(n)$, которые уникальны с точностью до зеркальных отражений и поворотов.
Известно, что $g(4)=20$, $g(7) = 390816$ и $g(8) = 23462347$. Значит, $g(7)+g(8) = 23853163$.


Найдите $g(7^7) + g(8^8)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
