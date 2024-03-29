##Scatterstone Nim

Alice and Bob are playing a modified game of Nim called Scatterstone Nim, with Alice going first, alternating turns with Bob. The game begins with an arbitrary set of stone piles with a total number of stones equal to $n$.
During a player's turn, he/she must pick a pile having at least $2$ stones and perform a split operation, dividing the pile into an arbitrary set of $p$ non-empty, arbitrarily-sized piles where $2 \leq p \leq k$ for some fixed constant $k$. For example, a pile of size $4$ can be split into $\{1, 3\}$ or $\{2, 2\}$, or $\{1, 1, 2\}$ if $k = 3$ and in addition $\{1, 1, 1, 1\}$ if $k = 4$.
If no valid move is possible on a given turn, then the other player wins the game.
A winning position is defined as a set of stone piles where a player can ultimately ensure victory no matter what the other player does. 
Let $f(n,k)$ be the number of winning positions for Alice on her first turn, given parameters $n$ and $k$. For example, $f(5, 2) = 3$ with winning positions $\{1, 1, 1, 2\}, \{1, 4\}, \{2, 3\}$. In contrast, $f(5, 3) = 5$ with winning positions $\{1, 1, 1, 2\}, \{1, 1, 3\}, \{1, 4\}, \{2, 3\}, \{5\}$.
Let $g(n)$ be the sum of $f(n,k)$ over all $2 \leq k \leq n$. For example, $g(7)=66$ and $g(10)=291$.
Find $g(200)$ mod $(10^9 + 7)$.
##Ним с разбрасыванием

Алиса и Боб играют в измененную игру ним, называющуюся "ним с разбрасыванием". Алиса ходит первой, чередуя ходы с Бобом. Игра начинается с произвольного множества кучек камней с общим количеством камней во всех кучках равным $n$.
Во время своего хода игрок должен взять кучку, имеющую не меньше $2$ камней, и произвести ее разделение на произвольное множество из $p$ непустых кучек произвольного размера, где $2 \leq p \leq k$ для выбранной постоянной $k$. Например, кучка размером $4$ может быть разделена на $\{1, 3\}$, или $\{2, 2\}$, или $\{1, 1, 2\}$, если $k = 3$, и, в дополнение к этому, на $\{1, 1, 1, 1\}$, если $k = 4$.
Если игрок не может выполнить действительный ход, другой игрок выигрывает.
Выигрышная позиция определяется как множество кучек камней, начиная с которой игрок может в конечном счете обеспечить свою победу независимо от действий другого игрока. 
Пусть $f(n,k)$ будет количеством выигрышных позиций для Алисы на ее первый ход при данных параметрах $n$ и $k$. Например, $f(5, 2) = 3$ с выигрышными позициями $\{1, 1, 1, 2\}, \{1, 4\}, \{2, 3\}$. В свою очередь, $f(5, 3) = 5$ с выигрышными позициями $\{1, 1, 1, 2\}, \{1, 1, 3\}, \{1, 4\}, \{2, 3\}, \{5\}$.
Пусть $g(n)$ будет суммой $f(n,k)$ для всех $2 \leq k \leq n$. Например, $g(7)=66$ и $g(10)=291$.
Найдите $g(200)$ mod $(10^9 + 7)$.
