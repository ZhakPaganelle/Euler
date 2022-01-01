##Exponent Difference


For any integer $n>0$ and prime number $p,$ define $\nu_p(n)$ as the greatest integer $r$ such that $p^r$ divides $n$. 


Define $$D(n, m)  = \sum_{p \text{ prime}} \left| \nu_p(n) - \nu_p(m)\right|.$$ For example, $D(14,24) = 4$.


Furthermore, define $$S(N) = \sum_{1 \le n, m \le N} D(n, m).$$ You are given $S(10) = 210$ and $S(10^2) = 37018$.


Find $S(10^{12})$. Give your answer modulo $1\,000\,000\,007$.

##Разница экспонент


Для любого целого числа $n>0$ и простого числа $p$ определим $\nu_p(n)$ как наибольшее целое число $r$, такое что $p^r$ делит $n$ нацело. 


Определим $$D(n, m)  = \sum_{p \text{ prime}} \left| \nu_p(n) - \nu_p(m)\right|.$$ Например, $D(14,24) = 4$.


Далее, определим $$S(N) = \sum_{1 \le n, m \le N} D(n, m).$$ Известно, что $S(10) = 210$ и $S(10^2) = 37018$.


Найдите $S(10^{12})$. В качестве ответа приведите остаток от деления полученного результата на  $1\,000\,000\,007$.
 Оригинал
