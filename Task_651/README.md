##Patterned Cylinders

An infinitely long cylinder has its curved surface fully covered with different coloured but otherwise identical rectangular stickers, without overlapping. The stickers are aligned with the cylinder, so two of their edges are parallel with the cylinder's axis, with four stickers meeting at each corner.
Let $a>0$ and suppose that the colouring is periodic along the cylinder, with the pattern repeating every $a$ stickers. (The period is allowed to be any divisor of $a$.) Let $b$ be the number of stickers that fit round the circumference of the cylinder.
Let $f(m, a, b)$ be the number of different such periodic patterns that use exactly $m$ distinct colours of stickers. Translations along the axis, reflections in any plane, rotations in any axis, (or combinations of such operations) applied to a pattern are to be counted as the same as the original pattern.
You are given that $f(2, 2, 3) = 11$, $f(3, 2, 3) = 56$, and $f(2, 3, 4) = 156$.
Furthermore, $f(8, 13, 21) \equiv 49718354 \pmod{1\,000\,000\,007}$,
and $f(13, 144, 233) \equiv 907081451 \pmod{1\,000\,000\,007}$.
Find $\sum_{i=4}^{40} f(i, F_{i-1}, F_i) \bmod 1\,000\,000\,007$, where $F_i$ are the Fibonacci numbers starting at $F_0=0$, $F_1=1$.
##Узорные цилиндры

Боковая поверхность бесконечно длинного цилиндра полностью покрыта разноцветными, но во всем остальном идентичными прямоугольными наклейками, которые не перекрываются. Наклейки выровнены вдоль цилиндра так, что две их стороны параллельны оси цилиндра и каждая наклейка касается своими углами четырех других.
Положим $a>0$, и положим, что расцветка периодична вдоль оси цилиндра и узор повторяется через каждые $a$ наклеек (период может быть любым делителем числа $a$). Пусть $b$ будет числом наклеек, которые помещаются на длине окружности цилиндра.
Пусть $f(m, a, b)$ будет количеством различных таких периодических узоров, в которых используется ровно $m$ различных цветов наклеек. Параллельный перенос вдоль оси, отражения в любой плоскости, вращения в любой плоскости (или комбинации подобных преобразований), примененные к узору, считаются такими же, как и изначальный узор.
Известно, что $f(2, 2, 3) = 11$, $f(3, 2, 3) = 56$ и $f(2, 3, 4) = 156$.
Более того, $f(8, 13, 21) \equiv 49718354 \pmod{1\,000\,000\,007}$ и $f(13, 144, 233) \equiv 907081451 \pmod{1\,000\,000\,007}$.
Найдите $\sum_{i=4}^{40} f(i, F_{i-1}, F_i) \bmod 1\,000\,000\,007$, где $F_i$ - числа Фибоначчи, начинающиеся с $F_0=0$, $F_1=1$.
