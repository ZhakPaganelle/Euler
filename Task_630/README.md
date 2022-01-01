##Crossed lines


Given a set, $L$, of unique lines, let $M(L)$ be the number of lines in the set and let $S(L)$ be the sum over every line of the number of times that line is crossed by another line in the set.  For example, two sets of three lines are shown below:


In both cases M(L) is 3 and S(L) is 6: each of the three lines is crossed by two other lines.  Note that even if the lines cross at a single point, all of the separate crossings of lines are counted.


Consider points ($T_{2k−1}$, $T_{2k}$), for integer $k >= 1$, generated in the following way:


$S_0 	=  	290797$ 
$S_{n+1} 	=  	{S_n}^2 \:\: \rm{mod} \:\: 50515093$
$T_n 	=  	( S_n \:\: \rm{mod} \:\: 2000 ) − 1000$


For example, the first three points are: (527, 144), (−488, 732), (−454, −947).  Given the first $n$ points generated in this manner, let $L_n$ be the set of unique lines that can be formed by joining each point with every other point, the lines being extended indefinitely in both directions.  We can then define $M(L_n)$ and $S(L_n)$ as described above.


For example, $M(L_3) = 3$ and $S(L_3) = 6$.  Also $M(L_{100}) = 4948$ and $S(L_{100}) = 24477690$.


Find $S(L_{2500})$.

##Пересекающиеся прямые


При данном множестве уникальных прямых $L$, пусть $M(L)$ будет количеством прямых в этом множестве, и пусть $S(L)$ будет суммой количеств пересечений с другими прямыми множества для каждой прямой. Например, два множества из трех прямых показаны ниже:



В обоих случаях M(L) равно 3 и S(L) равно 6: каждая из трех прямых пересекается с двумя другими прямыми. Заметим, что даже если прямые пересекаются в одной точке, для каждой прямой это пересечение считается отдельно.


Рассмотрим точки ($T_{2k−1}$, $T_{2k}$) для целого $k >= 1$, сгенерированные следующим образом:


$S_0 	=  	290797$ 
$S_{n+1} 	=  	{S_n}^2 \:\: \rm{mod} \:\: 50515093$
$T_n 	=  	( S_n \:\: \rm{mod} \:\: 2000 ) − 1000$


Например, первыми тремя точками являются: (527, 144), (−488, 732), (−454, −947). При данных первых $n$ таким образом сгенерированных точках, пусть $L_n$ будет множеством уникальных прямых, образованных соединением каждой точки с каждой другой точкой и продлением полученных отрезков на бесконечное расстояние в обоих направлениях. Можем определить $M(L_n)$ и $S(L_n)$, как описано выше.


Например, $M(L_3) = 3$ и $S(L_3) = 6$. Также, $M(L_{100}) = 4948$ и $S(L_{100}) = 24477690$.

Найдите $S(L_{2500})$.

