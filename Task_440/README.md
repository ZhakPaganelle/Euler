##GCD and Tiling

We want to tile a board of length n and height 1 completely, with either 1 × 2 blocks or 1 × 1 blocks with a single decimal digit on top:
For example, here are some of the ways to tile a board of length n = 8:
Let T(n) be the number of ways to tile a board of length n as described above.
For example, T(1) = 10 and T(2) = 101.
Let S(L) be the triple sum ∑a,b,c gcd(T(ca), T(cb)) for 1 ≤ a, b, c ≤ L.
For example:
S(2) = 10444
S(3) = 1292115238446807016106539989
S(4) mod 987 898 789 = 670616280.
Find S(2000) mod 987 898 789.
##НОД и укладка плитки

Мы хотим выложить стол длиной n и шириной 1 без зазоров или плитками 1 × 2, или плитками 1 × 1, подписанными одной десятичной цифрой:

Например, вот несколько способов выложить плиткой стол длиной n = 8:

Пусть T(n) будет количеством способов выложить плиткой стол длиной n указанным выше способом.
Например, T(1) = 10 и T(2) = 101.
Пусть S(L) будет тройной суммой ∑a,b,c НОД(T(ca), T(cb)) для 1 ≤ a, b, c ≤ L.
Например:
S(2) = 10444
S(3) = 1292115238446807016106539989
S(4) mod 987 898 789 = 670616280.
Найдите S(2000) mod 987 898 789.
