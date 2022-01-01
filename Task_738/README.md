##Counting Ordered Factorisations

Define $d(n,k)$ to be the number of ways to write $n$ as a product of $k$ ordered integers
Further define $D(N,K)$ to be the sum of $d(n,k)$ for $1\le n\le N$ and $1\le k\le K$.
You are given that $D(10, 10) = 153$ and $D(100, 100) = 35384$.
Find $D(10^{10},10^{10})$ giving your answer modulo $1\,000\,000\,007$.
##Подсчет упорядоченных факторизаций

Определим $d(n,k)$ как количество способов записать число $n$ в виде произведения $k$ упорядоченных целых чисел
\[
n = x_1\times x_2\times x_3\times \ldots\times x_k\qquad 1\le x_1\le x_2\le\ldots\le x_k
\]
Далее определим $D(N,K)$ как сумму $d(n,k)$ для $1\le n\le N$ и $1\le k\le K$.
Вам известно, что $D(10, 10) = 153$ и $D(100, 100) = 35384$.
Найдите $D(10^{10},10^{10})$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$. Оригинал
