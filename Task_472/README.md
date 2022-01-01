##Comfortable Distance II

There are N seats in a row. N people come one after another to fill the seats according to the following rules:

Note that due to rule 1, some seats will surely be left unoccupied, and the maximum number of people that can be seated is less than N (for N > 1).
Here are the possible seating arrangements for N = 15:


We see that if the first person chooses correctly, the 15 seats can seat up to 7 people.
We can also see that the first person has 9 choices to maximize the number of people that may be seated.
Let f(N) be the number of choices the first person has to maximize the number of occupants for N seats in a row. Thus, f(1) = 1, f(15) = 9, f(20) = 6, and f(500) = 16.
Also, ∑ f(N) = 83 for 1 ≤ N ≤ 20 and  ∑ f(N) = 13343 for 1 ≤ N ≤ 500.
Find ∑ f(N) for 1 ≤ N ≤ 1012. Give the last 8 digits of your answer.
##Комфортное расстояние 2

N сидений расположено в ряд. N человек приходят один за другим и занимают места в соответствии со следующими правилами:


Никто не садится рядом с кем-то другим.
Первый человек выбирает любое сидение.
Каждый следующий человек выбирает дальнейшее сидение от всех уже сидящих, в то же время не нарушая правило номер 1. Если есть несколько возможностей, удовлетворяющих этому условию, человек выбирает сидение, расположенное левее всего.


Заметим, что из-за первого правила обязательно останутся незанятые сиденья, а максимальное число рассевшихся человек будет меньше N (для N > 1).
Вот несколько возможных размещений сидящих для N = 15:


Мы видим, что в зависимости от выбора первого человека 15 сидений могут разместить до 7 человек.
Также мы видим, что у первого человека есть 9 возможностей привести число рассаженных людей к максимальному значению.
Пусть f(N) будет количеством выбранных первым человеком сидений, которые приведут к максимальному количеству сидящих людей в ряду из N сидений. Таким образом, f(1) = 1, f(15) = 9, f(20) = 6 и f(500) = 16.
Также, ∑f(N) = 83 для 1 ≤ N ≤ 20 и ∑f(N) = 13343 для 1 ≤ N ≤ 500.
Найдите ∑f(N) для 1 ≤ N ≤ 1012. В качестве ответа приведите последние 8 цифр полученного числа.
