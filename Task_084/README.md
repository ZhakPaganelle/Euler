##Monopoly odds

In the game, Monopoly, the standard board is set up in the following way:
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.
At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.
If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
##Вероятности в "Монополии"

Стандартная доска игры Монополия выглядит следующим образом:



GO
A1
CC1
A2
T1
R1
B1
CH1
B2
B3
JAIL


H2
 
C1


T2
 
U1


H1
 
C2


CH3
 
C3


R4
 
R2


G3
 
D1


CC3
 
CC2


G2
 
D2


G1
 
D3


G2J
F3
U2
F2
F1
R3
E3
E2
CH2
E1
FP



Игрок начинает на клетке GO и складывает выпавшие на двух шестигранных кубиках числа, чтобы определить количество клеток, которое он должен пройти по часовой стрелке. Пользуясь только этим правилом, вероятность посещения каждой клетки равна 2,5 %. Однако попадание на G2J (Отправляйтесь в тюрьму), CC (Общественный фонд) и CH (Шанс) меняет распределение.
В дополнение к G2J и одной карте в CC и в CH, которые приказывают игроку отправиться в тюрьму, также если игрок выкидывает три дубля подряд, он не двигается в свой третий ход, а отправляется сразу в тюрьму.
В начале игры карты CC и CH перемешиваются. Когда игрок попадает на клетку CC или CH, он берет верхнюю карту с соответствующей колоды и, после выполнения указанных на ней инструкций, возвращает ее в низ колоды. В каждой колоде 16 карт, однако для решения этой задачи важны только карты, связанные с перемещением игрока. Любые другие инструкции игнорируются и игрок остается на той же клетке.

Общественный фонд (2/16 карт):

Пройдите к GO
Идите в JAIL


Шанс (10/16 карт):

Пройдите к GO
Идите в JAIL
Идите на C1
Идите на E3
Идите на H2
Идите на R1
Пройдите к следующей R (железнодорожная станция)
Пройдите к следующей R
Пройдите к следующей U (коммунальное предприятие)
Вернитесь назад на 3 клетки



Суть этой задачи заключается в вероятности посещения одной конкретной клетки. То есть, вероятность оказаться на этой клетке по завершении хода. Поэтому ясно, что за исключением G2J, чья вероятность посещения равна нулю, клетка CH будет иметь наименьшую вероятность посещения, потому что в 5/8 случаев игроку придется переместиться на другую клетку, а нас интересует именно клетка, на которой завершится ход игрока. Мы также не будем разделять попадание в тюрьму как посетитель или как заключенный, также не берем во внимание правило, что выкинув дубль, игрок выходит из тюрьмы - предположим, что игроки платят за выход из тюрьмы на следующий же ход после попадания в нее.
Начиная с GO и последовательно нумеруя клетки от 00 до 39, мы можем соединить эти двузначные числа, чтобы получить соответствующую определенному множеству клеток строку.
Статистически можно показать, что три наиболее популярных клетки будут JAIL (6,24%) = Клетка 10, E3 (3,18%) = Клетка 24, и GO (3,09%) = Клетка 00. Итак, их можно перечислить как строку из шести цифр: 102400.
Найдите такую шестизначную строку, если игроки будут использовать вместо двух шестигранных кубиков два четырехгранных.
