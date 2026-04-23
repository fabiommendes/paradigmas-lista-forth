variable size
0 size !

variable buf 1000 cells allot

\ ==============================================================================
\ DEFINIÇÕES
\ ==============================================================================

: get-number ( -- n )
    pad 20 accept pad swap  ( lê até 20 caracteres e deixa addr n na pilha )
    s>number? if            ( converte string para número de dupla precisão e uma flag )
        drop                ( remove a parte de dupla precisão, deixando apenas a parte baixa na pilha )
    else 
        2drop 0             ( limpa a pilha em caso de falha e retorna 0 )
    then 
;

: push ( a -- ) ;

: pop ( -- a ) ;

: get ( i -- a ) ;

: set ( a i -- ) ;

: print-array ( -- ) ;

: array-sum ( -- sum ) ;

: array-max ( -- max ) ;

: array-min ( -- min ) ;

: array-average ( F: -- avg ) ;

\ ==============================================================================
\ TESTES
\ ==============================================================================
\ Não esqueça de apagar ou comentar código fora das definições antes de enviar 
\ a submissão final ou rodar os testes usando o pytest.

read-array 
." Números: " print-array cr
." Tamanho: " size @ . cr
." Soma: " array-sum . cr
." Max: " array-max . cr
." Media: " array-average F. cr

bye
