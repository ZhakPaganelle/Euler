##Open chess positions


A position in chess is an (orientated) arrangement of chess pieces placed on a chessboard of given size. In the following, we consider all positions in which $n$ pawns are placed on a  $n \times n$  
board in such a way, that there is a single pawn in every row and every column.



We call such a position an open position, if a rook, starting at the (empty) lower left corner and using only moves towards the right or upwards, can reach the upper right corner without moving onto any field occupied by a pawn. 

Let $f(n)$ be the number of open positions for a $n \times n$ chessboard.
For example, $f(3)=2$, illustrated by the two open positions for a $3  \times 3$ chessboard below.



You are also given $f(5)=70$.
Find $f(10^8)$ modulo $1\,008\,691\,207$.
##Открытые шахматные позиции

Шахматная позиция - это направленное расположение шахматных фигур на шахматной доске определенного размера. В этой задаче рассмотрим все позиции, в которых $n$ пешек расставлены на доске $n \times n$ таким образом, что в каждом ряду и столбце доски находится всего одна пешка.
Назовем такую позицию открытой, если ладья, помещенная в пустом нижнем левом углу доски, может попасть в правый верхний угол доски, используя ходы только в направлениях вверх и направо.
Пусть $f(n)$ будет количеством открытых позиций на шахматной доске $n \times n$.
Например, $f(3)=2$, что показано двумя открытыми позициями на доске $3 \times 3$ ниже.





Вам также дано, что $f(5)=70$.
Найдите остаток от деления $f(10^8)$ на $1\,008\,691\,207$.
