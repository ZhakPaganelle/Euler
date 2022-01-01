##Searching a triangular array for a sub-triangle having minimum-sum

In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.
In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.
We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers sk in the range ±219, using a type of random number generator (known as a Linear Congruential Generator) as follows:
t := 0

for k = 1 up to k = 500500:

    t := (615949*t + 797807) modulo 220
    sk := t−219
Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc
Our triangular array is then formed using the pseudo-random numbers thus:
Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).

The "sum of a sub-triangle" is defined as the sum of all the elements it contains.

Find the smallest possible sub-triangle sum.
##Поиск под-треугольника с наименьшей суммой в треугольном массиве

В треугольном массиве положительных и отрицательных целых чисел мы хотим найти такой под-треугольник, чтобы сумма всех чисел, из которых он состоит, была по возможности меньшей.
В примере ниже отчетливо видно, что выделенный треугольник удовлетворяет условию, т.к. его сумма равна −42.



Мы собираемся сделать такой треугольный массив с одной тысячей строк, поэтому нам необходимо сгенерировать 500500 псевдослучайных числа sk в диапазоне ±219, воспользовавшись определенным типом генератора случайных чисел (известен как "линейный конгруэнтный генератор") следующим образом:
t := 0

при k = 1 до k = 500500:

    t := (615949*t + 797807) modulo 220

    sk := t−219
Таким образом: s1 = 273519, s2 = −153582, s3 = 450905 и т.д.
После этого наш треугольный массив формируется из полученных псевдо-случайных чисел следующим образом:

s1

s2  s3

s4  s5  s6 

s7  s8  s9  s10

...

Под-треугольники можно начинать с любого элемента массива и продолжать их вниз настолько, насколько это необходимо (выбирая два элемента на следующей строке, три элемента на идущей через одну строке и т.д.).

"Сумма под-треугольника" определяется как сумма всех его элементов.

Найдите наименьшую возможную сумму под-треугольника.
