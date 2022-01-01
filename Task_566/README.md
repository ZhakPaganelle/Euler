##Cake Icing Puzzle

Adam plays the following game with his birthday cake.
He cuts a piece forming a circular sector of 60 degrees and flips the piece upside down, with the icing on the bottom.
He then rotates the cake by 60 degrees counterclockwise, cuts an adjacent 60 degree piece and flips it upside down.
He keeps repeating this, until after a total of twelve steps, all the icing is back on top.
Amazingly, this works for any piece size, even if the cutting angle is an irrational number: all the icing will be back on top after a finite number of steps.
Now, Adam tries something different: he alternates cutting pieces of size $x=\frac{360}{9}$ degrees, $y=\frac{360}{10}$ degrees and $z=\frac{360 }{\sqrt{11}}$ degrees. The first piece he cuts has size x and he flips it. The second has size y and he flips it. The third has size z and he flips it. He repeats this with pieces of size x, y and z in that order until all the icing is back on top, and discovers he needs 60 flips altogether.
Let F(a, b, c) be the minimum number of piece flips needed to get all the icing back on top for pieces of size $x=\frac{360}{a}$ degrees, $y=\frac{360}{b}$ degrees and $z=\frac{360}{\sqrt{c}}$ degrees.
Let $G(n) = \sum_{9 \le a < b < c \le n} F(a,b,c)$, for integers a, b and c.
You are given that F(9, 10, 11) = 60, F(10, 14, 16) = 506, F(15, 16, 17) = 785232.
You are also given G(11) = 60, G(14) = 58020 and G(17) = 1269260.
Find G(53).
##Загадка глазури на торте

Адам играет в следующую игру с тортом со своего дня рождения:
Он отрезает кусок, образующий сектор круга в 60 градусов, и переворачивает кусок вверх ногами так, что глазурь остается снизу.
Потом он поворачивает торт на 60 градусов против часовой стрелки, отрезает прилегающий 60-градусный кусок и переворачивает его.
Он продолжает этот процесс, пока, наконец, после двенадцати шагов, вся глазурь снова не окажется сверху.
Удивительно, но это работает с любым выбранным размером куска, даже если угол отреза иррационален: вся глазурь снова окажется сверху после конечного количества шагов.
Теперь Адам пробует что-то новое: он поочередно отрезает куски размерами $x=\frac{360}{9}$ градусов, $y=\frac{360}{10}$ градусов и $z=\frac{360 }{\sqrt{11}}$ градусов. Превым он отрезает кусок размером x и переворачивает его. Вторым он отрезает кусок размером y и переворачивает его. Третьим он отрезает кусок размером z и переворачивает его. Он повторяет этот процесс с кусками размером x, y и z в таком порядке до тех пор, пока вся глазурь снова не окажется сверху, и обнаруживает, что для этого ему необходимо всего 60 переворотов.

Пусть F(a, b, c) будет минимальным количеством переворотов кусков, необходимым для того, чтобы вся глазурь снова оказалась сверху, для кусков размерами $x=\frac{360}{a}$ градусов, $y=\frac{360}{b}$ градусов и $z=\frac{360}{\sqrt{c}}$ градусов.
Пусть $G(n) = \sum_{9 \le a < b < c \le n} F(a,b,c)$ для целых a, b и c.
Известно, что F(9, 10, 11) = 60, F(10, 14, 16) = 506, F(15, 16, 17) = 785232.
Вам также дано, что G(11) = 60, G(14) = 58020 и G(17) = 1269260.
Найдите G(53).
