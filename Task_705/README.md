##Total Inversion Count of Divided Sequences


The inversion count of a sequence of digits is the smallest number of adjacent pairs that must be swapped to sort the sequence.
For example, 34214 has inversion count of 5:
$34214 \to 32414 \to 23414 \to 23144 \to 21344 \to12344$.


If each digit of a sequence is replaced by one of its divisors a divided sequence is obtained. 
For example, the sequence 332 has 8 divided sequences: $\{332,331,312,311,132,131,112,111\}$.


Define $G(N)$ to be the concatenation of all primes less than $N$, ignoring any zero digit. 
For example, $G(20) = 235711131719$.


Define $F(N)$ to be the sum of the inversion count for all possible divided sequences from the master sequence $G(N)$. 
You are given $F(20) = 3312$ and $F(50) = 338079744$.


Find $F(10^8)$. Give your answer modulo $1\,000\,000\,007$.

##Суммарное число инверсий разделенных последовательностей


Число инверсий последовательности цифр - это наименьшее количество пар соседних цифр, которое надо поменять местами, чтобы отсортировать последовательность по возрастанию.
Например, число инверсий последовательности 34214 равно 5:
$34214 \to 32414 \to 23414 \to 23144 \to 21344 \to12344$.


Если каждую цифру в последовательности заменить на один из ее делителей, получим разделенную последовательность. 
Например, последовательность 332 имеет 8 разделенных последовательностей: $\{332,331,312,311,132,131,112,111\}$.


Определим $G(N)$ как объединение всех простых чисел меньше $N$, исключая все цифры ноль. 
Например, $G(20) = 235711131719$.


Определим $F(N)$ как сумму чисел инверсий для всех возможных разделенных последовательностей от исходной последовательности $G(N)$. 
Известно, что $F(20) = 3312$ и $F(50) = 338079744$.


Найдите $F(10^8)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал