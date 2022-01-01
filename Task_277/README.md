##A Modified Collatz sequence


A modified Collatz sequence of integers is obtained from a starting value $a_1$ in the following way:

$a_{n+1} = \, \,\, \frac {a_n} 3 \quad$ if $a_n$ is divisible by $3$. We shall denote this as a large downward step, "D".

$a_{n+1} = \frac {4 a_n+2} 3 \, \,$ if $a_n$ divided by $3$ gives a remainder of $1$. We shall denote this as an upward step, "U".


$a_{n+1} = \frac {2 a_n -1} 3 \, \,$ if $a_n$ divided by $3$ gives a remainder of $2$. We shall denote this as a small downward step, "d".


The sequence terminates when some $a_n = 1$.


Given any integer, we can list out the sequence of steps.
For instance if $a_1=231$, then the sequence $\{a_n\}=\{231,77,51,17,11,7,10,14,9,3,1\}$ corresponds to the steps "DdDddUUdDD".


Of course, there are other sequences that begin with that same sequence "DdDddUUdDD....".
For instance, if $a_1=1004064$, then the sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
In fact, $1004064$ is the smallest possible $a_1 > 10^6$ that begins with the sequence DdDddUUdDD.


What is the smallest $a_1 > 10^{15}$ that begins with the sequence "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?

##Модифицированная последовательность Коллатца

Модифицированную последовательность Коллатца, состояющую из целых чисел, получают из начального значения a1 следующим образом:

an+1 = an/3 если an делится на 3 без остатка. Обозначим это событие большим шагом вниз, "D".

an+1 = (4an + 2)/3 если, при делении на 3, an дает в остатке 1. Обозначим это событие шагом вверх, "U".


an+1 = (2an - 1)/3 если, при делении на 3, an дает в остатке 2. Обозначим это событие малым шагом вниз, "d".


Последовательность завершается на элементе an = 1.

Для любого заданного целого числа мы можем перечислить последовательность всех шагов.
Например, если a1=231, то последовательности {an}={231,77,51,17,11,7,10,14,9,3,1} соответствуют шаги "DdDddUUdDD".


Разумеется, существуют другие последовательности, начало которых совпадает с упомянутой выше "DdDddUUdDD....".
например, если a1=1004064, то получится следующая последовательность шагов DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
Между прочим, 1004064 является наименьшим возможным значением a1 > 106, соответствующая которому последовательность шагов начинается с DdDddUUdDD.


Чему равно наименьшее значение a1 > 1015, которому соответствует последовательность шагов, начинающаяся с "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?
