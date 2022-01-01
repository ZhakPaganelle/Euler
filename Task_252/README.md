##Convex Holes


Given a set of points on a plane, we define a convex hole to be a convex polygon having as vertices any of the given points and not containing any of the given points in its interior (in addition to the vertices, other given points may lie on the perimeter of the polygon). 


As an example, the image below shows a set of twenty points and a few such convex holes. 
The convex hole shown as a red heptagon has an area equal to 1049694.5 square units, which is the highest possible area for a convex hole on the given set of points.



For our example, we used the first 20 points (T2k−1, T2k), for k = 1,2,…,20, produced with the pseudo-random number generator:

i.e. (527, 144), (−488, 732), (−454, −947), …


What is the maximum area for a convex hole on the set containing the first 500 points in the pseudo-random sequence? Specify your answer including one digit after the decimal point.

##Выпуклые отверстия


При данном множестве точек на плоскости, определим выпуклое отверстие как выпуклый многоугольник, имеющий в качестве вершин любые из данных точек и не содержащий данные точки внутри себя (в дополнение к этому, данные точки могут лежать на сторонах многоугольника).


К примеру, рисунок ниже показывает множество из двадцати точек и несколько выпуклых отверстий. Выпуклое отверстие, обозначенное красным семиугольником, имеет площадь 1 049 694.5 единиц площади, что является самой большой возможной площадью для выпуклого отверстия при данном множестве точек.



В нашем примере мы использовали первые 20 точек (T
2k−1

, T
2k

), для k = 1,2,…,20, полученных с помощью следующего генератора псевдослучайных чисел:


S0
= 
290797 

Sn+1
= 
Sn2 mod 50515093

Tn
= 
( Sn mod 2000 ) − 1000 



К примеру, (527, 144), (−488, 732), (−454, −947), …



Какова максимальная площадь выпуклого отверстия при данном множестве из первых 500 точек такой псевдослучайной последовательности? Укажите ответ, включая одну цифру после десятичной точки.

