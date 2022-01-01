##Unfair race

$n$ runners in very different training states want to compete in a race. Each one of them is given a different starting number $k$ $(1\leq k \leq n)$ according to the runner's (constant) individual racing speed being $v_k=\frac{k}{n}$.
In order to give the slower runners a chance to win the race, $n$ different starting positions are chosen randomly (with uniform distribution) and independently from each other within the racing track of length $1$. After this, the starting position nearest to the goal is assigned to runner $1$, the next nearest starting position to runner $2$ and so on, until finally the starting position furthest away from the goal is assigned to runner $n$. The winner of the race is the runner who reaches the goal first.
Interestingly, the expected running time for the winner is $\frac{1}{2}$, independently of the number of runners. Moreover, while it can be shown that all runners will have the same expected running time of $\frac{n}{n+1}$, the race is still unfair, since the winning chances may differ significantly for different starting numbers:
Let $P_{n,k}$ be the probability for runner $k$ to win a race with $n$ runners and $E_n = \sum_{k=1}^n k P_{n,k}$ be the expected starting number of the winner in that race. It can be shown that, for example,
$P_{3,1}=\frac{4}{9}$, $P_{3,2}=\frac{2}{9}$, $P_{3,3}=\frac{1}{3}$ and $E_3=\frac{17}{9}$ for a race with $3$ runners. 
You are given that $E_4=2.21875$, $E_5=2.5104$ and $E_{10}=3.66021568$.
Find $E_{1000000}$ rounded to 4 digits after the decimal point.
##Нечестный забег

$n$ бегунов очень разной степени физической подготовки хотят соревноваться в беге. Каждому из них дан отличный стартовый номер $k$ $(1\leq k \leq n)$ в соответствии с его (неизменной) личной скоростью бега, равной $v_k=\frac{k}{n}$.
Для того, чтобы дать более медленным бегунам шанс победить в забеге, $n$ различных стартовых позиций выбираются случайно (с равномерным распределением) и независимо друг от друга на беговой дорожке длиной $1$. После этого ближайшая к финишу стартовая позиция назначается бегуну с номером $1$, следующая ближайшая стартовая позиция - бегуну с номером $2$, и так далее, пока, наконец, самая отдаленная от финиша стартовая позиция не будет назначена бегуну с номером $n$. Победителем забега является бегун, первый достигший финиша.
Любопытно, что ожидаемое время бега победителя равно $\frac{1}{2}$ независимо от количества бегунов. Более того, хоть и можно показать, что все бегуны имеют одинаковое ожидаемое время бега, равное $\frac{n}{n+1}$, забег все равно нечестен, так как шансы на победу могут значительно отличаться для разных стартовых номеров:
Пусть $P_{n,k}$ будет вероятностью, с которой бегун номер $k$ победит в забеге с $n$ участниками, и $E_n = \sum_{k=1}^n k P_{n,k}$ будет ожидаемым стартовым номером победителя этого забега. Можно показать, например, что
$P_{3,1}=\frac{4}{9}$, $P_{3,2}=\frac{2}{9}$, $P_{3,3}=\frac{1}{3}$ и $E_3=\frac{17}{9}$ для забега с $3$ бегунами. 
Известно, что $E_4=2.21875$, $E_5=2.5104$ и $E_{10}=3.66021568$.
Найдите $E_{1000000}$, округленное до 4 цифр после десятичной точки.
