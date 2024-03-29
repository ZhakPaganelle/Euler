##Randomly Decaying Sequence

Given a fixed real number $c$, define a random sequence $(X_n)_{n\ge 0}$ by the following random process:
If we desire there to be precisely a 25% probability that $X_{100}<1$, then this can be arranged by fixing $c$ such that $\log_{10} c \approx 46.27$.
Suppose now that $c$ is set to a different value, so that there is precisely a 25% probability that $X_{10\,000\,000}<1$.
Find $\log_{10} c$ and give your answer rounded to two places after the decimal point.
##Случайно затухающая последовательность

Для выбранного вещественного числа $c$ зададим случайную последовательность $(X_n)_{n\ge 0}$ следующим случайным процессом:

$X_0 = c$ (с вероятностью 1).
Для $n>0$, $X_n = U_n X_{n-1}$, где $U_n$ - случайно выбранное вещественное число между нулем и единицей, равномерно и независимо от предыдущих выбранных чисел $(U_m)_{m<n}$.

Если мы хотим достичь точной вероятности 25% того, что $X_{100}<1$, это можно сделать, задав значение $c$ такое, что $\log_{10} c \approx 46.27$.
Положим, что $c$ задано такое значение, что вероятность $X_{10\,000\,000}<1$ равна ровно 25%.
Найдите $\log_{10} c$ и дайте ваш ответ округленным до второго знака после десятичной точки.
Оригинал
