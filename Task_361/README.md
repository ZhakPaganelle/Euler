##Subsequence of Thue-Morse sequence

The Thue-Morse sequence {Tn} is a binary sequence satisfying:

The first several terms of {Tn} are given as follows:
01101001100101101001011001101001....


We define {An} as the sorted sequence of integers such that the binary expression of each element appears as a subsequence in {Tn}.
For example, the decimal number 18 is expressed as 10010 in binary. 10010 appears in {Tn} (T8 to T12), so 18 is an element of {An}.
The decimal number 14 is expressed as 1110 in binary. 1110 never appears in {Tn}, so 14 is not an element of {An}.


The first several terms of An are given as follows:

We can also verify that A100 = 3251 and A1000 = 80852364498.


Find the last 9 digits of $\sum \limits_{k = 1}^{18} {A_{10^k}}$.

##Подпоследовательность последовательности Морса-Туэ


Последовательность Морса-Туэ {Tn} - это двоичная последовательность, удовлетворяющая следующим условиям:


T0 = 0
T2n = Tn
T2n+1 = 1 - Tn


Первые несколько элементов {Tn} выглядят следующим образом:

01101001100101101001011001101001....


Определим {An} как отсортированную последовательность целых чисел такую, что двоичная форма каждого элемента является подпоследовательностью {Tn}.

Например, десятичное число 18 в двоичном виде выглядит как 10010. 10010 встречается в {Tn} (от T8 до T12), значит, 18 являестя элементом {An}.

Десятичное число 14 в двоичном виде выглядит как 1110. 1110 никогда не встречается в {Tn}, значит, 14 не является элементом {An}.


Первые несколько элементов An выглядят следующим образом:





n0123456789101112…
An012345691011121318…

Мы также можем убедиться, что A100 = 3251 и A1000 = 80852364498.


Найдите последние 9 цифр значения .

