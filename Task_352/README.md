##Blood tests


Each one of the 25 sheep in a flock must be tested for a rare virus, known to affect 2% of the sheep population.
An accurate and extremely sensitive PCR test exists for blood samples, producing a clear positive / negative result, but it is very time-consuming and expensive.


Because of the high cost, the vet-in-charge suggests that instead of performing 25 separate tests, the following procedure can be used instead:
The sheep are split into 5 groups of 5 sheep in each group. 
For each group, the 5 samples are mixed together and a single test is performed. Then,


Since the probability of infection for any specific animal is only 0.02, the first test (on the pooled samples) for each group will be:


Thus, the expected number of tests for each group is 1 + 0.0960792032 × 5 = 1.480396016.
Consequently, all 5 groups can be screened using an average of only 1.480396016 × 5 = 7.40198008 tests, which represents a huge saving of more than 70% !


Although the scheme we have just described seems to be very efficient, it can still be improved considerably (always assuming that the test is sufficiently sensitive and that there are no adverse effects caused by mixing different samples). E.g.:


To simplify the very wide range of possibilities, there is one restriction we place when devising the most cost-efficient testing scheme: whenever we start with a mixed sample, all the sheep contributing to that sample must be fully screened (i.e. a verdict of infected / virus-free must be reached for all of them) before we start examining any other animals.


Using the optimal strategy, let T(s,p) represent the average number of tests needed to screen a flock of s sheep for a virus having probability p to be present in any individual.
Thus, rounded to six decimal places, T(25, 0.02) = 4.155452 and T(25, 0.10) = 12.702124.


Find ∑ T(10000, p) for p=0.01, 0.02, 0.03, ... 0.50.
Give your answer rounded to six decimal places.

##Тесты крови


Каждую 25-ю овцу из стада необходимо проверить на редкий вирус, который поражает 2% популяции овец. Существует точный и высокочувствительный ПЦР тест образцов крови, который дает однозначный положительный/отрицательный результат, но он дорогой и очень затратный по времени.


Из-за высокой цены, главный ветеринар предлагает вместо 25 отдельных тестов проводить следующую процедуру: Овец распределяют на 5 груп по 5 овец в каждой. 5 образцов крови каждой овцы из группы смешиваются вместе, после чего проводится один тест. Тогда,

Если результат отрицательный, то все овцы в этой группе считаются здоровыми.
Если результат положительный, проводится 5 дополнительных тестов. Отдельный тест для образца крови каждого животного, чтобы определить зараженных особей.


Поскольку вероятность заражения каждого отдельно взятого животного составляет всего 0.02, то первый тест (объединенных образцов) для каждой группы будет:

Отрицательным (и больше тестов не потребуется) с вероятностью 0.985 = 0.9039207968.
Положительным (потребуется 5 дополнительных тестов) с вероятностью 1 - 0.9039207968 = 0.0960792032.


Таким образом, ожидаемое количество тестов для каждой группы составвит 1 + 0.0960792032 × 5 = 1.480396016.
Следовательно, все 5 групп можно просеять со средним количеством тестов 1.480396016 × 5 = 7.40198008, что дает огромный выигрыш, более чем 70% !


Хотя описанная выше процедура выглядит очень эффективной, ее можно существенно улучшить (всегда предполагается, что тест достаточно чувствителен и что нет никаких побочных эффектов при смешивании образцов крови). К примеру:


Можно начать с теста смеси всех 25 образцов крови. Можно убедиться, что примерно в 60.35% случаев тест будет отрицательным и дополнительные тесты не потребуются. Более подробное тестирование потребуется лишь в оставшихся 39.65% случаев.
Если известно, что по крайней мере одно из животных в группе из 5 особей инфицировано, и что первые 4 индивидуальных теста дадут отрицательный результат, то совершенно не требуется проводить тест для пятого животного (очевидно, что именно оно и будет инфицировано).
Можно попробовать изменить количество групп / количество особей в группе, меняя эти числа на каждом уровне так, чтобы общее число проведенных тестов было минимальным.


Чтобы упростить очень широкий ряд возможностей, введем ограничение на получение наиболее эффективной по затратам схемы тестирования: когда мы протестируем смешанный образец, необходимо полностью разделить всех овец, чьи образцы крови участвовали в тестировании (т.е. получить результат для каждого животного из группы - инфицированно оно или нет), прежде чем можно будет проводить тестирование остальных групп животных.


В данном примере оказывается, что наиболее эффективная по затратам методика тестирования (будем называть ее оптимальной стратегией) потребует в среднем всего лишь 4.155452 тестов!


Для такой оптимальной стратегии определим T(s,p) как среднее количество тестов, необходимое для отсеивания больных животных в стаде из s овец, при вероятности заболевания каждой особи p.
Таким образом, округлив результат до шестого знака после десятичной точки, T(25,0.02) = 4.155452 и T(25,0.10) = 12.702124.


Найдите ΣT(10000,p) для всех p=0.01, 0.02, 0.03, ... 0.50.
Ответ округлите до шестого знака после десятичной точки.

