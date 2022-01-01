##π sequences


For every $n \ge 1$ the prime-counting function $\pi(n)$ is equal to the number of primes
not exceeding $n$.
E.g. $\pi(6)=3$ and $\pi(100)=25$.


We say that a sequence of integers $u  = (u_0,\cdots,u_m)$ is a $\pi$ sequence if 


For $u_0=10$ there are three distinct $\pi$ sequences: (10,4),  (10,4,2) and (10,4,2,1).


Let  $c(u)$ be the number of elements of $u$ that are not prime.
Let $p(n,k)$ be the number of $\pi$ sequences $u$  for which $u_0\le n$ and $c(u)=k$.
Let $P(n)$ be the product of all $p(n,k)$ that are larger than 0.
You are given: P(10)=3×8×9×3=648 and P(100)=31038676032.


Find $P(10^8)$. Give your answer modulo 1000000007. 

##Последовательности π


Для каждого $n \ge 1$ функция подсчета простых чисел $\pi(n)$ равна количеству простых чисел не больше $n$.
Например, $\pi(6)=3$ и $\pi(100)=25$.


Скажем, что последовательность целых чисел $u  = (u_0,\cdots,u_m)$ является последовательностью $\pi$, если 
 $u_n \ge 1$ для каждого $n$
 $u_{n+1}= \pi(u_n)$
 $u$ имеет два или больше элементов

Для $u_0=10$ существует три различные последовательности $\pi$: (10,4), (10,4,2) и (10,4,2,1).


Пусть $c(u)$ будет количеством элементов $u$, которые не являются простыми числами.
Пусть $p(n,k)$ будет количеством последовательностей $\pi$ $u$, для которых $u_0\le n$ и $c(u)=k$.
Пусть $P(n)$ будет произведением всех $p(n,k)$ больше 0.
Известно: P(10)=3×8×9×3=648 и P(100)=31038676032.


Найдите $P(10^8)$. В качестве ответа дайте остаток от деления полученного результата на 1000000007. 

