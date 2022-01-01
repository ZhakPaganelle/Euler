##Power sets of power sets

Let P(n) be the set of the first n positive integers {1, 2, ..., n}.
Let Q(n) be the set of all the non-empty subsets of P(n).
Let R(n) be the set of all the non-empty subsets of Q(n).
An element X ∈ R(n) is a non-empty subset of Q(n), so it is itself a set.
From X we can construct a graph as follows:
For example, X = {{1}, {1,2,3}, {3}, {5,6}, {6,7}} results in the following graph:
This graph has two connected components.
Let C(n,k) be the number of elements of R(n) that have exactly k connected components in their graph.
You are given C(2,1) = 6, C(3,1) = 111, C(4,2) = 486, C(100,10) mod 1 000 000 007 = 728209718.
Find C(104,10) mod 1 000 000 007.
##Булеан булеанов

Пусть P(n) будет множеством первых n натуральных чисел {1, 2, ..., n}.
Пусть Q(n) будет множеством всех непустых подмножеств P(n).
Пусть R(n) будет множеством всех непустых подмножеств Q(n).
Элемент X ∈ R(n) является непустым подмножеством Q(n), поэтому он сам по себе является множеством.
Из X мы можем построить граф следующим образом:
Каждый элемент Y ∈ X соответствует вершине графа и обозначается Y;
Две вершины Y1 и Y2 соединены, если Y1 ∩ Y2 ≠ ∅.
Например, из X = {{1}, {1,2,3}, {3}, {5,6}, {6,7}} получается следующий граф:

Этот граф имеет две компоненты связности.
Пусть C(n,k) будет количеством элементов R(n), которые имеют ровно k компонент связности в своем графе.
Известно, что C(2,1) = 6, C(3,1) = 111, C(4,2) = 486, C(100,10) mod 1 000 000 007 = 728209718.
Найдите C(104,10) mod 1 000 000 007.
