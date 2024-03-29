##Restricted Factorisations

Consider writing a natural number as product of powers of natural numbers with given exponents, additionally requiring different base numbers for each power.
For example, $256$ can be written as a product of a square and a fourth power in three ways such that the base numbers are different.
That is, $256=1^2\times 4^4=4^2\times 2^4=16^2\times 1^4$
Though $4^2$ and $2^4$ are both equal, we are concerned only about the base numbers in this problem. Note that permutations are not considered distinct, for example $16^2\times 1^4$ and $1^4 \times 16^2$ are considered to be the same.
Similarly, $10!$ can be written as a product of one natural number, two squares and three cubes in two ways ($10!=42\times5^2\times4^2\times3^3\times2^3\times1^3=21\times5^2\times2^2\times4^3\times3^3\times1^3$) whereas $20!$ can be given the same representation in $41680$ ways.
Let $F(n)$ denote the number of ways in which $n$ can be written as a product of one natural number, two squares, three cubes and four fourth powers.
You are given that $F(25!)=4933$, $F(100!) \bmod 1\,000\,000\,007=693\,952\,493$,
and $F(1\,000!) \bmod 1\,000\,000\,007=6\,364\,496$.
Find $F(1\,000\,000!) \bmod 1\,000\,000\,007$.
##Ограниченные разложения на множители

Рассмотрим запись натурального числа в виде произведения степеней натуральных чисел с заданными показателями степеней, сверх того требуя различные основания степеней для каждой степени.
Например, $256$ может быть записано как произведение квадрата и четвертой степени тремя способами с различными основаниями степеней.
А именно, $256=1^2\times 4^4=4^2\times 2^4=16^2\times 1^4$
Хоть $4^2$ и $2^4$ и имеют равные значения, в рамках этой задачи нас интересуют только различные основания степеней. Заметим, что перестановки не считаются различными, например, $16^2\times 1^4$ и $1^4 \times 16^2$ считаются одинаковыми.
Похожим образом, $10!$ может быть записано как произведение натурального числа, двух квадратов и трех кубов двумя способами ($10!=42\times5^2\times4^2\times3^3\times2^3\times1^3=21\times5^2\times2^2\times4^3\times3^3\times1^3$), в то время как $20!$ можно привести в такой же вид $41680$ способами.
Пусть $F(n)$ обозначает количество различных способов, которыми число $n$ можно записать в виде произведения одного натурального числа, двух квадратов, трех кубов и четырех четвертых степеней.
Известно, что $F(25!)=4933$, $F(100!) \bmod 1\,000\,000\,007=693\,952\,493$
и $F(1\,000!) \bmod 1\,000\,000\,007=6\,364\,496$.
Найдите $F(1\,000\,000!) \bmod 1\,000\,000\,007$.
