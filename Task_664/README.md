##An infinite game

Peter is playing a solitaire game on an infinite checkerboard, each square of which can hold an unlimited number of tokens.
Each move of the game consists of the following steps:
The board is marked with a line called the dividing line. Initially, every square to the left of the dividing line contains a token, and every square to the right of the dividing line is empty:
Peter's goal is to get a token as far as possible to the right in a finite number of moves. However, he quickly finds out that, even with his infinite supply of tokens, he cannot move a token more than four squares beyond the dividing line.
Peter then considers starting configurations with larger supplies of tokens: each square in the $d$th column to the left of the dividing line starts with $d^n$ tokens instead of 1. This is illustrated below for $n=1$:
Let $F(n)$ be the maximum number of squares Peter can move a token beyond the dividing line. For example, $F(0)=4$.
You are also given that $F(1)=6$, $F(2)=9$, $F(3)=13$, $F(11)=58$ and $F(123)=1173$.
Find $F(1234567)$.
##Бесконечная игра

Петр играет в одиночную игру на бесконечной шахматной доске, каждая клетка которой может содержать бесконечное количество фишек.
Каждый ход в игре состоит из следующих шагов:

Выберите фишку $T$ для перемещения. Это может быть любая фишка на доске, кроме тех, чьи все четыре прилегающие клетки пусты.
Выберите и сбросьте одну фишку $D$ с клетки, прилегающего к $T$.
Переместите $T$ на любую	 из прилегающих к ней клеток (даже если она уже занята).



Доска изначально помечена линией, называющейся разделительной линией. Изначально каждая клетка слева от разделительной линии содержит одну фишку, а каждая клетка справа от разделительной линии пуста:


Цель Петра - переместить фишку как можно дальше вправо за конечное число ходов. Однако, он быстро осознает, что даже с бесконечным запасом фишек он не может переместить фишку дальше, чем на четыре клетки вправо от разделительной линии.
Тогда Петр рассматривает начальные расположения с бóльшими запасами фишек: каждая клетка в $d$-том столбце слева от разделительной линии начинает с $d^n$ фишками вместо 1. Ниже это проиллюстрировано для $n=1$:


Пусть $F(n)$ будет максимальным количеством клеток, на которое Петр может переместить фишку за разделительную лнию. Например, $F(0)=4$.
Также известно, что $F(1)=6$, $F(2)=9$, $F(3)=13$, $F(11)=58$ и $F(123)=1173$.
Найдите $F(1234567)$.
