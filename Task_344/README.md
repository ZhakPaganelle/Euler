##Silver dollar game

One variant of N.G. de Bruijn's silver dollar game can be described as follows:
On a strip of squares a number of coins are placed, at most one coin per square. Only one coin, called the silver dollar, has any value. Two players take turns making moves. At each turn a player must make either a regular or a special move.
A regular move consists of selecting one coin and moving it one or more squares to the left. The coin cannot move out of the strip or jump on or over another coin.
Alternatively, the player can choose to make the special move of pocketing the leftmost coin rather than making a regular move. If no regular moves are possible, the player is forced to pocket the leftmost coin.
The winner is the player who pockets the silver dollar.
A winning configuration is an arrangement of coins on the strip where the first player can force a win no matter what the second player does.
Let W(n,c) be the number of winning configurations for a strip of n squares, c worthless coins and one silver dollar.
You are given that W(10,2) = 324 and W(100,10) = 1514704946113500.
Find W(1 000 000, 100) modulo the semiprime 1000 036 000 099 (= 1 000 003 · 1 000 033).

##Игра "серебрянный доллар"

Один из вариантов игры Н. Г. де Брейна серебрянный доллар можно описать следующим образом:
На ленте с квадратными клетками размещены монеты, не более одной монеты на клетку. Ценность представляет лишь одна из них, называемая серебрянным долларом. Два игрока по очереди совершают ходы. Во время каждого хода, игрок должен совершить либо обычный, либо особый ход.
Обычный ход осуществляется выбором одной монеты и перемещением ее на одну или более клеток влево. Монету нельзя перемещать за пределы ленты, а также перепрыгивать через другие монеты или на них.
Кроме того, игрок может совершить особый ход, присвоив себе левую крайнюю монету, вместо совершения обычного хода. Если обычный ход совершить невозможно, игрок вынужден присвоить себе левую крайнюю монету.
Выигрывает тот игрок, который присвоит себе серебрянный доллар.



Определим выигрышную конфигурацию как такое расположение монет на ленте, при котором первый игрок может обеспечить себе победу независимо от действий второго игрока.
Пусть W(n,c) - число выигрышных конфигураций для ленты с n клетками, c бесполезными монетами и одним серебрянным долларом.
Дано: W(10,2) = 324 и W(100,10) = 1514704946113500.
Найдите W(1 000 000, 100) по модулю полупростого числа 1000 036 000 099 (= 1 000 003 · 1 000 033).

