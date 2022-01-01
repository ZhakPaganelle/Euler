##Box-ball system


Consider an infinite row of boxes. Some of the boxes contain a ball. For example, an initial configuration of 2 consecutive occupied boxes followed by 2 empty boxes, 2 occupied boxes, 1 empty box, and 2 occupied boxes can be denoted by the sequence (2, 2, 2, 1, 2), in which the number of consecutive occupied and empty boxes appear alternately.


A turn consists of moving each ball exactly once according to the following rule: Transfer the leftmost ball which has not been moved to the nearest empty box to its right.


After one turn the sequence (2, 2, 2, 1, 2) becomes (2, 2, 1, 2, 3) as can be seen below; note that we begin the new sequence starting at the first occupied box.


A system like this is called a Box-Ball System or BBS for short.


It can be shown that after a sufficient number of turns, the system evolves to a state where the consecutive numbers of occupied boxes is invariant. In the example below, the consecutive numbers of occupied boxes evolves to [1, 2, 3]; we shall call this the final state.


We define the sequence {ti}:

Starting from the initial configuration (t0, t1, …, t10), the final state becomes [1, 3, 10, 24, 51, 75].
Starting from the initial configuration (t0, t1, …, t10 000 000), find the final state.
Give as your answer the sum of the squares of the elements of the final state. For example, if the final state is [1, 2, 3] then 14 ( = 12 + 22 + 32) is your answer.

##Система шаров и коробок


Рассмотрим бесконечный ряд коробок. Некоторые из них содержат один шар. Например, начальное расположение из 2 последовательных полных коробок, за которыми следуют 2 пустые, потом 2 полные, потом 1 пустая коробка и 2 полные, может быть обозначено последовательностью (2, 2, 2, 1, 2), в которой попеременно записано количество последовательных полных и пустых коробок.


Один ход заключается в перемещении каждого шара ровно один раз по следующему правилу: переместите самый левый шар, который еще не был перемещен, в ближайшую пустую коробку справа от него.


После одного хода последовательность (2, 2, 2, 1, 2) становится (2, 2, 1, 2, 3), как показано ниже. Заметьте, что запись новой последовательности начинается с первой полной коробки.





Подобная система называется системой шаров и коробок (Box-Ball System, или сокращенно BBS).


Можно показать, что после достаточного количества ходов система достигает состояния, в котором последовательные количества полных коробок больше не меняются. В примере ниже последовательное количество полных коробок достигает [1, 2, 3] - назовем это конечным состоянием.





Определим последовательность {ti}:

s0 = 290797
sk+1 = sk2 mod 50515093
tk = (sk mod 64) + 1



Начиная с исходного расположения (t0, t1, …, t10), конечное состояние будет [1, 3, 10, 24, 51, 75].
Найдите конечное состояние для исходного расположения (t0, t1, …, t10 000 000).
Дайте ответ как сумму квадратов элементов конечного состояния. Например, если конечное состояние - [1, 2, 3], тогда 12 + 22 + 32 = 14 будет Вашим ответом.

