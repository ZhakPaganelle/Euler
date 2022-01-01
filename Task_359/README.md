##Hilbert's New Hotel


An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get a room at Hilbert's newest infinite hotel. The hotel contains an infinite number of floors (numbered 1, 2, 3, etc.), and each floor contains an infinite number of rooms (numbered 1, 2, 3, etc.). 


Initially the hotel is empty. Hilbert declares a rule on how the nth person is assigned a room: person n gets the first vacant room in the lowest numbered floor satisfying either of the following:


Person 1 gets room 1 in floor 1 since floor 1 is empty.
Person 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect square.
Person 2 instead gets room 1 in floor 2 since floor 2 is empty.
Person 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.


Eventually, every person in the line gets a room in the hotel.


Define P(f, r) to be n if person n occupies room r in floor f, and 0 if no person occupies the room. Here are a few examples:
P(1, 1) = 1
P(1, 2) = 3
P(2, 1) = 2
P(10, 20) = 440
P(25, 75) = 4863
P(99, 100) = 19454


Find the sum of all P(f, r) for all positive f and r such that f × r = 71328803586048 and give the last 8 digits as your answer.

##Новый отель Гилберта


Бесконечное число людей (пронумерованных 1, 2, 3, и т.д.) стоят в очереди за комнатой в новейшем бесконечном отеле Гилберта. В отеле бесконечное количество этажей (пронумерованных 1, 2, 3, и т.д.), и каждый этаж содержит бесконечное число комнат (пронумерованных 1, 2, 3, и т.д.).


Изначально отель пуст. Гилберт объявляет правило, по которому n-тый человек получает комнату: человек n получает первую свободную комнату на самом низком этаже, отвечающем хотя бы одному из следуюших условий:


этаж пуст


этаж не пуст и, если последний занявший на нем комнату человек имеет номер m, то m + n является квадратом целого числа



Человек 1 получает комнату 1 на этаже 1, так как он пуст.

Человек 2 не получает комнату 2 на этаже 1, так как 1 + 2 = 3 не является квадратом целого числа.

Вместо этого, человек 2 получает комнату 1 на этаже 2, так как он пуст.

Человек 3 получает комнату 2 на этаже 1, так как 1 + 3 = 4 является квадратом целого числа.


Рано или поздно, каждый человек в очереди получит свою комнату в отеле.


Пусть P(f, r) будет равно n, если человек n занял комнату r на этаже f, и равно 0, если никто не занял эту комнату. Вот несколько примеров:

P(1, 1) = 1

P(1, 2) = 3

P(2, 1) = 2

P(10, 20) = 440

P(25, 75) = 4863

P(99, 100) = 19454


Найдите сумму всех P(f, r) для всех натуральных f и r таких, что f 
×
 r = 71328803586048, и в качестве ответа приведите последние 8 цифр полученного результата.

