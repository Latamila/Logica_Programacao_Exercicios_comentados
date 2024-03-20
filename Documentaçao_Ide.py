def ao_quadrado(num):
    '''Esta função recebe como parâmetro um número,
       retornando ao usuário o resultado do número
       em questão elevado ao quadrado.
       Ex: ao_quadrado(16) retornará 256.
    '''
    return num ** 2
 
#print(ao_quadrado(18)) retornará 324
print(ao_quadrado.__doc__)

'''

Neste exemplo, a equipe de Data Science precisa ter acesso 
apenas à documentação das funções para análise geral. 

Quando estamos falando em documentação, toda e qualquer 
estrutura em Python possui tanto sua documentação formal 
acessível pelo site oficial da linguagem, quanto uma 
documentação reduzida e dinâmica que pode ser consultada 
diretamente durante a escrita do código.


Uma boa prática de programação é sempre que possível
comentar e documentar nossos próprios códigos, 
principalmente se os mesmos serão distribuídos para terceiros.


Nesse processo, podemos criar um modelo de documentação 
dinâmica chamada docstring, que por parte de sintaxe 
simplesmente é escrita como um comentário de múltiplas 
linhas (comentário identificado por aspas triplas ‘’’) 
logo nas primeiras linhas do corpo de uma função.

Em nosso exemplo é criada uma função de nome ao_quadrado( ) 
que recebe obrigatoriamente como parâmetro um dado/valor 
para num. 

Dentro do corpo da função temos uma docstring, seguido de 
um retorno padrão definido pela própria expressão matemática
que irá pegar o valor de num e elevar ao quadrado.


 ao_quadrado(16) retornará 256.'''
