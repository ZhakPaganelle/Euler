##Incomplete words

In the context of formal languages, any finite sequence of letters of a given alphabet $\Sigma$ is called a word over $\Sigma$. We call a word incomplete if it does not contain every letter of $\Sigma$.

For example, using the alphabet $\Sigma=\{ a, b, c\}$, '$ab$', '$abab$' and '$\,$' (the empty word) are incomplete words over $\Sigma$, while '$abac$' is a complete word over $\Sigma$.

Given an alphabet $\Sigma$ of $\alpha$ letters, we define $I(\alpha,n)$ to be the number of incomplete words over $\Sigma$ with a length not exceeding $n$. 
For example, $I(3,0)=1$, $I(3,2)=13$ and $I(3,4)=79$.

Find $I(10^7,10^{12})$. Give your answer modulo $1\,000\,000\,007$.
##Неполные слова

В контексте формальных языков любая конечная последовательность букв данного алфавита $\Sigma$ называется словом над $\Sigma$. Назовем слово неполным, если оно не содержит все буквы $\Sigma$.

Например, используя алфавит $\Sigma=\{ a, b, c\}$, '$ab$', '$abab$' и '$\,$' (пустое слово) являются неполными словами над $\Sigma$, в то время как '$abac$' является полным словом над $\Sigma$.

Для данного алфавита $\Sigma$ из $\alpha$ букв определим $I(\alpha,n)$ как количество неполных слов над $\Sigma$ длиной не больше $n$. 
Например, $I(3,0)=1$, $I(3,2)=13$ и $I(3,4)=79$.

Найдите $I(10^7,10^{12})$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
