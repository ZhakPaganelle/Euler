##Counting Binary Matrices

A binary matrix is a matrix consisting entirely of 0s and 1s. Consider the following transformations that can be performed on a binary matrix:
Two binary matrices $A$ and $B$ will be considered equivalent if there is a sequence of such transformations that when applied to $A$ yields $B$. For example, the following two matrices are equivalent:
via the sequence of two transformations "Flip all elements in column 3" followed by "Swap rows 1 and 2".
Define $c(n)$ to be the maximum number of $n\times n$ binary matrices that can be found such that no two are equivalent. For example, $c(3)=3$. You are also given that $c(5)=39$ and $c(8)=656108$.
Find $c(20)$, and give your answer modulo $1\,001\,001\,011$.
##Подсчет двоичных матриц

Двоичная матрица - это матрица, состоящая исключительно из нулей и единиц. Рассмотрим следующие преобразования, которые можно выполнить над двоичной матрицей:

Поменять местами любые два ряда
Поменять местами любые два столбца
Обратить все элементы одного ряда (1 становятся 0, а 0 становятся 1)
Обратить все элементы одного столбца

Две бинарные матрицы $A$ и $B$ будем считать эквивалентными, если существует последовательность преобразований, которые при выполнении над $A$, дают в результате $B$. Например, следующие две матрицы эквивалентны:
$A=\begin{pmatrix} 
  1 & 0 & 1 \\ 
  0 & 0 & 1 \\
  0 & 0 & 0 \\
\end{pmatrix} \quad B=\begin{pmatrix} 
  0 & 0 & 0 \\ 
  1 & 0 & 0 \\
  0 & 0 & 1 \\
\end{pmatrix}$
через последовательность из двух преобразований "Обратить все элементы столбца 3" и "Поменять местами ряды 1 и 2".
Определим $c(n)$ как максимальное количество двоичных матриц $n\times n$, из которых никакие две не эквивалентны. Например, $c(3)=3$. Вам также дано, что $c(5)=39$ и $c(8)=656108$.
Найдите $c(20)$. В качестве ответа приведите остаток от деления полученного результата на $1\,001\,001\,011$.
