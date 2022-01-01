##Even Stevens

Every day for the past $n$ days Even Stevens brings home his groceries in a plastic bag. He stores these plastic bags in a cupboard. He either puts the plastic bag into the cupboard with the rest, or else he takes an even number of the existing bags (which may either be empty or previously filled with other bags themselves) and places these into the current bag.
After 4 days there are 5 possible packings and if the bags are numbered 1 (oldest), 2, 3, 4, they are:
Note that 1, 2, 3 inside 4 is invalid because every bag must contain an even number of bags.
Define $f(n)$ to be the number of possible packings of $n$ bags. Hence $f(4)=5$. You are also given $f(8)=1\,385$.
Find $f(24\,680)$ giving your answer modulo $1\,020\,202\,009$.
##Чет Обормот

Последние $n$ дней Чет Обормот каждый день приносит домой покупки в пластиковом пакете. Он хранит все пакеты в шкафу. Каждый день он или кладет пластиковый пакет в шкаф к остальным пакетам, или же достает из шкафа четное число имеющихся пакетов (которые могут быть пустыми или содержать в себе еще пакеты) и кладет их в сегодняшний пакет.
На 4 день существует 5 возможных расфасовок пакетов. Если все пакеты пронумеровать 1 (самый старый), 2, 3, 4, возможны следующие расфасовки:

Четыре пустых пакета,
1 и 2 внутри 3, 4 пустой,
1 и 3 внутри 4, 2 пустой,
1 и 2 внутри 4, 3 пустой,
2 и 3 внутри 4, 1 пустой.

Заметим, что расфасовка "1, 2 и 3 внутри 4" невозможна, так как каждый пакет может содержать только четное количество пакетов.
Определим $f(n)$ как количество возможных расфасовок $n$ пакетов. Таким образом, $f(4)=5$. Также известно, что $f(8)=1\,385$.
Найдите $f(24\,680)$. В качестве ответа приведите остаток от деления полученного результата на $1\,020\,202\,009$. Оригинал
