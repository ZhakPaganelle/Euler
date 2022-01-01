##Searching for a maximum-sum subsequence

Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).
Now, let us repeat the search, but on a much larger scale:
First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":
For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.
Thus, s10 = −393027 and s100 = 86613.
The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.
Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
##Поиск подпоследовательностей с максимальной суммой

Взглянув в таблицу ниже, легко убедиться в том, что максимально возможная сумма соседних чисел в любом направлении (горизонтальном, вертикальном, обоих диагональных) равна 16 (= 8 + 7 + 1).

−2532
9−651
3273
−18−4  8

Теперь, давайте повторим поиск, но на этот раз в гораздо более крупных масштабах:
Для начала, сгенерируем четыре миллиона псевдо-случайных чисел с помощью особой формы "запаздывающего генератора Фибоначчи":
Для 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
Для 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.
Таким образом, s10 = −393027 и s100 = 86613.
Затем члены s упорядочиваются в виде таблицы размерами 2000×2000, при этом первыми 2000 числами последовательно заполняется первая строка, следущими 2000 числами - вторая строка, и т.д.
Наконец, найдите наибольшую сумму любого количества соседних записей в любом направлении (по горизонтали, по вертикали и по диагонали).
