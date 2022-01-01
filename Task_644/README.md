##Squares on the line

Sam and Tom are trying a game of (partially) covering a given line segment of length $L$ by taking turns in placing unit squares onto the line segment. 
As illustrated below, the squares may be positioned in two different ways, either "straight" by placing the midpoints of two opposite sides on the line segment, or "diagonal" by placing two opposite corners on the line segment. Newly placed squares may touch other squares, but are not allowed to overlap any other square laid down before.
The player who is able to place the last unit square onto the line segment wins.

With Sam starting each game by placing the first square, they quickly realise that Sam can easily win every time by placing the first square in the middle of the line segment, making the game boring. 

Therefore they decide to randomise Sam's first move, by first tossing a fair coin to determine whether the square will be placed straight or diagonal onto the line segment and then choosing the actual position on the line segment randomly with all possible positions being equally likely. Sam's gain of the game is defined to be 0 if he loses the game and $L$ if he wins. Assuming optimal play of both players after Sam's initial move, you can see that Sam's expected gain, called $e(L)$, is only dependent on the length of the line segment.

For example, if $L=2$, Sam will win with a probability of 1, so $e(2)= 2$. 
Choosing $L=4$, the winning probability will be 0.33333333 for the straight case and 0.22654092 for the diagonal case, leading to $e(4)=1.11974851$ (rounded to 8 digits after the decimal point each). 

Being interested in the optimal value of $L$ for Sam, let's define $f(a,b)$ to be the maximum of $e(L)$ for some $L \in [a,b]$. 
You are given $f(2,10)=2.61969775$, being reached for $L= 7.82842712$, and $f(10,20)=
5.99374121$ (rounded to 8 digits each).

Find $f(200,500)$, rounded to 8 digits after the decimal point.
##Квадраты на прямой

Сэм и Том испытывают игру, состоящую в (частичном) покрытии данного отрезка длины $L$, по очереди располагая на нем единичные квадраты. 
Как показано ниже, квадрат можно расположить одним из двух способов: или "прямо", поместив на отрезке середины двух противоположных сторон квадрата, или "диагонально", поместив на отрезке противоположные вершины квадрата. Размещенный таким образом квадрат может касаться других квадратов, но не может перекрывать ни один из ранее помещенных квадратов.
Игрок, поместивший последний единичный квадрат на отрезок, побеждает.


Если Сэм всегда ходит первым, игроки быстро выяснили, что он может запросто выигрывать каждый раз, помещая первый квадрат в середину отрезка, что сделало игру скучной. 

Поэтому они решили сделать первый ход Сэма случайным, подкидывая честную монету для определения, будет ли первый квадрат помещен прямо или диагонально, а также случайно выбирая положение первого квадрата на отрезке, причем все возможные расположения имеют одинаковую вероятность. Выигрыш Сэма от каждой игры считается равным 0, если он ее проигрывает, и $L$, если выигрывает. Предполагая, что оба игрока играют оптимальным образом после первого хода Сэма, можно заметить, что ожидаемый выигрыщ Сэма $e(L)$ зависит только от длины отрезка.

Например, если $L=2$, Сэм победит с вероятностью 1, поэтому $e(2)= 2$. 
При $L=4$ вероятность победы будет равна 0.33333333 для прямого расположения и 0.22654092 для диагонального, что приведет к $e(4)=1.11974851$ (округленному до 8 знака после десятичной точки). 

Будучи заинтересованными в оптимальном для Сэма значении $L$, определим $f(a,b)$ как максимальное значение $e(L)$ при выбраннном $L \in [a,b]$. 
Известно, что $f(2,10)=2.61969775$ достигается при $L= 7.82842712$, и $f(10,20)=
5.99374121$ (оба округлены до 8 знака).

Найдите $f(200,500)$, округленное до 8 знака после десятичной точки.
