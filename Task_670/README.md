##Colouring a Strip

A certain type of tile comes in three different sizes - 1×1, 1×2, and 1×3 - and in four different colours: blue, green, red and yellow. There is an unlimited number of tiles available in each combination of size and colour.
These are used to tile a $2\times n$ rectangle, where $n$ is a positive integer, subject to the following conditions:
For example, the following is an acceptable tiling of a $2\times 12$ rectangle:
but the following is not an acceptable tiling, because it violates the "no four corners meeting at a point" rule:
Let $F(n)$ be the number of ways the $2\times n$ rectangle can be tiled subject to these rules. Where reflecting horizontally or vertically would give a different tiling, these tilings are to be counted separately.
For example, $F(2) = 120$, $F(5) = 45876$, and $F(100)\equiv 53275818 \pmod{1\,000\,004\,321}$.
Find $F(10^{16}) \bmod 1\,000\,004\,321$.
##Раскрашивание полоски

Определенный тип плитки имеет три возможных размера - 1×1, 1×2 и 1×3 - и четыре возможных цвета: синий, зеленый, красный и желтый. В доступе имеется неограниченное количество плиток каждого сочетания размера и цвета.
Эти плитки используются, чтобы выложить прямоугольник $2\times n$, где $n$ - натуральное число, отвечающее следующим условиям:
Прямоугольник должен быть полностью покрыт неперекрывающимися плитками.
Нельзя, чтобы углы четырех плиток сходились в одной точке.
Соседние плитки должны быть разных цветов.
Например, следующий способ выложить прямоугольник $2\times 12$ является приемлемым:

, 
в то время как следующий способ приемлемым не является, так как он нарушает правило "четыре угла не должны сходиться в одной точке":


Пусть $F(n)$ будет количеством способов выложить прямоугольник $2\times n$ в соответствии с этими правилами. Если вертикальное или горизонтальное отражение выкладки дает отличную от нее выкладку, такие выкладки следует считать отдельно.
Например, $F(2) = 120$, $F(5) = 45876$ и $F(100)\equiv 53275818 \pmod{1\,000\,004\,321}$.
Найдите $F(10^{16}) \bmod 1\,000\,004\,321$.
