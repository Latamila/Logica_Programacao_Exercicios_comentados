'''
Crie um programa que recebe do usuário uma sequência de números aleatórios
separados por vírgula, armazene os números um a um, em formato de texto, 
como elementos ordenados de uma lista. Mostre em tela a lista com 
seus respectivos elementos após ordenados.

'''

numeros = input('Digite os números, separados por vírgula:')
 
lista = numeros.split(",")
lista.sort()
 
print(lista)

'''
Inicialmente temos uma variável de nome numeros que por 
meio da função input( ) recebe do usuário uma sequência
de números aleatórios.
Em seguida, é criada uma nova variável de nome lista que 
simplesmente recebe como atributo o conteúdo de numeros
separados por vírgula por meio da função split( ).
Na sequência aplicamos sobre nossa variável lista o método 
sort( ), que neste caso, sem definirmos nenhum parâmetro 
específico, simplesmente reordenará os elementos em sua 
forma crescente.
Por fim, exibimos em tela o conteúdo da variável lista 
por meio de nossa função print( ).

'''
