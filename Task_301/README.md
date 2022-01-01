##Nim

Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.
We'll consider the three-heap normal-play version of Nim, which works as follows:
If $(n_1,n_2,n_3)$ indicates a Nim position consisting of heaps of size $n_1$, $n_2$, and $n_3$, then there is a simple function, which you may look up or attempt to deduce for yourself, $X(n_1,n_2,n_3)$ that returns:
For example $X(1,2,3) = 0$ because, no matter what the current player does, the opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by the opponent until no stones remain; so the current player loses. To illustrate:
For how many positive integers $n \le 2^{30}$ does $X(n,2n,3n) = 0$ ?
##Ним

Ним - это игра с кучками камней, в которой двое игроков по очереди убирают любое количество камней из любой кучки, пока не останется ни одного камня.
Мы рассмотрим версию нормальной игры с тремя кучками, которая проходит следующим образом:
- в начале игры имеется три кучки камней;
- во время своего хода игрок убирает любое положительное число камней из любой одной кучки;
- первый игрок, который не сможет сделать ход (потому что не останется камней), проигрывает.
Если (n1,n2,n3) указывает позицию в игре с кучками размеров n1, n2 и n3, то существует простая функция X(n1,n2,n3) (которую вы можете разыскать или попытаться вывести самостоятельно), которая возвращает:
ноль, если при совершенной стратегии игрок, чья очередь делать ход, в конце концов проиграет; или
ненулевой результат, если при совершенной стратегии игрок, чья очередь делать ход, в конце концов выиграет.
Например, X(1,2,3) = 0, потому что, независимо от действий текущего игрока, его противник может ответить ходом, который оставит кучки равных размеров, и тогда каждый ход текущего игрока может повторяться его противником, пока не останется камней - то есть, текущий игрок проигрывает. Для иллюстрации:
- текущий игрок ходит в позицию (1,2,1),
- противник ходит в (1,0,1),
- текущий игрок ходит в (0,0,1),
- противник ходит в (0,0,0) и выигрывает.
Для скольки натуральных n ≤ 230 выполняется X(n,2n,3n) = 0 ?

