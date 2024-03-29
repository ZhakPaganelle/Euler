##Square prime factors II

For an integer $n$, we define the square prime factors of $n$ to be the primes whose square divides $n$. For example, the square prime factors of $1500=2^2 \times 3 \times 5^3$ are $2$ and $5$.
Let $C_k(N)$ be the number of integers between $1$ and $N$ inclusive with exactly $k$ square prime factors. It can be shown that with growing $N$ the ratio $\frac{C_k(N)}{N}$ gets arbitrarily close to a constant $c_{k}^{\infty}$, as suggested by the table below.
##Квадратные простые множители II

Для целого числа $n$ определим квадратные простые множители $n$ как простые числа, на чьи квадраты делится число $n$. Например, квадратные простые множители числа $1500=2^2 \times 3 \times 5^3$ равны $2$ и $5$.
Пусть $C_k(N)$ будет количеством целых чисел между $1$ и $N$ включительно, имеющих ровно $k$ квадратных простых множителей. Можно показать, что при увеличении $N$ дробь $\frac{C_k(N)}{N}$ приближается сколь угодно близко к постоянной $c_{k}^{\infty}$, как показан в таблице ниже.

\[\begin{array}{|c|c|c|c|c|c|}
\hline
& k = 0 & k = 1 & k = 2 & k = 3 & k = 4 \\
\hline
C_k(10) & 7 & 3 & 0 & 0 & 0 \\
\hline
C_k(10^2) & 61 & 36 & 3 & 0 & 0 \\
\hline
C_k(10^3) & 608 & 343 & 48 & 1 & 0 \\
\hline
C_k(10^4) & 6083 & 3363 & 533 & 21 & 0 \\
\hline
C_k(10^5) & 60794 & 33562 & 5345 & 297 & 2 \\
\hline
C_k(10^6) & 607926 & 335438 & 53358 & 3218 & 60 \\
\hline
C_k(10^7) & 6079291 & 3353956 & 533140 & 32777 & 834 \\
\hline
C_k(10^8) & 60792694 & 33539196 & 5329747 & 329028 & 9257 \\
\hline
C_k(10^9) & 607927124 & 335389706 & 53294365 & 3291791 & 95821 \\
\hline
c_k^{\infty} & \frac{6}{\pi^2} & 3.3539\times 10^{-1} & 5.3293\times 10^{-2} & 3.2921\times 10^{-3} & 9.7046\times 10^{-5}\\
\hline
\end{array}\]

Найдите $c_{7}^{\infty}$. Дайте ответ в стандартном виде числа, округленный до 5 значимых цифр, используя $e$ для отделения мантиссы от порядка. Например, если ответом является число $0.000123456789$, его надо привести в виде $1.2346e\text{-}4$.
