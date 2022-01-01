##Binary Blackboard

Oscar and Eric play the following game. First, they agree on a positive integer $n$, and they begin by writing its binary representation on a blackboard. They then take turns, with Oscar going first, to write a number on the blackboard in binary representation, such that the sum of all written numbers does not exceed $2n$.
The game ends when there are no valid moves left. Oscar wins if the number of $1$s on the blackboard is odd, and Eric wins if it is even.
Let $S(N)$ be the sum of all $n \le 2^N$ for which Eric can guarantee winning, assuming optimal play.
For example, the first few values of $n$ for which Eric can guarantee winning are $1,3,4,7,15,16$. Hence $S(4)=46$.
You are also given that $S(12) = 54532$ and $S(1234) \equiv 690421393 \pmod{1\,000\,000\,007}$.
Find $S(12\,345\,678)$. Give your answer modulo $1\,000\,000\,007$.
##Двоичная доска

Оскар и Эрик играют в игру: сначала, они договариваются о натуральном числе $n$ и начинают с записи на доске его представления в двоичной системе счисления. Затем они по очереди, начиная с Оскара, дописывают на доске число в двоичной форме, так чтобы сумма всех записанных чисел не превышала $2n$.
Игра заканчивается, когда больше не остается возможных ходов. Если на конец игры количество единиц на доске нечетное, то побеждает Оскар, а если четное - Эрик.
Пусть $S(N)$ будет суммой всех $n \le 2^N$, при которых Эрик может гарантировать свою победу при условии оптимальной игры.
Например, первые несколько значений $n$, при которых Эрик можут гаранитровано победить - $1,3,4,7,15,16$. Поэтому $S(4)=46$.
Также известно, что $S(12) = 54532$ и $S(1234) \equiv 690421393 \pmod{1\,000\,000\,007}$.
Найдите $S(12\,345\,678)$. В качестве ответа приведите остаток от деления полученного результата на  $1\,000\,000\,007$. Оригинал
