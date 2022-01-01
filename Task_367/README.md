##Bozo sort


Bozo sort, not to be confused with the slightly less efficient bogo sort, consists out of checking if the input sequence is sorted and if not swapping randomly two elements. This is repeated until eventually the sequence is sorted.


If we consider all permutations of the first 4 natural numbers as input the expectation value of the number of swaps, averaged over all 4! input sequences is 24.75.
The already sorted sequence takes 0 steps. 


In this problem we consider the following variant on bozo sort.
If the sequence is not in order we pick three elements at random and shuffle these three elements randomly.
All 3!=6 permutations of those three elements are equally likely. 
The already sorted sequence will take 0 steps.
If we consider all permutations of the first 4 natural numbers as input the expectation value of the number of shuffles, averaged over all 4! input sequences is 27.5. 
Consider as input sequences the permutations of the first 11 natural numbers.
Averaged over all 11! input sequences, what is the expected number of shuffles this sorting algorithm will perform?


Give your answer rounded to the nearest integer.

##Сортировка бозо


Сортировка бозо, не путайте с немного менее эффективной сортировкой бого, заключается в проверке, отсортирована ли исходная последовательность и - если нет - перестановке двух случайных элементов. Это действие повторяется, пока последовательность не будет отсортирована.


Если мы рассмотрим все сочетания первых 4 натуральных чисел в качестве исходных последовательностей, ожидаемое количество перестановок, среднее для всех 4! исходных последовательностей, будет равно 24.75.
Уже отсортированная последовательность требует 0 перестановок.


В этой задаче мы рассмотрим следующий вариант сортировки бозо:
Если последовательность не упорядочена, мы выбираем три случайных элемента и случайным образом меняем их местами.
Все 3!=6 сочетаний этих элементов имеют одинаковую вероятность.
Уже отсортированная последовательность требует 0 перестановок.
Если мы рассмотрим все сочетания первых 4 натуральных чисел в качестве исходных последовательностей, ожидаемое количество перестановок, среднее для всех 4! исходных последовательностей, будет равно 27.5. 
Используйте в качестве исходных последовательностей все сочетания первых 11 натуральных чисел.
Каково ожидаемое количество перестановок, среднее для всех 11! исходных последовательностей, при таком сортировочном алгоритме?


Дайте ответ, округленный до ближайшего целого.

