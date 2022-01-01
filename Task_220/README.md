##Heighway Dragon

Let D0 be the two-letter string "Fa".  For n≥1, derive Dn from Dn-1 by the string-rewriting rules:
"a" → "aRbFR"
"b" → "LFaLb"
Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.
These strings can be interpreted as instructions to a computer graphics program, with "F" meaning "draw forward one unit", "L" meaning "turn left 90 degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being ignored.  The initial position of the computer cursor is (0,0), pointing up towards (0,1).
Then Dn is an exotic drawing known as the Heighway Dragon of order n.  For example, D10 is shown below; counting each "F" as one step, the highlighted spot at (18,16) is the position reached after 500 steps.
What is the position of the cursor after 1012 steps in D50 ?
Give your answer in the form x,y with no spaces.
##Дракон Хейтуэя

Пусть D0 будет двухбуквенной строкой "Fa". Для n≥1, Dn образуется из Dn-1 путем следующих правил переписывания строк:
"a" → "aRbFR"
"b" → "LFaLb"
Таким образом, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", и так далее.
Эти строки могут быть истолкованы как инструкции для программы компьютерной графики так, что "F" значит "рисовать на одну единицу вперед", "L" значит "повернуть налево на 90 градусов", "R" значит "повернуть направо на 90 градусов", а "a" и "b" игнорируются. Начальное положение компьютерного курсора (0,0), направление - наверх, на (0,1).
Тогда Dn становится необычным рисунком, известным как дракон Хейтуэя порядка n. Например, D10 показан ниже; считая каждое "F" как один шаг, выделенная точка на (18,16) является положением, достигнутым в 500 шагов.


Каким будет положение курсора после 1012 шагов в D50 ?
Дайте ответ в виде x,y без пробелов.
