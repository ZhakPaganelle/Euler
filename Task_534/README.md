##Weak Queens

The classical eight queens puzzle is the well known problem of placing eight chess queens on a 8×8 chessboard so that no two queens threaten each other. Allowing configurations to reappear in rotated or mirrored form, a total of 92 distinct configurations can be found for eight queens. The general case asks for the number of distinct ways of placing n queens on a n×n board, e.g. you can find 2 distinct configurations for n=4.
Let's define a weak queen on a n×n board to be a piece which can move any number of squares if moved horizontally, but a maximum of n−1−w squares if moved vertically or diagonally, 0≤w<n being the "weakness factor". For example, a weak queen on a n×n board with a weakness factor of w=1 located in the bottom row will not be able to threaten any square in the top row as the weak queen would need to move n−1 squares vertically or diagonally to get there, but may only move n−2 squares in these directions. In contrast, the weak queen is not handicapped horizontally, thus threatening every square in its own row, independently from its current position in that row.
Let Q(n,w) be the number of ways n weak queens with weakness factor w can be placed on a n×n board so that no two queens threaten each other. It can be shown, for example, that Q(4,0)=2, Q(4,2)=16 and Q(4,3)=256.
Let $S(n)=\displaystyle\sum_{w=0}^{n-1} Q(n,w)$.
You are given that S(4)=276 and S(5)=3347.
Find S(14).
##Слабые ферзи

Классическая задача о восьми ферзях - хорошо известная головоломка о расположении восьми шахматных ферзей на шахматной доске 8×8 так, чтобы никакие два ферзя не угрожали друг другу. Если считать повороты и отражения одного и того же расположения фигур различными расположениями, можно найти всего 92 возможных различных расположения для восьми ферзей. В общем случае стоит вопрос о количестве возможных различных расположений n ферзей на доске n×n. Например, существует 2 различных расположения для n=4.
Определим слабого ферзя на доске n×n как фигуру, которая может двигаться на любое количество клеток по горизонтали, но максимум - на n−1−w клеток по верикали или диагонали, где 0≤w<n - "фактор слабости". Например, слабый ферзь на доске n×n с фактором слабости w=1, расположенный в нижнем ряду, не сможет угрожать ни одной клетке верхнего ряда, так как слабому ферзю понадобилось бы переместиться на n−1 клеток по вертикали или диагонали, чтобы туда добраться, но он может двигаться только на n−2 клеток в этих направлениях. В то же время, слабый ферзь не ограничен в движении по горизонтали, и, таким образом, угрожает каждой клетке своего ряда, независимо от его положения в этом ряду.
Пусть Q(n,w) будет количеством способов расположения n слабых ферзей с фактором слабости w на доске n×n так, чтобы никакие два ферзя не угрожали друг другу. Можно показать, например, что Q(4,0)=2, Q(4,2)=16 и Q(4,3)=256.
Пусть $S(n)=\displaystyle\sum_{w=0}^{n-1} Q(n,w)$.
Известно, что S(4)=276 и S(5)=3347.
Найдите S(14).
