##Compromise or persist

Alice is playing a game with n cards numbered 1 to n.
A game consists of iterations of the following steps.
(1) Alice picks one of the cards at random.
(2) Alice cannot see the number on it. Instead, Bob, one of her friends, sees the number and tells Alice how many previously-seen numbers are bigger than the number which he is seeing.
(3) Alice can end or continue the game. If she decides to end, the number becomes her score. If she decides to continue, the card is removed from the game and she returns to (1). If there is no card left, she is forced to end the game.
Let F(n) be the Alice's expected score if she takes the optimized strategy to minimize her score.
For example, F(3) = 5/3. At the first iteration, she should continue the game. At the second iteration, she should end the game if Bob says that one previously-seen number is bigger than the number which he is seeing, otherwise she should continue the game.
We can also verify that F(4) = 15/8 and F(10) ≈ 2.5579365079.
Find F(106). Give your answer rounded to 10 decimal places behind the decimal point.
##Уступить или настоять

Алиса играет в игру с n картами, пронумерованными от 1 до n.
Игра состоит из повторения следующих трех шагов:
(1) Алиса берет случайную карту.
(2) Алиса не видит, какое на этой карте число. Вместо этого Боб - один из ее друзей - видит число и говорит Алисе, сколько увиденных до этого чисел было больше этого числа.
(3) Алиса может завершить или продолжить игру. Если она решает закончить, количество ее очков становится равно последнему открытому числу. Если она решает продолжить, эта карта убирается из игры и Алиса снова начинает с шага (1). Если больше не осталось никаких карт, Алиса вынуждена закончить игру этим ходом.
Пусть F(n) будет ожидаемым количеством очков Алисы, если она выберет оптимальную стратегию для получения наименьшего количества очков.
Например, F(3) = 5/3. В первой итерации ей стоит продолжить игру. Во второй итерации ей стоит прекратить игру, если Боб скажет, что одно ранее увиденное число было больше того, которое он видит сейчас. В противном случае, ей стоит продолжить игру.
Можно также показать, что F(4) = 15/8 и F(10) ≈ 2.5579365079.
Найдите F(106). Дайте ответ округленным до 10 цифр после десятичной точки.
