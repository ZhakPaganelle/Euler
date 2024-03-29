##Not Zeckendorf


Consider the Fibonacci sequence $\{1,2,3,5,8,13,21,\ldots\}$.


We let $f(n)$ be the number of ways of representing an integer $n\ge 0$ as the sum of different Fibonacci numbers.
For example, $16 = 3+13 = 1+2+13 = 3+5+8 = 1+2+5+8$ and hence $f(16) = 4$. 
By convention $f(0) = 1$.


Further we define
$$\displaystyle S(n) = \sum_{k=0}^n f(k)$$
You are given $S(100) = 415$ and $S(10^4) = 312807$.


Find $\displaystyle S(10^{13})$.

##Не Цекендорф


Рассмотрим последовательность Фибоначчи $\{1,2,3,5,8,13,21,\ldots\}$.


Пусть $f(n)$ будет количеством способов представления целого числа $n\ge 0$ как суммы различных чисел Фибоначчи.
Например, $16 = 3+13 = 1+2+13 = 3+5+8 = 1+2+5+8$, из чего следует $f(16) = 4$. 
Условимся, что $f(0) = 1$.


Далее определим
$$\displaystyle S(n) = \sum_{k=0}^n f(k)$$
Известно, что $S(100) = 415$ и $S(10^4) = 312807$.


Найдите $\displaystyle S(10^{13})$.
 Оригинал
