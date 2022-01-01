##Jumping Flea

A regular hexagon table of side length $N$ is divided into equilateral triangles of side length $1$. The picture below is an illustration of the case $N = 3$.
An flea of negligible size is jumping on this table. The flea starts at the centre of the table. Thereafter, at each step, it chooses one of the six corners of the table, and jumps to the mid-point between its current position and the chosen corner.
For every triangle $T$, we denote by $J(T)$ the minimum number of jumps required for the flea to reach the interior of $T$. Landing on an edge or vertex of $T$ is not sufficient.
For example, $J(T) = 3$ for the triangle marked with a star in the picture: by jumping from the centre half way towards F, then towards C, then towards E.
Let $S(N)$ be the sum of $J(T)$ for all the upper-pointing triangles $T$ in the upper half of the table. For the case $N = 3$, these are the triangles painted black in the above picture.
You are given that $S(3) = 42$, $S(5) = 126$, $S(123) = 167178$, and $S(12345) = 3185041956$.
Find $S(123456789)$.
##Прыгающая блоха

Стол в форме правильного шестиугольника с длиной стороны $N$ разделен на равносторонние треугольники с длиной стороны $1$. На изображении ниже показан случай с $N = 3$.



Блоха пренебрежительно малого размера прыгает по столу. Блоха начинает путь в центре стола. Далее, с каждым шагом она выбирает один из шести углов стола и перепрыгивает на среднюю точку между своим текущим расположением и выбранным углом.
Для каждого треугольника $T$ обозначим минимальное количество прыжков, необходимое блохе, чтобы попасть внутрь треугольника $T$, как $J(T)$. Приземление на сторону или вершину треугольник $T$ не засчитывается.
Например, для обозначенного звездочкой на изображении треугольника $J(T) = 3$: прыжок на половину пути от центра до F, затем к C, затем к E.
Пусть $S(N)$ будет суммой $J(T)$ для всех треугольников $T$, расположенных на верхней половине стола и направленных вершиной вверх. Такие треугольники для случая $N = 3$ закрашены черным на изображении выше.
Известно, что $S(3) = 42$, $S(5) = 126$, $S(123) = 167178$ и $S(12345) = 3185041956$.
Найдите $S(123456789)$. Оригинал
