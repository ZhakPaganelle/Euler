##Incomplete words II

In the context of formal languages, any finite sequence of letters of a given alphabet $\Sigma$ is called a word over $\Sigma$. We call a word incomplete if it does not contain every letter of $\Sigma$.

For example, using the alphabet $\Sigma=\{ a, b, c\}$, '$ab$', '$abab$' and '$\,$' (the empty word) are incomplete words over $\Sigma$, while '$abac$' is a complete word over $\Sigma$.

Given an alphabet $\Sigma$ of $\alpha$ letters, we define $I(\alpha,n)$ to be the number of incomplete words over $\Sigma$ with a length not exceeding $n$. 
For example, $I(3,0)=1$, $I(3,2)=13$ and $I(3,4)=79$.

Let $\displaystyle S(k,n)=\sum_{\alpha=1}^k I(\alpha,n)$.
For example, $S(4,4)=406$, $S(8,8)=27902680$ and $S (10,100) \equiv 983602076 \text { mod } 1\,000\,000\,007$.

Find $S(10^7,10^{12})$. Give your answer modulo $1\,000\,000\,007$.

##Неполные слова II

В контексте формальных языков любая конечная последовательность букв данного алфавита $\Sigma$ называется словом над $\Sigma$. Назовем слово неполным, если оно не содержит все буквы $\Sigma$.

Например, используя алфавит $\Sigma=\{ a, b, c\}$, '$ab$', '$abab$' и '$\,$' (пустое слово) являются неполными словами над $\Sigma$, в то время как '$abac$' является полным словом над $\Sigma$.

Для данного алфавита $\Sigma$ из $\alpha$ букв определим $I(\alpha,n)$ как количество неполных слов над $\Sigma$ длиной не больше $n$. 
Например, $I(3,0)=1$, $I(3,2)=13$ и $I(3,4)=79$.

Пусть $\displaystyle S(k,n)=\sum_{\alpha=1}^k I(\alpha,n)$.
Например, $S(4,4)=406$, $S(8,8)=27902680$ и $S (10,100) \equiv 983602076 \text { mod } 1\,000\,000\,007$.

Найдите $S(10^7,10^{12})$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.

