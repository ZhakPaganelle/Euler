##Numbers in decimal expansions

Let p = p1 p2 p3 ... be an infinite sequence of random digits, selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.
It can be seen that p corresponds to the real number 0.p1 p2 p3 .... 
It can also be seen that choosing a random real number from the interval [0,1) is equivalent to choosing an infinite sequence of random digits selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.
For any positive integer n with d decimal digits, let k be the smallest index such that pk, pk+1, ...pk+d-1 are the decimal digits of n, in the same order.
Also, let g(n) be the expected value of k; it can be proven that g(n) is always finite and, interestingly, always an integer number.
For example, if n = 535, then
for p = 31415926535897...., we get k = 9
for p = 355287143650049560000490848764084685354..., we get k = 36
etc and we find that g(535) = 1008.
Given that $\sum \limits_{n = 2}^{999} {g \left ( \left \lfloor \dfrac{10^6}{n} \right \rfloor \right )} = 27280188$, find $\sum \limits_{n = 2}^{999999} {g \left ( \left \lfloor \dfrac{10^{16}}{n} \right \rfloor \right )}$.
##Числа в десятичном расширении

Пусть p = p 1 p 2  p3 ... - бесконечная последовательность случайных цифр, выбираемых из множества {0,1,2,3,4,5,6,7,8,9} с равными вероятностями.
Нетрудно убедиться в том, что p соответствует действительному числу 0,p1  p2 p3  .... 
Также, легко заметить, что выбор случайного действительного числа из интервала [0,1) эквивалентен выбору бесконечной последовательности случайных цифр из множества {0,1,2,3,4,5,6,7,8,9} с равными вероятностями.
При любом натуральном числе n из d десятичных цифр, допустим, что k является наименьшим индексом, таким, что  p k, p k+1 , ...p k+d-1 являются десятичными цифрами n, при этом, в таком же порядке.
Помимо этого, пусть g(n) - ожидаемое значение k; можно доказать, чтоg(n) всегда конечное и, что самое интересное, целое число.
К примеру, если n = 535, то
при p = 31415926535897...., получим k = 9
при p = 355287143650049560000490848764084685354..., получим k = 36
и т.д., пока не обнаружим, что g(535) = 1008.
Известно, что . Найдите .
Примечание:  обозначает функцию округления в меньшую сторону.
