##Flipping game

The flipping game is a two player game played on a N by N square board.
Each square contains a disk with one side white and one side black.
The game starts with all disks showing their white side.
A turn consists of flipping all disks in a rectangle with the following properties:



Players alternate turns. A player wins by turning the grid all black.
Let W(N) be the number of winning moves for the first player on a N by N board with all disks white, assuming perfect play.
W(1) = 1, W(2) = 0, W(5) = 8 and W(102) = 31395.
For N=5, the first player's eight winning first moves are:

Find W(106).
##Игра в перевороты

Игра в перевороты - это игра для двух игроков, происходящая на квадратной доске размером N на N.
Каждый квадрат содержит диск, окрашенный с одной стороны в белый цвет, а с другой - в черный.
В начале игры все диски повернуты белой стороной вверх.
За один ход переворачиваются все диски в прямоугольнике, имеющем следующие свойства:

в верхнем правом углу прямоугольника находится белый диск
ширина прямоугольника является квадратом целого числа (1, 4, 9, 16, ...)
длина прямоугольника является треугольным числом (1, 3, 6, 10, ...)


Игроки ходят поочередно. Игрок побеждает, если после его хода все диски на доске повернуты черной стороной вверх.
Пусть W(N) будет количеством выигрышных ходов для первого игрока на доске размером N на N, покрытой изначально белыми дисками, при идеальной игре.
W(1) = 1, W(2) = 0, W(5) = 8 и W(102) = 31395.
Для N=5, восемью выигрышными первыми ходами первого игрока являются:


Найдите W(106).
