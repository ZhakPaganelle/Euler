##Gnomon numbering

For integers m, n (0 ≤ n < m), let L(m, n) be an m×m grid with the top-right n×n grid removed.
For example, L(5, 3) looks like this:

We want to number each cell of L(m, n) with consecutive integers 1, 2, 3, ... such that the number in every cell is smaller than the number below it and to the left of it.
For example, here are two valid numberings of L(5, 3):

Let LC(m, n) be the number of valid numberings of L(m, n).
It can be verified that LC(3, 0) = 42, LC(5, 3) = 250250, LC(6, 3) = 406029023400 and LC(10, 5) mod 76543217 = 61251715.
Find LC(10000, 5000) mod 76543217.
##Нумерация гномонов

Для целых m, n (0 ≤ n < m), пусть L(m, n) будет сеткой m×m, из верхнего правого угла которой убран квадрат n×n.
Например, L(5, 3) выглядит таким образом:

Мы хотим пронумеровать каждую ячейку L(m, n) последовательными целыми числами 1, 2, 3, ... так, чтобы число в каждой ячейке было меньше чисел в соседних ячейках слева и снизу.
Например, вот два варианта такой нумерации L(5, 3):

Пусть LC(m, n) будет количеством возможных вариантов нумерации L(m, n).
Можно показать, что LC(3, 0) = 42, LC(5, 3) = 250250, LC(6, 3) = 406029023400 и LC(10, 5) mod 76543217 = 61251715.
Найдите LC(10000, 5000) mod 76543217.
