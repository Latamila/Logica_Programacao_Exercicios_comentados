'''Escreva um simples programa que recebe do usuário um número qualquer, retornando ao mesmo se este número digitado é um número perfeito.


Inicialmente temos de relembrar o que é um número perfeito, que na matemática nada mais é do que um número o qual pode ser dividido por todos seus divisores. 

Ex: O número 6 é um número perfeito, uma vez que o mesmo é divisível por 1, por 3 e por 3, de modo que a soma entre 1, 2 e 3 é igual a 6.


Sendo assim, indo para o código, de início criamos uma variável de nome x que recebe, já validando como número inteiro via int( ) um número digitado pelo usuário por meio da função input( ).


Em seguida é criada a função num_perfeito( ) que recebe o conteúdo da variável x como próprio parâmetro.


No corpo dessa função é criada uma variável de nome sima, inicialmente definida com valor 0.


Na sequência, é criado um laço for que percorre um intervalo entre 1 até o valor de x, haja visto que uma das validações que teremos de realizar para reconhecer um número como perfeito é o mesmo ser divisível por seus antecessores.


Logo, nesse laço de repetição criamos uma estrutura condicional que verifica se a divisão inteira entre o valor de x e cada elemento percorrido pelo laço for é igual a 0. 

Caso essa condição seja verdadeira, o valor de soma é atualizado somando seu valor atual com o valor de i. 

Caso contrário, soma apenas tem seu valor atualizado com o valor de x.


Dentro dessa lógica, com um laço simples e uma condicional simples conseguimos realizar todas validações necessárias para verificar um número como perfeito ou não.


Por fim, apenas criamos uma estrutura condicional onde se o retorno de num_perfeito( ) por sua vez parametrizado com o valor de x for True, é exibido em tela uma mensagem dizendo que tal valor é perfeito. 

Do mesmo modo, caso a condição anterior não seja verdadeira, é exibida em tela uma mensagem dizendo que o valor de x não é um número perfeito.


Supondo que o usuário tenha digitado 6, o retorno será:
6 é um número perfeito!!!
 
Supondo que o usuário tenha digitado 8, o retorno será:
8 não é um número perfeito...
'''

x = int(input('Digite um número: '))
 
def num_perfeito(x):
    soma = 0
    for i in range(1, x):
        if x % i == 0:
            soma += i
    return soma == x
 
if num_perfeito(x):
    print(f'{x} é um número perfeito!!!')
else:
    print(f'{x} não é um número perfeito...')
