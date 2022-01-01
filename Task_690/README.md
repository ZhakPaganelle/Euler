##Tom and Jerry


Tom (the cat) and Jerry (the mouse) are playing on a simple graph $G$.


Every vertex of $G$ is a mousehole, and every edge of $G$ is a tunnel connecting two mouseholes.


Originally, Jerry is hiding in one of the mouseholes.
Every morning, Tom can check one (and only one) of the mouseholes. If Jerry happens to be hiding there then Tom catches Jerry and the game is over.
Every evening, if the game continues, Jerry moves to a mousehole which is adjacent (i.e. connected by a tunnel, if there is one available) to his current hiding place. The next morning Tom checks again and the game continues like this.


Let us call a graph $G$ a Tom graph, if our super-smart Tom, who knows the configuration of the graph but does not know the location of Jerry, can guarantee to catch Jerry in finitely many days.
For example consider all graphs on 3 nodes:


For graphs 1 and 2, Tom will catch Jerry in at most three days. For graph 3 Tom can check the middle connection on two consecutive days and hence guarantee to catch Jerry in at most two days. These three graphs are therefore Tom Graphs. However, graph 4 is not a Tom Graph because the game could potentially continue forever.


Let $T(n)$ be the number of different Tom graphs with $n$ vertices. Two graphs are considered the same if there is a bijection $f$ between their vertices, such that $(v,w)$ is an edge if and only if $(f(v),f(w))$ is an edge.


We have $T(3) = 3$, $T(7) = 37$, $T(10) = 328$ and $T(20) = 1416269$.


Find $T(2019)$ giving your answer modulo $1\,000\,000\,007$.

##Том и Джерри


Том (кот) и Джерри (мышь) играют на неориентированном графе $G$.


Каждая вершина графа $G$ - это мышиная нора, а каждое ребро графа $G$ - туннель, соединяющий две мышиные норы.


Изначально Джерри прячется в одной из нор.
Каждое утро Том может проверить одну и только одну из нор. Если окажется, что в ней прячется Джерри, Том ловит Джерри и игра завершается.
Каждый вечер, если игра еще продолжается, Джерри перемещается в соседнюю нору (т.е. соединенную туннелем с норой, где он прятался), если есть такая возможность. На следующее утро Том снова проверяет, и игра таким образом продолжается.


Назовем граф $G$ графом Тома, если наш супер-умный Том, который знает конфигурацию графа, но не знает местоположение Джерри, может гаранитровать, что поймает Джерри за конечное число дней.
Например, рассмотрим все графы с 3 вершинами:





В случае графов №1 и №2 Том поймает Джерри не больше, чем за 3 дня. В случае графа №3 Том может два дня подряд проверять среднюю вершину и гарантированно поймать Джерри в пределах 2 дней. Таким образом, эти три графа являются графами Тома. Однако, граф №4 таковым не является, так как игра может потенциально продолжаться бесконечно.


Пусть $T(n)$ будет количеством различных графов Тома с $n$ вершинами. Два графа считаются одинаковыми, если существует такая биекция $f$ между их вершинами, что $(v,w)$ является ребром тогда и только тогда, когда $(f(v),f(w))$ является ребром.


Известно, что $T(3) = 3$, $T(7) = 37$, $T(10) = 328$ и $T(20) = 1416269$.


Найдите $T(2019)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
