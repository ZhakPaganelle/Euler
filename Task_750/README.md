##Optimal Card Stacking


Card Stacking is a game on a computer starting with an array of $N$ cards labelled $1,2,\ldots,N$.
A stack of cards can be moved by dragging horizontally with the mouse to another stack but only when the resulting stack is in sequence. The goal of the game is to combine the cards into a single stack using minimal total drag distance.


For the given arrangement of 6 cards the minimum total distance is $1 + 3 + 1 + 1 + 2 = 8$.


For $N$ cards, the cards are arranged so that the card at position $n$ is $3^n\bmod(N+1), 1\le n\le N$.


We define $G(N)$ to be the minimal total drag distance to arrange these cards into a single sequence.
For example, when $N = 6$ we get the sequence $3,2,6,4,5,1$ and $G(6) = 8$.
You are given $G(16) = 47$.


Find $G(976)$.


Note: $G(N)$ is not defined for all values of $N$.

##Оптимальное	собирание стопку


"Собирание карт в стопку" - это компьютерная игра, начинающаяся с набора из $N$ карт, пронумерованных $1,2,\ldots,N$.
Стопку карт можно переместить, перетягивая ее мышкой в горизонтальном направлении на другую стопку, но только при условии, что в получившейся стопке все карты будут расположены по порядку. Цель игры - собрать все карты в одну стопку, используя минимальное суммарное расстояние перемещений.





Для данного расположения 6 карт минимальное суммарное расстояние равно $1 + 3 + 1 + 1 + 2 = 8$.


$N$ карт изначально расположены так, что карта на позиции $n$ имеет номер $3^n\bmod(N+1), 1\le n\le N$.


Определим $G(N)$ как минимальное суммарное расстояние перемещений, необходимое, чтобы собрать все карты в одну последовательность.
Например, для $N = 6$ мы получим исходное расположение $3,2,6,4,5,1$ и $G(6) = 8$.
Известно, что $G(16) = 47$.


Найдите $G(976)$.


Примечание: $G(N)$ определено не для всех значений $N$.
 Оригинал
