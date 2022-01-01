##Geoboard Shapes

A geoboard (of order N) is a square board with equally-spaced pins protruding from the surface, representing an integer point lattice for coordinates 0 ≤ x,y ≤ N.
John begins with a pinless geoboard. Each position on the board is a hole that can be filled with a pin. John decides to generate a random integer between 1 and N+1 (inclusive) for each hole in the geoboard. If the random integer is equal to 1 for a given hole, then a pin is placed in that hole.
After John is finished generating numbers for all (N+1)2 holes and placing any/all corresponding pins, he wraps a tight rubberband around the entire group of pins protruding from the board. Let S represent the shape that is formed. S can also be defined as the smallest convex shape that contains all the pins.
The above image depicts a sample layout for N = 4. The green markers indicate positions where pins have been placed, and the blue lines collectively represent the rubberband. For this particular arrangement, S has an area of 6. If there are fewer than three pins on the board (or if all pins are collinear), S can be assumed to have zero area.
Let E(N) be the expected area of S given a geoboard of order N. For example, E(1) = 0.18750, E(2) = 0.94335, and E(10) = 55.03013 when rounded to five decimal places each.
Calculate E(100) rounded to five decimal places.
##Фигуры на геодоске

Геодоска (порядка N) - это квадратная доска, на поверхности которой через равные интервалы расположены штырьки, представляющие точки с целочисленными координатами на координатной сетке 0 ≤ x,y ≤ N.
Джон начинает с геодоски без штырьков. Каждая позиция на доске представляет собой отверстие, в которое может быть вставлен штырек. Джон генерирует случайное число между 1 и N+1 (включительно) для каждого отверстия на геодоске, и если это число равно 1, вставляет в это отверстие штырек.
После того, как Джон закончил генерировать числа для всех (N+1)2 отверстий и вставил все необходимые штырьки, он обтягивает тугой резинкой всю группу штырьков на доске. Пусть S обозначает образованную резинкой фигуру. S также можно определить как наименьшую выпуклую фигуру, содержащую все штырьки.

На картинке выше изображен пример доски для N = 4. Зеленые точки показывают позиции, где стоят штырьки, а совокупность синих отрезков изображает резинку. Для этого конкретного расположения площадь S равна 6. Если на доске меньше трех штырьков (или все штырьки лежат на одной прямой), площадь S считается равной нулю.
Пусть E(N) будет ожидаемой площадью S для геодоски порядка N. Например, E(1) = 0.18750, E(2) = 0.94335 и E(10) = 55.03013 при округлении до пятого знака после десятичной точки.
Рассчитайте E(100), округленное до пятого знака после десятичной точки.
