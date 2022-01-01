##Chromatic Conundrum

Let F(r,c,n) be the number of ways to colour a rectangular grid with r rows and c columns using at most n colours such that no two adjacent cells share the same colour. Cells that are diagonal to each other are not considered adjacent.
For example, F(2,2,3) = 18, F(2,2,20) = 130340, and F(3,4,6) = 102923670.
Let S(r,c,n) = $\sum_{k=1}^{n}$ F(r,c,k).
For example, S(4,4,15) mod 109+7 = 325951319.
Find S(9,10,1112131415) mod 109+7.
##Хроматическая загадка

Пусть F(r,c,n) будет количеством способов раскрасить прямоугольную сетку из r рядов и c столбцов, используя не больше n цветов так, чтобы никакие две соседние клетки не были одного цвета. Клетки, расположенные по диагонали друг к другу, не считаются соседними.
Например, F(2,2,3) = 18, F(2,2,20) = 130340 и F(3,4,6) = 102923670.
Пусть S(r,c,n) = $\sum_{k=1}^{n}$ F(r,c,k).
Например, S(4,4,15) mod 109+7 = 325951319.
Найдите S(9,10,1112131415) mod 109+7.
