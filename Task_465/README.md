##Polar polygons

The kernel of a polygon is defined by the set of points from which the entire polygon's boundary is visible. We define a polar polygon as a polygon for which the origin is strictly contained inside its kernel.
For this problem, a polygon can have collinear consecutive vertices. However, a polygon still cannot have self-intersection and cannot have zero area.
For example, only the first of the following is a polar polygon (the kernels of the second, third, and fourth do not strictly contain the origin, and the fifth does not have a kernel at all):


Notice that the first polygon has three consecutive collinear vertices.
Let P(n) be the number of polar polygons such that the vertices (x, y) have integer coordinates whose absolute values are not greater than n.
Note that polygons should be counted as different if they have different set of edges, even if they enclose the same area. For example, the polygon with vertices [(0,0),(0,3),(1,1),(3,0)] is distinct from the polygon with vertices [(0,0),(0,3),(1,1),(3,0),(1,0)].
For example, P(1) = 131, P(2) = 1648531, P(3) = 1099461296175 and P(343) mod 1 000 000 007 = 937293740.
Find P(713) mod 1 000 000 007.
##Полярные многоугольники

Ядро многоугольника определено как множество точек, из которых обозрима вся граница многоугольника. Мы определим полярный многоугольник как многоугольник, для которого начало координат строго содержится в его ядре.
В рамках этой задачи многоугольник может иметь коллинеарные последовательные вершины. Однако, многоугольник по-прежнему не может самопересекаться или иметь нулевую площадь.
Например, только первый из следующих многоугольников является полярным (ядра второго, третьего и четвертого не содержат строго начало координат, а пятый вообще не имеет ядра):

Обратите внимание, что первый многоугольник имеет три последовательные коллинеарные вершины.
Пусть P(n) будет количеством полярных многоугольников, таких что их вершины (x, y) имеют целочисленные координаты, чьи абсолютные значения не превышают n.
Заметим, что многоугольники считаются разными, если они имеют различное множество сторон, даже если они заключают одинаковую площадь. Например, многоугольник со вершинами [(0,0),(0,3),(1,1),(3,0)] отличается от многоугольника со вершинами [(0,0),(0,3),(1,1),(3,0),(1,0)].
Для примера, P(1) = 131, P(2) = 1648531, P(3) = 1099461296175 и P(343) mod 1 000 000 007 = 937293740.
Найдите P(713) mod 1 000 000 007.
