##Fibonacci tree game


A Fibonacci tree is a binary tree recursively defined as:

On such a tree two players play a take-away game. On each turn a player selects a node and removes that node along with the subtree rooted at that node.
The player who is forced to take the root node of the entire tree loses.



Here are the winning moves of the first player on the first turn for T(k) from k=1 to k=6.



For example, f(5) = 1 and f(10) = 17.


Find f(10000). Give the last 18 digits of your answer.

##Игра в дерево Фибоначчи


Дерево Фибоначчи - это двоичное дерево, рекурсивно задаваемое следующим образом:


T(0) - пустое дерево.
T(1) - двоичное дерево с одним узлом.
T(k) состоит из корневого узла, имеющего T(k-1) и T(k-2) в качестве потомков.


Два игрока играют в игру с таким деревом. Каждый ход игрок выбирает узел и убирает его вместе со всем поддеревом, исходящим из этого узла.
Игрок, вынужденный убрать корневой узел всего дерева, проигрывает.

Ниже показаны выигрышные первые ходы первого игрока при игре с деревом T(k) от k=1 до k=6.


Пусть f(k) будет количеством выигрышных первых ходов для первого игрока (т.е. первых ходов, после которых второй игрок лишен выигрышной стратегии) в игре с деревом T(k).


Например, f(5) = 1 и f(10) = 17.


Найдите f(10000). Приведите последние 18 цифр полученного числа.

