def soma(*args):
    num = 0
    for valordigitado in args:
        num += valordigitado
    print(f'O resultado da soma é: {num}')
    
soma(18,23,81)

def identificacao(*args, **kwargs):
    for n in args:
        nome = n
        for k, v in kwargs.items():
           idade = k
           sexo = v 
           print(f'Nome = {nome}, {idade}, {sexo}')
       
pessoa = identificacao('Fernando', idade=33, sexo='M')

'''
Este é um exercício interessante pois coloca à prova dife
rentes níveis de desempacotamento de dados de *args e 
**kwargs, de modo que para conseguirmos realizar as devidas 
interações com os parâmetros, é de suma importância gerar a 
cadeia de interações na ordem e indentação correta.
De acordo com o enunciado da questão, teremos de fazer uso 
tanto de número de parâmetros indefinido, porém justapostos, 
quanto de parâmetros nomeados. Para isso, definimos nossa função 
identificacao( ) que recebe como parâmetros *args e **kwargs.
Apenas fazendo um adendo, a nomenclatura ‘args’ e ‘kwargs’ pode 
ser substituída por qualquer outro nome, como *números e **nomes 
por exemplo, o marcador em si que o interpretador Python identifica 
na verdade são os “ * “ e “ ** “. Outro ponto que não havia sido 
comentado é que quando usamos de *args e **kwargs, por convenção 
usamos desses marcadores nessa ordem, nunca **kwargs e *args 
pois em algumas IDEs essa ordem pode gerar exceções.

Dando sequência com nosso código, para guardar o dado/valor de 
*args simplesmente usamos de um laço for que lê esse argumento, 
o salvando em uma variável.
Dentro desse laço criaremos um novo laço de repetição, agora com
as variáveis temporárias k e v que percorrerão os argumentos em 
*kwargs.items( ) uma vez que os dados estarão em formato de dicionário,
guardando esses dados/valores em suas respectivas variáveis.
Por fim, podemos usar de nossa velha conhecida função print( ) para 
exibir em tela tais dados.
Fora do corpo de nossa função, no escopo global do código, declaramos
uma variável de nome pessoa que chama a função identificacao( ) 
parametrizando a mesma com ‘Fernando’, que por justaposição será atrelado 
ao campo *args, seguido de dois outros parâmetros nomeados idade e sexo, 
que justamente por serem nomeados irão gerar e compor os campos em *kwargs.

'''
