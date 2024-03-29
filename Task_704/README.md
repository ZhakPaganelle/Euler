##Factors of Two in Binomial Coefficients


Define $g(n, m)$ to be the largest integer $k$ such that $2^k$ divides $\binom{n}m$. 
For example, $\binom{12}5 = 792 = 2^3 \cdot 3^2 \cdot 11$, hence $g(12, 5) = 3$. 
Then define $F(n) = \max \{ g(n, m) : 0 \le m \le n \}$. $F(10) = 3$ and $F(100) = 6$.


Let $S(N)$ = $\displaystyle\sum_{n=1}^N{F(n)}$. You are given that $S(100) = 389$ and $S(10^7) = 203222840$.


Find $S(10^{16})$.

##Степени двойки как множители биномиальных коэффициентов


Определим $g(n, m)$ как наибольшее целое число $k$, такое что $2^k$ делит нацело $\binom{n}m$. 
Например, $\binom{12}5 = 792 = 2^3 \cdot 3^2 \cdot 11$, отсюда $g(12, 5) = 3$. 
Теперь определим $F(n) = \max \{ g(n, m) : 0 \le m \le n \}$. $F(10) = 3$ и $F(100) = 6$.


Пусть $S(N)$ = $\displaystyle\sum_{n=1}^N{F(n)}$. Известно, что $S(100) = 389$ и $S(10^7) = 203222840$.


Найдите $S(10^{16})$.
 Оригинал
