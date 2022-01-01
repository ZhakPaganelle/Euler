##Mahjong

The game of Mahjong is played with tiles belonging to $s$ suits. Each tile also has a number in the range $1\ldots n$, and for each suit/number combination there are exactly four indistinguishable tiles with that suit and number. (The real Mahjong game also contains other bonus tiles, but those will not feature in this problem.)
A winning hand is a collection of $3t+2$ Tiles (where $t$ is a fixed integer) that can be arranged as $t$ Triples and one Pair, where:
For example, here is a winning hand with $n=9$, $s=3$, $t=4$, consisting in this case of two Chows, two Pungs, and one Pair:
Note that sometimes the same collection of tiles can be represented as $t$ Triples and one Pair in more than one way. This only counts as one winning hand. For example, this is considered to be the same winning hand as above, because it consists of the same tiles:
Let $w(n, s, t)$ be the number of distinct winning hands formed of $t$ Triples and one Pair, where there are $s$ suits available and tiles are numbered up to $n$.
For example, with a single suit and tiles numbered up to 4, we have $w(4, 1, 1) = 20$: there are 12 winning hands consisting of a Pung and a Pair, and another 8 containing a Chow and a Pair. You are also given that $w(9, 1, 4) = 13259$, $w(9, 3, 4) = 5237550$, and $w(1000, 1000, 5) \equiv 107662178 \pmod{1\,000\,000\,007}$.
Find $w(10^8, 10^8, 30)$. Give your answer modulo $1\,000\,000\,007$.
##Маджонг

В игре Маджонг используются кости $s$ мастей. На каждой кости есть также число в промежутке $1\ldots n$, и для каждой комбинации масти и числа существует ровно четыре неотличимых кости с таким числом и мастью (настоящий маджонг также содержит другие дополнительные кости, но мы не рассматриваем их в этой задаче).
Выигрышной рукой считается набор из $3t+2$ костей (где $t$ - определенное целое число), который можно разложить на $t$ троек и одну пару, где:

Тройка - это или чоу, или панг
Чоу - это три кости одной масти и последовательных чисел
Панг - это три идентичные кости (одной масти и числа)
Пара - это две идентичные кости (одной масти и числа)

Например, ниже показана выигрышная рука при $n=9$, $s=3$, $t=4$, состоящая в данном случае из двух чоу, двух панг и одной пары:



Заметим, что иногда такой же набор костей можно представить как $t$ тройки и одну пару более, чем одним образом. Это считается только как одна выигрышная рука. Например, такой набор считается такой же выигрышной рукой, как в примере выше, так как он состоит из тех же костей:



Пусть $w(n, s, t)$ будет количеством различных выигрышных рук, образованных из $t$ троек и одной пары, при $s$ возможных мастях и костях, пронумерованных от 1 до $n$.
Например, при одной единственной масти и числах от 1 до 4 мы получим $w(4, 1, 1) = 20$: существует 12 выигрышных рук, состоящих из панг и пары, и 8, состоящих из чоу и пары. Также известно, что $w(9, 1, 4) = 13259$, $w(9, 3, 4) = 5237550$ и $w(1000, 1000, 5) \equiv 107662178 \pmod{1\,000\,000\,007}$.
Найдите $w(10^8, 10^8, 30)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
Оригинал
