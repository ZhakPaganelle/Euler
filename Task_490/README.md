##Jumping frog

There are n stones in a pond, numbered 1 to n. Consecutive stones are spaced one unit apart.
A frog sits on stone 1. He wishes to visit each stone exactly once, stopping on stone n. However, he can only jump from one stone to another if they are at most 3 units apart. In other words, from stone i, he can reach a stone j if 1 ≤ j ≤ n and j is in the set {i-3, i-2, i-1, i+1, i+2, i+3}.
Let f(n) be the number of ways he can do this. For example, f(6) = 14, as shown below:
1 → 2 → 3 → 4 → 5 → 6 
1 → 2 → 3 → 5 → 4 → 6 
1 → 2 → 4 → 3 → 5 → 6 
1 → 2 → 4 → 5 → 3 → 6 
1 → 2 → 5 → 3 → 4 → 6 
1 → 2 → 5 → 4 → 3 → 6 
1 → 3 → 2 → 4 → 5 → 6 
1 → 3 → 2 → 5 → 4 → 6 
1 → 3 → 4 → 2 → 5 → 6 
1 → 3 → 5 → 2 → 4 → 6 
1 → 4 → 2 → 3 → 5 → 6 
1 → 4 → 2 → 5 → 3 → 6 
1 → 4 → 3 → 2 → 5 → 6 
1 → 4 → 5 → 2 → 3 → 6
Other examples are f(10) = 254 and f(40) = 1439682432976.
Let S(L) = ∑ f(n)3 for 1 ≤ n ≤ L.
Examples:
S(10) = 18230635
S(20) = 104207881192114219
S(1 000) mod 109 = 225031475
S(1 000 000) mod 109 = 363486179
Find S(1014) mod 109.
##Прыгающая лягушка

В пруду лежат в ряд n камней, пронумерованные от 1 до n. Номера последовательно лежащих камней различаются на единицу.
На камне № 1 сидит лягушка. Она хочет посетить каждый камень ровно один раз и в конце концов оказаться на камне № n. Однако, она может допрыгнуть только до камня, находящегося не дальше, чем за три единицы от ее текущего местоположения. Другими словами, с камня № i она может попасть на камень № j, если 1 ≤ j ≤ n и j является элементом множества {i-3, i-2, i-1, i+1, i+2, i+3}.
Пусть f(n) будет количеством способов, какими лягушка может достичь своей цели. Например, f(6) = 14, как показано ниже:
1 → 2 → 3 → 4 → 5 → 6 
1 → 2 → 3 → 5 → 4 → 6 
1 → 2 → 4 → 3 → 5 → 6 
1 → 2 → 4 → 5 → 3 → 6 
1 → 2 → 5 → 3 → 4 → 6 
1 → 2 → 5 → 4 → 3 → 6 
1 → 3 → 2 → 4 → 5 → 6 
1 → 3 → 2 → 5 → 4 → 6 
1 → 3 → 4 → 2 → 5 → 6 
1 → 3 → 5 → 2 → 4 → 6 
1 → 4 → 2 → 3 → 5 → 6 
1 → 4 → 2 → 5 → 3 → 6 
1 → 4 → 3 → 2 → 5 → 6 
1 → 4 → 5 → 2 → 3 → 6
Другие примеры: f(10) = 254 и f(40) = 1439682432976.
Пусть S(L) = ∑ f(n)3 для 1 ≤ n ≤ L.
Примеры:
S(10) = 18230635
S(20) = 104207881192114219
S(1 000) mod 109 = 225031475
S(1 000 000) mod 109 = 363486179
Найдите S(1014) mod 109.
