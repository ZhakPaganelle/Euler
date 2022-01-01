##Cross flips

N×N disks are placed on a square game board. Each disk has a black side and white side.
At each turn, you may choose a disk and flip all the disks in the same row and the same column as this disk: thus 2×N-1 disks are flipped. The game ends when all disks show their white side. The following example shows a game on a 5×5 board.
It can be proven that 3 is the minimal number of turns to finish this game.
The bottom left disk on the N×N board has coordinates (0,0);
the bottom right disk has coordinates (N-1,0) and the top left disk has coordinates (0,N-1). 
Let CN be the following configuration of a board with N×N disks:
A disk at (x,y) satisfying $N - 1 \le \sqrt{x^2 + y^2} \lt N$, shows its black side; otherwise, it shows its white side. C5 is shown above.
Let T(N) be the minimal number of turns to finish a game starting from configuration CN or 0 if configuration CN is unsolvable.
We have shown that T(5)=3. You are also given that T(10)=29 and T(1 000)=395253.
Find $\sum \limits_{i = 3}^{31} {T(2^i - i)}$.
##Флип Флоп

На квадратном поле расставлены N×N фишек. У каждой фишки есть белая сторона и черная сторона.
Во время очередного хода происходит выбор фишки, после чего все фишки в соответствующем ряду и колонне переворачиваются: т.е. переворачивается 2×N-1 фишек. Игра завершается, когда все фишки повернуты белой стороной к верху. Ниже представлен пример игры на поле размерами 5×5 клеток.

Можно доказать, что 3 - минимальное число ходов, необходимое для завершения этой игры.
На игровом поле размерами N×N нижняя левая фишка имеет координаты (0,0), нижняя правая фишка - координаты (N-1,0), а верхняя левая - (0,N-1). 
Обозначим через CN следующую конфигурацию игрового поля размерами N×N клеток: Фишка с координатами (x,y), удовлетворяющими неравенство , повернута кверху черной стороной, в противном случае - белой стороной. К примеру, конфигурация C5 показана на рисунке выше.
Пусть T(N) - минимальное число ходов, необходимых для завершения игры с исходной конфигурации поля CN.
Если конфигурация CN не может привести к завершению игры, то T(N)=0. Как было показано, T(5)=3. Кроме того, известно, что T(10)=29 и T(1 000)=395253.
Найдите .
