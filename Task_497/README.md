##Drunken Tower of Hanoi

Bob is very familiar with the famous mathematical puzzle/game, "Tower of Hanoi," which consists of three upright rods and disks of different sizes that can slide onto any of the rods. The game begins with a stack of n disks placed on the leftmost rod in descending order by size. The objective of the game is to move all of the disks from the leftmost rod to the rightmost rod, given the following restrictions:
Moving on to a variant of this game, consider a long room k units (square tiles) wide, labeled from 1 to k in ascending order. Three rods are placed at squares a, b, and c, and a stack of n disks is placed on the rod at square a.
Bob begins the game standing at square b. His objective is to play the Tower of Hanoi game by moving all of the disks to the rod at square c. However, Bob can only pick up or set down a disk if he is on the same square as the rod / stack in question.
Unfortunately, Bob is also drunk. On a given move, Bob will either stumble one square to the left or one square to the right with equal probability, unless Bob is at either end of the room, in which case he can only move in one direction. Despite Bob's inebriated state, he is still capable of following the rules of the game itself, as well as choosing when to pick up or put down a disk.
The following animation depicts a side-view of a sample game for n = 3, k = 7, a = 2, b = 4, and c = 6:

Let E(n,k,a,b,c) be the expected number of squares that Bob travels during a single optimally-played game. A game is played optimally if the number of disk-pickups is minimized.
Interestingly enough, the result is always an integer. For example, E(2,5,1,3,5) = 60 and E(3,20,4,9,17) = 2358.
Find the last nine digits of ∑1≤n≤10000 E(n,10n,3n,6n,9n).
##Пьяная ханойская башня

Боб очень хорошо знаком с известной математической игрой/головоломкой "ханойская башня". Она состоит из трех вертикальных штырей и дисков разных размеров, которые можно надевать на штыри. Игра начинается со стопки из n дисков, размещенной на самом левом штыре в порядке уменьшения размера диска снизу вверх. Цель игры - переместить все диски с левого штыря на правый при следующих ограничениях:

Только один диск может быть перемещен за ход.
Ход состоит в снятии самого верхнего диска со штыря и помещении его на верх другой стопки дисков или на пустой штырь.
Нельзя помещать диск на диск меньшего размера.

В "пьяном" варианте этой игры рассмотрим длинную комнату длиной в k единиц (квадратных плиток). Каждый квадрат пронумерован от 1 до k в возрастающем порядке. В квадратах с номерами a, b и c расположены три штыря. На штыре в квадрате a находится стопка из n дисков.
Боб начинает игру стоя в квадрате b. Его цель - решить ханойскую башню переместив все диски на штырь в квадрате c. Однако, Боб может взять диск со штыря или положить его на штырь только когда он находится в одном квадрате с этим штырем.
К несчастью, Боб еще и пьян. В каждый свой ход Боб с одинаковой вероятностью может перейти направо или налево в соседний квадрат, кроме случаев, когда Боб находится в одном из концов комнаты. Тогда он может двигаться только в одном направлении. Несмотря на то, что Боб в подпитии, он по-прежнему способен следовать правилам игры и выбирать, когда взять или положить диск на штырь.
Следующая анимация показывает вид сбоку на пример такой игры для n = 3, k = 7, a = 2, b = 4 и c = 6:

Пусть E(n,k,a,b,c) будет ожидаемым количеством квадратов, которые Боб пройдет в течение одной оптимально сыгранной игры. Игра считается сыгранной оптимально при минимальном возможном количестве взятий дисков.
Любопытно, что результат всегда будет целым числом. Например, E(2,5,1,3,5) = 60 и E(3,20,4,9,17) = 2358.
Найдите последние девять цифр числа ∑1≤n≤10000 E(n,10n,3n,6n,9n).
