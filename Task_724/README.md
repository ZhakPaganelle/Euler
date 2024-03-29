##Drone Delivery

A depot uses $n$ drones to disperse packages containing essential supplies along a long straight road.
Initially all drones are stationary, loaded with a supply package.
Every second, the depot selects a drone at random and sends it this instruction:
The road is wide enough that drones can overtake one another without risk of collision.
Eventually, there will only be one drone left at the depot waiting to receive its first instruction. As soon as that drone has flown one centimetre along the road, all drones drop their packages and return to the depot.
Let $E(n)$ be the expected distance in centimetres from the depot that the supply packages land.
For example, $E(2) = \frac{7}{2}$, $E(5) = \frac{12019}{720}$, and $E(100) \approx 1427.193470$.
Find $E(10^8)$. Give your answer rounded to the nearest integer.
##Доставка дроном

Склад использует $n$ дронов для доставки посылок с предметами первой необходимости вдоль длинной прямой дороги.
Изначально каждый дрон нагружен посылкой и неподвижен.
Каждую секунду склад случайно выбирает дрона и отправляет ему следующую инструкцию:

Если ты неподвижен - начни двигаться вдоль дороги со скоростью 1 см/сек.
Если ты в движении - увеличь свою скорость на 1 см/сек вдоль дороги, не меняя направление движения.

Дорога достаточно широка, чтобы дроны могли обгонять друг друга, не рискуя столкнуться.
В конце концов, на складе останется только один дрон, еще не получивший свою первую инструкцию. Как только этот дрон пролетит 1 см вдоль дороги, все дроны сбрасывают свой груз и возвращаются на склад.
Пусть $E(n)$ будет ожидаемым расстоянием от склада, на котором приземляются посылки.
Например, $E(2) = \frac{7}{2}$, $E(5) = \frac{12019}{720}$ и $E(100) \approx 1427.193470$.
Найдите $E(10^8)$. Приведите ответ округленным до ближайшего целого числа. Оригинал
