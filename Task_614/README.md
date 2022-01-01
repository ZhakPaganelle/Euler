##Special partitions 2

An integer partition of a number $n$ is a way of writing $n$ as a sum of positive integers. Partitions that differ only by the order of their summands are considered the same.
We call an integer partition special if 1) all its summands are distinct, and 2) all its even summands are also divisible by 4. For example, the special partitions of $10$ are: \[10 = 1+4+5=3+7=1+9\]
The number $10$ admits many more integer partitions (a total of 42), but only those three are special.
Let be $P(n)$ the number of special integer partitions of $n$. You are given that $P(1) = 1$, $P(2) = 0$, $P(3) = 1$, $P(6) = 1$, $P(10)=3$, $P(100) = 37076$ and $P(1000)=3699177285485660336$.
Find $\displaystyle \sum_{i=1}^{10^7}{P(i)}$. Give the result modulo $10^9+7$.
##Особые разложения 2

Целочисленное разложение числа $n$ - это способ записи $n$ как суммы натуральных чисел. Разложения, различающиеся только порядком слагаемых, считаются одинаковыми.
Назовем целочисленное разложение особым, если 1) все его слагаемые различны и 2) все его четные слагаемые также делятся на 4. 
Например, особыми разложениями числа $10$ являются: \[10 = 1+4+5=3+7=1+9\]
Число $10$ имеет куда больше целочисленных разложений (всего 42), но только эти три являются особыми.
Пусть $P(n)$ будет количеством особых целочисленных разложений числа $n$. Известно, что $P(1) = 1$, $P(2) = 0$, $P(3) = 1$, $P(6) = 1$, $P(10) = 3$, $P(100) = 37076$ и $P(1000) = 3699177285485660336$.
Найдите $\displaystyle \sum_{i=1}^{10^7}{P(i)}$. В качестве ответа приведите остаток от деления полученного числа на $10^9+7$.
