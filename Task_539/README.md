##Odd elimination


Start from an ordered list of all integers from 1 to n. Going from left to right, remove the first number and every other number afterward until the end of the list. Repeat the procedure from right to left, removing the right most number and every other number from the numbers left. Continue removing every other numbers, alternating left to right and right to left, until a single number remains.


Starting with n = 9, we have:1 2 3 4 5 6 7 8 9
2 4 6 82 6
6


Let P(n) be the last number left starting with a list of length n.
Let $\displaystyle S(n) = \sum_{k=1}^n P(k)$.
You are given P(1)=1, P(9) = 6, P(1000)=510, S(1000)=268271.


Find S(1018) mod 987654321.

##Нечетный отсев


Начните с упорядоченного списка всех целых чисел от 1 до n. Двигаясь слева направо, исключите из списка первое число и каждое второе следующее за ним число до конца списка. Повторите эту процедуру справа налево, исключая из списка самое правое число и каждое второе число налево от него. Продолжайте исключать из списка каждое второе число, меняя направление слева направо и справа налево, пока не останется одно единственное число.


Начав с n = 9, мы получим:1 2 3 4 5 6 7 8 9
2 4 6 82 6
6


Пусть P(n) будет последним оставшимся числом из списка длиной n.
Пусть $\displaystyle S(n) = \sum_{k=1}^n P(k)$.
Известно, что P(1)=1, P(9) = 6, P(1000)=510, S(1000)=268271.


Найдите S(1018) mod 987654321.

