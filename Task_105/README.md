##Special subset sums: testing

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.
Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).
NOTE: This problem is related to Problem 103 and Problem 106.
##Суммы особых подмножеств: проверка

Пусть S(A) представляет собой сумму элементов множества А размером n. Будем называть это множество особым суммарным множеством, если для любых двух непустых и непересекающихся подмножеств B и C справедливо следующее:

S(B) ≠ S(C); т.е. суммы элементов подмножеств не могут быть равными.
Если B содержит больше элементов, чем C, то S(B) > S(C).

К примеру, {81, 88, 75, 42, 87, 84, 86, 65} не является особым суммарным множеством, поскольку 65 + 87 + 88 = 75 + 81 + 84. В свою очередь, {157, 150, 164, 119, 79, 159, 161, 139, 158} удовлетворяет обоим правилам для всех возможных комбинаций пар подмножеств и его S(A) = 1286.
В текстовом файле sets.txt (щелкнув правой кнопкой мыши, выберите 'Save Link/Target As...') размером 4KБ записана сотня множеств, содержащих от семи до двенадцати элементов (два примера, рассмотренные выше, являются первыми двумя множествами в файле). Найдите все особые суммарные множества A1, A2, ..., Ak и найдите значение S(A1) + S(A2) + ... + S(Ak).
Примечание: Данная задача имеет также отношение к задачам №103 и №106.
