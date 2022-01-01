##Spilling the beans

In Plato's heaven, there exist an infinite number of bowls in a straight line.
Each bowl either contains some or none of a finite number of beans.
A child plays a game, which allows only one kind of move: removing two beans from any bowl, and putting one in each of the two adjacent bowls. The game ends when each bowl contains either one or no beans.
For example, consider two adjacent bowls containing 2 and 3 beans respectively, all other bowls being empty. The following eight moves will finish the game:
You are given the following sequences:

$\def\htmltext#1{\style{font-family:inherit;}{\text{#1}}}$
$
\begin{align}
\qquad t_0 &= 123456,\cr
\qquad t_i &= \cases{
\;\;\frac{t_{i-1}}{2},&$\htmltext{if }t_{i-1}\htmltext{ is even}$\cr
\left\lfloor\frac{t_{i-1}}{2}\right\rfloor\oplus 926252,&$\htmltext{if }t_{i-1}\htmltext{ is odd}$\cr}\cr
&\qquad\htmltext{where }\lfloor x\rfloor\htmltext{ is the floor function }\cr
&\qquad\!\htmltext{and }\oplus\htmltext{is the bitwise XOR operator.}\cr
\qquad b_i &= (t_i\bmod2^{11}) + 1.\cr
\end{align}
$

The first two terms of the last sequence are $b_1 = 289$ and $b_2 = 145$.
If we start with $b_1$ and $b_2$ beans in two adjacent bowls, $3419100$ moves would be required to finish the game.
Consider now $1500$ adjacent bowls containing $b_1, b_2, \ldots, b_{1500}$ beans respectively, all other bowls being empty. Find how many moves it takes before the game ends.
##Рассыпание бобов

В раю Платона существует бесконечное количество мисок, выложенных в прямую линию. В каждой миске находится либо конечное число бобов, либо нет бобов вообще. Ребенок играет в игру, в которой разрешен только один вид хода: забрать два боба из любой миски и положить по одному в каждую из двух соседних мисок. Игра закончится, когда в каждой миске будет находиться либо один боб, либо ни одного.
К примеру, рассмотрим две рядом расположенные миски, в которых лежат, соответственно, 2 и 3 боба. Все остальные миски - пустые. Следующими восьмью ходами можно завершить игру:

Заданы следующие последовательности: 

t0 = 123456.
   

 

ti =
   







ti-1
2



         ,
      


         если ti-1 четно
      





ti-1
2






         926252,
      

         если ti-1 нечетно
      








      где ⌊x⌋ - функция округления вниз,
   





      а  оператор поэлементного исключающего ИЛИ.
   

 

bi = ( ti mod 211) + 1.
   

Первые два члена этой последовательности равны b1 = 289 и b2 = 145. Если начать с b1 и b2 бобами в двух соседних мисках, то для завершения игры потребуется 3419100 ходов.
Теперь, рассмотрим 1500 последовательных мисок, в каждой из которых, соответственно, лежат b1, b2,..., b1500 бобов.
Остальные миски - пустые. Найдите, сколько ходов необходимо сделать, чтобы завершить игру. 