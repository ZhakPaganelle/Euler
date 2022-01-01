##Stone Game II

A game is played with two piles of stones and two players.
On each player's turn, the player may remove a number of stones from the larger pile.
The number of stones removed must be a positive multiple of the number of stones in the smaller pile.
E.g. Let the ordered pair $(6,14)$ describe a configuration with 6 stones in the smaller pile and 14 stones in the larger pile, then the first player can remove 6 or 12 stones from the larger pile.
The player taking all the stones from a pile wins the game.
A winning configuration is one where the first player can force a win. For example, $(1,5)$, $(2,6)$, and $(3,12)$ are winning configurations because the first player can immediately remove all stones in the second pile.
A losing configuration is one where the second player can force a win, no matter what the first player does. For example, $(2,3)$ and $(3,4)$ are losing configurations: any legal move leaves a winning configuration for the second player.
Define $S(N)$ as the sum of $(x_i + y_i)$ for all losing configurations $(x_i, y_i), 0 \lt x_i \lt y_i \le N$.
We can verify that $S(10) = 211$ and $S(10^4) = 230312207313$.
Find $S(10^{16}) \mod 7^{10}$.
##Игра в камушки II

В данной игре участвуют два игрока и используются две кучки камушков. Во время своего хода игрок извлекает определенное число камушков из большей кучки. Число выбранных камушков должно быть положительным и кратным числу камушков в меньшей кучке.


Например, пусть упорядоченная пара (6,14) описывает ситуацию с 6 камушками в меньшей кучке и 14 в большей. Тогда первый игрок может забрать либо 6, либо 12 камушков из большей кучки.


Побеждает тот игрок, который забрал все камушки из одной кучки.


Выигрышная ситуация - такая ситуация, в которой первый игрок может обеспечить себе победу. К примеру, (1,5), (2,6) и (3,12) являются выигрышными, поскольку первый игрок может забрать все камушки из второй кучки при первом же ходе.


Проигрышная ситуация - такая ситуация, в которой второй игрок может обеспечить себе победу, независимо от того, что предпримет первый игрок. К примеру, (2,3) и (3,4) являются проигрышными: любой разрешенный ход оставит выигрышную ситуацию второму игроку.


Определим S(N) как сумму (xi+yi) для всех проигрышных ситуаций (xi,yi), 0 < xi < yi ≤ N. Можно убедиться, что S(10) = 211 и S(104) = 230312207313.


Найдите S(1016) mod 710.

