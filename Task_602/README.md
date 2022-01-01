##Product of Head Counts


Alice enlists the help of some friends to generate a random number, using a single unfair coin. She and her friends sit around a table and, starting with Alice, they take it in turns to toss the coin. Everyone keeps a count of how many heads they obtain individually. The process ends as soon as Alice obtains a Head. At this point, Alice multiplies all her friends' Head counts together to obtain her random number.


As an illustration, suppose Alice is assisted by Bob, Charlie, and Dawn, who are seated round the table in that order, and that they obtain the sequence of Head/Tail outcomes THHH—TTTT—THHT—H beginning and ending with Alice. Then Bob and Charlie each obtain 2 heads, and Dawn obtains 1 head. Alice's random number is therefore $2\times 2\times 1 = 4$.


Define $e(n, p)$ to be the expected value of Alice's random number, where $n$ is the number of friends helping (excluding Alice herself), and $p$ is the probability of the coin coming up Tails.


It turns out that, for any fixed $n$, $e(n, p)$ is always a polynomial in $p$. For example, $e(3, p) = p^3 + 4p^2 + p$.


Define $c(n, k)$ to be the coefficient of $p^k$ in the polynomial $e(n, p)$. So $c(3, 1) = 1$, $c(3, 2) = 4$, and $c(3, 3) = 1$.


You are given that $c(100, 40) \equiv 986699437 \text{ } (\text{mod } 10^9+7)$.


Find $c(10000000, 4000000) \mod 10^9+7$.

##Произведение выпавших решек


Алиса попросила нескольких друзей помочь с генерированием случайного числа, используя нечестную монету. Она и ее друзья садятся вокруг стола и, начиная с Алисы, по очереди подбрасывают монету. Каждый ведет учет того, сколько они выбрасывают решек. Процесс завершается, как только Алиса выбрасывает решку. В этот момент она перемножает количества решек всех ее друзей, чтобы получить случайное число.


В качестве иллюстрации положим, что Алисе помогают Боб, Чарли и Дон, они сидят за столом именно в таком порядке и получают следующую последовательность выпавших орлов и решек: ОРРР—ОООО—ОРРО—Р, начиная и заканчивая Алисой. Так Боб и Чарли каждый выбрасывают 2 решки, а Дон - одну. Случайное число Алисы таким образом равно $2\times 2\times 1 = 4$.


Определим $e(n, p)$ как ожидаемое значение случайного числа Алисы, где $n$ - количество помогающих друзей (не считая саму Алису), а $p$ - вероятность, что монета упадет орлом.


Оказывается, что для любого выбранного $n$ $e(n, p)$ всегда является многочленом с переменной $p$. Например, $e(3, p) = p^3 + 4p^2 + p$.


Определим $c(n, k)$ как коэффициент при $p^k$ в многочлене $e(n, p)$. Таким образом, $c(3, 1) = 1$, $c(3, 2) = 4$ и $c(3, 3) = 1$.


Известно, что $c(100, 40) \equiv 986699437 \text{ } (\text{mod } 10^9+7)$.


Найдите $c(10000000, 4000000) \mod 10^9+7$.

