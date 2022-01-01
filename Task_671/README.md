##Colouring a Loop

A certain type of flexible tile comes in three different sizes - 1×1, 1×2, and 1×3 - and in $k$ different colours. There is an unlimited number of tiles available in each combination of size and colour.
These are used to tile a closed loop of width $2$ and length (circumference) $n$, where $n$ is a positive integer, subject to the following conditions:
For example, the following is an acceptable tiling of a $2\times 23$ loop with $k=4$ (blue, green, red and yellow):
but the following is not an acceptable tiling, because it violates the "no four corners meeting at a point" rule:
Let $F_k(n)$ be the number of ways the $2\times n$ loop can be tiled subject to these rules when $k$ colours are available. (Not all $k$ colours have to be used.) Where reflecting horizontally or vertically would give a different tiling, these tilings are to be counted separately.
For example, $F_4(3) = 104$, $F_5(7) = 3327300$, and $F_6(101)\equiv 75309980 \pmod{1\,000\,004\,321}$.
Find $F_{10}(10\,004\,003\,002\,001) \bmod 1\,000\,004\,321$.
##Раскрашивание кольца

Определенный тип гибкой плитки имеет три возможных размера - 1×1, 1×2 и 1×3, и $k$ возможных цветов. В доступе имеется неограниченное количество плиток каждого сочетания размера и цвета.
Эти плитки используются, чтобы выложить кольцо шириной $2$ и длиной (длиной окружности) $n$, где $n$ - натуральное число, отвечающее следующим условиям:
Кольцо должно быть полностью покрыто неперекрывающимися плитками.
Нельзя, чтобы углы четырех плиток сходились в одной точке.
Соседние плитки должны быть разных цветов.
Например, следующий способ выложить кольцо $2\times 23$ при $k=4$ (синий, зеленый, красный и желтый) является приемлемым:

, 
в то время как следующий способ приемлемым не является, так как он нарушает правило "четыре угла не должны сходиться в одной точке":


Пусть $F_k(n)$ будет количеством способов выложить кольцо $2\times n$ в соответствии с этими правилами, если доступны плитки $k$ цветов (не обязательно использовать все цвета). Если вертикальное или горизонтальное отражение выкладки дает отличную от нее выкладку, такие выкладки следует считать отдельно.
Например, $F_4(3) = 104$, $F_5(7) = 3327300$ и $F_6(101)\equiv 75309980 \pmod{1\,000\,004\,321}$.
Найдите $F_{10}(10\,004\,003\,002\,001) \bmod 1\,000\,004\,321$.
