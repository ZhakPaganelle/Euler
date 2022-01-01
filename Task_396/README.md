##Weak Goodstein sequence


For any positive integer n, the nth weak Goodstein sequence {g1, g2, g3, ...} is defined as:


For example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}:


It can be shown that every weak Goodstein sequence terminates.


Let G(n) be the number of nonzero elements in the nth weak Goodstein sequence.
It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381.
It can also be verified that ∑ G(n) = 2517 for 1 ≤ n < 8.


Find the last 9 digits of ∑ G(n) for 1 ≤ n < 16.

##Слабые последовательности Гудштайна


Для любого натурального n, n-тая слабая последовательность Гудштайна {g1, g2, g3, ...} определяется следующим образом:


 g1 = n
 для k > 1, gk находится, записывая gk-1 по основанию k, интерпретируя его как число по основанию k + 1 и вычитая 1.


Последовательность завершается, когда gk принимает значение 0.


Например, шестая слабая последовательность Гудштайна - {6, 11, 17, 25, ...}:


 g1 = 6;
 g2 = 11, так как 6 = 1102, 1103 = 12, и 12 - 1 = 11;
 g3 = 17, так как 11 = 1023, 1024 = 18, и 18 - 1 = 17;
 g4 = 25, так как 17 = 1014, 1015 = 26, и 26 - 1 = 25;


и так далее.


Можно показать, что каждая слабая последовательность Гудштайна конечна.


Пусть G(n) будет количеством ненулевых элеметов n-той слабой последовательности Гудштайна.
Может быть доказано, что G(2) = 3, G(4) = 21 и G(6) = 381.
Может также быть доказано, что ΣG(n) = 2517 для 1 ≤ n < 8.


Найдите последние 9 цифр ΣG(n) для 1 ≤ n < 16.

