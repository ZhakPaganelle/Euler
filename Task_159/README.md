##Digital root sums of factorisations

A composite number can be factored many different ways.  
For instance, not including multiplication by one, 24 can be factored in 7 distinct ways:
Recall that the digital root of a number, in base 10, is found by adding together the digits of that number, 
and repeating that process until a number is arrived at that is less than 10.  
Thus the digital root of 467 is 8.
We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.
 The chart below demonstrates all of the DRS values for 24.
The maximum Digital Root Sum  of 24 is 11.
The function mdrs(n) gives the maximum Digital Root Sum of n. So  mdrs(24)=11.
Find ∑ mdrs(n) for 1 < n < 1,000,000.
##Суммы цифровых корней множителей

Сложное число может быть разложено на множители разными путями. К примеру, если исключить умножение на единицу, 24 может быть разложено семью разными способами:

24 = 2×2×2×3
24 = 2×3×4
24 = 2×2×6
24 = 4×6
24 = 3×8
24 = 2×12
24 = 24

Напомним, что цифровой корень числа по основанию 10 можно найти, складывая цифры этого числа, и повторяя этот процесс, пока в результате не получится число меньше 10. Таким образом, цифровой корень числа 467 равен 8.
Назовем Суммой Цифровых Корней (СЦК) сумму цифровых корней каждого из множителей числа.
 Таблица ниже демонстрирует все значения СЦК для числа 24.

Разложение на множителиСумма Цифровых Корней
2×2×2×3
9
2×3×4
9
2×2×6
10
4×6
10
3×8
11
2×12
5
24
6

Максимальная СЦК для 24 равна 11.

Функция mdrs(n) возвращает максимальную СЦК для числа n. Таким образом, mdrs(24)=11.
Найдите ∑mdrs(n) для 1 < n < 1 000 000.
