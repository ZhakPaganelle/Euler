##Binary Circles

2N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.
For N=3, two such circular arrangements are possible, ignoring rotations:
For the first arrangement, the 3-digit subsequences, in clockwise order, are: 000, 001, 010, 101, 011, 111, 110 and 100.
Each circular arrangement can be encoded as a number by concatenating the binary digits starting with the subsequence of all zeros as the most significant bits and proceeding clockwise. The two arrangements for N=3 are thus represented as 23 and 29:

Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.
Find S(5).
##Двоичные окружности

2N двоичных цифры можно разместить в окружности так, чтобы все N-разрядные числа, считываемые в направлении часовой стрелки, были различными.
Для N=3, существует два таких способа записи, не учитывая повороты:

Для первого варианта, 3-разрядные последовательности, считываемые в направлении часовой стрелки: 000, 001, 010, 101, 011, 111, 110 и 100.
Каждая такая сформированная окружность может быть закодирована в виде числа, объединяя все двоичные разряды - начиная с последовательности нулей в качестве старших разрядов, и считывая далее в направлении часовой стрелки. В таком случае, два расположения для N=3 можно представить числами 23 и 29:
00010111 2 = 23
00011101 2 = 29
Обозначив через S(N) сумму всех различающихся числовых представлений, получим S(3) = 23 + 29 = 52.
Найдите S(5).
