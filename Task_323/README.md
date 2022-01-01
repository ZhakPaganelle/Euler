##Bitwise-OR operations on random integers

Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 ≤ yi < 232, every value equally likely).
For the sequence xi the following recursion is given:
It can be seen that eventually there will be an index N such that xi = 232 -1 (a bit-pattern of all ones) for all i ≥ N.
Find the expected value of N. 
Give your answer rounded to 10 digits after the decimal point.
##Операция поразрядного логического ИЛИ над случайными целыми числами

Пусть y0, y1, y2,... - последовательность случайных 32 битовых чисел без знака
(т.е., все значения 0 ≤ yi < 232 равновероятны).
Для последовательности xi задана следующая рекурсия:

x0 = 0 и
xi = xi-1 |
yi-1, при i > 0. (где | - оператор поразрядного логического ИЛИ)

Можно показать, что существует такой индекс N, при котором xi = 232 -1 (последовательность исключительно из единиц) для всех i ≥ N.
Найдите ожидаемое значение N. 
Ответ округлите до 10 знака после десятичной точки.
