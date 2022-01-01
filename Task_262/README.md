##Mountain Range

The following equation represents the continuous topography of a mountainous region, giving the elevation h at any point (x,y):
A mosquito intends to fly from A(200,200) to B(1400,1400), without leaving the area given by 0 ≤ x, y ≤ 1600.
Because of the intervening mountains, it first rises straight up to a point A', having elevation f. Then, while remaining at the same elevation f, it flies around any obstacles until it arrives at a point B' directly above B.
First, determine fmin which is the minimum constant elevation allowing such a trip from A to B, while remaining in the specified area.
Then, find the length of the shortest path between A' and B', while flying at that constant elevation fmin.
Give that length as your answer, rounded to three decimal places.
Note: For convenience, the elevation function shown above is repeated below, in a form suitable for most programming languages:
h=( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
##Горная местность

Следующим уравнением описывается непрерывная топография горного региона, если известно, что возвышение h в любой точке (x,y):



Комар намеревается пролететь из точки A(200,200) в точку B(1400,1400), не покидая область, заданную 0 ≤ x, y ≤ 1600.
Из-за мешающих гор, ему необходимо сперва подняться наверх до точки A' с возвышением f. Затем, оставаясь на том же уровне возвышения f, он облетит все возможные преграды и прибудет в точку B' непосредственно над B.
Во-первых, определите такое значение fmin, при котором величина постоянного возвышения минимальна, что позволит пройти путь от точки А до точки В, оставаясь в указанной области.
Затем, найдите длину наикратчайшей траектории между точками A' и B', при неизменном уровне возвышения fmin.
Укажите эту длину в качестве ответа, округлив ее до третьего знака после десятичной точки.
Примечание: Для удобства, функция возвышения, написанная выше, приводится в виде, подходящем для большинства языков программирования:
h=( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
