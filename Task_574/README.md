##Verifying Primes

Let $q$ be a prime and $A \ge B >0$ be two integers with the following properties:

It can be shown that, given these conditions, any sum $A+B<q^2$ and any difference $1<A-B<q^2$ has to be a prime number. Thus you can verify that a number $p$ is prime by showing that either $p=A+B<q^2$ or $p=A-B<q^2$ for some $A,B,q$ fulfilling the conditions listed above.
Let $V(p)$ be the smallest possible value of $A$ in any sum $p=A+B$ and any difference $p=A-B$, that verifies $p$ being prime. Examples:
$V(2)=1$, since $2=1+1< 2^2$. 
$V(37)=22$, since $37=22+15=2 \cdot 11+3 \cdot 5< 7^2$ is the associated sum with the smallest possible $A$.
$V(151)=165$ since $151=165-14=3 \cdot 5 \cdot 11 - 2 \cdot 7<13^2$ is the associated difference with the smallest possible $A$. 

Let $S(n)$ be the sum of $V(p)$ for all primes $p<n$. For example, $S(10)=10$ and $S(200)=7177$.

Find $S(3800)$.

##Проверка простых чисел

Пусть $q$ будет простым числом, и $A \ge B >0$ будут двумя целыми числами со следующими свойствами:
 $A$ и $B$ не имеют ни одного общего простого множителя, то есть $\text{НОД}(A,B)=1$.
 Произведение $AB$ делится на каждое простое число меньше $q$.
Можно показать, что при этих условиях любая сумма $A+B<q^2$ и любая разность $1<A-B<q^2$ должны быть простыми числами. Таким образом, можно доказать, что число $p$ - простое, показав, что или $p=A+B<q^2$, или $p=A-B<q^2$ для некоторых $A,B,q$ удовлетворяет вышеназванным условиям.
Пусть $V(p)$ будет наименьшим возможным значением $A$ в любой сумме $p=A+B$ и любой разности $p=A-B$, которое подтверждает, что $p$ - простое число. Примеры:
$V(2)=1$, так как $2=1+1< 2^2$. 
$V(37)=22$, так как $37=22+15=2 \cdot 11+3 \cdot 5< 7^2$ - соответствующая сумма с наименьшим возможным $A$.
$V(151)=165$, так как $151=165-14=3 \cdot 5 \cdot 11 - 2 \cdot 7<13^2$ - соответствующая разность с наименьшим возможным $A$. 

Пусть $S(n)$ будет суммой $V(p)$ для всех простых чисел $p<n$. Например, $S(10)=10$ и $S(200)=7177$.

Найдите $S(3800)$.

