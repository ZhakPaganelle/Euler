##Risky moon


A moon could be described by the sphere $C(r)$ with centre $(0,0,0)$ and radius $r$. 


There are stations on the moon at the points on the surface of $C(r)$ with integer coordinates. The station at $(0,0,r)$ is called North Pole station, the station at $(0,0,-r)$ is called South Pole station.


All stations are connected with each other via the shortest road on the great arc through the stations. A journey between two stations is risky. If d is the length of the road between two stations, $\left(\frac{d}{\pi r}\right)^2$ is a measure for the risk of the journey (let us call it the risk of the road). If the journey includes more than two stations, the risk of the journey is the sum of risks of the used roads.


A direct journey from  the North Pole station to the South Pole station has the length $\pi r$ and risk 1. The journey from the North Pole station to the South Pole station via $(0,r,0)$ has the same length, but a smaller risk:

The minimal risk of a journey from the North Pole station to the South Pole station on $C(r)$ is $M(r)$.


You are given that $M(7)=0.1784943998$  rounded to 10 digits behind the decimal point. 


Find $\displaystyle{\sum_{n=1}^{15}M(2^n-1)}$.


Give your answer rounded to 10 digits behind the decimal point in the form a.bcdefghijk.

##Луна с риском


Луну можно описать сферой C(r) с центром в точке с координатами (0,0,0) и радиусом r.


Предположим, что на поверхности луны C(r) расположены две станции с цело-численными координатами. Станцию в точке с координатами (0,0,r) назовем станцией Северного Полюса, а станцию в точке с координатами (0,0,-r) - соответственно, станцией Южного Полюса.


Все станции соединены между собой кратчайшими путями по большим дугам, проходящим через точки расположения станций. Переход от одной станции к другой - рискован. Если d - длина пути между двумя станциями, то (d/(π r))2 - мера риска такого путешествия (назовем ее риском пути). Если путешествие происходит более чем между двумя соседними станциями, то риск всего пути определяется суммой рисков всех использованных путей.


Длина пути путешествия от станции Северного Полюса до станции Южного Полюса составляет πr и его риск равен 1. Путешествие от станции Северного Полюса до станции Южного Полюса по (0,r,0) будет настолько же длинным, однако с меньшим риском: (½πr/(πr))2 +(½πr/(πr))2=0.5.


Наименьший риск пути от станции Северного Полюса до станции Южного Полюса на поверхности C(r) составляет M(r).


Дано, что M(7)=0.1784943998 после округления до 10 знака после десятичной точки.


Найдите ∑M(2n-1) для всех 1≤n≤15.


Ответ округлите до 10 знака после десятичной точки и приведите его в виде a.bcdefghijk.

