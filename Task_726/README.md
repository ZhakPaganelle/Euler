##Falling bottles


Consider a stack of bottles of wine. There are $n$ layers in the stack with the top layer containing only one bottle and the bottom layer containing $n$ bottles. For $n=4$ the stack looks like the picture below.


The collapsing process happens every time a bottle is taken. A space is created in the stack and that space is filled according to the following recursive steps:


This process happens recursively; for example, taking bottle $A$ in the diagram above. Its place can be filled with either $B$ or $C$. If it is filled with $C$ then the space that $C$ creates can be filled with $D$ or $E$. So there are 3 different collapsing processes that can happen if $A$ is taken, although the final shape (in this case) is the same.


Define $f(n)$ to be the number of ways that we can take all the bottles from a stack with $n$ layers. 
Two ways are considered different if at any step we took a different bottle or the collapsing process went differently.


You are given $f(1) = 1$, $f(2) = 6$ and $f(3) = 1008$.


Find $S(10^4)$ and give your answer modulo $1\,000\,000\,033$.

##Падающие бутылки


Рассмотрим стопку бутылок вина. В стопке $n$ слоев, верхний слой состоит из одной бутылки, нижний - из $n$ бутылок. При $n=4$ стопка будет выглядеть как на изображении ниже:




Обвал бутылок просиходит каждый раз, когда из стопки вынимают бутылку. В стопке образуется пустое пространство, которое заполняется в соответствии со следующими рекурсивными шагами:

Если сверху нет ни одной бутылки: ничего не происходит. Например, если вынуть бутылку $F$.
Если сверху касается одна бутылка: она упадет и займет пустое место, создав новое пустое место на слой выше. Например, если вынуть бутылку $D$.
Если сверху касаются две бутылки: одна из них упадет и займет пустое место, создав новое пустое место на слой выше. Например, если вынуть бутылку $C$.


Этот процесс происходит рекурсивно. Например, при вынимании бутылки $A$ на схеме выше, на ее место упадет или $B$, или $C$. Если туда упадет $C$, ее освободившееся место может занять $D$ или $E$. Итого может произойти 3 разных процесса обвала, если вынуть бутылку $A$, но в этом примере финальная форма стопки всегда будет одинаковой.


Определим $f(n)$ как количество способов, которыми можно вынуть все бутылки из стопки в $n$ слоев. Два способа считаются различными, если в какой-то из шагов была вынута другая бутылка или обвал произошел иначе.


Известно, что $f(1) = 1$, $f(2) = 6$ и $f(3) = 1008$.

Также определим

$\displaystyle	S(n) = \sum_{k=1}^n f(k)$

Найдите $S(10^4)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,033$.

Оригинал
