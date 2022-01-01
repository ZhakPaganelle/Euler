##One more one

Consider the following process that can be applied recursively to any positive integer $n$:
Define $g(n)$ to be the number of 1's that must be added before the process ends. For example:
Eight 1's are added so $g(125) = 8$. Similarly $g(1000) = 9$ and $g(10000) = 21$.
Define $S(N) = \sum_{n=1}^{N} g(n)$ and $H(K) = S\left(\frac{7^K-1}{11}\right)$. You are given $H(10) = 690409338$.
Find $H(10^9)$ modulo $1\,117\,117\,717$.
##Еще одна единица

Рассмотрим следующий процесс, который рекурсивно применим к любому натуральному числу $n$:

если $n = 1$, ничего не происходит и процесс завершается,
если $n$ делится на 7, разделить его на 7,
иначе, прибавить 1.

Определим $g(n)$ как количество единиц, которые необходимо прибавить до конца процесса. Например:
$125\xrightarrow{\scriptsize{+1}} 126\xrightarrow{\scriptsize{\div 7}} 18\xrightarrow{\scriptsize{+1}} 19\xrightarrow{\scriptsize{+1}} 20\xrightarrow{\scriptsize{+1}} 21\xrightarrow{\scriptsize{\div 7}} 3\xrightarrow{\scriptsize{+1}} 4\xrightarrow{\scriptsize{+1}} 5\xrightarrow{\scriptsize{+1}} 6\xrightarrow{\scriptsize{+1}} 7\xrightarrow{\scriptsize{\div 7}} 1$.
Добавлено 8 единиц, таким образом, $g(125) = 8$. Аналогично, $g(1000) = 9$ и $g(10000) = 21$.
Определим $S(N) = \sum_{n=1}^{N} g(n)$ и $H(K) = S\left(\frac{7^K-1}{11}\right)$. Известно, что $H(10) = 690409338$.
Найдите $H(10^9)$ mod $1\,117\,117\,717$.
