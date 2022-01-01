##Powers of $1+\sqrt 7$


When $(1+\sqrt 7)$ is raised to an integral power, $n$, we always get a number of the form $(a+b\sqrt 7)$.
We write $(1+\sqrt 7)^n = \alpha(n) + \beta(n)\sqrt 7$.


For a given number $x$ we  define $g(x)$ to be the smallest positive integer $n$ such that:
$$\begin{align}
\alpha(n) &\equiv 1 \pmod x\qquad \text{and }\\
\beta(n) &\equiv 0 \pmod x\end{align}
$$
and $g(x) = 0$ if there is no such value of $n$. For example, $g(3) = 0$, $g(5) = 12$.


Further define
$$ G(N) = \sum_{x=2}^{\strut N} g(x)$$
You are given $G(10^2) = 28891$ and $G(10^3)  = 13131583$.


Find $G(10^6)$.

##Степени 1+√7


При возведении $(1+\sqrt 7)$ в целочисленную степень $n$ мы всегда получим число вида $(a+b\sqrt 7)$.
Запишем $(1+\sqrt 7)^n = \alpha(n) + \beta(n)\sqrt 7$.


Для данного числа $x$ определим $g(x)$ как наименьшее натуральное чило $n$, такое что:
$$\begin{align}
\alpha(n) &\equiv 1 \pmod x\qquad \text{и }\\
\beta(n) &\equiv 0 \pmod x\end{align}
$$
и $g(x) = 0$, если такого значения $n$ не существует. Например, $g(3) = 0$, $g(5) = 12$.


Далее определим
$$ G(N) = \sum_{x=2}^{\strut N} g(x)$$
Известно, что $G(10^2) = 28891$ и $G(10^3)  = 13131583$.


Найдите $G(10^6)$.
 Оригинал
