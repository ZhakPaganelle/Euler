##Paths to Equality

Define two functions on lattice points:
A path to equality of length $n$ for a pair $(a,b)$ is a sequence $\Big((a_1,b_1),(a_2,b_2),\ldots,(a_n,b_n)\Big)$, where:
$a_n = b_n$ is called the final value.
For example,
This is a path to equality for $(45,90)$ and is of length 10 with final value 1476. There is no path to equality of $(45,90)$ with smaller length.
Find the unique path to equality for $(45,90)$ with smallest odd length. Enter the final value as your answer.
##Пути к равенству

Определим две функции на точках решетки:
$r(x,y) = (x+1,2y)$
$s(x,y) = (2x,y+1)$
Путь к равенству длиной $n$ для пары $(a,b)$ является последовательностью $\Big((a_1,b_1),(a_2,b_2),\ldots,(a_n,b_n)\Big)$, где:

$(a_1,b_1) = (a,b)$
$(a_k,b_k) = r(a_{k-1},b_{k-1})$ or $(a_k,b_k) = s(a_{k-1},b_{k-1})$ для $k > 1$
$a_k \ne b_k$ для $k < n$
$a_n = b_n$

$a_n = b_n$ называется конечным значением.
Например,
$(45,90)\xrightarrow{r} (46,180)\xrightarrow{s}(92,181)\xrightarrow{s}(184,182)\xrightarrow{s}(368,183)\xrightarrow{s}(736,184)\xrightarrow{r}$
$(737,368)\xrightarrow{s}(1474,369)\xrightarrow{r}(1475,738)\xrightarrow{r}(1476,1476)$
Это - путь к равенству для $(45,90)$, его длина равна 10 и финальное значение равно 1476. Не существует более короткого пути к равенству для $(45,90)$.
Найдите единственный путь к равенству для $(45,90)$ с наименьшей нечетной длиной. В качестве ответа приведите его конечное значение.
Оригинал
