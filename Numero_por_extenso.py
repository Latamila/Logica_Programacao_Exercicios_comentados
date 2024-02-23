def num_p_texto(n):
    if n == 0:
        return 'zero'
 
    unidade = ('', 'um', 'dois', 'tres', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove')
 
    dezena = ('', '', 'vinte e', 'trinta e', 'quarenta e', 'cinquenta e', 'sessenta e', 'setenta e', 'oitenta e', 'noventa e')
 
    dez_x = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
 
    h, t, u = '', '', ''
 
    if n == 100:
        h = unidade[0] + 'cem'
        n = n % 100
    elif n >= 20:
        t = dezena[n // 10]
        n = n % 10
    elif n >= 10:
        t = dez_x[n - 10]
        n = 0
 
    u = unidade[n]
    return ' '.join(filter(None, [h, t, u]))
 
num = int(input('Digite o número a ser convertido: '))
 
if num <= 100:
  print(f'{num} por extenso é: {num_p_texto(num)}')
else:
  print('Número Inválido!!!')
 
 
if num <= 100:
  print(f'{num} por extenso é: {num_p_texto(num)}')
else:
  print('Número Inválido!!!')


'''
Para esse exercício podemos usar de uma abordagem um pouco parecida com a do exercício onde convertemos um certo texto para Morse, porém aqui, temos que levar em consideração que quando estamos escrevendo por extenso um determinado número, existe uma nomenclatura específica para unidades, dezenas, centenas (que não usaremos de acordo com o enunciado do exercício) e dos números intermediários entre 10 a 19.
Sendo assim, também estaremos fazendo a equivalência de um determinado número com um elemento de uma lista via índice para substituir número por texto, mas com algumas diferenças se comparado ao exercício anterior.
Inicialmente criamos nossa função num_p_texto( ) que receberá um número a ser convertido. Dentro do corpo dessa função inicialmente criamos uma estrutura condicional onde se o valor de n for igual a 0, é retornado apenas ‘zero’, mas caso essa condição não seja verdadeira, aí sim partimos para as conversões número -> texto.
Então criamos uma variável de nome unidade, com números descritos por extenso desde nenhum, ‘um’ até ‘nove’. Como uma espécie de validação, vamos criar essas estruturas em formato de tupla para que não sejam modificadas.
Também criamos uma tupla atribuída a dezena com números descritos desde ‘vinte e’ até ‘noventa e’. O mesmo é feito para a variável dez_x, onde os elementos da tupla correspondem desde ‘dez’ até ‘dezenove’.
Finalizando essa parte criamos as variáveis h, t e u, inicialmente com strings vazias. Caso você não tenha notado, o grande diferencial aqui, quando comparado ao exercício anterior é que para montar a nomenclatura de um determinado número por extenso, o mesmo terá de percorrer nossas variáveis unidade, dezena e dez_x para montar os blocos que formam o nome do número.
Finalizada a estrutura anterior, criamos agora nossa segunda estrutura condicional, ainda indentada como a anterior, verificando se o valor de n é igual a 100, caso sim, para retornar apenas ‘cem’ temos de instanciar nossa variável h, atribuindo para a mesma o conteúdo de unidade em sua posição de índice 0 concatenado com a string ‘cem’. Por fim, n tem seu valor atualizado com o módulo da divisão de seu valor por 100.
De forma parecida, em nosso elif definimos como condição que se o valor de n for igual ou maior a 20, nossa variável t recebe como atributo o conteúdo de dezena, na posição de índice que corresponde a divisão exata do número por 10. Aqui, n tem seu valor atualizado para o módulo da divisão de seu valor por 10.
E finalmente em nossa terceira estrutura condicional, caso nenhuma das anteriores seja verdadeira, estipulamos que se o valor de n foi igual ou maior ou menor que 100, é exibida em tela uma mensagem onde via f’strings interpolamos o valor de num, assim como na segunda máscara de substituição chamamos nossa função num_p_texto( ) parametrizando a mesma com o valor de num.
Caso essa condição não seja válida, simplesmente é retornado ao usuário uma mensagem de número inválido pois subentende-se que o mesmo tenha digitado um número maior que 100, algo que não esperamos em nossa função.
'''
