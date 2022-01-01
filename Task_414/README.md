##Kaprekar constant


6174 is a remarkable number; if we sort its digits in increasing order and subtract that number from the number you get when you sort the digits in decreasing order, we get 7641-1467=6174.
Even more remarkable is that if we start from any 4 digit number and repeat this process of sorting and subtracting, we'll eventually end up with 6174 or immediately with 0 if all digits are equal. 
This also works with numbers that have less than 4 digits if we pad the number with leading zeroes until we have 4 digits.
E.g. let's start with the number 0837:
8730-0378=8352
8532-2358=6174


6174 is called the Kaprekar constant. The process of sorting and subtracting and repeating this until either 0 or the Kaprekar constant is reached is called the Kaprekar routine.


We can consider the Kaprekar routine for other bases and number of digits. 
Unfortunately, it is not guaranteed a Kaprekar constant exists in all cases; either the routine can end up in a cycle for some input numbers or the constant the routine arrives at can be different for different input numbers.
However, it can be shown that for 5 digits and a base b = 6t+3≠9, a Kaprekar constant exists.
E.g. base 15: (10,4,14,9,5)15
base 21: (14,6,20,13,7)21

Define Cb to be the Kaprekar constant in base b for 5 digits.
Define the function sb(i) to be


Define S(b) as the sum of sb(i) for 0 < i < b5.
E.g. S(15) = 5274369 
S(111) = 400668930299


Find the sum of S(6k+3) for 2 ≤ k ≤ 300.
Give the last 18 digits as your answer.

##Постоянная Капрекара


6174 - примечательное число: если мы упорядочим его цифры в порядке возрастания и вычтем полученное число из числа, полученного упорядочиванием тех же цифр по убыванию, мы получим 7641-1467=6174.
Еще более примечательно то, что начав с любого четырехзначного числа и повторяя описанный процесс упорядочивания цифр и вычитания, мы в конце концов получим 6174 или сразу 0, если все цифры одинаковы. 
Это также происходит и с числами с меньшим количеством цифр, если мы дополним их ведущими нулями до 4-хзначного числа.
К примеру, начнем с числа 0837:
8730-0378=8352
8532-2358=6174


6174 называется постоянной Капрекара. Процесс упорядочивания цифр и вычитания, повторяемый до получения числа 0 или постоянной Капрекара, называется преобразованием Капрекара.


Можно рассмотреть преобразования Капрекара для других систем исчисления и другого количества цифр. 
К сожалению, постоянная Капрекара существует не во всех случаях: преобразование может привести к циклу при некоторых исходных числах, или же постоянная, к которой преобразование приведет, может быть разной для разных исходных чисел.
Тем не менее, можно показать, что для 5-изначных чисел в основании b = 6t+3≠9 постоянная Капрекара существует.
Например, основание 15: (10,4,14,9,5)15
основание 21: (14,6,20,13,7)21


Определим Cb как постоянную Капрекара в основании b для 5-изначных чисел.
Определим функцию sb(i), равную

 0, если i = Cb или если i, записанное в основании b, состоит из 5 одинаковых цифр
 числу итераций преобразования Капрекара в основании b, приводящему к Cb, во всех остальных случаях

Заметим, что мы можем определить sb(i) для всех целых i < b5. Если i, записанное в основании b, имеет меньше пяти цифр, то это число дополняется ведущими нулями до пятизначного перед тем, как применяется преобразование Капрекара.


Определим S(b) как сумму sb(i) для 0 < i < b5.
Например S(15) = 5274369 
S(111) = 400668930299


Найдите сумму S(6k+3) для 2 ≤ k ≤ 300.
В качестве ответа приведите последние 18 цифр полученного числа.

