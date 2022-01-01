##Circular Logic

A k-input binary truth table is a map from k input bits
(binary digits, 0 [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth tables for the logical AND and XOR functions are:
How many 6-input binary truth tables, τ, satisfy the formula
for all 6-bit inputs (a, b, c, d, e, f)?

##Круговая логика

 Таблица истинности логики с k-входами - это порядок присвоения одного выходного бита k входным битам (двоичным цифрам, 0 [false] или 1 [true]). К примеру, так выглядят двоичные 2-входовые таблицы истинности для операций логического И (AND), а также исключающего ИЛИ (XOR):



x
y
x AND y
000
010
100
111



x
y
x XOR y
000
011
101
110


Сколько 6-входовых двоичных таблиц истинности τ удовлетворят следующей формуле

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

для всех возможных 6-разрядных входов (a, b, c, d, e, f)?

