##Poohsticks Marathon


Christopher Robin and Pooh Bear love the game of Poohsticks so much that they invented a new version which allows them to play for longer before one of them wins and they have to go home for tea. The game starts as normal with both dropping a stick simultaneously on the upstream side of a bridge. But rather than the game ending when one of the sticks emerges on the downstream side, instead they fish their sticks out of the water, and drop them back in again on the upstream side. The game only ends when one of the sticks emerges from under the bridge ahead of the other one having also 'lapped' the other stick - that is, having made one additional journey under the bridge compared to the other stick.


On a particular day when playing this game, the time taken for a stick to travel under the bridge varies between a minimum of 30 seconds, and a maximum of 60 seconds. The time taken to fish a stick out of the water and drop it back in again on the other side is 5 seconds. The current under the bridge has the unusual property that the sticks' journey time is always an integral number of seconds, and it is equally likely to emerge at any of the possible times between 30 and 60 seconds (inclusive). It turns out that under these circumstances, the expected time for playing a single game is 1036.15 seconds (rounded to 2 decimal places). This time is measured from the point of dropping the sticks for the first time, to the point where the winning stick emerges from under the bridge having lapped the other.


The stream flows at different rates each day, but maintains the property that the journey time in seconds is equally distributed amongst the integers from a minimum, $n$, to a maximum, $m$, inclusive. Let the expected time of play in seconds be $E(m,n)$. Hence $E(60,30)=1036.15...$


Let $S(k)=\sum_{m=2}^k\sum_{n=1}^{m-1}E(m,n)$.


For example $S(5)=7722.82$ rounded to 2 decimal places.


Find $S(100)$ and give your answer rounded to 2 decimal places.

##Чемпионат по пустякам


Кристофер Робин и Винни-Пух так полюбили игру в пустяки, что изобрели ее новую версию, в которую они могут играть дольше, пока один из них не выиграет и они не пойдут домой пить чай. Эта игра начинается, как обычно, с того, что оба одновременно бросают палочки в воду с одной стороны моста. Однако, вместо того, чтобы закончить игру, когда одна из палочек появится с другой стороны моста, они вылавливают свои палочки и снова бросают их. Игра заканчивается только тогда, когда одна из палочек появляется с другой стороны моста быстрее другой, при том "обогнав ее на один круг" - то есть, сделав на один заплыв под мостом больше, чем другая.


Однажды, когда они играли в эту игру, время, которое палочка затрачивала на проплывание под мостом, было между 30 и 60 секундами. Выуживание палочки и бросание ее снова в воду занимало 5 секунд. Течение под мостом имело необычное свойство, заключавшееся в том, что время заплыва палочки всегда было целым числом секунд и палочка имела одинаковую вероятность показаться с другой стороны моста через от 30 до 60 секунд (включительно). Оказалось, что при таких обстоятельствах ожидаемая продолжительность одной игры была 1036.15 секунд (округленная до 2 знака после десятичной точки). Это - время, замеренное с момента первого бросания обеих палочек до момента, когда победившая палочка показалась из-под моста, обогнав другую на один круг.


Каждый день скорость течения меняется, но оно сохраняет свойство, заключающееся в том, что время заплыва палочки равномерно распределено между минимумом $n$ секунд и максимумом $m$ секунд (включительно). Пусть ожидаемая продолжительность игры будет $E(m,n)$. Таким образом, $E(60,30)=1036.15...$


Пусть $S(k)=\sum_{m=2}^k\sum_{n=1}^{m-1}E(m,n)$.


Например, $S(5)=7722.82$, округленное до 2 знака после десятичной точки.


Найдите $S(100)$ и дайте ваш ответ округленным до 2 знака после десятичной точки.

