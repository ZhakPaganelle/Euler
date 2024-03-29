##Number Sequence Game

The number sequence game starts with a sequence S of N numbers written on a line.
Two players alternate turns. The players on their respective turns must select and remove either the first or the last number remaining in the sequence.
A player's own score is (determined by) the sum of all the numbers that player has taken. Each player attempts to maximize their own sum.
Player 1 score is 1 + 10 = 11.
Let F(N) be the score of player 1 if both players follow the optimal strategy for the sequence S = {s1, s2, ..., sN} defined as:
The sequence begins with S = {0, 45, 2070, 4284945, 753524550, 478107844, 894218625, ...}.
You are given F(2) = 45, F(4) = 4284990, F(100) = 26365463243, F(104) = 2495838522951.
Find F(108).
##Игра в числовые последовательности

Игра в числовые последовательности начинается с последовательности S из N чисел, записанных в ряд.
Два игрока ходят по очереди. В свой ход каждый игрок должен выбрать или первое, или последнее число в последовательности и убрать его из нее.
Очки игрока равны сумме всех чисел, которые были им убраны. Каждый игрок стремится получить как можно большее количество очков.
Если N = 4 и S = {1, 2, 10, 3}, тогда каждый игрок получает максимальную возможную сумму следующим образом:

Игрок 1: убирает первое число (1)
Игрок 2: убирает последнее число из оставшейся последовательности (3)
Игрок 1: убирает последнее число из оставшейся последовательности (10)
Игрок 2: убирает оставшееся число (2)

Игрок 1 получает 1 + 10 = 11 очков.
Пусть F(N) будет количеством очков игрока 1, если оба игрока следуют оптимальной стратегии игры для последовательности S = {s1, s2, ..., sN}, определенной как:

s1 = 0
si+1 = (si2 + 45) modulo 1 000 000 007

Последовательность начинается следующим образом: S = {0, 45, 2070, 4284945, 753524550, 478107844, 894218625, ...}.
Известно, что F(2) = 45, F(4) = 4284990, F(100) = 26365463243, F(104) = 2495838522951.
Найдите F(108).
