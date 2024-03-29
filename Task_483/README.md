##Repeated permutation


We define a permutation as an operation that rearranges the order of the elements {1, 2, 3, ..., n}.
There are n! such permutations, one of which leaves the elements in their initial order.
For n = 3 we have 3! = 6 permutations:
- P1 = keep the initial order
- P2 = exchange the 1st and 2nd elements
- P3 = exchange the 1st and 3rd elements
- P4 = exchange the 2nd and 3rd elements
- P5 = rotate the elements to the right
- P6 = rotate the elements to the left


If we select one of these permutations, and we re-apply the same permutation repeatedly, we eventually restore the initial order.For a permutation Pi, let f(Pi) be the number of steps required to restore the initial order by applying the permutation Pi repeatedly.For n = 3, we obtain:- f(P1) = 1 : (1,2,3) → (1,2,3)- f(P2) = 2 : (1,2,3) → (2,1,3) → (1,2,3)- f(P3) = 2 : (1,2,3) → (3,2,1) → (1,2,3)- f(P4) = 2 : (1,2,3) → (1,3,2) → (1,2,3)- f(P5) = 3 : (1,2,3) → (3,1,2) → (2,3,1) → (1,2,3)- f(P6) = 3 : (1,2,3) → (2,3,1) → (3,1,2) → (1,2,3)


Let g(n) be the average value of f2(Pi) over all permutations Pi of length n.g(3) = (12 + 22 + 22 + 22 + 32 + 32)/3! = 31/6 ≈ 5.166666667e0g(5) = 2081/120 ≈ 1.734166667e1g(20) = 12422728886023769167301/2432902008176640000 ≈ 5.106136147e3


Find g(350) and write the answer in scientific notation rounded to 10 significant digits, using a lowercase e to separate mantissa and exponent, as in the examples above.

##Повторенные перестановки


Определим перестановку как результат операции, меняющей местами элементы множества {1, 2, 3, ..., n}.
Существует всего n! таких перестановок, одна из которых оставляет элементы в их изначальном порядке.
Для n = 3 существует 3! = 6 перестановок:
- P1 = изначальный порядок
- P2 = поменять местами 1ый и 2ой элементы
- P3 = поменять местами 1ый и 3ий элементы
- P4 = поменять местами 2ой и 3ий элементы
- P5 = сдвинуть все элементы вправо на одну позицию
- P6 = сдвинуть все элементы влево на одну позицию


Если мы выберем одну из этих перестановок и применим такую же перестановку несколько раз, в конце концов мы вернемся к изначальному расположению элементов.
Для перестановки Pi, пусть f(Pi) будет количеством шагов, необходимых для достижения изначального порядка элементов путем повторного применения перестановки Pi.
Для n = 3 мы получим:
- f(P1) = 1 : (1,2,3) → (1,2,3)
- f(P2) = 2 : (1,2,3) → (2,1,3) → (1,2,3)
- f(P3) = 2 : (1,2,3) → (3,2,1) → (1,2,3)
- f(P4) = 2 : (1,2,3) → (1,3,2) → (1,2,3)
- f(P5) = 3 : (1,2,3) → (3,1,2) → (2,3,1) → (1,2,3)
- f(P6) = 3 : (1,2,3) → (2,3,1) → (3,1,2) → (1,2,3)


Пусть g(n) будет средним значением f2(Pi) для всех перестановок Pi длиной n.
g(3) = (12 + 22 + 22 + 22 + 32 + 32)/3! = 31/6 ≈ 5.166666667e0
g(5) = 2081/120 ≈ 1.734166667e1
g(20) = 12422728886023769167301/2432902008176640000 ≈ 5.106136147e3


Найдите g(350) и запишите ответ в стандартном виде округленным до 10 значимых цифр. Используйте строчную латинскую букву "e" для отделения мантиссы от порядка, как это сделанно в вышеприведенных примерах.

