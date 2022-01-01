##Standing on the shoulders of trolls


$N$ trolls are in a hole that is $D_N$ cm deep. The $n$-th troll is characterized by:


Trolls can pile up on top of each other, with each troll standing on the shoulders of the one below him. A troll can climb out of the hole and escape if his hands can reach to the surface. Once a troll escapes he cannot participate any further in the escaping effort.


The trolls execute an optimal strategy for maximizing the total IQ of the escaping trolls, defined as $Q(N)$.


Let
$r_n = \left[ \left( 5^n \bmod (10^9 + 7) \right) \bmod 101 \right] + 50$

$h_n = r_{3n}$

$l_n = r_{3n+1}$

$q_n = r_{3n+2}$

$D_N = \frac{1}{\sqrt{2}} \sum_{n=0}^{N-1} h_n$.


For example, the first troll ($n=0$) is 51cm tall to his shoulders, has 55cm long arms, and has an IQ of 75.


You are given that $Q(5) = 401$ and $Q(15)=941$.


Find $Q(1000)$.
##На плечах троллей


$N$ троллей находятся в яме глубиной $D_N$ см. $n$-й тролль описывается следующим образом:


расстояние от его ступней до плеч равно $h_n$ см
длина его рук равна $l_n$ см
его IQ (коэффициент вспыльчивости) равен $q_n$.


Тролли могут выстраиваться в пирамиду, забираясь на плечи стоящего внизу. Тролль может вылезти из ямы и сбежать, если его руки дотягиваются до поверхности. Сбежавший тролль больше не принимает участие в пирамиде.


Тролли следуют оптимальной стратегии с целью макисимизации суммарного IQ сбежавших троллей, обозначенного $Q(N)$.


Пусть
$r_n = \left[ \left( 5^n \bmod (10^9 + 7) \right) \bmod 101 \right] + 50$

$h_n = r_{3n}$

$l_n = r_{3n+1}$

$q_n = r_{3n+2}$

$D_N = \frac{1}{\sqrt{2}} \sum_{n=0}^{N-1} h_n$.


Например, первый тролль ($n=0$) имеет рост 51 см в плечах, руки длиной 55 см и IQ, равный 75.


Известно, что $Q(5) = 401$ и $Q(15)=941$.


Найдите $Q(1000)$. Оригинал
