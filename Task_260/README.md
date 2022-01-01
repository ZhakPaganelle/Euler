##Stone Game

A game is played with three piles of stones and two players.
On each player's turn, the player may remove one or more stones from the piles. However, if the player takes stones from more than one pile, then the same number of stones must be removed from each of the selected piles.
In other words, the player chooses some $N \gt 0$ and removes:
The player taking the last stone(s) wins the game.
A winning configuration is one where the first player can force a win.
For example, $(0,0,13)$, $(0,11,11)$, and $(5,5,5)$ are winning configurations because the first player can immediately remove all stones.
A losing configuration is one where the second player can force a win, no matter what the first player does.
For example, $(0,1,2)$ and $(1,3,3)$ are losing configurations: any legal move leaves a winning configuration for the second player.
Consider all losing configurations $(x_i, y_i, z_i)$ where $x_i \le y_i \le z_i \le 100$.
We can verify that $\sum (x_i + y_i + z_i) = 173895$ for these.
Find $\sum (x_i + y_i + z_i)$ where $(x_i, y_i, z_i)$ ranges over the losing configurations with $x_i \le y_i \le z_i \le 1000$.
##Игра в камушки

В игру играют два игрока с помощью трех кучек камушков.
Когда приходит его ход, игрок берет один или более камушков из кучки. Однако, беря камушки из более, чем одной кучки, игрок должен взять такое же количество камушков из всех выбранных кучек.
Другими словами, игрок выбирает N>0 камушков, взяв:
N камушков из одной кучки; или
N камушков из каждой из любых двух кучек (всего 2N); или
N камушков из каждой из трех кучек (всего 3N).
Победит тот игрок, который возьмет последний камушек.

Под выигрышной конфигурацией подразумевается такая, в которой первый игрок может сразу победить.
К примеру, (0,0,13), (0,11,11) и (5,5,5) являются выигрышными конфигурациями, т.к. игрок может сразу взять все камушки.
Под проигрышной конфигурацией подразумевается такая, в которой второй игрок сразу выиграет, вне зависимости от того, что сделает первый игрок.
К примеру, конфигурации (0,1,2) и (1,3,3) являются проигрышными, т.к. в результате любого разрешенного шага первого игрока выиграет второй игрок.
Рассмотрим все проигрышные конфигурации (xi,yi,zi), где xi ≤ yi ≤ zi ≤ 100.
Можно убедиться, что для них Σ(xi+yi+zi) = 173895.
Найдите Σ(xi+yi+zi), где (xi,yi,zi) - диапазон всех проигрышных конфигураций
при xi ≤ yi ≤ zi ≤ 1000.
