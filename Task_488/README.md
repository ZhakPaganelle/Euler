##Unbalanced Nim

Alice and Bob have enjoyed playing Nim every day. However, they finally got bored of playing ordinary three-heap Nim.
So, they added an extra rule:
- Must not make two heaps of the same size.
The triple (a,b,c) indicates the size of three heaps.
Under this extra rule, (2,4,5) is one of the losing positions for the next player.
To illustrate:
- Alice moves to (2,4,3)
- Bob   moves to (0,4,3)
- Alice moves to (0,2,3)
- Bob   moves to (0,2,1)
Unlike ordinary three-heap Nim, (0,1,2) and its permutations are the end states of this game.
For an integer N, we define F(N) as the sum of a+b+c for all the losing positions for the next player, with 0 < a < b < c < N.
For example, F(8) = 42, because there are 4 losing positions for the next player, (1,3,5), (1,4,6), (2,3,6) and (2,4,5).
We can also verify that F(128) = 496062.
Find the last 9 digits of F(1018).
##Несбалансированный Ним

Элис и Боб наслаждаются игрой в Ним каждый день. Однако, им уже поднадоел обычный Ним с тремя кучками.
Поэтому они добавили еще одно правило:
- Нельзя создавать две кучки одинакового размера.
Тройка (a,b,c) описывает размеры трех кучек в текущем положении.
При игре с дополнительным правилом (2,4,5) является одним из проигрышных положений для следующего игрока.
Это видно на следующем примере:
- Элис ходит на (2,4,3)
- Боб ходит на (0,4,3)
- Элис ходит на (0,2,3)
- Боб ходит на (0,2,1)
В отличие от обычного Нима с тремя кучками, в новом варианте игры положение (0,1,2) и его перестановки являются проигрышными для следующего игрока.
Для целого N определим F(N) как сумму a+b+c для всех проигрышных положений для следующего игрока, где 0 < a < b < c < N.
Например, F(8) = 42, потому что существует 4 проигрышных положения для следующего игрока: (1,3,5), (1,4,6), (2,3,6) и (2,4,5).
Также можно показать, что F(128) = 496062.
Найдите последние 9 цифр F(1018).
