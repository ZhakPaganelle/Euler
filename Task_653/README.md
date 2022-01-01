##Frictionless Tube

Consider a horizontal frictionless tube with length $L$ millimetres, and a diameter of 20 millimetres. The east end of the tube is open, while the west end is sealed. The tube contains $N$ marbles of diameter 20 millimetres at designated starting locations, each one initially moving either westward or eastward with common speed $v$.
Since there are marbles moving in opposite directions, there are bound to be some collisions. We assume that the collisions are perfectly elastic, so both marbles involved instantly change direction and continue with speed $v$ away from the collision site. Similarly, if the west-most marble collides with the sealed end of the tube, it instantly changes direction and continues eastward at speed $v$. On the other hand, once a marble reaches the unsealed east end, it exits the tube and has no further interaction with the remaining marbles.
To obtain the starting positions and initial directions, we use the pseudo-random sequence $r_j$ defined by:
$r_1 = 6\,563\,116$
$r_{j+1} = r_j^2 \bmod 32\,745\,673$
The west-most marble is initially positioned with a gap of $(r_1 \bmod 1000) + 1$ millimetres between it and the sealed end of the tube, measured from the west-most point of the surface of the marble. Then, for $2\le j\le N$, counting from the west, the gap between the $(j-1)$th and $j$th marbles, as measured from their closest points, is given by $(r_j \bmod 1000) + 1$ millimetres.
Furthermore, the $j$th marble is initially moving eastward if $r_j \le 10\,000\,000$, and westward if $r_j > 10\,000\,000$.
For example, with $N=3$, the sequence specifies gaps of 117, 432, and 173 millimetres. The marbles' centres are therefore 127, 579, and 772 millimetres from the sealed west end of the tube. The west-most marble initially moves eastward, while the other two initially move westward.
Under this setup, and with a five metre tube ($L=5000$), it turns out that the middle (second) marble travels 5519 millimetres before its centre reaches the east-most end of the tube.
Let $d(L, N, j)$ be the distance in millimetres that the $j$th marble travels before its centre reaches the eastern end of the tube. So $d(5000, 3, 2) = 5519$. You are also given that $d(10\,000, 11, 6) = 11\,780$ and $d(100\,000, 101, 51) = 114\,101$.
Find $d(1\,000\,000\,000, 1\,000\,001, 500\,001)$.
##Свободная от трения труба

Рассмотрим горизонтальную свободную от трения трубу длиной $L$ миллиметров и диаметром 20 миллиметров. Восточный конец трубы открыт, а западный - закрыт. В трубе в определенных начальных положениях находятся $N$ шариков диаметром 20 миллиметров, каждый из них изначально движется на запад или на восток с одинаковой скоростью $v$.
Так как есть шарики, движущиеся в противоположные стороны, между ними неизбежны столкновения. Мы полагаем, что столкновения идеально эластичны и оба столкнувшихся шарика мгновенно меняют направление движения и продолжают двигаться от места столкновения со скоростью $v$. Таким же образом, если самый западный шарик столкнется с закрытым концом трубы, он мгновенно изменит направление движения и продолжит двигаться на восток со скоростью $v$. С другой стороны, если шарик достигнет открытого восточного конца, он покинет трубу и больше не взаимодействует с оставшимися шариками.
Чтобы получить начальные положения и направления движения шариков, используем псевдослучайную последовательность $r_j$, заданную следующим образом:
$r_1 = 6\,563\,116$
$r_{j+1} = r_j^2 \bmod 32\,745\,673$
Самый западный шарик изначально размещается на расстоянии $(r_1 \bmod 1000) + 1$ миллиметров от закрытого конца трубы, считая от самой западной точки на поверхности шарика. Затем, для $2\le j\le N$, считая с запада на восток, расстояние между $(j-1)$-тым и $j$-тым шариком, отмеренное между их ближайшими точками, задано как $(r_j \bmod 1000) + 1$ миллиметров.
Наконец, $j$-тый шарик изначально движется на восток, если if $r_j \le 10\,000\,000$, или на запад, если $r_j > 10\,000\,000$.
Например, при $N=3$, последовательность определяет расстояния в 117, 432 и 173 миллиметра. Таким образом, центры шариков находятся на расстоянии 127, 579 и 772 миллиметров от закрытого конца трубы. Самый западный шарик изначально движется на восток, а остальны два - изначально на запад.
При таком исходном состоянии и длине трубы 5 метров ($L=5000$), оказывается, что средний (второй) шарик пройдет путь 5519 миллиметров до того, как его центр достигнет восточного конца трубы.
Пусть $d(L, N, j)$ будет длиной пути $j$-того шарика, пройденного им до того, как его центр достигнет восточного конца трубы. Таким образом, $d(5000, 3, 2) = 5519$. Также известно, что $d(10\,000, 11, 6) = 11\,780$ и $d(100\,000, 101, 51) = 114\,101$.
Найдите $d(1\,000\,000\,000, 1\,000\,001, 500\,001)$.
