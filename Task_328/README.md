##Lowest-cost Search

We are trying to find a hidden number selected from the set of integers {1, 2, ..., n} by asking questions. 
Each number (question) we ask, has a cost equal to the number asked and we get one of three possible answers:
Given the value of n, an optimal strategy minimizes the total cost (i.e. the sum of all the questions asked) for the worst possible case. E.g.
If n=3, the best we can do is obviously to ask the number "2". The answer will immediately lead us to find the hidden number (at a total cost = 2).
If n=8, we might decide to use a "binary search" type of strategy: Our first question would be "4" and if the hidden number is higher than 4 we will need one or two additional questions.
Let our second question be "6". If the hidden number is still higher than 6, we will need a third question in order to discriminate between 7 and 8.
Thus, our third question will be "7" and the total cost for this worst-case scenario will be 4+6+7=17.
We can improve considerably the worst-case cost for n=8, by asking "5" as our first question.
If we are told that the hidden number is higher than 5, our second question will be "7", then we'll know for certain what the hidden number is (for a total cost of 5+7=12).
If we are told that the hidden number is lower than 5, our second question will be "3" and if the hidden number is lower than 3 our third question will be "1", giving a total cost of 5+3+1=9.
Since 12>9, the worst-case cost for this strategy is 12. That's better than what we achieved previously with the "binary search" strategy; it is also better than or equal to any other strategy.
So, in fact, we have just described an optimal strategy for n=8.
Let C(n) be the worst-case cost achieved by an optimal strategy for n, as described above.
Thus C(1) = 0, C(2) = 1, C(3) = 2 and C(8) = 12.
Similarly, C(100) = 400 and $\sum \limits_{n = 1}^{100} {C(n)} = 17575$.
Find $\sum \limits_{n = 1}^{200000} {C(n)}$ .
##Поиск с наименьшим весом

Наша цель - угадать загаданное число из множества целых чисел {1, 2, ..., n} при помощи вопросов. Каждое число (вопрос), про которое мы спрашиваем, имеет вес, равный этому числу, и мы можем получить один из трех возможных ответов:

 "Ваше число меньше, чем загаданное", или
 "Да, это оно!", или
 "Ваше число больше, чем загаданное".

При заданном значении n, оптимальная стратегия минимизирует суммарный вес (т.е. сумму всех заданных вопросов)
для наихудшего возможного случая. Т.е.:
При n=3, лучшее, что можно сделать, очевидно, спросить про число "2". Ответ мгновенно приведет нас к загаданному числу (при суммарном весе = 2).
При n=8, можно попытаться воспользоваться стратегией "двоичного поиска": первый вопрос будет про "4", и, если загаданное число больше, чем 4, то понадобится еще одна или две попытки-вопроса.
Пусть второй вопрос будет про "6". Если загаданное число все еще больше 6, то потребуется третий вопрос, чтобы выяснить - загаданное число равно 7 или 8.
Таким образом, третий вопрос будет про "7", и общий вес этого наихудшего случая оставит 4+6+7=
17.
Можно существенно уменьшить вес наихудшего случая при n=8, задав первый вопрос про "5".
Если окажется, что загаданное число больше 5, то второй вопрос будет про "7", и тогда мы наверняка узнаем загаданное число (при общем весе 5+7=12).
Если же окажется, что загаданное число меньше 5, то второй вопрос будет про "3", а если загаданное число будет меньше чем 3, то третий вопрос будет про "1". Итого, общий вес составит 5+3+1=9.
Т.к. 12>9, то вес наихудшего случая при такой стратегии будет равен 12. Это лучше результата, который был получен выше при помощи стратегии "двоичного поиска". Кроме того, этот результат не хуже результата любой другой стратегии.
Таким образом, мы только что описали оптимальную стратегию при n=8.
Пусть C(n) - вес наихудшего возможного случая, достигнутый оптимальной стратегией для n чисел, описанный выше.
Таким образом, C(1) = 0, C(2) = 1, C(3) = 2 и C(8) = 12.
Аналогично, C(100) = 400 и  C(n) = 17575.
Найдите C(n).
