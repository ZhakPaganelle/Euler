##Superinteger

An integer s is called a superinteger of another integer n if the digits of n form a subsequence of the digits of s.
For example, 2718281828 is a superinteger of 18828, while 314159 is not a superinteger of 151.

Let p(n) be the nth prime number, and let c(n) be the nth composite number. For example, p(1) = 2, p(10) = 29, c(1) = 4 and c(10) = 18.
{p(i) : i ≥ 1} = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...}
{c(i) : i ≥ 1} = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, ...}
Let PD the sequence of the digital roots of {p(i)} (CD is defined similarly for {c(i)}):
PD = {2, 3, 5, 7, 2, 4, 8, 1, 5, 2, ...}
CD = {4, 6, 8, 9, 1, 3, 5, 6, 7, 9, ...}
Let Pn be the integer formed by concatenating the first n elements of PD (Cn is defined similarly for CD).
P10 = 2357248152
C10 = 4689135679
Let f(n) be the smallest positive integer that is a common superinteger of Pn and Cn. For example, f(10) = 2357246891352679, and f(100) mod 1 000 000 007 = 771661825.
Find f(10 000) mod 1 000 000 007.
##Суперцелое

Целое число s называется суперцелым по отношению к другому целому n, если цифры числа n образуют подпоследовательность цифр числа s.
Например, 2718281828 является суперцелым по отношению к 18828, в то время как 314159 не является суперцелым по отношению к 151.

Пусть p(n) будет n-тым простым числом, а c(n) будет n-тым составным числом. Например, p(1) = 2, p(10) = 29, c(1) = 4 и c(10) = 18.
{p(i) : i ≥ 1} = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...}
{c(i) : i ≥ 1} = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, ...}
Пусть PD будет последовательностью цифровых корней {p(i)} (CD определяется аналогичным образом для {c(i)}):
PD = {2, 3, 5, 7, 2, 4, 8, 1, 5, 2, ...}
CD = {4, 6, 8, 9, 1, 3, 5, 6, 7, 9, ...}
Пусть Pn будет целым числом, образованным путем объединения первых n элементов PD (Cn определяется аналогичным образом для CD).
P10 = 2357248152
C10 = 4689135679
Пусть f(n) будет наименьшим целым числом, являющимся суперцелым как по отношению к Pn, так и к Cn. Например, f(10) = 2357246891352679 и f(100) mod 1 000 000 007 = 771661825.
Найдите f(10 000) mod 1 000 000 007.
