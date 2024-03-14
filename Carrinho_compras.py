'''
89 – Dada uma estrutura inicial de um carrinho de compras com 5 itens e seus respectivos valores, assim como uma função que soma os valores dos itens do carrinho, retornando um valor total. Aprimore a função deste código usando de list comprehension:
'''

# Estrutura Inicial
carrinho = []
 
carrinho.append(('Item 1', 30))
carrinho.append(('Item 2', 45))
carrinho.append(('Item 3', 22))
carrinho.append(('Item 4', 93))
carrinho.append(('Item 5', 6))

total = 0
 
for produto in carrinho:
  total = total + produto[1]
 
print(f'O valor total é: R$ {total}')
 
 
# Código Otimizado
total2 = sum([y for x, y in carrinho])
 
print(f'O Valor total é: R$ {total2}')

'''
Conforme o enunciado, é fornecida uma estrutura inicial onde simplesmente temos um carrinho, seguido de algumas linhas de código adicionando manualmente itens neste carrinho, finalizando com uma função que soma os valores dos itens, exibindo em tela o valor total.
Normalmente quando falamos de aprimorar/otimizar um código, estamos falando não só de o trazer para a forma sintática mais atual, mas também mais otimizada e reduzida.Em nosso exemplo, claro que por se tratar de um pequeno bloco de código, o impacto em performance na execução de nosso programa será mínimo, mas em aplicações reais blocos de código declarados de forma não otimizada podem sim afetar o desempenho de modo que traga uma experiência ruim ao usuário.
Nesse exercício, como seria possível otimizar um simples bloco de código de uma função? A resposta mais lógica seria reescrevendo o mesmo usando de comprehension.
Uma vez que o algoritmo em questão, é percorrer os elementos de uma lista, separando-os individualmente e de acordo com sua posição de índice somar os valores dos mesmos retornando esse dado, esse processo pode muito bem ser reescrito por: total2 = sum([y for x, y in carrinho]), onde usamos a função soma do próprio sistema sum( ), por sua vez parametrizado com um laço for que percorre o carrinho, desempacotando apenas os dados de y e somando estes valores.Por fim, por meio da função print( ) podemos exibir na composição de uma mensagem o último valor da variável total2.
'''
