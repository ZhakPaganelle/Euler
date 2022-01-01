##Rounded Square Roots

We define the rounded-square-root of a positive integer n as the square root of n rounded to the nearest integer.
The following procedure (essentially Heron's method adapted to integer arithmetic) finds the rounded-square-root of n:
Let d be the number of digits of the number n.
If d is odd, set $x_0 = 2 \times 10^{(d-1)/2}$.
If d is even, set $x_0 = 7 \times 10^{(d-2)/2}$.
Repeat:
until $x_{k+1} = x_k$.
As an example, let us find the rounded-square-root of n = 4321.n has 4 digits, so $x_0 = 7 \times 10^{(4-2)/2} = 70$.
$$x_1 = \Biggl\lfloor{\dfrac{70 + \lceil{4321 / 70}\rceil}{2}}\Biggr\rfloor = 66$$
$$x_2 = \Biggl\lfloor{\dfrac{66 + \lceil{4321 / 66}\rceil}{2}}\Biggr\rfloor = 66$$

Since $x_2 = x_1$, we stop here.
So, after just two iterations, we have found that the rounded-square-root of 4321 is 66 (the actual square root is 65.7343137…).

The number of iterations required when using this method is surprisingly low.
For example, we can find the rounded-square-root of a 5-digit integer (10,000 ≤ n ≤ 99,999) with an average of 3.2102888889 iterations (the average value was rounded to 10 decimal places).

Using the procedure described above, what is the average number of iterations required to find the rounded-square-root of a 14-digit number (1013 ≤ n < 1014)?
Give your answer rounded to 10 decimal places.

Note: The symbols $\lfloor x \rfloor$ and $\lceil x \rceil$ represent the floor function and ceiling function respectively.

##Округленные квадратные корни

Определим округленный квадратный корень натурального числа n как квадратный корень n, округленный в сторону ближайшего целого числа.
Следующая процедура (по-существу, это - применение метода Герона для целочисленной арифметики) находит округленный квадратный корень числа n:
Пусть d - количество цифр числа n.
Если d нечетное число, x0 = 2×10(d-1)⁄2.
Если d четное число, x0 = 7×10 (d-2)⁄2.
Повторять цикл:
$$x_{k+1} = \Biggl\lfloor{\dfrac{x_k + \lceil{n / x_k}\rceil}{2}}\Biggr\rfloor$$

до тех пор, пока не будет достигнуто xk +1 = xk.

В качестве примера, рассмотрим округленный квадратный корень n = 4321.
n состоит из 4 цифр, так что $x_0 = 7 \times 10^{(4-2)/2} = 70$.
$$x_1 = \Biggl\lfloor{\dfrac{70 + \lceil{4321 / 70}\rceil}{2}}\Biggr\rfloor = 66\\
x_2 = \Biggl\lfloor{\dfrac{66 + \lceil{4321 / 66}\rceil}{2}}\Biggr\rfloor = 66$$

Поскольку x2 = x1, то здесь мы и останавливаемся.
Таким образом, по завершении всего двух итераций нам удалось найти округленный квадратный корень числа 4321, равный 66 (точное значение корня составляет 65.7343137…).

Число необходимых итераций для данного метода на удивление невелико.
К примеру, мы можем найти округленное значение квадратного корня для числа из 5 цифр (10 000 ≤ n ≤ 99 999), выполнив в среднем 3.2102888889 итераций (среднее значение округлено до 10 знака после десятичной точки).

Используя описанную выше процедуру, определите, чему равно среднее число итераций при нахождении округленного значения квадратного корня для 14-значного числа (1013 ≤ n < 1014)?
Ответ округлите с точностью до 10 знака после десятичной точки.

Примечание: Символами ⌊x⌋ и ⌈x⌉ обозначают функции округления вниз и округления вверх, соответственно.

