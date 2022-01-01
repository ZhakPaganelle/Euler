##Sliders

You probably know the game Fifteen Puzzle. Here, instead of numbered tiles, we have seven red tiles and eight blue tiles.
A move is denoted by the uppercase initial of the direction (Left, Right, Up, Down) in which the tile is slid, e.g. starting from configuration (S), by the sequence LULUR we reach the configuration (E):

For each path, its checksum is calculated by (pseudocode):

For the sequence LULUR given above, the checksum would be 19761398.
Now, starting from configuration (S),
find all shortest ways to reach configuration (T).

What is the sum of all checksums for the paths having the minimal length?
##Пятнашки

Наверняка вам знакома игра пятнашки. Вместо пронумерованных плиток, мы воспользуемся семью красными

плитками и восемью синими.
Ходы обозначаются заглавной начальной буквой направления (Left, Right, Up, Down), в котором передвигают плитку на свободное место,

т.е. начав с конфигурации (S), и выполнив последовательность перемещений LULUR, мы получим

конфигурацию (E):


(S), (E)


Контрольная сумма каждого пути рассчитывается следующим образом (псевдо-код):

checksum = 0
checksum = (checksum × 243 + m1) mod 100 000 007
checksum = (checksum × 243 + m2) mod 100 000 007
   …
checksum = (checksum × 243 + mn) mod 100 000 007

где mk является ASCII-кодом k-той буквы в последовательности переходов.

Соответствующие ASCII-коды направлений:



L76
R82
U85
D68


Для приведенной выше последовательности LULUR контрольная сумма составит 19761398.
А теперь, начав с конфигурации (S), найдите все кратчайшие пути к конфигурации (T).


(S), (T)


Чему равна сумма всех контрольных сумм для кратчайших путей?
