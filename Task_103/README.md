##Special subset sums: optimum

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.
n = 1: {1}n = 2: {1, 2}n = 3: {2, 3, 4}n = 4: {3, 5, 6, 7}n = 5: {6, 9, 11, 12, 13}
It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.
By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.
Given that A is an optimum special sum set for n = 7, find its set string.
NOTE: This problem is related to Problem 105 and Problem 106.
##Суммы особых подмножеств: оптимум

Пусть S(A) представляет собой сумму элементов множества А размером n. Будем называть это множество особым суммарным множеством, если для любых двух непустых и непересекающихся подмножеств B и C справедливо следующее:

S(B) ≠ S(C); т.е. суммы элементов подмножеств не могут быть равными.
Если B содержит больше элементов, чем C, то S(B) > S(C).

Если минимизировать сумму S(A) при заданном значении n, получим оптимальное особое суммарное множество. Ниже даны первые пять оптимальных особых суммарных множеств.
n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}
Похоже на то, что для заданного оптимального множества A = {a1, a2, ... , an}, следующим оптимальным множеством будет множество вида B = {b, a1+b, a2+b, ... ,an+b}, где b - "средний" элемент предыдущей строки.
Применяя данное "правило", можно было бы ожидать, что оптимальным множеством при n = 6 станет A = {11, 17, 20, 22, 23, 24}, у которого S(A) = 117. Однако, данное множество не является оптимальным, поскольку мы всего-лишь применили алгоритм нахождения близкого к оптимальному множества. Оптимальным множеством при for n = 6 будет A = {11, 18, 19, 20, 22, 25}, у которого S(A) = 115. Этому множеству соответствует строка 111819202225.
Дано, что A является оптимальным особым суммарным множеством при n = 7. Найдите строку, соответствующую этому множеству.
Примечание: Данная задача имеет также отношение к задачам №105 и №106.
