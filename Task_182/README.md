##RSA encryption

The RSA encryption is based on the following procedure:
Generate two distinct primes p and q.Compute n=pq and φ=(p-1)(q-1).
Find an integer e, 1<e<φ, such that gcd(e,φ)=1.
A message in this system is a number in the interval [0,n-1].
A text to be encrypted is then somehow converted to messages (numbers in the interval [0,n-1]).
To encrypt the text,  for each message, m, c=me mod n is calculated.
To decrypt the text, the following procedure is needed: calculate d such that ed=1 mod φ, then for each encrypted message, c, calculate m=cd mod n.
There exist values of e and m  such that me mod n=m.We call messages m for which me mod n=m unconcealed messages.
An issue when choosing e is that there should not be too many unconcealed messages.  For instance, let p=19 and q=37.
Then n=19*37=703 and φ=18*36=648.
If we choose e=181, then, although gcd(181,648)=1 it turns out that all possible messagesm (0≤m≤n-1) are unconcealed when calculating me mod n.
For any valid choice of e there exist some unconcealed messages.
It's important that the number of unconcealed messages is at a minimum.
Choose p=1009 and q=3643.
Find the sum of all values of e, 1<e<φ(1009,3643) and gcd(e,φ)=1, so that the number of unconcealed messages for this value of e is at a minimum.
##Шифрование методом RSA

Алгоритм шифрования RSA основывается на следующей процедуре:
Генерация двух различных простых чисел p и q. Вычисление n=pq и φ=(p-1)(q-1).
Поиск целого числа e, 1<e<φ, такого, что НОД(e,φ)=1.
Сообщение в этой системе представлено в виде числа, принадлежащего интервалу [0,n-1].
Шифруемый текст каким-нибудь способом преобразовывается в такие сообщения (числа, принадлежащие интервалу [0,n-1]).
Чтобы зашифровать текст, для каждого сообщения m, необходимо вычислить c=me mod n.
Для дешифровки текста выполняется следующая процедура: найти такое d, чтобы ed=1 mod φ, затем для каждого зашифрованного сообщения c вычислить m=cd mod n.
Существуют такие значения e и m, что me mod n=m.Сообщения m, для которых me mod n=m, будем называть открытыми.
Проблема выбора e состоит в том, что не должно быть слишком много открытых сообщений.
К примеру, пусть p=19 и q=37.
Тогда n=19*37=703 и φ=18*36=648.
Если выберем e=181, то, несмотря на то, что НОД(181,648)=1, окажется, что все возможные сообщения
m (0≤m<n-1) будут открытыми после вычисления me mod n.
Для любого верного выбора e существуют некоторые открытые сообщения.
Важно, чтобы число таких открытых сообщений было минимальным.
Дано: p=1009 и q=3643.
Найдите сумму всех значений e, 1<e<φ(1009,3643) и НОД(e,φ)=1, для которых число открытых сообщений будет минимальным.
