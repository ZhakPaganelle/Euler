##Hallway of square steps

Peter moves in a hallway with N+1 doors consecutively numbered from 0 through N. All doors are initially closed. Peter starts in front of door 0, and repeatedly performs the following steps:
We call an action any sequence of those steps. Peter never performs the exact same action twice, and makes sure to perform all possible actions that don't bring him past the last door.
Let F(N) be the number of doors that are open after Peter has performed all possible actions. You are given that F(5) = 1, F(100) = 27, F(1000) = 233 and F(106) = 112168.
Find F(1012).
##Квадратные шаги по коридору

Петр перемещается по коридору с N+1 дверями, последовательно пронумерованными от 0 до N. Изначально все двери закрыты. Петр начинает перед дверью 0 и повторяет следующие шаги:
Сначала он отходит от своей позиции на число дверей, равное квадрату целого числа.
Затем он отходит от своей новой позиции на число дверей, равное еще большему квадрату целого числа.
Он изменяет состоние двери, оказавшейся перед ним (открывает, если он закрыта, или закрывает, если открыта).
Наконец, он возвращается к двери 0.
Назовем любую последовательность этих шагов действием. Петр никогда не выполняет одно и то же действие дважды и выполняет все возможные действия, которые не приведут его дальше, чем последняя дверь.
Пусть F(N) будет количеством дверей, которые остались открытыми после того, как Петр выполнил все возможные действия. Известно, что F(5) = 1, F(100) = 27, F(1000) = 233 и F(106) = 112168.
Найдите F(1012).
