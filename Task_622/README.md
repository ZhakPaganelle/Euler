##Riffle Shuffles


A riffle shuffle is executed as follows: a deck of cards is split into two equal halves, with the top half taken in the left hand and the bottom half taken in the right hand. Next, the cards are interleaved exactly, with the top card in the right half inserted just after the top card in the left half, the 2nd card in the right half just after the 2nd card in the left half, etc. (Note that this process preserves the location of the top and bottom card of the deck)


Let $s(n)$ be the minimum number of consecutive riffle shuffles needed to restore a deck of size $n$ to its original configuration, where $n$ is a positive even number.

Amazingly, a standard deck of $52$ cards will first return to its original configuration after only $8$ perfect shuffles, so $s(52) = 8$. It can be verified that a deck of $86$ cards will also return to its original configuration after exactly $8$ shuffles, and the sum of all values of $n$ that satisfy $s(n) = 8$ is $412$.


Find the sum of all values of n that satisfy $s(n) = 60$.

##Перетасовка колоды


Перетасовка колоды выполняется следующим образом: колода карт разделяется на две равные половины, верхняя половина берется в левую руку, а нижняя - в правую. Далее, карты идеально чередуются: верхняя карта правой половины вставляется сразу после верхней карты левой половины, вторая карта правой половины - сразу после второй карты левой, и так далее. (Заметим, что этот процесс сохраняет положение верхней и нижней карты колоды).


Пусть $s(n)$ будет минимальным количеством последовательных перетасовок, необходимых, чтобы вернуть колоду из $n$ кард в изначальный порядок, где $n$ - положительное четное число.

Удивительно, но стандартная колода из $52$ карт вернется к изначальному порядку карт всего после $8$ идеальных перетасовок, поэтому $s(52) = 8$. Можно показать, что колода из $86$ карт тоже вернется к своему изначальному порядку после ровно $8$ перетасовок, и сумма всех значений $n$, удовлетворяющих $s(n) = 8$, равна $412$.


Найдите сумму всех значений $n$, удовлетворяющих $s(n) = 60$.

