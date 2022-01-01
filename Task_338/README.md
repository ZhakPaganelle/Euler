##Cutting Rectangular Grid Paper

A rectangular sheet of grid paper with integer dimensions w × h is given. Its grid spacing is 1.
When we cut the sheet along the grid lines into two pieces and rearrange those pieces without overlap, we can make new rectangles with different dimensions.
For example, from a sheet with dimensions 9 × 4 , we can make rectangles with dimensions 18 × 2, 12 × 3 and 6 × 6 by cutting and rearranging as below:
Similarly, from a sheet with dimensions 9 × 8 , we can make rectangles with dimensions 18 × 4 and 12 × 6 .
For a pair w and h, let F(w,h) be the number of distinct rectangles that can be made from a sheet with dimensions w × h .
For example, F(2,1) = 0, F(2,2) = 1, F(9,4) = 3 and F(9,8) = 2. 
Note that rectangles congruent to the initial one are not counted in F(w,h).
Note also that rectangles with dimensions w × h and dimensions h × w are not considered distinct.
For an integer N, let G(N) be the sum of F(w,h) for all pairs w and h which satisfy 0 < h ≤ w ≤ N.
We can verify that G(10) = 55, G(103) = 971745 and G(105) = 9992617687.
Find G(1012). Give your answer modulo 108.
##Разрезание бумаги в клеточку

Возьмем прямоугольный лист бумаги в клеточку размерами w × h. Шаг клетки составляет 1.
Если разрезать такой лист по границам клеток и совместить полученные куски без перекрытия, то можно образовать прямоугольники других размеров.
К примеру, из листа рамерами 9 × 4 , можно создать прямоугольники размерами 18 × 2, 12 × 3 и 6 × 6, если разрезать и соединить полученные куски, как это показано ниже:  

Аналогично, из листа размерами 9 × 8 , можно образовать прямоугольники размерами 18 × 4 и 12 × 6 .
Для пары чисел w и h определим F(w,h) как количество отличных прямоугольников, которые можно образовать из листа бумаги размерами w × h .
Например, F(2,1) = 0, F(2,2) = 1, F(9,4) = 3 и F(9,8) = 2. 
Учтите, что прямоугольники, конгруэнтные заданному, не учитываются в F(w,h).
Также учтите, что прямоугольник размерами w × h и прямоугольник размерами h × w не считаются отличными.
Для целых значений N определим G(N) в виде суммы F (w,h) для всех тех пар w и h, которые удовлетворяют требованию 0 < h ≤ w ≤ N.
Можно убедиться, что G(10) = 55, G(103) = 971745 и G(105) = 9992617687.
Найдите G(1012). Ответ приведите по модулю 108.
