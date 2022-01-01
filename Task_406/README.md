##Guessing Game

We are trying to find a hidden number selected from the set of integers {1, 2, ..., n} by asking questions. 
Each number (question) we ask, we get one of three possible answers:
Given the value of n, a, and b, an optimal strategy minimizes the total cost for the worst possible case.
For example, if n = 5, a = 2, and b = 3, then we may begin by asking "2" as our first question.
If we are told that 2 is higher than the hidden number (for a cost of b=3), then we are sure that "1" is the hidden number (for a total cost of 3).
If we are told that 2 is lower than the hidden number (for a cost of a=2), then our next question will be "4".
If we are told that 4 is higher than the hidden number (for a cost of b=3), then we are sure that "3" is the hidden number (for a total cost of 2+3=5).
If we are told that 4 is lower than the hidden number (for a cost of a=2), then we are sure that "5" is the hidden number (for a total cost of 2+2=4).
Thus, the worst-case cost achieved by this strategy is 5. It can also be shown that this is the lowest worst-case cost that can be achieved. 
So, in fact, we have just described an optimal strategy for the given values of n, a, and b.
Let $C(n, a, b)$ be the worst-case cost achieved by an optimal strategy for the given values of n, a and b.
Here are a few examples:
$C(5, 2, 3) = 5$
$C(500, \sqrt 2, \sqrt 3) = 13.22073197\dots$
$C(20000, 5, 7) = 82$
$C(2000000, \sqrt 5, \sqrt 7) = 49.63755955\dots$
Let $F_k$ be the Fibonacci numbers: $F_k=F_{k-1}+F_{k-2}$ with base cases $F_1=F_2= 1$.Find $\displaystyle \sum \limits_{k = 1}^{30} {C \left (10^{12}, \sqrt{k}, \sqrt{F_k} \right )}$, and give your answer rounded to 8 decimal places behind the decimal point.
##Игра в угадывание

Мы пытаемся найти неизвестное число, выбранное из множества целых чисел {1, 2, ..., n}, задавая вопросы. 
С каждым числом (вопросом), которое мы спрашиваем, мы получаем один из трех возможных ответов:

 "Названное вами число меньше загаданного" (и с вас взимается плата a), или
 "Названное вами число больше загаданного" (и с вас взимается плата b), или
 "Да, это - оно!" (и игра завершается).

При данных значениях n, a и b, оптимальная стратегия приведет к наименьшим затратам в худшем возможном случае.
Например, если n = 5, a = 2 и b = 3, тогда мы можем начать, назвав "2" в качестве нашей первой попытки.
Если нам сообщают, что 2 больше загаданного числа (за плату b=3), тогда мы уверены, что "1" - это загаданное число (всего потратив 3).
Если нам сообщают, что 2 меньше загаданного числа (за плату a=2), тогда наша следующая попытка будет "4".
Если нам сообщают, что 4 больше загаданного числа (за плату b=3), тогда мы уверены, что "3" - это загаданное число (всего потратив 2+3=5).
Если нам сообщают, что 4 меньше загаданного числа (за плату a=2), тогда мы уверены, что "5" - это загаданное число (всего потратив 2+2=4).
Итак, при этой стратегии затраты в худшем возможном случае составят 5. Можно также показать, что это - самая маленькая затрата в худшем возможном случае, которую можно достичь. 
Таким образом, мы только что описали оптимальную стратегию для данных значений n, a и b.
Пусть C(n, a, b) будет затратами в худшем возможном случае при оптимальной стратегии для данных значений n, a и b.
Вот несколько примеров:
C(5, 2, 3) = 5
C(500, √2, √3) = 13.22073197...
C(20000, 5, 7) = 82
C(2000000, √5, √7) = 49.63755955...
Пусть Fk будет числами Фибоначчи: Fk = Fk-1 + Fk-2 с начальными значениями F1 = F2 = 1.Найдите ∑1≤k≤30 C(1012, √k, √Fk), и приведите полученный ответ округленным до 8 знака после десятичной точки.
