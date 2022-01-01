##Concatenation Coincidence

A non-decreasing sequence of integers $a_n$ can be generated from any positive real value $\theta$ by the following procedure:
\begin{align}
\begin{split}
b_1 &= \theta \\
b_n &= \left\lfloor b_{n-1} \right\rfloor \left(b_{n-1} - \left\lfloor b_{n-1} \right\rfloor + 1\right)~~~\forall ~ n \geq 2 \\
a_n &= \left\lfloor b_{n} \right\rfloor
\end{split}
\end{align}
Where $\left\lfloor . \right\rfloor$ is the floor function.
For example, $\theta=2.956938891377988...$ generates the Fibonacci sequence: $2, 3, 5, 8, 13, 21, 34, 55, 89, ...$
The concatenation of a sequence of positive integers $a_n$ is a real value denoted $\tau$ constructed by concatenating the elements of the sequence after the decimal point, starting at $a_1$: $a_1.a_2a_3a_4...$
For example, the Fibonacci sequence constructed from $\theta=2.956938891377988...$ yields the concatenation $\tau=2.3581321345589...$ Clearly, $\tau \neq \theta$ for this value of $\theta$.
Find the only value of $\theta$ for which the generated sequence starts at $a_1=2$ and the concatenation of the generated sequence equals the original value: $\tau = \theta$. Give your answer rounded to 24 places after the decimal point.
##Совпадение конкатенаций

Неубывающая последовательность целых чисел $a_n$ может быть сгенерированна из любого положительного вещественного значения $\theta$ следующим образом:
\begin{align}
\begin{split}
b_1 &= \theta \\
b_n &= \left\lfloor b_{n-1} \right\rfloor \left(b_{n-1} - \left\lfloor b_{n-1} \right\rfloor + 1\right)~~~\forall ~ n \geq 2 \\
a_n &= \left\lfloor b_{n} \right\rfloor
\end{split}
\end{align}
Где $\left\lfloor . \right\rfloor$ - функция пол.
Например, $\theta=2.956938891377988...$ генерирует последовательность Фибоначчи: $2, 3, 5, 8, 13, 21, 34, 55, 89, ...$
Конкатенация последовательности натуральных чисел $a_n$ - это вещественное значение, обозначенное $\tau$, составленное конкатенацией элементов последовательности после десятичной точки, начиная с $a_1$: $a_1.a_2a_3a_4...$
Например, сгенерированная из $\theta=2.956938891377988...$ последовательность Фибоначчи дает конкатенацию  $\tau=2.3581321345589...$ Очевидно, $\tau \neq \theta$ для этого значения $\theta$.
Найдите единственное значение $\theta$, для которого сгенерированная последовательность начинается с $a_1=2$ и конкатенация сгенерированной последовательности равна исходному значению: $\tau = \theta$. Дайте ваш ответ округленным до 24 знака после десятичной точки. Оригинал
