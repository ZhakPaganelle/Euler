##Infinite string tour

Create a sequence of numbers using the "Blum Blum Shub" pseudo-random number generator:
Concatenate these numbers  s0s1s2… to create a string w of infinite length.
Then, w = 14025256741014958470038053646…
For a positive integer k, if no substring of w exists with a sum of digits equal to k, p(k) is defined to be zero. If at least one substring of w exists with a sum of digits equal to k, we define p(k) = z, where z is the starting position of the earliest such substring.
For instance:
The substrings 1, 14, 1402, … 
with respective sums of digits equal to 1, 5, 7, …
start at position 1, hence p(1) = p(5) = p(7) = … = 1.
The substrings 4, 402, 4025, …
with respective sums of digits equal to 4, 6, 11, …
start at position 2, hence p(4) = p(6) = p(11) = … = 2.
The substrings 02, 0252, …
with respective sums of digits equal to 2, 9, …
start at position 3, hence p(2) = p(9) = … = 3.


Note that substring 025 starting at position 3, has a sum of digits equal to 7, but there was an earlier substring (starting at position 1) with a sum of digits equal to 7, so p(7) = 1, not 3.
We can verify that, for 0 < k ≤ 103, ∑ p(k) = 4742.
Find ∑ p(k), for 0 < k ≤ 2×1015.
##Бесконечное путешествие по строке

Создайте последовательность чисел с помощью генератора псевдослучайных чисел "Blum Blum Shub":


s0
=
14025256

sn+1
=
sn2 mod 20300713


Соедините эти числа  s0s1s2… чтобы получить строку w бесконечной длины.

Тогда, w = 14025256741014958470038053646…
Для натурального числа k, если не существует такой подстроки w, сумма чьих цифр равна k, p(k) определяется как равное нулю. Если существует хотя бы одна подстрока w, сумма чьих цифр равна k, мы определим p(k) = z, где z - начальная позиция первой такой подстроки.
Для примера:
Подстроки 1, 14, 1402, … 
с суммами цифр 1, 5, 7, … соответственно
начинаются с позиции 1, посему p(1) = p(5) = p(7) = … = 1.
Подстроки 4, 402, 4025, …
с суммами цифр 4, 6, 11, … соответственно
начинаются с позиции 2, посему p(4) = p(6) = p(11) = … = 2.
Подстроки 02, 0252, …
с суммами цифр 2, 9, … соответственно
начинаются с позиции 3, посему p(2) = p(9) = … = 3.
Обратите внимание, что подстрока 025, начинающаяся с позиции 3, имеет сумму цифр, равную 7, однако существует подстрока до нее (начинающаяся с позиции 1) с суммой цифр, равной 7, поэтому p(7) = 1, а не 3.
Можно показать, что для 0 < k ≤ 103, ∑ p(k) = 4742.
Найдите ∑ p(k) для 0 < k ≤ 2·1015.
