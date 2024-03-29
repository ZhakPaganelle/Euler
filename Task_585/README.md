##Nested square roots

Consider the term $\small \sqrt{x+\sqrt{y}+\sqrt{z}}$ that is representing a nested square root. $x$, $y$ and $z$ are positive integers and $y$ and $z$ are not allowed to be perfect squares, so the number below the outer square root is irrational. Still it can be shown that for some combinations of $x$, $y$ and $z$ the given term can be simplified into a sum and/or difference of simple square roots of integers, actually denesting the square roots in the initial expression. 
Here are some examples of this denesting:
$\small \sqrt{3+\sqrt{2}+\sqrt{2}}=\sqrt{2}+\sqrt{1}=\sqrt{2}+1$
$\small \sqrt{8+\sqrt{15}+\sqrt{15}}=\sqrt{5}+\sqrt{3}$
$\small \sqrt{20+\sqrt{96}+\sqrt{12}}=\sqrt{9}+\sqrt{6}+\sqrt{3}-\sqrt{2}=3+\sqrt{6}+\sqrt{3}-\sqrt{2}$
$\small \sqrt{28+\sqrt{160}+\sqrt{108}}=\sqrt{15}+\sqrt{6}+\sqrt{5}-\sqrt{2}$
As you can see the integers used in the denested expression may also be perfect squares resulting in further simplification.
Let F($n$) be the number of different terms $\small \sqrt{x+\sqrt{y}+\sqrt{z}}$, that can be denested into the sum and/or difference of a finite number of square roots, given the additional condition that $0<x \le n$. That is,
$\small \displaystyle \sqrt{x+\sqrt{y}+\sqrt{z}}=\sum_{i=1}^k s_i\sqrt{a_i}$
with $k$, $x$, $y$, $z$ and all $a_i$ being positive integers, all $s_i =\pm 1$ and $x\le n$. Furthermore $y$ and $z$  are not allowed to be perfect squares.
Nested roots with the same value are not considered different, for example $\small \sqrt{7+\sqrt{3}+\sqrt{27}}$, $\small \sqrt{7+\sqrt{12}+\sqrt{12}}$ and $\small \sqrt{7+\sqrt{27}+\sqrt{3}}$, that can all three be denested into $\small 2+\sqrt{3}$, would only be counted once.
You are given that F(10)=17, F(15)=46, F(20)=86, F(30)=213 and F(100)=2918 and F(5000)=11134074.
Find F(5000000).
##Вложенные квадратные корни

Рассмотрим выражение $\small \sqrt{x+\sqrt{y}+\sqrt{z}}$, которое представляет собой вложенный квадратный корень. $x$, $y$ и $z$ - натуральные числа, а $y$ и $z$ не могут быть полными квадратами, так что число под внешним квадратным корнем иррационально. Тем не менее, можно показать, что для некоторых комбинаций $x$, $y$ и $z$ данное выражение может быть упрощено до вида суммы и/или разницы квадратных корней целых чисел, таки образом разложив квадратные корни в изначальном выражении. 
Вот несколько примеров такого разложения:
$\small \sqrt{3+\sqrt{2}+\sqrt{2}}=\sqrt{2}+\sqrt{1}=\sqrt{2}+1$
$\small \sqrt{8+\sqrt{15}+\sqrt{15}}=\sqrt{5}+\sqrt{3}$
$\small \sqrt{20+\sqrt{96}+\sqrt{12}}=\sqrt{9}+\sqrt{6}+\sqrt{3}-\sqrt{2}=3+\sqrt{6}+\sqrt{3}-\sqrt{2}$
$\small \sqrt{28+\sqrt{160}+\sqrt{108}}=\sqrt{15}+\sqrt{6}+\sqrt{5}-\sqrt{2}$
Как видите, целые числа, использованные в разложенном выражении, могут также быть полными квадратами, что позволяет далее упростить выражение.
Пусть F($n$) будет количеством различных выражений $\small \sqrt{x+\sqrt{y}+\sqrt{z}}$, которые могут быть разложены в сумму и/или разность конечного количества квадратных корней с дополнительным условием, что $0<x \le n$. То есть,
$\small \displaystyle \sqrt{x+\sqrt{y}+\sqrt{z}}=\sum_{i=1}^k s_i\sqrt{a_i}$,
где $k$, $x$, $y$, $z$ и все $a_i$ - натуральные числа, все $s_i =\pm 1$ и $x\le n$. Более того, $y$ и $z$ не могут быть полными квадратами.
Вложенные квадратные корни, имеющие одинаковые значения, не считаются различными. Например, все три корня $\small \sqrt{7+\sqrt{3}+\sqrt{27}}$, $\small \sqrt{7+\sqrt{12}+\sqrt{12}}$ и $\small \sqrt{7+\sqrt{27}+\sqrt{3}}$ могут быть разложены в $\small 2+\sqrt{3}$, и поэтому считаются как один квадратный корень.
Известно, что F(10)=17, F(15)=46, F(20)=86, F(30)=213, F(100)=2918 и F(5000)=11134074.
Найдите F(5000000).
