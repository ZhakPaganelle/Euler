##Yarra Gnisrever

Let $N$ and $K$ be two positive integers.
$F_n$ is the $n$-th Fibonacci number: $F_1 = F_2 = 1$, $F_n = F_{n - 1} + F_{n - 2}$ for all $n \geq 3$.
Let $s_n = F_{2n - 1} \mod N$ and let $t_n = F_{2n} \mod N$.
Start with an array of integers $A = (A[0], \cdots, A[N - 1])$ where initially every $A\text{[}i]$ is equal to $i$.
Now perform $K$ successive operations on $A$, where the $j$-th operation consists of reversing the order of those elements in $A$ with indices between $s_j$ and $t_j$ (both ends inclusive).
Define $R(N,K)$ to be $\sum_{i = 0}^{N - 1}i \times A\text {[}i]$ after $K$ operations.
For example, $R(5, 4) = 27$, as can be seen from the following procedure:
Initial position: $(0, 1, 2, 3, 4)$
Step 1 - Reverse $A[1]$ to $A[1]$: $(0, 1, 2, 3, 4)$
Step 2 - Reverse $A[2]$ to $A[3]$: $(0, 1, 3, 2, 4)$
Step 3 - Reverse $A[0]$ to $A[3]$: $(2, 3, 1, 0, 4)$
Step 4 - Reverse $A[3]$ to $A[1]$: $(2, 0, 1, 3, 4)$
$R(5, 4) = 0 \times 2 + 1 \times 0 + 2 \times 1 + 3 \times 3 + 4 \times 4 = 27$
Also, $R(10^2, 10^2) = 246597$ and $R(10^4, 10^4) = 249275481640$.
Find $R(10^{18}, 10^6)$ giving your answer modulo $10^9$.
##Виссам Йынтарбо

Пусть $N$ и $K$ будут натуральными числами.
$F_n$ является $n$-тым числом Фибоначчи: $F_1 = F_2 = 1$, $F_n = F_{n - 1} + F_{n - 2}$ для всех $n \geq 3$.
Пусть $s_n = F_{2n - 1} \mod N$, и пусть $t_n = F_{2n} \mod N$.
Начните с массива целых чисел $A = (A[0], \cdots, A[N - 1])$, где изначально каждое $A\text{[}i]$ равно $i$.
Далее, выполните $K$ последовательных операций над $A$, где $j$-тая операция состоит в обращении порядка элементов $A$ с индексами между $s_j$ и $t_j$ (обе границы включительно).
Определим $R(N,K)$ как $\sum_{i = 0}^{N - 1}i \times A\text {[}i]$ после $K$ операций.
Например, $R(5, 4) = 27$, как можно увидеть из следующей процедуры:
Начальное положение: $(0, 1, 2, 3, 4)$
Шаг 1 - Обратить $A[1]$ на $A[1]$: $(0, 1, 2, 3, 4)$
Шаг 2 - Обратить $A[2]$ на $A[3]$: $(0, 1, 3, 2, 4)$
Шаг 3 - Обратить $A[0]$ на $A[3]$: $(2, 3, 1, 0, 4)$
Шаг 4 - Обратить $A[3]$ на $A[1]$: $(2, 0, 1, 3, 4)$
$R(5, 4) = 0 \times 2 + 1 \times 0 + 2 \times 1 + 3 \times 3 + 4 \times 4 = 27$
Также известно, что $R(10^2, 10^2) = 246597$ и $R(10^4, 10^4) = 249275481640$.
Найдите $R(10^{18}, 10^6)$. В качестве ответа приведите остаток от деления полученного результата на $10^9$.
Оригинал
