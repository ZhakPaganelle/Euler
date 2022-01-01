##Minimum of subsequences

Let $S_n$ be an integer sequence produced with the following pseudo-random number generator:

Let $A(i, j)$ be the minimum of the numbers $S_i, S_{i+1}, \ldots, S_j$ for $i\le j$.
Let $M(N) = \sum A(i, j)$ for $1 \le i \le j \le N$.
We can verify that $M(10) = 432256955$ and $M(10\,000) = 3264567774119$.

Find $M(2\,000\,000\,000)$.

##Минимум подпоследовательностей



Пусть Sn будет последовательностью целых чисел, созданной с помощью следующего генератора псевдослучайных чисел:



S0
= 
290797 

Sn+1
= 
Sn2 mod 50515093



Пусть A(i, j) будет минимум чисел Si, Si+1, ... , Sj для i 
≤
 j.
Пусть M(N) = ΣA(i, j) для 1 
≤
 i 
≤
 j 
≤
 N.



Можно убедиться, что M(10) = 432256955 и M(10 000) = 3264567774119.


Найдите M(2 000 000 000).

