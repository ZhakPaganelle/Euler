##Grid Graphs


Consider a directed graph made from an orthogonal lattice of $H\times W$ nodes. 
The edges are the horizontal and vertical connections between adjacent nodes.
$W$ vertical directed lines are drawn and all the edges on these lines inherit that direction. Similarly, $H$ horizontal directed lines are drawn and all the edges on these lines inherit that direction.


Two nodes, $A$ and $B$ in a directed graph, are strongly connected if there is both a path, along the directed edges, from $A$ to $B$ as well as from $B$ to $A$. Note that every node is strongly connected to itself.


A strongly connected component in a directed graph is a non-empty set $M$ of nodes satisfying the following two properties:


There are $2^H\times 2^W$ ways of drawing the directed lines. Each way gives a directed graph $\mathcal{G}$. We define $S(\mathcal{G})$ to be the number of strongly connected components in $\mathcal{G}$.


The illustration below shows a directed graph with $H=3$ and $W=4$ that consists of four different strongly connected components (indicated by the different colours).


Define $C(H,W)$ to be the sum of $S(\mathcal{G})$ for all possible graphs on a grid of $H\times W$. You are given $C(3,3) = 408$, $C(3,6) = 4696$ and $C(10,20) \equiv 988971143 \pmod{1\,000\,000\,007}$.


Find $C(10\,000,20\,000)$ giving your answer modulo $1\,000\,000\,007$.

##Графы решеток


Рассмотрим ориентированный граф, построенный на ортогональной решетке с $H\times W$ вершинами. Ребрами графа являются горизонтальные и вертикальные отрезки, соединяющие соседние вершины. Далее, проводятся $W$ вертикальных направленных линий и все ребра на этих линиях наследуют их направление. Таким же образом проводятся $H$ горизонтальных направленных линий, и все ребра на этих линиях наследуют их направление.


Две вершины ориентированного графа $A$ и $B$ являются сильно соединенными, если одновременно существуют следующие два пути вдоль направленных ребер: из $A$ в $B$ и из $B$ в $A$. Заметим, что каждая вершина сильно соединена сама с собой.


Сильно соединенным компонентом в ориентированном графе называется непустое множество $M$, содержащее вершины, удовлетворяющие следующим двум условиям:


Все вершины во множестве $M$ сильно соединены друг с другом.
$M$ максимально, иными словами, ни одна вершина в $M$ не соединена сильно ни с одной вершиной вне $M$.


Существует $2^H\times 2^W$ способов провести направленные линии. Каждый способ дает ориентированный граф $\mathcal{G}$. Определим $S(\mathcal{G})$ как количество сильно соединенных компонентов $\mathcal{G}$.


Изображение ниже показывает ориентированный граф с $H=3$ и $W=4$, состоящий из четырех различных сильно соединенных компонентов (обозначенных разными цветами).




Определим $C(H,W)$ как сумму $S(\mathcal{G})$ для всех возможных графов на решетке $H\times W$. Известно, что $C(3,3) = 408$, $C(3,6) = 4696$ и $C(10,20) \equiv 988971143 \pmod{1\,000\,000\,007}$.


Найдите $C(10\,000,20\,000)$. В качестве ответа приведите остаток от деления полученного результата на  $1\,000\,000\,007$.
 Оригинал
