'''Escreva um programa, da forma mais reduzida o possível, que recebe do usuário 
uma série de nomes, separando os mesmos e os organizando em ordem alfabética. 
Em seguida, exiba em tela os nomes já ordenados. 
 '''
nomes = [x for x in input('Digite os nomes, separados por vírgula: ').split(', ')]
nomes.sort()
 
print(', '.join(nomes))

'''
Quando estamos trabalhando em certos contextos onde se faz necessário o uso de códigos reduzidos, temos várias alternativas não somente para otimizar nossos códigos em escrita, mas também no que diz respeito a sua performance. Para isto, temos desde comprehension até expressões reduzidas que simplificam funções. Em nosso exemplo, uma vez que o usuário tenha dado entrada em vários nomes, precisamos percorrer cada um destes nomes para os separar permitindo assim a reorganização dos mesmos conforme pede o exercício.
Da forma mais reduzida o possível, então criamos uma variável de nome nomes que recebe como atributo uma lista, dentro dessa lista criamos um laço for reduzido que percorrerá cada um dos elementos digitados pelo usuário e retornados por meio da função input( ), separando cada um desses elementos por meio do método split( ) por sua vez parametrizado com ‘, ‘ para que o marcador que identificará a separação de cada um dos elementos seja uma vírgula e espaço, condizendo com a mensagem repassada ao usuário na própria função input( ).
A cada laço, um dos nomes é separado e atribuído a variável temporária x, gerando ao final
