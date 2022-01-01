##Flexible digit sum


Given any positive integer $n$, we can construct a new integer by inserting plus signs between some of the digits of the base $B$ representation of $n$, and then carrying out the additions.


For example, from $n=123_{10}$  ($n$ in base 10) we can construct the four base 10 integers $123_{10}$,  $1+23=24_{10}$, $12+3=15_{10}$ and $1+2+3=6_{10}$


Let $f(n,B)$  be the smallest number of steps needed to arrive at a single-digit number in base $B$. For example, $f(7,10)=0$ and $f(123,10)=1$.


Let $g(n,B_1,B_2)$ be the sum of the positive integers $i$ not exceeding $n$ such that $f(i,B_1)=f(i,B_2)$.


You are given $g(100,10,3)=3302$. 


Find $g(10^7,10,3)$

##Гибкая сумма цифр


При любом данном натуральном числе $n$ можно построить новое целое число путем вставки знаков "плюс" между некоторыми цифрами числа $n$, представленного в $B$-ичной системе счисления, и выполнения сложения.


Например, из $n=123_{10}$ ($n$ в 10-ичной системе счисления) мы можем построить четыре целых числа в 10-ичной системе счисления: $123_{10}$, $1+23=24_{10}$, $12+3=15_{10}$ и $1+2+3=6_{10}$


Пусть $f(n,B)$ будет наименьшим количеством шагов, необходимых для получения однозначного числа в $B$-ичной системе счисления. Например, $f(7,10)=0$ и $f(123,10)=1$.


Пусть $g(n,B_1,B_2)$ будет суммой натуральных чисел $i$ не превышающих $n$, таких что $f(i,B_1)=f(i,B_2)$.


Известно, что $g(100,10,3)=3302$. 


Найдите $g(10^7,10,3)$

