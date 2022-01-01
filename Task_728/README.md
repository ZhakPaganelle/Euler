##Circle of Coins

Consider $n$ coins arranged in a circle where each coin shows heads or tails. A move consists of turning over $k$ consecutive coins: tail-head or head-tail. Using a sequence of these moves the objective is to get all the coins showing heads.
Consider the example, shown below, where $n=8$ and $k=3$ and the initial state is one coin showing tails (black). The example shows a solution for this state.
For given values of $n$ and $k$ not all states are solvable.  Let $F(n,k)$ be the number of states that are solvable. You are given that $F(3,2) = 4$, $F(8,3) = 256$ and $F(9,3) = 128$.
Further define:
You are also given that $S(3) = 22$, $S(10) = 10444$ and $S(10^3) \equiv 853837042 \pmod{1\,000\,000\,007}$
Find $S(10^7)$. Give your answer modulo $1\,000\,000\,007$
##Круг из монет

Рассмотрим $n$ монет, расположенных в круг, где каждая монета повернута орлом или решкой. Один ход заключается в переворачивании $k$ последовательно расположенных монет: орел-решка или решка-орел. Задача - используя последовательность ходов, перевернуть все монеты решкой вверх.
Расммотрим пример, показанный ниже, где $n=8$ и $k=3$ и в начальном расположении одна монета повернута решкой (черная). В примере показано решение для такого начального расположения.


Не все начальные расположения имеют решение для данных значений $n$ и $k$. Пусть $F(n,k)$ будет количеством начальных расположений, которые имеют решение. Известно, что $F(3,2) = 4$, $F(8,3) = 256$ и $F(9,3) = 128$.
Далее определим:

$\displaystyle	S(N) = \sum_{n=1}^N\sum_{k=1}^n F(n,k)$
Также известно, что $S(3) = 22$, $S(10) = 10444$ и $S(10^3) \equiv 853837042 \pmod{1\,000\,000\,007}$
Найдите $S(10^7)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$
Оригинал
