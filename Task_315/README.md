##Digital root clocks


Sam and Max are asked to transform two digital clocks into two "digital root" clocks.
A digital root clock is a digital clock that calculates digital roots step by step.
When a clock is fed a number, it will show it and then it will start the calculation, showing all the intermediate values until it gets to the result.
For example, if the clock is fed the number 137, it will show: "137" → "11" → "2" and then it will go black, waiting for the next number.
Every digital number consists of some light segments: three horizontal (top, middle, bottom) and four vertical (top-left, top-right, bottom-left, bottom-right).
Number "1" is made of vertical top-right and bottom-right, number "4" is made by middle horizontal and vertical top-left, top-right and bottom-right. Number "8" lights them all.
The clocks consume energy only when segments are turned on/off.
To turn on a "2" will cost 5 transitions, while a "7" will cost only 4 transitions.
Sam and Max built two different clocks.
Sam's clock is fed e.g. number 137: the clock shows "137", then the panel is turned off, then the next number ("11") is turned on, then the panel is turned off again and finally the last number ("2") is turned on and, after some time, off.
For the example, with number 137, Sam's clock requires:
Max's clock works differently. Instead of turning off the whole panel, it is smart enough to turn off only those segments that won't be needed for the next number.
For number 137, Max's clock requires:
Of course, Max's clock consumes less power than Sam's one.
The two clocks are fed all the prime numbers between A = 107 and B = 2×107. 
Find the difference between the total number of transitions needed by Sam's clock and that needed by Max's one.
##Дисплеи с цифровыми корнями


Сэма и Макса попросили превратить пару цифровых дисплеев в дисплеи с "цифровыми корнями".
Дисплей с цифровыми корнями - это цифровой дисплей, который показывают цифровые корни на каждом шагу расчета.
Когда дисплею задают число, он показывает его и начинает производить расчет, при этом показывая все промежуточные значения, пока не получит окончательный результат.
К примеру, если в дисплей ввести число 137, то он последовательно отобразит: "137"
 → "11"
 → "2",
    а затем погаснет, ожидая ввода следующего числа.
Любая цифра образуется несколькими световыми сегментами: тремя горизонтальными (верхний, средний, нижний) и четырьмя вертикальными (верхий левый, верхний правый, нижний левый, нижний правый).
Цифру "1" образуют вертикальные сегменты - верхний правый и нижний правый, цифру "4" образуют средний горизонтальный сегмент и вертикальные верхний левый, верхний правый и нижний правый сегменты. Для цифры "8" загораются все сегменты.
Дисплей потребляет энергию только когда включает/выключает сегменты.
Для того, чтобы включить цифру "2", потребуется 5 переходов, в то время как для "7" - всего 4 перехода.
Сэм и Макс собрали два разных дисплея.
Когда в дисплей Сэма вводят число, например, 137: дисплей показывает "137", затем дисплей гаснет, после чего загорается следующее число ("11"), затем дисплей снова гаснет и наконец загорается последнее число ("2"), а через некоторое время дисплей гаснет окончательно.
Для примера с числом 137 дисплею Сэма потребуется:

"137"
:
(2 + 5 + 4) × 2 = 22 перехода (показать/отключить "137").

"11"
:
(2 + 2) × 2 = 8 переходов (показать/отключить "11").

"2"
:
(5) × 2 = 10 переходов(показать/отключить "2").

Таким образом, всего потребуется 40 переходов.
Дисплей Макса работает иначе. Вместо того, чтобы включать/отключать весь дисплей, он достаточно "умен", чтобы выключать только те сегменты, которые не понадобятся для индикации следующего числа.
При вводе числа 137, дисплею Макса потребуется:

"137"
:
2 + 5 + 4 = 11 переходов (показать "137")
7 переходов (на отключение сегментов, которые не нужны для отображения числа "11").

"11"
:
0 переходов (число "11" уже правильно отображено на дисплее)
3 перехода (отключить первую цифру "1", а также нижний сегмент второй цифры "1"; 
верхний же сегмент остается для отображения числа "2").

"2"
:
4 перехода (включить недостающие сегменты для числа "2")
5 переходов (чтобы убрать с дисплея число "2").

Таким образом, всего потребуется 30 переходов.
Разумеется, дисплей Макса потребляет меньше энергии, чем дисплей Сэма.
В оба дисплея вводят простые числа между A = 107 и B = 2 × 107. 
Найдите разность общего количества переходов, необходимых дисплеям Сэма и Макса для отображения этих чисел.
