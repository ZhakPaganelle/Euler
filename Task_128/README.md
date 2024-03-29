##Hexagonal tile differences

A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.
New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three rings.
By finding the difference between tile n and each of its six neighbours we shall define PD(n) to be the number of those differences which are prime.
For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.
In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.
It can be shown that the maximum value of PD(n) is 3.
If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.
Find the 2000th tile in this sequence.
##Разности шестиугольных плиток

Шестиугольная плитка с номером 1 окружена кольцом из шести других шестиугольных плиток, которые нумеруются от 2 до 7 против часовой стрелки, начиная с плитки, находящейся ровно сверху от 1.
Новые кольца из плиток, которые добавляются по тому же принципу, нумеруются числами от 8 до 19, от 20 до 37, от 38 до 61, и т.д. На рисунке ниже показаны первые 3 кольца.



Найдем разности между плиткой n и каждой из шести соседних плиток и определим PD(n) как число разностей, являющихся простыми числами.
К примеру, идя по часовой стрелке вокруг плитки 8, разности равны: 12, 29, 11, 6, 1 и 13. Таким образом, PD(8) = 3.
Подобным образом, разности вокруг плитки 17 равны: 1, 17, 16, 1, 11, и 10, так что PD(17) = 2.
Можно показать, что максимальное значение PD(n) = 3.
Если записать все номера плиток, для которых PD(n) = 3, в возрастающем порядке, формируя последовательность, то 10-й член этой последовательности будет 271.
Найдите 2000-ю плитку в этой последовательности.
