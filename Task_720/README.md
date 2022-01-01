##Unpredictable Permutations

Consider all permutations of $\{1, 2, \ldots N\}$, listed in lexicographic order.For example, for $N=4$, the list starts as follows:

Let us call a permutation $P$ unpredictable if there is no choice of three indices $i \lt j \lt k$ such that $P(i)$, $P(j)$ and $P(k)$ constitute an arithmetic progression. For example, $P=(3, 4, 2, 1)$ is not unpredictable because $P(1), P(3), P(4)$ is an arithmetic progression.


Let $S(N)$ be the position within the list of the first unpredictable permutation.


For example, given $N = 4$, the first unpredictable permutation is $(1, 3, 2, 4)$ so $S(4) = 3$.
You are also given that $S(8) = 2295$ and $S(32) \equiv 641839205 \pmod{1\,000\,000\,007}$.


Find $S(2^{25})$. Give your answer modulo $1\,000\,000\,007$.

##Непредсказуемые перестановки

Рассмотрим все перестановки $\{1, 2, \ldots N\}$, упорядоченные в лексикографическом порядке.Например, для $N=4$ список перестановок выглядит следующим образом:
\[
(1, 2, 3, 4) \\
(1, 2, 4, 3) \\
(1, 3, 2, 4) \\
(1, 3, 4, 2) \\
(1, 4, 2, 3) \\
(1, 4, 3, 2) \\
(2, 1, 3, 4) \\
\vdots
\]


Назовем перестановку $P$ непредсказуемой, если невозможно выбрать значения трех индексов $i \lt j \lt k$ так, чтобы $P(i)$, $P(j)$ и $P(k)$ образовали арифметическую прогрессию. Например, $P=(3, 4, 2, 1)$  не является непредсказуемой, потому что $P(1), P(3), P(4)$ образуют арифметическую прогрессию.


Пусть $S(N)$ будет позицией первой непредсказуемой перестановки в списке.


Например, при $N = 4$ первой непредсказуемой перестановкой является $(1, 3, 2, 4)$, поэтому $S(4) = 3$.
Также известно, что $S(8) = 2295$ и $S(32) \equiv 641839205 \pmod{1\,000\,000\,007}$.


Найдите $S(2^{25})$. В качестве ответа приведите остаток от деления полученного результата на  $1\,000\,000\,007$.
 Оригинал
