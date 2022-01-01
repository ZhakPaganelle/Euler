##Selective Amnesia

Larry and Robin play a memory game involving a sequence of random numbers between 1 and 10, inclusive, that are called out one at a time. Each player can remember up to 5 previous numbers. When the called number is in a player's memory, that player is awarded a point. If it's not, the player adds the called number to his memory, removing another number if his memory is full.
Both players start with empty memories. Both players always add new missed numbers to their memory but use a different strategy in deciding which number to remove:
Larry's strategy is to remove the number that hasn't been called in the longest time.
Robin's strategy is to remove the number that's been in the memory the longest time.
Example game:
Denoting Larry's score by L and Robin's score by R, what is the expected value of |L-R| after 50 turns? Give your answer rounded to eight decimal places using the format x.xxxxxxxx .
##Выборочная амнезия

Лэрри и Робин играют в игру на запоминание последовательности случайных чисел от 1 до 10 включительно, которые во время игры называются по одному. Каждый игрок может запомнить до пяти названных чисел. Если названное число присутствует в памяти игрока, он получает одно очко. В противном случае игрок добавляет это число в свою память, стирая одно из имеющихся там чисел, если вся его память заполнена.
Оба игрока начинают с пустой памятью. Оба игрока запоминают каждое отсутствующее в памяти число, но при этом используют разные стратегии, чтобы решить, какое число стереть из памяти: 
Лэрри стирает то число, которое дольше всех не было названо. 
Робин стирает то число, которое дольше всех находилось в его памяти.
Пример такой игры:


Ход
Названноечисло
ПамятьЛэрри
ОчкиЛэрри
ПамятьРобина
ОчкиРобина


1
1
1
0
1
0


2
2
1,2
0
1,2
0


3
4
1,2,4
0
1,2,4
0


4
6
1,2,4,6
0
1,2,4,6
0


5
1
1,2,4,6
1
1,2,4,6
1


6
8
1,2,4,6,8
1
1,2,4,6,8
1


7
10
1,4,6,8,10
1
2,4,6,8,10
1


8
2
1,2,6,8,10
1
2,4,6,8,10
2


9
4
1,2,4,8,10
1
2,4,6,8,10
3


10
1
1,2,4,8,10
2
1,4,6,8,10
3

Если обозначить очки Лэрри L, а очки Робина R, каково ожидаемое значение |L-R| после 50 ходов? Дайте ответ, округленный до восьмого знака после десятичной точки в виде x.xxxxxxxx .
