##Efficient exponentiation

The most naive way of computing n15 requires fourteen multiplications:
n × n × ... × n = n15
But using a "binary" method you can compute it in six multiplications:
n × n = n2n2 × n2 = n4n4 × n4 = n8n8 × n4 = n12n12 × n2 = n14n14 × n = n15
However it is yet possible to compute it in only five multiplications:
n × n = n2n2 × n = n3n3 × n3 = n6n6 × n6 = n12n12 × n3 = n15
We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
For 1 ≤ k ≤ 200, find ∑ m(k).
##Эффективный метод возведения в степень

Наиболее простой способ нахождения n15 требует выполнения 14 умножений:
n × n × ... × n = n15
Если воспользоваться "двойным" методом, n15 можно найти, выполнив 6 умножений:
n × n = n2
n2 × n2 = n4
n4 × n4 = n8
n8 × n4 = n12
n12 × n2 = n14
n14 × n = n15
Однако, количество умножений можно еще уменьшить – до 5 умножений:
n × n = n2
n2 × n = n3
n3 × n3 = n6
n6 × n6 = n12
n12 × n3 = n15
Определим m(k) как минимальное количество умножений для нахождения nk. К примеру, m(15) = 5.
Найдите ∑ m(k) для 1 ≤ k ≤ 200.
