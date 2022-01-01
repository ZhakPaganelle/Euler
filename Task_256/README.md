##Tatami-Free Rooms

Tatami are rectangular mats, used to completely cover the floor of a room, without overlap.
Assuming that the only type of available tatami has dimensions 1×2, there are obviously some limitations for the shape and size of the rooms that can be covered.
For this problem, we consider only rectangular rooms with integer dimensions a, b and even size s = a·b.
We use the term 'size' to denote the floor surface area of the room, and — without loss of generality — we add the condition a ≤ b.
There is one rule to follow when laying out tatami: there must be no points where corners of four different mats meet.
For example, consider the two arrangements below for a 4×4 room:
The arrangement on the left is acceptable, whereas the one on the right is not: a red "X" in the middle, marks the point where four tatami meet.
Because of this rule, certain even-sized rooms cannot be covered with tatami: we call them tatami-free rooms.
Further, we define T(s) as the number of tatami-free rooms of size s.
The smallest tatami-free room has size s = 70 and dimensions 7×10.
All the other rooms of size s = 70 can be covered with tatami; they are: 1×70, 2×35 and 5×14.
Hence, T(70) = 1.
Similarly, we can verify that T(1320) = 5 because there are exactly 5 tatami-free rooms of size s = 1320:
20×66, 22×60, 24×55, 30×44 and 33×40.
In fact, s = 1320 is the smallest room-size s for which T(s) = 5.
Find the smallest room-size s for which T(s) = 200.
##Комнаты без татами

Татами - прямоугольные маты, которыми полностью покрывают пол комнаты, без перекрытий.
Предположим, что единственный возможный вид татами имеет размеры 1×2, очевидно, что на размер и форму комнаты накладываются некоторые ограничения, чтобы пол комнаты можно было покрыть целиком.
В данной задаче мы рассматриваем только комнаты прямоугольной формы с целыми размерами a, b и четным размером s = a·b.
Под термином 'размер' мы подразумеваем площадь поверхности пола комнаты и, без потери условия обобщенности, добавим требование a ≤ b.
При покрытии татами есть одно правило, которому необходимо следовать: не должно быть ни одной такой точки, где происходил бы стык четырех разных матов.
К примеру, рассмотрим два варианта покрытия пола комнаты 4×4 ниже:



Вариант покрытия слева приемлем, в то время как правый вариант - нет: красный символ "X" в середине указывает место стыка четырех матов татами
Из-за такого правила, даже для комнат с четными размерами не всегда можно покрыть пол татами: такие комнаты мы будем называть комнатами без татами.
Далее, определим T(s) как число комнат без татами размером s.
Наименьшая комната без татами имеет размер s = 70 и размерности 7×10.
Полы всех остальных комнат размером s = 70 можно покрыть татами; размерности таких комнат: 1×70, 2×35 и 5×14.
Значит, T(70) = 1.
Аналогично, мы можем убедиться в том, что T(1320) = 5, т.к. существует ровно 5 комнат без татами размером s = 1320: 20×66, 22×60, 24×55, 30×44 и 33×40.
К слову, s = 1320 является наименьшим размером s комнаты, для которой T (s) = 5.
Найдите наименьший размер комнаты s, при котором T(s) = 200.
