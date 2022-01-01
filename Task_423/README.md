##Consecutive die throws

Let n be a positive integer.
A 6-sided die is thrown n times. Let c be the number of pairs of consecutive throws that give the same value.
For example, if n = 7 and the values of the die throws are (1,1,5,6,6,6,3), then the following pairs of consecutive throws give the same value:
(1,1,5,6,6,6,3)
(1,1,5,6,6,6,3)
(1,1,5,6,6,6,3)
Therefore, c = 3 for (1,1,5,6,6,6,3).
Define C(n) as the number of outcomes of throwing a 6-sided die n times such that c does not exceed π(n).1
For example, C(3) = 216, C(4) = 1290, C(11) = 361912500 and C(24) = 4727547363281250000.
Define S(L) as ∑ C(n) for 1 ≤ n ≤ L.
For example, S(50) mod 1 000 000 007 = 832833871.
Find S(50 000 000) mod 1 000 000 007.
 1 π denotes the prime-counting function, i.e. π(n) is the number of primes ≤ n.
##Последовательные броски кубика

Пусть n будет натуральным числом.
6-гранный кубик бросают n раз. Пусть c будет количеством пар последовательных бросков с одинаковым результатом.
Например, если n = 7 и были выброшены числа (1,1,5,6,6,6,3), тогда одинаковый результат имеют следующие пары последовательных бросков:
(1,1,5,6,6,6,3)
(1,1,5,6,6,6,3)
(1,1,5,6,6,6,3)
Посему, c = 3 для (1,1,5,6,6,6,3).
Определим C(n) как количество возможных реузальтатов n бросков 6-гранного кубика таких, что c не превышает π(n).1
Например, C(3) = 216, C(4) = 1290, C(11) = 361912500 и C(24) = 4727547363281250000.
Определим S(L) как ∑ C(n) для 1 ≤ n ≤ L.
Например, S(50) mod 1 000 000 007 = 832833871.
Найдите S(50 000 000) mod 1 000 000 007.
1 π обозначает функцию распределения простых чисел, т.е. π(n) - это количество простых чисел ≤ n.
