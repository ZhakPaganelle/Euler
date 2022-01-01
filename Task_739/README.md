##Summation of Summations


Take a sequence of length $n$. Discard the first term then make a sequence of the partial summations. Continue to do this over and over until we are left with a single term. We define this to be $f(n)$.


Consider the example where we start with a sequence of length 8:


$
\begin{array}{rrrrrrrr}
1&1&1&1&1&1&1&1\\
 &1&2&3&4&5& 6 &7\\
 & &2&5&9&14&20&27\\
 & & &5&14&28&48&75\\
 & & & &14&42&90&165\\
 & & & & & 42 & 132 & 297\\
 & & & & & & 132 &429\\
 & & & & & & &429\\
\end{array}
$


Then the final number is $429$, so $f(8) = 429$.


For this problem we start with the sequence $1,3,4,7,11,18,29,47,\ldots$
This is the Lucas sequence where two terms are added to get the next term. 
Applying the same process as above we get $f(8) = 2663$.
You are also given $f(20) = 742296999 $ modulo $1\,000\,000\,007$


Find $f(10^8)$. Give your answer modulo $1\,000\,000\,007$.

##Сложение сумм


Возьмем последовательность длиной $n$. Отбросим первый элемент, затем образуем последовательность частичных сумм. Повторим это снова и снова, пока не останется единственный элемент. Определим это как $f(n)$.


Рассмотрим пример, в котором начнем с последовательности длиной 8:


$
\begin{array}{rrrrrrrr}
1&1&1&1&1&1&1&1\\
 &1&2&3&4&5& 6 &7\\
 & &2&5&9&14&20&27\\
 & & &5&14&28&48&75\\
 & & & &14&42&90&165\\
 & & & & & 42 & 132 & 297\\
 & & & & & & 132 &429\\
 & & & & & & &429\\
\end{array}
$


Последнее число - $429$, поэтому $f(8) = 429$.


В этой задаче начнем с последовательности $1,3,4,7,11,18,29,47,\ldots$
Это - последовательность Люка, в которой для получения следующего элемента складываются два предыдущих. 
Применяя тот же процесс, как выше, получим $f(8) = 2663$.
Также известно, что $f(20) = 742296999 $ modulo $1\,000\,000\,007$


Найдите $f(10^8)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
