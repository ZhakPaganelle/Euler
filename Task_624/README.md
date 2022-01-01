##Two heads are better than one


An unbiased coin is tossed repeatedly until two consecutive heads are obtained. Suppose these occur on the $(M-1)$th and $M$th toss.
Let $P(n)$ be the probability that $M$ is divisible by $n$. For example, the outcomes HH, HTHH, and THTTHH all count towards $P(2)$, but THH and HTTHH do not.

You are given that $P(2) =\frac 3 5$ and $P(3)=\frac 9  {31}$. Indeed, it can be shown that $P(n)$ is always a rational number.

For a prime $p$ and a fully reduced fraction $\frac a b$, define $Q(\frac a b,p)$ to be the smallest positive $q$ for which $a \equiv b q \pmod{p}$.
For example $Q(P(2), 109) = Q(\frac 3 5, 109) = 66$, because $5 \cdot 66 = 330 \equiv 3 \pmod{109}$ and 66 is the smallest positive such number.
Similarly $Q(P(3),109) = 46$.

Find $Q(P(10^{18}),1\,000\,000\,009)$.
##Одна решка - хорошо, а две - лучше


Честную монету повторно подбрасывают, пока не выпадут две последовательные решки. Положим, что это происходит на $(M-1)$-й м $M$-й бросок.
Пусть $P(n)$ будет вероятностью, что $M$ делится на $n$. Например, результаты РР, РОРР и ОРООРР все считаются в $P(2)$, однако, ОРР и РООРР - нет.

Известно, что $P(2) =\frac 3 5$ и $P(3)=\frac 9  {31}$. Действительно, можно показать, что $P(n)$ всегда рациональное число.

Для простого числа $p$ и несократимой дроби $\frac a b$ определим $Q(\frac a b,p)$ как наименьшое положительное $q$, для которого $a \equiv b q \pmod{p}$.
Например $Q(P(2), 109) = Q(\frac 3 5, 109) = 66$, потому что $5 \cdot 66 = 330 \equiv 3 \pmod{109}$ и 66 - наименьшее такое положительное число.
Похожим образом, $Q(P(3),109) = 46$.

Найдите $Q(P(10^{18}),1\,000\,000\,009)$.
