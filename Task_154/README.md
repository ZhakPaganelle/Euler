##Exploring Pascal's pyramid

A triangular pyramid is constructed using spherical balls so that each ball rests on exactly three balls of the next lower level.
Then, we calculate the number of paths leading from the apex to each position:
A path starts at the apex and progresses downwards to any of the three spheres directly below the current position.
Consequently, the number of paths to reach a certain position is the sum of the numbers immediately above it (depending on the position, there are up to three numbers above it).
The result is Pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion 
(x + y + z)n.
How many coefficients in the expansion of (x + y + z)200000 are multiples of 1012?
##Исследуем пирамиду Паскаля

Треугольная пирамида составлена из шаров таким образом, что каждый шар лежит ровно на трех шарах нижнего уровня.

Итак, рассчитаем количество путей, ведущих из вершины к каждому шару:
Каждый путь начинается в вершине и следует вниз к одному из трех шаров, находящихся под текущим положением.
В результате выходит, что количество путей до определенного шара равно сумме количеств возможных путей до шаров, находящихся над ним (в зависимости от положения, над ним может находиться до трех шаров).
Таким образом получаем пирамиду Паскаля, где числа на каждом уровне n равны коэффициентам разложения трехчлена 
(x + y + z)n.
Сколько коэффициентов разложения (x + y + z)200000 делятся на 1012?
