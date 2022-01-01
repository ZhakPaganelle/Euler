##Creative numbers

Alice plays the following game, she starts with a list of integers $L$ and on each step she can either:

For example starting from the list $L=\{8\}$, Alice can remove $8$ and add $2$ and $3$ resulting in $L=\{2,3\}$ in a first step. Then she can obtain $L=\{9\}$ in a second step.
Note that the same integer is allowed to appear multiple times in the list.
An integer $n>1$ is said to be creative if for any integer $m>1$ Alice can obtain a list that contains $m$ starting from $L=\{n\}$.


Find the sum of all creative integers less than or equal to $10^{12}$.
##Творческие числа

Алиса играет в игру. Она начинает со списка целых чисел $L$ и на каждом шаге она может:

или убрать из списка $L$ два элемента $a$ и $b$ и добавить $a^b$ в $L$,
или, наоборот, убрать из $L$ элемент $c$, который может быть записан как $a^b$, где $a$ и $b$ - два целых числа, таких что $a, b > 1$, и добавить в $L$ оба числа $a$ и $b$.

Например, начиная со списка $L=\{8\}$, Алиса может убрать $8$ и добавить $2$ и $3$, получив первым шагом список $L=\{2,3\}$. Далее, вторым шагом она может получить $L=\{9\}$.
Заметим, что одинаковые целые числа могут оказаться в списке больше одного раза.
Целое число $n>1$ называется творческим, если для любого целого $m>1$ Алиса может получить список, содержащий $m$ и начинающийся с $L=\{n\}$.
Найдите сумму всех творческих чисел не больше $10^{12}$.
