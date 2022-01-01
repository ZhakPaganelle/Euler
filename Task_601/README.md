##Divisibility streaks


For every positive number $n$ we define the function  $streak(n)=k$   as the smallest positive integer $k$ such that $n+k$ is not divisible by $k+1$.
E.g:
13 is divisible by 1 
14 is divisible by 2 
15 is divisible by 3 
16 is divisible by 4 
17 is NOT divisible by 5 
So $streak(13) = 4$.  
Similarly:
120 is divisible by 1 
121 is NOT divisible by 2 
So $streak(120) = 1$.


Define $P(s, N)$ to be the number of integers $n$, $1 < n < N$, for which $streak(n) = s$.
So $P(3, 14) = 1$ and $P(6, 10^6) = 14286$.


Find the sum, as $i$ ranges from 1 to 31, of $P(i, 4^i)$.

##Серии делимостей


Для каждого положительного числа $n$ определим функцию $streak(n)=k$ как наименьшее натуральное число $k$, такое что $n+k$ не делится на $k+1$.
Например:
13 делится на 1;
14 делится на 2;
15 делится на 3;
16 делится на 4;
17 НЕ делится на 5.
Итак, $streak(13) = 4$.  
Таким же образом:
120 делится на 1;
121 НЕ делится на 2.
Итак, $streak(120) = 1$.


Определим $P(s, N)$ как количество целых чисел $n$, $1 < n < N$, для которых $streak(n) = s$.
Итак, $P(3, 14) = 1$ и $P(6, 10^6) = 14286$.


Найдите сумму $P(i, 4^i)$, где $i$ принимает значения от 1 до 31.

