##Polymorphic Bacteria


If a population starts with a single bacterium of type $\alpha$, then it can be shown that there is a 0.07243802 probability that the population will eventually die out, and a 0.92756198 probability that the population will last forever. These probabilities are given rounded to 8 decimal places.


Now consider another species of bacteria, $S_{k,m}$ (where $k$ and $m$ are positive integers), which occurs in $k$ different types $\alpha_i$ for $0\le i< k$. The rules governing this species' lifecycle involve the sequence $r_n$ defined by:


Every minute, for each $i$, each bacterium $A$ of type $\alpha_i$ will independently choose an integer $j$ uniformly at random in the range $0\le j<m$. What it then does depends on $q = r_{im+j} \bmod 5$:

In fact, our original species was none other than $S_{2,2}$, with $\alpha=\alpha_0$ and $\beta=\alpha_1$.


Let $P_{k,m}$ be the probability that a population of species $S_{k,m}$, starting with a single bacterium of type $\alpha_0$, will eventually die out. So $P_{2,2} = 0.07243802$. You are also given that $P_{4,3} = 0.18554021$ and $P_{10,5} = 0.53466253$, all rounded to 8 decimal places.


Find $P_{500,10}$, and give your answer rounded to 8 decimal places.

##Полиморфные бактерии

Особи одного вида бактерий бывают двух разных типов: $\alpha$ и $\beta$. Одиночные бактерии способны размножаться и мутировать между типами в соответствии со следующими правилами:
Каждую минуту все особи одновременно претерпевают какое-то преобразование.
Каждая особь $A$ типа $\alpha$ независимо от других делает одно из следующих (случайно, с равной вероятностью):
клонирует себя, производя новую бактерию типа $\alpha$ (сама $A$ также остается)
разделяется на 3 новые бактерии типа $\beta$ (замещающие $A$)

Каждая особь $B$ типа $\beta$ независимо от других делает одно из следующих (случайно, с равной вероятностью):
порождает новую бактерию типа $\alpha$ (сама $B$ также остается)
умирает


Если популяция начинается с единственной бактерии типа $\alpha$, тогда можно показать, что популяция в конечном счете вымрет с вероятностью 0.07243802 или будет существовать вечно с вероятностью 0.92756198. Эти вероятности округлены до 8 десятичного знака.


Теперь рассмотрим другой вид бактерий $S_{k,m}$ (где $k$ и $m$ - натуральные числа), который представлен $k$ различными типами $\alpha_i$ для $0\le i< k$. Правила, определяющие жизненный цикл этого вида, основаны на последовательности $r_n$, определенной следующим образом:

$r_0 = 306$
$r_{n+1} = r_n^2 \bmod 10\,007$

Каждую минуту для каждого $i$ каждая бактерия $A$ типа $\alpha_i$ независимо случайно выбирает целое число $j$ равномерно из интервала $0\le j<m$. То, что она после этого делает, зависит от $q = r_{im+j} \bmod 5$:
Если $q=0$, $A$ умирает.
Если $q=1$, $A$ клонирует себя, производя новую бактерию типа $\alpha_i$ (сама $A$ также остается).
Если $q=2$, $A$ мутирует, изменяя свой тип на $\alpha_{(2i) \bmod k}$.
Если $q=3$, $A$ разделяется на 3 новые бактерии типа type $\alpha_{(i^2+1) \bmod k}$ (замещающие $A$).
Если $q=4$, $A$ порождает новую бактерию типа $\alpha_{(i+1) \bmod k}$ (сама $A$ также остается).

По факту, наши первоначальные виды являются ничем иным, как $S_{2,2}$ с $\alpha=\alpha_0$ и $\beta=\alpha_1$.


Пусть $P_{k,m}$ будет вероятностью, что популяция вида $S_{k,m}$, начавшаяся с единственной бактерии типа $\alpha_0$, в конечном счете вымрет. Таким образом, $P_{2,2} = 0.07243802$. Также известно, что $P_{4,3} = 0.18554021$ и $P_{10,5} = 0.53466253$, все числа округлены до 8 десятичного знака.


Найдите $P_{500,10}$ и дайте ваш ответ округленным до 8 десятичного знака.

