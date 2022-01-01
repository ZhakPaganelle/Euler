##Solving $\mathcal{I}$-equations

We define the $\mathcal{I}$ operator as the function
\[\mathcal{I}(x,y) = (1+x+y)^2+y-x\]
and $\mathcal{I}$-expressions as arithmetic expressions built only from variables names and applications of $\mathcal{I}$. A variable name may consist of one or more letters. For example, the three expressions $x$, $\mathcal{I}(x,y)$, and $\mathcal{I}(\mathcal{I}(x,ab),x)$ are all $\mathcal{I}$-expressions.
For two $\mathcal{I}$-expressions $e_1$ and $e_2$ such that the equation $e_1=e_2$ has a solution in non-negative integers, we define the least simultaneous value of $e_1$ and $e_2$ to be the minimum value taken by $e_1$ and $e_2$ on such a solution. If the equation $e_1=e_2$ has no solution in non-negative integers, we define the least simultaneous value of $e_1$ and $e_2$ to be $0$. For example, consider the following three $\mathcal{I}$-expressions:
\[\begin{array}{l}A = \mathcal{I}(x,\mathcal{I}(z,t))\\
B = \mathcal{I}(\mathcal{I}(y,z),y)\\
C = \mathcal{I}(\mathcal{I}(x,z),y)\end{array}\]
The least simultaneous value of $A$ and $B$ is $23$, attained for $x=3,y=1,z=t=0$. On the other hand, $A=C$ has no solutions in non-negative integers, so the least simultaneous value of $A$ and $C$ is $0$. The total sum of least simultaneous pairs made of $\mathcal{I}$-expressions from $\{A,B,C\}$ is $26$.
Find the sum of least simultaneous values of all $\mathcal{I}$-expressions pairs made of distinct expressions from file I-expressions.txt (pairs $(e_1,e_2)$ and $(e_2,e_1)$ are considered to be identical). Give the last nine digits of the result as the answer.
##Решение $\mathcal{I}$-уравнений

Определим оператор $\mathcal{I}$ как функцию \[\mathcal{I}(x,y) = (1+x+y)^2+y-x\] и $\mathcal{I}$-выражения как арифметические выражения, составленные только из имен переменных и применения оператора $\mathcal{I}$. Имя переменной может состоять из одной или нескольких букв. Например, все три выражения $x$, $\mathcal{I}(x,y)$ и $\mathcal{I}(\mathcal{I}(x,ab),x)$ являются $\mathcal{I}$-выражениями.
Для двух $\mathcal{I}$-выражений $e_1$ и $e_2$, таких что уравнение $e_1=e_2$ имеет решение среди неотрицательных целых чисел, определим наименьшее одновременное значение $e_1$ и $e_2$ как минимальное значение, принимаемое $e_1$ и $e_2$ в таком решении. Если уравнение $e_1=e_2$ не имеет решения среди неотрицательных целых чисел, определим наименьшее одновременное значение $e_1$ и $e_2$ как равное $0$. Например, рассмотрим следующие три $\mathcal{I}$-выражения:
\[\begin{array}{l}A = \mathcal{I}(x,\mathcal{I}(z,t))\\
B = \mathcal{I}(\mathcal{I}(y,z),y)\\
C = \mathcal{I}(\mathcal{I}(x,z),y)\end{array}\]
Наименьшее одновременное значение $A$ и $B$ равно $23$, что соответствует $x=3,y=1,z=t=0$. С другой стороны, $A=C$ не имеет решения среди неотрицательных целых чисел, поэтому наименьшее одновременное значение $A$ и $C$ равно $0$. Общая сумма наименьших одновременных пар, образованных $\mathcal{I}$-выражениями из $\{A,B,C\}$ равна $26$.
Найдите сумму наименьших одновременных значений всех пар $\mathcal{I}$-выражений, образованных различными выражениями из файла I-expressions.txt (пары $(e_1,e_2)$ и $(e_2,e_1)$ считаются идентичными). В качестве ответа приведите последние девять цифр полученного числа.
Оригинал
