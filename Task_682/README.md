##5-Smooth Pairs

5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.
Let $\Omega(a)$ be the count of prime factors of $a$ (counted with multiplicity).
Let $s(a)$ be the sum of the prime factors of $a$ (with multiplicity).
For example, $\Omega(300) = 5$ and $s(300) = 2+2+3+5+5 = 17$.
Let $f(n)$ be the number of pairs, $(p,q)$, of Hamming numbers such that $\Omega(p)=\Omega(q)$ and $s(p)+s(q)=n$.
You are given $f(10)=4$ (the pairs are $(4,9),(5,5),(6,6),(9,4)$) and $f(10^2)=3629$.
Find $f(10^7) \bmod 1\,000\,000\,007$.
##5-гладкие пары

5-гладкие числа - это числа, чей наибольший простой делитель не больше 5.
5-гладкие числа также называются числами Хамминга.
Пусть $\Omega(a)$ будет количеством простых делителей числа $a$ (считая повторы).
Пусть $s(a)$ будет суммой простых делителей числа $a$ (считая повторы).
Например, $\Omega(300) = 5$ и $s(300) = 2+2+3+5+5 = 17$.
Пусть $f(n)$ будет количеством пар $(p,q)$ чисел Хамминга, таких что $\Omega(p)=\Omega(q)$ и $s(p)+s(q)=n$.
Известно, что $f(10)=4$ (пары $(4,9),(5,5),(6,6),(9,4)$) и $f(10^2)=3629$.
Найдите $f(10^7) \bmod 1\,000\,000\,007$. Оригинал
