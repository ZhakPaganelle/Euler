##Maximum Integer Partition Product

An integer partition of a number n is a way of writing n as a sum of positive integers.
Partitions that differ only in the order of their summands are considered the same.
A partition of n into distinct parts is a partition of n in which every part occurs at most once.
The partitions of 5 into distinct parts are:
5, 4+1 and 3+2.
Let f(n) be the maximum product of the parts of any such partition of n into distinct parts and let m(n) be the number of elements of any such partition of n with that product.
So f(5)=6 and m(5)=2.
For n=10 the partition with the largest product is 10=2+3+5, which gives f(10)=30 and m(10)=3.
And their product, f(10)·m(10) = 30·3 = 90
It can be verified that
∑ f(n)·m(n) for 1 ≤ n ≤ 100 = 1683550844462.
Find ∑ f(n)·m(n) for 1 ≤ n ≤ 1014.
Give your answer modulo 982451653, the 50 millionth prime.
##Максимальное произведение разбиения

Разбиение целого числа n — это представление n в виде суммы натуральных чисел — частей.
Разбиения, которые отличаются только порядком слагаемых, считаются одинаковыми.
Разбиение n на различные части — это разбиение n, в которое каждая часть входит не более одного раза.
Разбиения на различные части числа 5:
5, 4+1 и 3+2.
Пусть f(n) — максимальное произведение частей среди таких разбиений n на различные части, и пусть m(n) — количество элементов разбиения n с этим произведением.
Тогда f(5)=6 и m(5)=2.
Для n=10 разбиением с наибольшим произведением является 10=2+3+5, которое дает f(10)=30 и m(10)=3.
И их произведение, f(10)·m(10) = 30·3 = 90.
Можно убедиться, что
∑f(n)·m(n) для 1 ≤ n ≤ 100 = 1683550844462.
Найдите ∑f(n)·m(n) для 1 ≤ n ≤ 1014.
Дайте ответ по модулю 982451653 (это 50-миллионное простое число).
