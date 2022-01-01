##The Chase II

Consider the following variant of "The Chase" game. This game is played between $n$ players sitting around a circular table using two dice. It consists of $n-1$ rounds, and at the end of each round one player is eliminated and has to pay a certain amount of money into a pot. The last player remaining is the winner and receives the entire contents of the pot.
At the beginning of a round, each die is given to a randomly selected player. A round then consists of a number of turns.
During each turn, each of the two players with a die rolls it. If a player rolls a 1 or a 2, the die is passed to the neighbour on the left; if the player rolls a 5 or a 6, the die is passed to the neighbour on the right; otherwise, the player keeps the die for the next turn.
The round ends when one player has both dice at the beginning of a turn. At which point that player is immediately eliminated and has to pay $s^2$ where $s$ is the number of completed turns in this round. Note that if both dice happen to be handed to the same player at the beginning of a round, then no turns are completed, so the player is eliminated without having to pay any money into the pot.
Let $G(n)$ be the expected amount that the winner will receive. For example $G(5)$ is approximately 96.544, and $G(50)$ is 2.82491788e6 in scientific notation rounded to 9 significant digits.
Find $G(500)$, giving your answer in scientific notation rounded to 9 significant digits.
##Погоня II

Рассмотрим следующий вариант игры "Погоня". В игре участвуют $n$ игроков, сидящих вокруг круглого стола и использующих два кубика. Игра состоит из $n-1$ раундов, и в конце каждого раунда один игрок выбывает из игры и должен заплатить определенную сумму денег в банк. Последний оставшийся игрок становится победителем и получает весь банк в качестве выигрыша.
В началае раунда каждый кубик дается случайно выбранному игроку. Раунд состоит из нескольких ходов.
Каждый ход каждый игрок с кубиком бросает его. Если игрок выбрасывает 1 или 2, он передает кубик соседу слева. Если он выбрасывает 5 или 6, он передает кубик соседу справа. Во всех остальных случаях, кубик остается у него до следующего хода.
Раунд кончается, когда в начале хода оба кубика оказываются у одного игрока. Этот ход прерывается, игрок выбывает из игры и должен заплатить $s^2$, где $s$ - число завершенных ходов в этом раунде. Заметим, что если оба кубика были выданы одному и тому же игроку в начале раунда, не было сделано ни одного хода и игрок выбывает, ничего не заплатив в банк.
Пусть $G(n)$ будет ожидаемым выигрышем, который получит победитель. Например, $G(5)$ примерно равно 96.544, а $G(50)$ равно 2.82491788e6 в стандартной записи числа, округленное до 9 значимых цифр.
Найдите $G(500)$ и приведите ответ в стандартной записи числа, округленный до 9 значимых цифр. Оригинал
