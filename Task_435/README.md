##Polynomials of Fibonacci numbers

The Fibonacci numbers $\{f_n, n \ge 0\}$ are defined recursively as $f_n = f_{n-1} + f_{n-2}$ with base cases $f_0 = 0$ and $f_1 = 1$.
Define the polynomials $\{F_n, n \ge 0\}$ as $F_n(x) = \displaystyle{\sum_{i=0}^n f_i x^i}$.
For example, $F_7(x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + 13x^7$, and $F_7(11) = 268\,357\,683$.
Let $n = 10^{15}$. Find the sum $\displaystyle{\sum_{x=0}^{100} F_n(x)}$ and give your answer modulo $1\,307\,674\,368\,000 \ (= 15!)$.
##Многочлены из чисел Фибоначчи

Числа Фибоначчи {fn, n ≥ 0} рекурсивно определяются как fn = fn-1 + fn-2 с начальными случаями f0 = 0 и f1 = 1.
Определим многочлены {Fn, n ≥ 0} как Fn(x) = ∑fixi для 0 ≤ i ≤ n.
Например, F7(x) = x + x2 + 2x3 + 3x4 + 5x5 + 8x6 + 13x7 и F7(11) = 268357683.
Пусть n = 1015. Найдите сумму [∑0≤x≤100 Fn(x)] mod 1307674368000 (= 15!).
