##Beds and Desks

At Euler University, each of the $n$ students (numbered from 1 to $n$) occupies a bed in the dormitory and uses a desk in the classroom.
Some of the beds are in private rooms which a student occupies alone, while the others are in double rooms occupied by two students as roommates. Similarly, each desk is either a single desk for the sole use of one student, or a twin desk at which two students sit together as desk partners.
We represent the bed and desk sharing arrangements each by a list of pairs of student numbers. For example, with $n=4$, if $(2,3)$ represents the bed pairing and $(1,3)(2,4)$ the desk pairing, then students 2 and 3 are roommates while 1 and 4 have single rooms, and students 1 and 3 are desk partners, as are students 2 and 4.
The new chancellor of the university decides to change the organisation of beds and desks: a permutation $\sigma$ of the numbers $1,2,\ldots,n$ will be chosen, and each student $k$ will be given both the bed and the desk formerly occupied by student number $\sigma(k)$.
The students agree to this change, under the conditions that:
In the example above, there are only two ways to satisfy these conditions: either take no action ($\sigma$ is the identity permutation), or reverse the order of the students.
With $n=6$, for the bed pairing $(1,2)(3,4)(5,6)$ and the desk pairing $(3,6)(4,5)$, there are 8 permutations which satisfy the conditions. One example is the mapping $(1, 2, 3, 4, 5, 6) \mapsto (1, 2, 5, 6, 3, 4)$.
With $n=36$, if we have bed pairing:
$(2,13)(4,30)(5,27)(6,16)(10,18)(12,35)(14,19)(15,20)(17,26)(21,32)(22,33)(24,34)(25,28)$
and desk pairing
$(1,35)(2,22)(3,36)(4,28)(5,25)(7,18)(9,23)(13,19)(14,33)(15,34)(20,24)(26,29)(27,30)$
then among the $36!$ possible permutations (including the identity permutation), 663552 of them satisfy the conditions stipulated by the students.
The downloadable text files beds.txt and desks.txt contain pairings for $n=500$. Each pairing is written on its own line, with the student numbers of the two roommates (or desk partners) separated with a comma. For example, the desk pairing in the $n=4$ example above would be represented in this file format as:
With these pairings, find the number of permutations that satisfy the students' conditions. Give your answer modulo $999\,999\,937$.
##Кровати и столы

В университете Эйлера каждый из $n$ студентов (пронумерованных от 1 до $n$) занимает одну кровать в общежитии и использует один стол в классе.
Некоторые кровати находятся в одиночных комнатах, где живет только один студент, а остальные кровати - в комнатах, где живут двое. Похожим образом, за каждым столом работает или один, или двое студентов.
Представим распределение совместного использования кроватей и столов в виде двух списков, содержащих пары номеров студентов. Например, при $n=4$, если $(2,3)$ обозначает сдвоенное расположение кроватей, а $(1,3)(2,4)$ - совместное использование столов, то студенты 2 и 3 являются соседями по комнате, в то время как студенты 1 и 4 живут в одиночных комнатах, и студенты 1 и 3 работают за одним столом, равно как и студенты 2 и 4.
Новый ректор университета решил изменить распределение кроватей и столов: он выберет перестановку $\sigma$  для чисел $1,2,\ldots,n$ и каждый студент номер $k$ получит кровать и стол, которые раньше занимал студент номер $\sigma(k)$.
Студенты согласились с этими изменениями при условии, что:
Любые два студента, ранее жившие в одной комнате, останутся соседями по комнате.
Любые два студента, ранее работавшие за одним столом, останутся работать за одним столом.
В примере выше существует только два способа удовлетворить эти условия: или ничего не менять ($\sigma$ является тождественной перестановкой), или же поменять порядок номеров студентов на обратный.
При $n=6$ для распределения кроватей $(1,2)(3,4)(5,6)$ и распределения столов $(3,6)(4,5)$ существует 8 перестановок, которые удовлетворяют требованиям студентов. Одним из примеров является отображение $(1, 2, 3, 4, 5, 6) \mapsto (1, 2, 5, 6, 3, 4)$.
При $n=36$, если дано распределение кроватей:
$(2,13)(4,30)(5,27)(6,16)(10,18)(12,35)(14,19)(15,20)(17,26)(21,32)(22,33)(24,34)(25,28)$
и распределение столов:
$(1,35)(2,22)(3,36)(4,28)(5,25)(7,18)(9,23)(13,19)(14,33)(15,34)(20,24)(26,29)(27,30)$,
тогда из $36!$ возможных перестановок (включая тождественные) всего 663552 перестановки удовлетворят требованиям, выдвинутым студентами.
Доступные для скачивания файлы beds.txt и desks.txt содержат распределения кроватей и столов для $n=500$. Каждая пара записана в отдельной строке, номера студентов в паре разделены запятой. Например, распределение столов для примера выше с $n=4$ выглядело бы в таком формате следующим образом:

1,3
2,4

При данных в файлах распределениях найдите количество перестановок, которые удовлетворяют требованиям студентов. В качестве ответа приведите остаток от деления полученного числа на $999\,999\,937$.
Оригинал
