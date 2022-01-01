##A Long Chess Match

Two friends $A$ and $B$ are great fans of Chess. They both enjoy playing the game, but after each game the player who lost the game would like to continue (to get back at the other player) and the player who won would prefer to stop (to finish on a high).
So they come up with a plan. After every game, they would toss a (biased) coin with probability $p$ of Heads (and hence probability $1-p$ of Tails). If they get Tails, they will continue with the next game. Otherwise they end the match. Also, after every game the players make a note of who is leading in the match.
Let $p_A$ denote the probability of $A$ winning a game and $p_B$ the probability of $B$ winning a game. Accordingly $1-p_A-p_B$ is the probability that a game ends in a draw. Let $\mathbb{E}_A(p_A,p_B,p)$ denote the expected number of times $A$ was leading in the match.

For example, $\mathbb{E}_A(0.25,0.25,0.5)\approx 0.585786$ and $\mathbb{E}_A(0.47,0.48,0.001)\approx 377.471736$, both rounded to six places after the decimal point.
Let $\displaystyle H(n)=\sum_{k=3}^n \mathbb{E}_A\left(\frac 1 {\sqrt{k+3}},\frac 1 {\sqrt{k+3}}+\frac 1 {k^2},\frac 1 {k^3}\right)$
For example $H(3) \approx 6.8345$, rounded to 4 digits after the decimal point.
Find $H(50)$, rounded to 4 digits after the decimal point.
##Долгий шахматный матч

Два друга $A$ и $B$ - большие фанаты шахмат. Им обоим нравится играть, но после каждой игры проигравший хочет играть снова (чтобы свести счеты с соперником), а победивший предпочитает остановиться (пока он на высоте).
Они придумали план. После каждой игры они будут подбрасывать нечестную монету, имеющую вероятность выпадения орла $p$ (и, соответственно, вероятность выпадения решки $1-p$). Если выпадет решка, они начнут следующую игру. В противном случае матч завершен. Также, после каждой игры игроки записывают, кто побеждает в матче.
Пусть $p_A$ будет обозначать вероятность того, что $A$ выиграет игру, а $p_B$ - что в игре победит $B$. Соответственно, $1-p_A-p_B$ - вероятность ничьей. Пусть $\mathbb{E}_A(p_A,p_B,p)$ будет обозначать ожидаемое количество раз, когда $A$ лидирует в матче.

Например, $\mathbb{E}_A(0.25,0.25,0.5)\approx 0.585786$ и $\mathbb{E}_A(0.47,0.48,0.001)\approx 377.471736$, оба числа округлены до шестого знака после десятичной точки.
Пусть $\displaystyle H(n)=\sum_{k=3}^n \mathbb{E}_A\left(\frac 1 {\sqrt{k+3}},\frac 1 {\sqrt{k+3}}+\frac 1 {k^2},\frac 1 {k^3}\right)$
Например, $H(3) \approx 6.8345$, округленное до 4 знака после десятичной точки.
Найдите $H(50)$, округленное до 4 знака после десятичной точки.
