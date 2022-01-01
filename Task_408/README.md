##Admissible paths through a grid

Let's call a lattice point (x, y) inadmissible if x, y and x + y are all positive perfect squares.
For example, (9, 16) is inadmissible, while (0, 4), (3, 1) and (9, 4) are not.
Consider a path from point (x1, y1) to point (x2, y2) using only unit steps north or east.
Let's call such a path admissible if none of its intermediate points are inadmissible.
Let P(n) be the number of admissible paths from (0, 0) to (n, n).
It can be verified that P(5) = 252, P(16) = 596994440 and P(1000) mod 1 000 000 007 = 341920854.
Find P(10 000 000) mod 1 000 000 007.
##Допустимые пути через сетку

Назовем точку (x, y) на единичной сетке недопустимой, если x, y и x + y являются положительными идеальными квадратами.
Например, (9, 16) недопустима, в то время как (0, 4), (3, 1) и (9, 4) - допустимы.
Рассмотрим путь из точки (x1, y1) в точку (x2, y2), состоящий только из единичных шагов в направлении на север или на восток.
Назовем такой путь допустимым, если ни одна из промежуточных точек пути не является недопустимой.
Пусть P(n) будет количеством допустимых путей от (0, 0) до (n, n).
Может быть показано, что P(5) = 252, P(16) = 596994440 и P(1000) mod 1 000 000 007 = 341920854.
Найдите P(10 000 000) mod 1 000 000 007.
