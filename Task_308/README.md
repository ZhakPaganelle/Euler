##An amazing Prime-generating Automaton

A program written in the programming language Fractran consists of a list of fractions.
The internal state of the Fractran Virtual Machine is a positive integer, which is initially set to a seed value. Each iteration of a Fractran program multiplies the state integer by the first fraction in the list which will leave it an integer.
For example, one of the Fractran programs that John Horton Conway wrote for prime-generation consists of the following 14 fractions:
$$\dfrac{17}{91}, \dfrac{78}{85}, \dfrac{19}{51}, \dfrac{23}{38}, \dfrac{29}{33}, \dfrac{77}{29}, \dfrac{95}{23}, \dfrac{77}{19}, \dfrac{1}{17}, \dfrac{11}{13}, \dfrac{13}{11}, \dfrac{15}{2}, \dfrac{1}{7}, \dfrac{55}{1}$$
Starting with the seed integer 2, successive iterations of the program produce the sequence:
15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...
The powers of 2 that appear in this sequence are 22, 23, 25, ...
It can be shown that all the powers of 2 in this sequence have prime exponents and that all the primes appear as exponents of powers of 2, in proper order!
If someone uses the above Fractran program to solve Project Euler Problem 7 (find the 10001st prime), how many iterations would be needed until the program produces 210001st prime ?
##Удивительный автомат для генерации простых чисел

Программа, написанная на языке программирования Fractran, состоит из списка дробей.
Внутреннее состояние виртуальной машины Fractran — это натуральное число, которое изначально устанавливается равным начальному числу генератора (seed value). При каждой итерации Fractran-программы число состояния машины умножается на первую дробь в списке, которая даст в результате целое число.
Например, одна из программ на Fractran, написанная Джоном Хортоном Конвейем для генерации простых чисел, состоит из следующих 14 дробей:



1791

,

7885

,

1951

,

2338

,

2933

,

7729

,

9523

,

7719

,

117

,

1113

,

1311

,

152

,

17

,

551

.


При начальном значении генератора 2, последовательное выполнение итераций программы производит последовательность:
15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...
В этой последовательности появляются следующие степени двойки: 22, 23, 25, ...
Можно показать, что все степени двойки в этой последовательности имеют простые показатели и, кроме того, все простые числа в показателях степеней двойки появляются в правильном порядке.
Если использовать приведенную выше программу на Fractran при решении 7-й задачи проекта «Эйлер» (найдите 10001-е простое число), то сколько итераций потребуется, прежде чем программа выдаст число 210001ое простое число?
