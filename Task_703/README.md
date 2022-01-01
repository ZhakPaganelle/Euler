##Circular Logic II

Given an integer $n$, $n \geq 3$, let $B=\{\mathrm{false},\mathrm{true}\}$ and let $B^n$ be the set of sequences of $n$ values from $B$. The function $f$ from $B^n$ to $B^n$ is defined by $f(b_1 \dots b_n) = c_1 \dots c_n$ where:
Let $S(n)$ be the number of functions $T$ from $B^n$ to $B$ such that for all $x$ in $B^n$, $T(x) ~\mathrm{AND}~ T(f(x)) = \mathrm{false}$.
You are given that $S(3) = 35$ and $S(4) = 2118$.
Find $S(20)$. Give your answer modulo $1\,001\,001\,011$.
##Круговая логика II

Для данного целого числа $n$, $n \geq 3$, пусть $B=\{\mathrm{false},\mathrm{true}\}$ и пусть $B^n$ будет множеством последовательностей $n$ значений из $B$. Функция $f$ для $B^n$ от $B^n$ определена как $f(b_1 \dots b_n) = c_1 \dots c_n$, где:

$c_i = b_{i+1}$ для $1 \leq i < n$.
$c_n = b_1 \;\mathrm{AND}\; (b_2 \;\mathrm{XOR}\; b_3)$, где $\mathrm{AND}$ и $\mathrm{XOR}$ - логические действия $\mathrm{AND}$ и исключающего $\mathrm{OR}$ .

Пусть $S(n)$ будет количеством функций $T$ для $B$ от $B^n$ таких что для всех $x$ в $B^n$ $T(x) ~\mathrm{AND}~ T(f(x)) = \mathrm{false}$.
Известно, что $S(3) = 35$ и $S(4) = 2118$.
Найдите $S(20)$. В качестве ответа приведите остаток от деления полученного результата на $1\,001\,001\,011$. Оригинал
