##Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
The cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
Consider the following five hands dealt to two players:
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
##Покерные ставки

В карточной игре покер ставка состоит из пяти карт и оценивается от самой младшей до самой старшей в следующем порядке:

Старшая карта: Карта наибольшего достоинства.
Одна пара: Две карты одного достоинства.
Две пары: Две различные пары карт
Тройка: Три карты одного достоинства.
Стрейт: Все пять карт по порядку, любые масти.
Флаш: Все пять карт одной масти.
Фул-хаус: Три карты одного достоинства и одна пара карт.
Каре: Четыре карты одного достоинства.
Стрейт-флаш: Любые пять карт одной масти по порядку.
Роял-флаш: Десятка, валет, дама, король и туз одной масти.

Достоинство карт оценивается по порядку:2, 3, 4, 5, 6, 7, 8, 9, 10, валет, дама, король, туз.
Если у двух игроков получились ставки одного порядка, то выигрывает тот, у кого карты старше: к примеру, две восьмерки выигрывают две пятерки (см. пример 1 ниже). Если же достоинства карт у игроков одинаковы, к примеру, у обоих игроков пара дам, то сравнивают карту наивысшего достоинства (см. пример 4 ниже); если же и эти карты одинаковы, сравнивают следующие две и т.д.
Допустим, два игрока сыграли 5 ставок следующим образом:



Ставка 1-й игрок 2-й игрок Победитель


1 5♥ 5♣ 6♠ 7♠ K♦Пара пятерок 2♣ 3♠ 8♠ 8♦ T♦Пара восьмерок 2-й игрок


2 5♦ 8♣ 9♠ J♠ A♣Старшая карта туз 2♣ 5♣ 7♦ 8♠ Q♥Старшая карта дама 1-й игрок


3 2♦ 9♣ A♠ A♥ A♣Три туза 3♦ 6♦ 7♦ T♦ Q♦Флаш, бубны 2-й игрок


4 4♦ 6♣ 9♥ Q♥ Q♣Пара дамСтаршая карта девятка 3♦ 6♦ 7♥ Q♦ Q♠Пара дамСтаршая карта семерка 1-й игрок


5 2♥ 2♦ 4♣ 4♦ 4♠Фул-хаусТри четверки 3♣ 3♦ 3♠ 9♠ 9♦Фул-хаусТри тройки 1-й игрок



Файл poker.txt содержит одну тысячу различных ставок для игры двух игроков. В каждой строке файла приведены десять карт (отделенные одним пробелом): первые пять - карты 1-го игрока, оставшиеся пять - карты 2-го игрока. Можете считать, что все ставки верны (нет неверных символов или повторов карт), ставки каждого игрока не следуют в определенном порядке, и что при каждой ставке есть безусловный победитель.
Сколько ставок выиграл 1-й игрок?
Примечание: карты в текстовом файле обозначены в соответствии с английскими наименованиями достоинств и мастей: T - десятка, J - валет, Q - дама, K - король, A - туз; S - пики, C - трефы, H - червы, D - бубны.

