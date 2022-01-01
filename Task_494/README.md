##Collatz prefix families


The Collatz sequence is defined as:
$a_{i+1} = \left\{  \large{\frac {a_i} 2 \atop 3 a_i+1} {\text{if }a_i\text{ is even} \atop \text{if }a_i\text{ is odd}} \right.$.


The Collatz conjecture states that starting from any positive integer, the sequence eventually reaches the cycle 1,4,2,1....
We shall define the sequence prefix p(n) for the Collatz sequence starting with a1 = n as the sub-sequence of all numbers not a power of 2 (20=1 is considered a power of 2 for this problem). For example:p(13) = {13, 40, 20, 10, 5} p(8) = {}
Any number invalidating the conjecture would have an infinite length sequence prefix.


Let Sm be the set of all sequence prefixes of length m. Two sequences {a1, a2, ..., am} and {b1, b2, ..., bm} in Sm are said to belong to the same prefix family if ai < aj if and only if bi < bj for all 1 ≤ i,j ≤ m.


For example, in S4, {6, 3, 10, 5} is in the same family as {454, 227, 682, 341}, but not {113, 340, 170, 85}.
Let f(m) be the number of distinct prefix families in Sm.
You are given f(5) = 5, f(10) = 55, f(20) = 6771.


Find f(90).

##Семейства префиксов Коллатца


Последовательность Коллатца определяется как:
$a_{i+1} = \left\{ \large{\frac {a_i} 2 \atop 3 a_i+1} {\text{если }a_i\text{ четно} \atop \text{если }a_i\text{ нечетно}} \right.$.


Гипотеза Коллатца состоит в том, что, начиная с любого натурального числа, эта последовательность рано или поздно достигнет цикла 1,4,2,1....
Определим префикс p(n) для последовательности Коллатца, начинающейся с a1 = n, как под-последовательность всех чисел, не являющихся степенями двойки (в данной задаче 20=1 считается степенью 2). Например:
p(13) = {13, 40, 20, 10, 5} 
p(8) = {}
Любое число, опровергающее гипотезу Коллатца, будет иметь бесконечно длинный префикс последовательности.


Пусть Sm будет множеством всех префиксов множества длиной m. Две последовательности {a1, a2, ..., am} и {b1, b2, ..., bm} в Sm будем считать принадлежащими к одному и тому же семейству префиксов при ai < aj в том и только том случае, если bi < bj для всех 1 ≤ i,j ≤ m.


Например, в S4 {6, 3, 10, 5} принадлежит к тому же семейству, что и {454, 227, 682, 341}, но не {113, 340, 170, 85}.
Пусть f(m) будет количеством различных семейств префиксов в Sm.
Известно, что f(5) = 5, f(10) = 55, f(20) = 6771.


Найдите f(90).

