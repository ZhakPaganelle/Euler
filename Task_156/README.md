##Counting Digits

Starting from zero the natural numbers are written down in base 10 like this:

0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n, we will update the number of ones that have occurred and call this number f(n,1). The first values for f(n,1), then, are as follows:
Note that f(n,1) never equals 3.

So the first two solutions of the equation f(n,1)=n are n=0 and n=1. The next solution is n=199981.
In the same manner the function f(n,d) gives the total number of digits d that have been written down after the number n has been written.

In fact, for every digit d ≠ 0, 0 is the first solution of the equation f(n,d)=n.
Let s(d) be the sum of all the solutions for which f(n,d)=n.

You are given that s(1)=22786974071.
Find  ∑ s(d) for 1 ≤ d ≤ 9.
Note: if, for some n, f(n,d)=n
 for more than one value of d this value of n is counted again for every value of d for which f(n,d)=n.
##Подсчет цифр

Начиная с нуля, натуральные числа записываются в основании 10 следующим способом:

0 1 2 3 4 5 6 7 8 9 10 11 12....

Рассмотрим цифру d=1. Записывая по порядку каждое из n чисел, мы обновляем счетчик цифр 1, появлявшихся в записанных числах, и полученное значение назовем f(n,1). В таком случае, первые значения f(n,1) будут следующими:



nf(n,1)

00

11

21

31

41

51

61

71

81

91

102

114

125

Заметим, что f(n,1) никогда не принимает значение 3.

Таким образом, первыми двумя решениями уравнения f(n,1)=n будут n=0 и n=1. Следующее решение равно n=199981.
Аналогичным образом, значение функции f(n,d) равно числу встретившихся цифр d, при записи всех целых чисел от 0 до n.

Между прочим, для каждой цифры d ≠ 0, первое решение уравнения f (n,d)=n равно 0.
Пусть s(d) является суммой всех решений, для которых f(n,d)=n.

Известно, что s(1)=22786974071.
Найдите ∑ s(d), где 1 ≤ d ≤ 9.
Примечание: если при некоторых значениях n функция f(n,d) равна n для более, чем одного значения d, то полученное значение n прибавляется вновь при каждой цифре d, для которой f(n,d)=n.
