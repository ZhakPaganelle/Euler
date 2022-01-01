##Kakuro

The above is an example of a cryptic kakuro (also known as cross sums, or even sums cross) puzzle, with its final solution on the right. (The common rules of kakuro puzzles can be found easily on numerous internet sites. Other related information can also be currently found at krazydad.com whose author has provided the puzzle data for this challenge.)
The downloadable text file (kakuro200.txt) contains the description of 200 such puzzles, a mix of 5x5 and 6x6 types. The first puzzle in the file is the above example which is coded as follows:
6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X
The first character is a numerical digit indicating the size of the information grid. It would be either a 6 (for a 5x5 kakuro puzzle) or a 7 (for a 6x6 puzzle) followed by a comma (,). The extra top line and left column are needed to insert information.
The content of each cell is then described and followed by a comma, going left to right and starting with the top line.
X = Gray cell, not required to be filled by a digit.
O (upper case letter)= White empty cell to be filled by a digit.
A = Or any one of the upper case letters from A to J to be replaced by its equivalent digit in the solved puzzle.
( ) = Location of the encrypted sums. Horizontal sums are preceded by a lower case "h" and vertical sums are preceded by a lower case "v". Those are followed by one or two upper case letters depending if the sum is a single digit or double digit one. For double digit sums, the first letter would be for the "tens" and the second one for the "units". When the cell must contain information for both a horizontal and a vertical sum, the first one is always for the horizontal sum and the two are separated by a comma within the same set of brackets, ex.: (hFE,vD). Each set of brackets is also immediately followed by a comma.
The description of the last cell is followed by a Carriage Return/Line Feed (CRLF) instead of a comma.
The required answer to each puzzle is based on the value of each letter necessary to arrive at the solution and according to the alphabetical order. As indicated under the example puzzle, its answer would be 8426039571. At least 9 out of the 10 encrypting letters are always part of the problem description. When only 9 are given, the missing one must be assigned the remaining digit.
You are given that the sum of the answers for the first 10 puzzles in the file is 64414157580.
Find the sum of the answers for the 200 puzzles.
##Какуро





Выше приведен пример головоломки какуро с шифром (cryptic kakuro), также известной как "пересекающиеся суммы", чье конечное решение показано справа. (Общие правила головоломок какуро можно легко найти на многих сайтах в Интернете. Необходимую информацию можно найти на krazydad.com, чей автор предоставил данные для головоломок в этой задаче.)


Загружаемый текстовый файл (kakuro200.txt) содержит описания 200 таких головоломок, с размерами поля 5х5 или 6х6. Первая головоломка в файле приведена выше в качестве примера и записана следуюшим образом:


6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X


Первый символ - число, показывающее размер поля головоломки. Оно может быть или 6 (для головоломки 5x5), или 7 (для головоломки 6x6), за которым следует запятая (,). Дополнительные ряд сверху и колонка слева необходимы для хранения информации.


Далее, отделяемое запятыми, описывается содержимое каждой ячейки, начиная с верхнего ряда и двигаясь слева направо.
X = Серая ячейка, не должна быть заполнена.
O (заглавная буква латинского алфавита) = Белая пустая ячейка, которая должна быть заполнена цифрой.
A (или любая заглавная буква латинского алфавита от A до J) = Должна быть заменена соответствующей отгаданному шифру цифрой.
( ) = Положение зашифрованных сумм. Перед горизонтальными суммами стоит прописная буква "h", а перед вертикальными - прописная буква "v". За этой буквой следует одна или две заглавные буквы, в зависимости от того, является ли сумма однозначным или двузначным числом. Для двузначных сумм первая буква соответствует разряду десятков, а вторая - разряду единиц. Если в одной ячейке содержится информация как о горизонтальной, так и о вертикальной сумме, первой всегда указывается горизонтальная сумма, и эти суммы разделеяются запятой внутри скобок, например: (hFE,vD). После каждой пары скобок следует запятая.


После описания последней ячейки вместо запятой следует символ "Возврат каретки/Подача строки" (CRLF).


Ответом для каждой головоломки является ключ к шифру - приведенные в алфавитном порядке цифровые значения каждой буквы, при которых головоломка какуро решается. Как показано под примером головоломки, ответом на нее является 8426039571. Как минимум 9 из 10 букв шифра всегда являются частью описания головоломки. Если даны только 9, то десятой букве назначается оставшаяся неиспользованной цифра.


Известно, что сумма ответов на первые 10 головоломок в файле равна 64414157580.


Найдите сумму ответов на все 200 головоломок.

