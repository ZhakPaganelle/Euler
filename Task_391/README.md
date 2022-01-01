##Hopping Game

Let $s_k$ be the number of 1’s when writing the numbers from 0 to $k$ in binary.
For example, writing 0 to 5 in binary, we have $0, 1, 10, 11, 100, 101$. There are seven 1’s, so $s_5 = 7$.
The sequence $S = \{s_k : k \ge 0\}$ starts $\{0, 1, 2, 4, 5, 7, 9, 12, ...\}$.
A game is played by two players. Before the game starts, a number $n$ is chosen. A counter $c$ starts at 0. At each turn, the player chooses a number from 1 to $n$ (inclusive) and increases $c$ by that number. The resulting value of $c$ must be a member of $S$. If there are no more valid moves, then the player loses.
For example, with $n = 5$ and starting with $c = 0$:
Player 1 chooses 4, so $c$ becomes $0 + 4 = 4$.
Player 2 chooses 5, so $c$ becomes $4 + 5 = 9$.
Player 1 chooses 3, so $c$ becomes $9 + 3 = 12$.
etc.
Note that $c$ must always belong to $S$, and each player can increase $c$ by at most $n$.
Let $M(n)$ be the highest number that the first player could choose at the start to force a win, and $M(n) = 0$ if there is no such move. For example, $M(2) = 2$, $M(7) = 1$, and $M(20) = 4$.
It can be verified that $\sum{M(n)^3} = 8150$ for $1 \le n \le 20$.
Find $\sum{M(n)^3}$ for $1 \le n \le 1000$.
##Игра в прыжки


Пусть sk будет количеством единиц, использованных при записи чисел от 0 до k в двоичном виде.
Например, записывая числа от 0 до 5 в двоичном виде, мы получаем 0, 1, 10, 11, 100, 101. Всего использовано семь единиц, таким образом, s5 = 7.

Последовательность S = {sk : k ≥ 0} начинается следующим образом: {0, 1, 2, 4, 5, 7, 9, 12, ...}.


В игру играют двое игроков. Перед началом игры выбирается число n. Счетчик c начинается с 0. На каждый ход игрок выбирает число от 1 до n (включительно) и увеличивает c на это число. Полученное значение c должно быть элементом S. Если игрок больше не имеет возможных ходов, он проигрывает.


Например:
Пусть n = 5. c начинается с 0.
Игрок 1 выбирает 4, посему c принимает значение 0 + 4 = 4.
Игрок 2 выбирает 5, посему c принимает значение 4 + 5 = 9.
Игрок 1 выбирает 3, посему c принимает значение 9 + 3 = 12.
И т.д.
Заметьте, что c должно всегда принадлежать S, и каждый игрок может увеличить c не больше, чем на n.


Пусть M(n) будет наибольшим числом, которое первый игрок может выбрать и обеспечить себе победу, и M(n) = 0, если такого хода не существует. Например, M(2) = 2, M(7) = 1 и M(20) = 4.


Дано, что Σ(M(n))3 = 8150 для 1 ≤ n ≤ 20.


Найдите Σ(M(n))3 для 1 ≤ n ≤ 1000.

