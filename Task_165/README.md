##Intersections

A segment is uniquely defined by its two endpoints. By considering two line segments in plane geometry there are three possibilities: 
the segments have zero points, one point, or infinitely many points in common.
Moreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of either one of the segments or of both. If a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.
We will call a common point T of two segments L1 and L2 a true intersection point of L1 and L2  if T is the only common point of L1 and L2  and T is an interior point of both segments.

Consider the three segments L1, L2, and L3:
L1: (27, 44) to (12, 32)
L2: (46, 53) to (17, 62)
L3: (46, 70) to (22, 40)
It can be verified that line segments L2 and L3 have a true intersection point. We note that as the one of the end points of L3: (22,40) lies on L1 this is not considered to be a true point of intersection. L1 and L2 have no common point. So among the three line segments, we find one true intersection point.
Now let us do the same for 5000 line segments. To this end, we generate 20000 numbers using the so-called "Blum Blum Shub" pseudo-random number generator.
s0 = 290797
sn+1 = sn×sn (modulo 50515093)
tn = sn (modulo 500)
To create each line segment, we use four consecutive numbers tn. That is, the first line segment is given by:
(t1, t2) to (t3, t4)
The first four numbers computed according to the above generator should be: 27, 144, 12 and 232. The first segment would thus be (27,144) to (12,232).
How many distinct true intersection points are found among the 5000 line segments?
##Пересечения

Отрезок однозначно определяется своими двумя конечными точками. Рассматривая два отрезка на геометрической плоскости, возможны три варианта:
у отрезков нет общих точек, есть одна общая точка или бесконечное множество общих точек.
Более того, если у двух отрезков одна общая точка, то возможно, что эта общая точка является одним из концов либо одного отрезка, либо обоих. Если общая точка двух отрезков не является конечной точкой ни одного из них, то такая точка лежит на обоих отрезках.
Будем называть общую точку T двух отрезков L1 и L2 истинной точкой пересечения отрезков L1 и L2, если T является единственной общей точкой отрезков L1 и L2, и, одновременно, Т лежит на обоих отрезках (не являясь концом ни одного из них).

Рассмотрим три отрезка L1, L2, и L3:
L1: от (27, 44) до (12, 32)
L2: от (46, 53) до (17, 62)
L3: от (46, 70) до (22, 40)
Нетрудно убедиться в том, что у отрезков L2 и L3 есть истинная точка пересечения. Отметим, что, т.к. одна из конечных точек L3: (22,40) лежит на отрезке L1, она не является истинной точкой пересечения. У отрезков L1 и L2 нет общих точек. Таким образом, у этих трех отрезков есть одна истинная точка пересечения.
Теперь, повторим то же самое для 5000 отрезков. Для этого, сгенерируем 20000 псевдослучайных чисел, воспользовавашись так называемым алгоритмом Blum-Blum-Shub:
s0 = 290797
sn+1 = sn×sn (modulo 50515093)
tn = sn (modulo 500)
Для построения каждого отрезка воспользуемся четырьмя последовательными числами tn. Это значит, что первый отрезок определяется следующими координатами:
от (t1, t2) до (t3, t4)
Первые четыре числа, сгенерированные с помощью этого алгоритма, будут равны 27, 144, 12 и 232. Таким образом, первый отрезок будет задаваться точками (27,144) и (12,232).
Сколько различных истинных точек пересечения можно найти у 5000 отрезков?
