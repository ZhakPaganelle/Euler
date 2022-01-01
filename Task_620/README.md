##Planetary Gears

A circle $C$ of circumference $c$ centimetres has a smaller circle $S$ of circumference $s$ centimetres lying off-centre within it. Four other distinct circles, which we call "planets", with circumferences $p$, $p$, $q$, $q$ centimetres respectively ($p<q$), are inscribed within $C$ but outside $S$, with each planet touching both $C$ and $S$ tangentially. The planets are permitted to overlap one another, but the boundaries of $S$ and $C$ must be at least 1cm apart at their closest point.
Now suppose that these circles are actually gears with perfectly meshing teeth at a pitch of 1cm. $C$ is an internal gear with teeth on the inside. We require that $c$, $s$, $p$, $q$ are all integers (as they are the numbers of teeth), and we further stipulate that any gear must have at least 5 teeth.
Note that "perfectly meshing" means that as the gears rotate, the ratio between their angular velocities remains constant, and the teeth of one gear perfectly align with the groves of the other gear and vice versa. Only for certain gear sizes and positions will it be possible for $S$ and $C$ each to mesh perfectly with all the planets. Arrangements where not all gears mesh perfectly are not valid.
Define $g(c,s,p,q)$ to be the number of such gear arrangements for given values of $c$, $s$, $p$, $q$: it turns out that this is finite as only certain discrete arrangements are possible satisfying the above conditions. For example, $g(16,5,5,6)=9$.
Here is one such arrangement:
Let $G(n) = \sum_{s+p+q\le n} g(s+p+q,s,p,q)$ where the sum only includes cases with $p<q$, $p\ge 5$, and $s\ge 5$, all integers. You are given that $G(16)=9$ and $G(20)=205$.
Find $G(500)$.
##Планетарные шестерни

В окружности $C$ с длиной окружности $c$ сантиметров лежит смещенная от центра меньшая окружность $S$ с длиной окружности $s$ сантиметров. Четыре другие отличающиеся окружности, называемые "планетами", с длинами окружности $p$, $p$, $q$, $q$  сантиметров соответственно ($p<q$) вписаны в $C$ снаружи $S$, и каждая планета касается обеих окружностей $C$ и $S$. Планеты могут пересекаться между собой, однако границы окружностей $S$ и $C$ должны находиться на расстоянии не меньше 1 см друг от друга в любой их точке.
Теперь представим, что эти окружности на самом деле шестерни с идеально зацепляющимися зубцами и шагом 1 сантиметр. $C$ является внутренней шестерней с зубцами внутри. Мы требуем, чтобы $c$, $s$, $p$, $q$ имели целочисленные значения (так как они представялют число зубцов), и мы также оговариваем, что любая шестерня должна иметь не меньше 5 зубцов.
Заметим, что "идеально зацепляющиеся" обозначает, что при вращении шестерней отношение их угловых скоростей остается неизменным и зубцы одной шестерни идеально входят в канавки другой, и наоборот. Идеальное зацепление $S$ и $C$ со всеми планетами возможно только при определенных размерах и положениях шестерней. Расположения, где не все шестерни идеально зацепляются, не считаются корректными.
Определим $g(c,s,p,q)$ как количество таких расположений шестерней для данных значений $c$, $s$, $p$, $q$: оказывается, что оно конечно, так как только определенные дискретные расположения удовлетворяют вышеуказанным условиям. Например, $g(16,5,5,6)=9$.
Вот одно из таких расположений:

Пусть $G(n) = \sum_{s+p+q\le n} g(s+p+q,s,p,q)$, где сумма включает в себя только случаи с целыми $p<q$, $p\ge 5$ и $s\ge 5$. Известно, что $G(16)=9$ и $G(20)=205$.
Найдите $G(500)$.
