##The Roundtable Lottery

A group of $p$ people decide to sit down at a round table and play a lottery-ticket trading game. Each person starts off with a randomly-assigned, unscratched lottery ticket. Each ticket, when scratched, reveals a whole-pound prize ranging anywhere from £1 to £$p$, with no two tickets alike. The goal of the game is for all of the players to maximize the winnings of the ticket they hold upon leaving the game.
An arbitrary person is chosen to be the first player. Going around the table, each player has only one of two options:
The game ends once all tickets have been scratched. All players still remaining at the table must leave with their currently-held tickets.
Assume that players will use the optimal strategy for maximizing the expected value of their ticket winnings.
Let $E(p)$ represent the expected number of players left at the table when the game ends in a game consisting of $p$ players.
E.g. $E(111) = 5.2912$ when rounded to 5 significant digits.
Let $S_1(N) = \sum \limits_{p = 1}^{N} {E(p)}$.
Let $S_k(N) = \sum \limits_{p = 1}^{N} {S_{k-1}(p)}$ for $k \gt 1$.
Find $S_{20}(10^{14})$ and write the answer in scientific notation rounded to 10 significant digits. Use a lowercase e to separate mantissa and exponent. For example, the answer for $S_3(100)$ would be 5.983679014e5.
##Лотерея круглого стола

Группа из p людей решила сесть за круглый стол и разыграть игру с обменом лотерейными билетами. Каждый игрок начинает со случайно назначенным нестертым лотерейным билетом. При стирании защитного покрытия на каждом билете становится виден его выигрыш - целое количество фунтов стерлингов между £1 и £p, причем все билеты имеют разный выигрыш. Цель игры для каждого игрока - получить как можно больший выигрыш на момент покидания игры.
Случайный человек выбирается первым игроком. Далее игроки ходят по кругу, каждый игрок в свой ход может выбрать одно из двух:
1. Игрок стирает покрытие на своем билете и показывает его выигрыш всем сидящим за столом.
2. Игрок может обменять свой нестертый билет на стертый билет предыдущего игрока и покинуть игру с этим билетом. Предыдущий игрок тогда стирает покрытие с полученного билета и показывает его выигрыш всем сидящим за столом.
Игра завершается, когда все билеты стерты. Все игроки, остающиеся за столом, должны покинуть игру с имеющимся на руках билетом.
Предположим, что каждый игрок следует оптимальной стратегии для максимизирования ожидаемого выигрыша его билета. 
Пусть E(p) будет ожидаемым числом игроков, остающихся за столом на момент завершения игры, при общем количестве игроков равным p (например, E(111) = 5.2912 при округлении до 5 значимых цифр).
Пусть S1(N) =  E(p)
Пусть Sk(N) =  Sk-1(p) для k > 1
Найдите S20(1014) и запишите ответ в стандартном виде округленным до 10 значимых цифр. Используйте строчную латинскую букву "e", чтобы отделить мантиссу от порядка (например, S3(100) = 5.983679014e5).
