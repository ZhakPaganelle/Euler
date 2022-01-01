##Siegbert and Jo


Siegbert and Jo take turns playing a game with a heap of $N$ pebbles:
1. Siegbert is the first to take some pebbles. He can take as many pebbles as he wants. (Between 1 and $N$ inclusive.)
2. In each of the following turns the current player must take at least one pebble and at most twice the amount of pebbles taken by the previous player.
3. The player who takes the last pebble wins.

Although Siegbert can always win by taking all the pebbles on his first turn, to make the game more interesting he chooses to take the smallest number of pebbles that guarantees he will still win (assuming both Siegbert and Jo play optimally for the rest of the game).


Let $H(N)$ be that minimal amount for a heap of $N$ pebbles.
$H(1)=1$, $H(4)=1$, $H(17)=1$, $H(8)=8$ and $H(18)=5$ .


Let $G(n)$ be $\displaystyle{\sum_{k=1}^n H(k)}$.
$G(13)=43$.


Find $G(23416728348467685)$.

##Зигберт и Джо


Зигберт и Джо играют в игру с кучей из $N$ камней и по очереди ходят:
1. Зигберт первый берет несколько камней. Он может взять столько камней, сколько хочет (от 1 до $N$ включительно).
2. В каждый последующий ход текущий игрок должен взять не меньше одного камня и не больше, чем дважды количество камней, взятых предыдущим игроком.
3. Игрок, взявший последний камень, побеждает.


Хотя Зигберт и может всегда побеждать, взяв первым ходом все камни, он решил сделать игру интереснее и брать первым ходом наименьшее количество камней, которое гарантирует ему победу (предполагая, что остальную игру Зигберт и Джо будут играть оптимально).


Пусть $H(N)$ будет таким наименьшим количеством камней в первый ход для кучи из $N$ камней.
$H(1)=1$, $H(4)=1$, $H(17)=1$, $H(8)=8$ и $H(18)=5$ .


Пусть $G(n)$ будет $\displaystyle{\sum_{k=1}^n H(k)}$.
$G(13)=43$.


Найдите $G(23416728348467685)$.
 Оригинал
