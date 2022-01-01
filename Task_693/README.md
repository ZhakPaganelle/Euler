##Finite Sequence Generator

Two positive integers $x$ and $y$ ($x > y$) can generate a sequence in the following manner:
The number of terms in this sequence is denoted $l(x,y)$.
For example, with $x = 5$ and $y = 3$, we get $a_5 = 3$, $a_6 = 3^2 \bmod 5 = 4$, $a_7 = 4^2\bmod 6 = 4$, etc. Giving the sequence of 29 terms:
$	3,4,4,2,4,7,9,4,4,3,9,6,4,16,4,16,16,4,16,3,9,6,10,19,25,16,16,8,0		$
Hence $l(5,3) = 29$.
$g(x)$ is defined  to be the maximum value of $l(x,y)$ for $y < x$. For example, $g(5) = 29$.
Further, define $f(n)$ to be the maximum value of $g(x)$ for $x \le n$. For example, $f(100) = 145$ and $f(10\,000) = 8824$.
Find $f(3\,000\,000)$.
##Генератор конечных последовательностей

Два натуральных числа $x$ и $y$ ($x > y$) могут быть использованиы, чтобы сгенерировать последовательность следующим образом:

Первый элемент $a_x = y$,
$a_{z+1} = a_z^2 \bmod z$ для $z = x, x+1,x+2,\ldots$ и
генерирование заканчивается на элементе, равном 0 или 1.

Число элементов этой последовательности обозначается $l(x,y)$.
Например, при $x = 5$ и $y = 3$ мы получим $a_5 = 3$, $a_6 = 3^2 \bmod 5 = 4$, $a_7 = 4^2\bmod 6 = 4$ и т.д. Это даст последовательность из 29 элементов:
$3,4,4,2,4,7,9,4,4,3,9,6,4,16,4,16,16,4,16,3,9,6,10,19,25,16,16,8,0$
Поэтому $l(5,3) = 29$.
Определим $g(x)$ как максимальное значение $l(x,y)$ для $y < x$. Например, $g(5) = 29$.
Далее, определим $f(n)$ как максимальное значение $g(x)$ для $x \le n$. Например, $f(100) = 145$ и $f(10\,000) = 8824$.
Найдите $f(3\,000\,000)$. Оригинал