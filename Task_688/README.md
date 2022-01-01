##Piles of Plates


We stack $n$ plates into $k$ non-empty piles where each pile is a different size. Define $f(n,k)$ to be the maximum number of plates possible in the smallest pile. For example when $n = 10$ and $k = 3$ the piles $2,3,5$ is the best that can be done and so $f(10,3) = 2$. It is impossible to divide 10 into 5 non-empty differently-sized piles and hence $f(10,5) = 0$.


Define $F(n)$ to be the sum of $f(n,k)$ for all possible pile sizes $k\ge 1$. For example $F(100) = 275$.


Further define $S(N) = \displaystyle\sum_{n=1}^N F(n)$. You are given $S(100) = 12656$.


Find $S(10^{16})$ giving your answer modulo $1\,000\,000\,007$.

##Стопки тарелок


Мы складываем $n$ тарелок в $k$ непустых стопок так, что все стопки имеют разный размер. Определим $f(n,k)$ как наибольшее возможное количество тарелок в самой маленькой стопке. Например, когда $n = 10$ и $k = 3$, стопки размеров $2,3,5$ являются самым лучшим решением, и таким образом $f(10,3) = 2$. 10 тарелок невозможно разделить на 5 непустых стопок различных размеров, поэтому $f(10,5) = 0$.


Определим $F(n)$ как сумму $f(n,k)$ для всех возможных количеств стопок $k\ge 1$. Например, $F(100) = 275$.


Далее определим $S(N) = \displaystyle\sum_{n=1}^N F(n)$. Известно, что $S(100) = 12656$.


Найдите $S(10^{16})$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
