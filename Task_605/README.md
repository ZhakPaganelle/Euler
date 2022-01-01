##Pairwise Coin-Tossing Game

Consider an $n$-player game played in consecutive pairs: Round $1$ takes place between players $1$ and $2$, round $2$ takes place between players $2$ and $3$, and so on and so forth, all the way up to round $n$, which takes place between players $n$ and $1$. Then round $n+1$ takes place between players $1$ and $2$ as the entire cycle starts again.
In other words, during round $r$, player $((r-1) \bmod n) + 1$ faces off against player $(r \bmod n) + 1$.
During each round, a fair coin is tossed to decide which of the two players wins that round. If any given player wins both rounds $r$ and $r+1$, then that player wins the entire game.
Let $P_n(k)$ be the probability that player $k$ wins in an $n$-player game, in the form of a reduced fraction. For example, $P_3(1) = 12/49$ and $P_6(2) = 368/1323$.
Let $M_n(k)$ be the product of the reduced numerator and denominator of $P_n(k)$. For example, $M_3(1) = 588$ and $M_6(2) = 486864$.
Find the last $8$ digits of $M_{10^8+7}(10^4+7)$.
##Игра парных подбрасываний монеты

Рассмотрим игру для $n$ игроков, в которую играют последовательно попарно: $1$ раунд происходит между игроками $1$ и $2$, раунд $2$ происходит между игроками $2$ и $3$, и так далее до раунда $n$, который происходит между игроками $n$ и $1$. После этого раунд $n+1$ происходит между игроками $1$ и $2$, и весь цикл начинается снова.
Иными словами, во время раунда $r$, игрок $((r-1) \bmod n) + 1$ играет против игрока $(r \bmod n) + 1$.
Для определения, кто из двух игроков победит, во время каждого раунда подбрасывается честная монета. Если какой-либо игрок побеждает в обоих раундах $r$ и $r+1$, он побеждает в этой игре.
Пусть $P_n(k)$ будет вероятностью, что игрок $k$ выиграет в игре с $n$ игроками, выраженной как несократимая дробь. Например, $P_3(1) = 12/49$ и $P_6(2) = 368/1323$.
Пусть $M_n(k)$ будет произведением числителя и знаменателя несократимой дроби $P_n(k)$. Например, $M_3(1) = 588$ и $M_6(2) = 486864$.
Найдите последние $8$ цифр в $M_{10^8+7}(10^4+7)$.
