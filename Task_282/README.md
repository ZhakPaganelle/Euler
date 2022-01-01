##The Ackermann function


For non-negative integers $m$, $n$, the Ackermann function $A(m,n)$ is defined as follows:

$$
A(m,n) = \cases{
n+1 &$\htmltext{ if  }m=0$\cr
A(m-1,1) &$\htmltext{ if   }m>0 \htmltext{  and  } n=0$\cr
A(m-1,A(m,n-1)) &$\htmltext{ if   }m>0 \htmltext{  and  } n>0$\cr
}$$


For example $A(1,0) = 2$, $A(2,2) = 7$ and $A(3,4) = 125$.


Find $\displaystyle\sum_{n=0}^6 A(n,n)$ and give your answer mod $14^8$.
##Функция Аккермана

Для неотрицательных целых чисел m, n, функция Аккермана A(m, n)

определяется следующим образом:



Например, A(1, 0) = 2, A(2, 2) = 7 и A(3, 4) = 125.


Найдите ∑0 ≤n ≤ 6 A

(n, n) и приведите ответ по mod 148.
