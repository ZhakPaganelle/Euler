##Investigating Gaussian Integers

As we all know the equation x2=-1 has no solutions for real x.

If we however introduce the imaginary number i this equation has two solutions: x=i and x=-i.

If we go a step further the equation (x-3)2=-4 has two complex solutions: x=3+2i and x=3-2i.
x=3+2i and x=3-2i are called each others' complex conjugate.

Numbers of the form a+bi are called complex numbers.

In general a+bi and a−bi are each other's complex conjugate.
A Gaussian Integer is a complex number a+bi such that both a and b are integers.

The regular integers are also Gaussian integers (with b=0).

To distinguish them from Gaussian integers with b ≠ 0 we call such integers "rational integers."

A Gaussian integer is called a divisor of a rational integer n if the result is also a Gaussian integer.

If for example we divide 5 by 1+2i we can simplify $\dfrac{5}{1 + 2i}$ in the following manner:

Multiply numerator and denominator by the complex conjugate of 1+2i: 1−2i.

The result is $\dfrac{5}{1 + 2i} = \dfrac{5}{1 + 2i}\dfrac{1 - 2i}{1 - 2i} = \dfrac{5(1 - 2i)}{1 - (2i)^2} = \dfrac{5(1 - 2i)}{1 - (-4)} = \dfrac{5(1 - 2i)}{5} = 1 - 2i$.

So 1+2i is a divisor of 5.

Note that 1+i is not a divisor of 5 because $\dfrac{5}{1 + i} = \dfrac{5}{2} - \dfrac{5}{2}i$.

Note also that if the Gaussian Integer (a+bi) is a divisor of a rational integer n, then its complex conjugate (a−bi) is also a divisor of n.
In fact, 5 has six divisors such that the real part is positive: {1, 1 + 2i, 1 − 2i, 2 + i, 2 − i, 5}.

The following is a table of all of the divisors for the first five positive rational integers:
For divisors with positive real parts, then, we have: $\sum \limits_{n = 1}^{5} {s(n)} = 35$.
For $\sum \limits_{n = 1}^{10^5} {s(n)} = 17924657155$.
What is $\sum \limits_{n = 1}^{10^8} {s(n)}$?
##Исследование целых чисел Гаусса

Как известно, уравнение x2=-1 не имеет решений в области действительных значений x.

Однако, если ввести мнимое число i, то у такого уравнения будет два решения: x=i и x=-i.

Если продолжить, то уравнение (x-3)2=-4 имеет два комплексных решения: x=3+2i и x=3-2i.

x=3+2i и x=3-2i, которые называют сопряженными друг другу.

Числа вида a+bi принято называть комплексными числами.

В общем случае, числа a+bi и a−bi являются комплексно-сопряженными.
Целое Гаусса - это такое комплексное число a+bi, для которого a и b являются целыми числами.

Обычные целые числа также являются целыми Гаусса (при b=0).

Для того чтобы отличить такие числа от целых Гаусса, у которых b ≠ 0, будем называть их "рациональными целыми числами."

Целое Гаусса называют делителем рационального целого числа, если результат деления также является целым Гаусса.

К примеру, если мы разделим 5 на 1+2i, то полученное выражение  можно упростить следующим способом:

Домножим числитель и знаменатель дроби на комплексно сопряженное значение числа 1+2i: 1−2i.

Получим
.

Таким образом, 1+2i является делителем числа 5.

Обратите внимание, что 1+i не является делителем числа 5, поскольку .

Также заметьте, что если целое Гаусса (a+bi) является делителем рационального целого числа n, то комплексно сопряженное ему число (a−bi) также будет являться делителем n.
Между прочим, для числа 5 существует 6 делителей с положительной вещественной частью: {1, 1 + 2i, 1 − 2i, 2 + i, 2 − i, 5}.

Ниже приведена таблица всех делителей для первых пяти положительных рациональных целых чисел:


n Делители целых Гаусса
с положительной веществ. частьюСумма s(n) этих делителей
111

21, 1+i, 1-i, 25

31, 34

41, 1+i, 1-i, 2, 2+2i, 2-2i,413

51, 1+2i, 1-2i, 2+i, 2-i, 512

В таком случае, для делителей с положительными вещественными частями, мы можем найти следующую сумму: .
При 1 ≤ n ≤ 105, ∑ s(n)=17924657155.
Чему равна сумма ∑ s(n), если 1 ≤ n ≤ 108?
