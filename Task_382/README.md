##Generating polygons


A polygon is a flat shape consisting of straight line segments that are joined to form a closed chain or circuit. A polygon consists of at least three sides and does not self-intersect.


A set S of positive numbers is said to generate a polygon P if:

For example:
The set {3, 4, 5} generates a polygon with sides 3, 4, and 5 (a triangle).
The set {6, 9, 11, 24} generates a polygon with sides 6, 9, 11, and 24 (a quadrilateral).
The sets {1, 2, 3} and {2, 3, 4, 9} do not generate any polygon at all.

Consider the sequence s, defined as follows:

Let Un be the set {s1, s2, ..., sn}. For example, U10 = {1, 2, 3, 4, 6, 9, 13, 19, 28, 41}.
Let f(n) be the number of subsets of Un which generate at least one polygon.
For example, f(5) = 7, f(10) = 501 and f(25) = 18635853.


Find the last 9 digits of f(1018).

##Генерирование многоугольников


Многоугольник - это плоская фигура, состоящая из соединенных между собой отрезков, образующих замкнутую цепь или контур. Многоугольник состоит как минимум из трех сторон и не пересекает сам себя.


Множество положительных чисел S генерирует многоугольник P, если:


 никакие две стороны P не имеют одинаковую длину,
 длина каждой стороны P содержится в S, и
 S не содержит никаких других значений.


Например:

Множество {3, 4, 5} генерирует многоугольник со сторонами 3, 4 и 5 (треугольник).

Множество {6, 9, 11, 24} генерирует многоугольник со сторонами 6, 9, 11 и 24 (четырехугольник).

Множества {1, 2, 3} и {2, 3, 4, 9} не генерируют никакие многоугольники.



Рассмотрим последовательность s, определенную следующим образом:


s1 = 1, s2 = 2, s3 = 3
sn = sn-1 + sn-3 для n
>
 3.


Пусть Un будет множеством {s1, s2, ..., sn}. Например, U10 = {1, 2, 3, 4, 6, 9, 13, 19, 28, 41}.

Пусть f(n) будет количеством подмножеств Un, которые генерируют хотя бы один многоугольник.

Например, f(5) = 7, f(10) = 501 и f(25) = 18635853.


Найдите последние 9 цифр f(1018).

