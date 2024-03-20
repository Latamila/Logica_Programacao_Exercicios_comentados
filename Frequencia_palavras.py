'''Escreva um programa que recebe uma frase qualquer, mapeando 
a mesma e retornando ao usuário cada palavra com a frequência 
com que a mesma aparece na frase em questão. 
 
frequencia = {}
 
texto = 'Se alguma coisa pode dar errado, dará errado, e mais, 
dará errado da pior maneira, no pior momento e de modo que 
cause o maior / pior dano possível'
'''
for palavra in texto.split():
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
 
palavras = frequencia.keys()
 
for i in palavras:
  print(f'{i} = {frequencia[i]}')

'''
Entendendo inicialmente a lógica do exercício, uma vez que 
temos uma string composta de diversas palavras formando uma 
frase, será necessário desmembrar e percorrer cada uma dessas
palavras para que possamos de fato iterar sobre as mesmas, 
nesse caso contabilizando sua frequência.
Sendo assim, inicialmente criamos uma variável de nome 
frequencia que recebe como atributo um dicionário vazio, 
nela, armazenaremos cada palavra e seu número de incidências.
Em seguida temos uma variável de nome texto que possui como 
atributo uma das leis de Murphy em forma de string.
Para desmembrar e percorrer cada elemento dessa string, 
realizamos um laço de repetição for que percorrerá cada 
elemento desmembrado de texto via texto.split( ), a cada 
laço de repetição atribuindo seu dado para a variável 
temporária palavra.
Dentro do corpo desse laço for instanciamos nosso dicionário 
frequencia, criando a chave [palavra] e atribuindo como valor 
para mesmo o dado oriundo de frequencia.get( ) parametrizado
com palavra, 0, tendo esse valor acrescido em uma unidade
cada vez que uma determinada palavra se repetir ao longo
do mapeamento da string.
Por fim é criada uma variável de nome palavras, que recebe 
apenas os dados de frequencia.keys, ou seja, somente as chaves
de nosso dicionário.
Para exibir em tela tais palavras e sua frequência, podemos simplificar 
o processo com um novo laço de repetição, dessa vez percorrendo o conteúdo 
da variável palavras, a cada ciclo de repetição atribuindo seu dado/valor
para a variável temporária i.
Como ação desse laço de repetição, por meio de nossa função print( ), 
por sua vez parametrizada com uma f’string, instanciamos em suas máscaras
de substituição cada palavra com sua respectiva frequência equivalente.
'''
