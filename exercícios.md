# Lista de exercícios - Forth


## `sort-two`

Crie uma palavra `sort-two ( a b -- x y )` que lê os dois números da pilha e os 
coloca de volta na pilha em ordem crescente.

## `sort-three`

Crie uma palavra `sort-three ( a b c -- x y z )` que lê os três números da pilha
e os coloca de volta na pilha em ordem crescente. Dica: use a palavra `sort-two`
para ajudar a resolver esse exercício.

## `dots`

Crie uma palavra `dots ( n -- )` que lê um número da pilha e imprime uma linha
com `n` pontos.

## `**`

Crie uma palavra `** ( a b -- a^b )` que lê dois números da pilha e deixa o
primeiro número elevado à potência do segundo número. Por exemplo, se a pilha
tiver os números `2 3 **`, a palavra deve deixar `8` na pilha. Dica: use um loop
para multiplicar o número `a` por ele mesmo `b` vezes. Assuma que `b` é um
número não-negativo.

## `3dup`

Podemos definir `2dup` como `over over`. Crie uma palavra similar `3dup ( a b c
-- a b c a b c )` que duplica os três números do topo da pilha.


## `put`

Crie uma palavra `put ( ... a n -- ... a ... )` que lê dois números da pilha e
coloca `a` na posição `n` da pilha, onde `n` é um número positivo. `a 0 put`
deixa `a` no topo da pilha, `a 1 put` seria equivalente a `a swap` e assim por
diante. Por exemplo, `10 20 30 40 50 99 2 put` deve deixar `10 20 30 99 40 50`
na pilha.


## `reverse` 

Crie uma palavra `reverse ( ... n -- ... )` que lê um número da pilha e inverte
a ordem dos últimos `n` números da pilha. Por exemplo, se a pilha tiver os
números `10 20 30 40 50 3 reverse`, a palavra deve deixar `10 20 50 40 30` na
pilha. Assuma que `n` é um número positivo e que a pilha tem pelo menos `n`
números.

## `drop-many`

Crie uma palavra `drop-many ( ... n -- ... )` que lê um número da pilha e remove os
últimos `n` números da pilha. Por exemplo, se a pilha tiver os números `10 20 30
40 50 3 drop-many`, a palavra deve deixar `10 20` na pilha. Assuma que `n` é um
número positivo.

## `drop-at`

Crie uma palavra `drop-at ( ... n -- ... )` que lê um número da pilha e remove o
número que está na posição `n` da pilha, onde `n` é um número positivo. Por
exemplo, se a pilha tiver os números `10 20 30 40 50 2 drop-at`, a palavra deve
deixar `10 20 40 50` na pilha, removendo o número `30`.

## `pop-at`

Crie uma palavra `pop-at ( ... n -- ... a )` que lê um número da pilha e move o
valor que está na posição `n` da pilha para o topo. Por exemplo, se a pilha
tiver os números `10 20 30 40 50 2 pop-at`, a palavra deve deixar a sequência
 `10 20 40 50 30` na pilha, movendo o número `30` para o topo.

## `print-change`

Crie uma palavra `print-change ( a -- )` que lê um número da pilha e imprime a
quantidade de notas de 100, 50, 20, 10, 5 e 2 e moedas de 1 necessárias para compor
esse valor. Por exemplo, se a pilha tiver o número `286`, a saída deve ser:

```2 nota(s) de 100
1 nota(s) de 50
1 nota(s) de 20
1 nota(s) de 10
1 nota(s) de 5
0 nota(s) de 2
1 moedas(s) de 1
```

## `max-n` 

Crie uma palavra `max-n ( ... n -- max )` que lê n números da pilha e deixa
apenas o maior deles no topo. Por exemplo, se a pilha tiver os números 
`3 1 4 1 4 max-n`, a palavra deve deixar `4` na pilha. 
Assuma que `n` é um número positivo e que a pilha tem pelo menos `n` números.


## `reset`

Crie uma palavra `reset ( ... -- )` que remove todos os números da pilha,
deixando-a vazia.


## `all-positive` 

Crie uma palavra `all-positive ( ... -- flag )` que lê todos os números da pilha
e deixa uma flag indicando se todos os números eram positivos ou não. 


## `all-sorted` 

Crie uma palavra `all-sorted ( ... -- flag )` que lê todos os números da pilha 
e deixa um booleano indicando se os números estavam em ordem crescente ou não.


## `filter-positive` 

Crie uma palavra `filter-positive ( ... -- ... )` que lê todos os números da pilha
e deixa apenas os números positivos. Por exemplo, se a pilha tiver os números
`-1 0 2 -3 4 filter-positive`, a palavra deve deixar `2 4` na pilha.


---

## Dicas e funções úteis

### Funções de manipulação da pilha
- `dup` duplica o número do topo da pilha, ou seja, `a` se torna `a a`.
- `pick` copia um número da pilha para o topo, onde `n pick` copia o número que 
  está `n` posições abaixo do topo. Por exemplo, `0 pick` equivale a `dup`, 
  `1 pick` equivale a `over`.
- `swap` troca os dois números do topo da pilha, ou seja, `a b` se torna `b a`.
- `over` copia o segundo número do topo da pilha para o topo, ou seja, `a b` se torna `a b a`. 
- `rot` move o terceiro número do topo da pilha para o topo, ou seja, `a b c` se torna `b c a`.
- `-rot` move o topo da pilha para o terceiro número, ou seja, `a b c` se torna `c a b`.
- `2dup` duplica os dois números do topo da pilha, ou seja, `a b` se torna `a b a b`.

### Funções numéricas
- `max / min` deixam o maior / menor dos dois números do topo da pilha, ou seja, `a b max` deixa o maior entre `a` e `b` no topo da pilha.

### Controle de fluxo/ambiente/execução
- `depth` deixa o número de itens na pilha, ou seja, `a b c depth` deixa `3` no topo da pilha.
- `exit` termina a execução da palavra atual, retornando o controle para a palavra que a chamou.
- `if ... else ... then` é uma estrutura de controle condicional.
- `begin ... until` loop estilo do-while.
- `begin ... while ... repeat` loop estilo while.
- `do ... loop` loop estilo for.
