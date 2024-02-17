def texto_p_morse(texto):
    d = {'A': '.-', 'B': '-...',
         'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-',
         'L': '.-..', 'M': '--', 'N': '-.',
         'O': '---', 'P': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--',
         'X': '-..-', 'Y':'-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.',
         '0': '-----', ',': '--..--', '.': '.-.-.-',
         '?': '..--..', '/': '-..-.', '-': '-....-',
         '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
         ' ': ' ', "'": '.----.', ':': '---...'}
 
    return ' '.join(d[i] for i in texto.upper())
 
texto = input('Digite o texto a ser convertido para Código Morse: ')
 
conversor = texto_p_morse(texto)
 
print(f'{texto} em Código Morse: {conversor}')

'''
O primeiro ponto a ser abordado nesse exercício é o fato de que para se 
converter um determinado texto para código Morse devemos buscar um dicionário 
que equipare caracteres normais em padrão Morse (ponto, traço), o que é facilmente 
encontrado com uma rápida pesquisa na internet.
Dessa forma, criamos nossa função texto_p_morse( ) que recebe um texto como parâmetro. 
Dentro da estrutura de código dessa função criamos nosso dicionário tradutor de Morse.
Como retorno da função em si, bastaria simplesmente associar chave e valor do dicionário,
dando entrada de um caractere e recebendo seu código Morse correspondente, porém, é interessante
aqui realizarmos algumas validações.
Primeira delas eliminando todo e qualquer espaço da string fornecida como dado de entrada, uma vez 
que para Morse não há necessidade de interpretar os espaços, assim como todo e qualquer texto inserido 
é convertido para maiúsculo, para ser identificado corretamente quando associado ao dicionário.
Validações feitas, agora sim podemos criar um laço for que percorre cada elemento do texto fornecido pelo usuário,
retornando do dicionário seu código equivalente.
Já no escopo global de nosso código criamos uma variável de nome texto que via input( ) recebe um texto do usuário, de
forma parecida criamos a variável conversor que chama nossa função texto_p_morse( ) parametrizando a mesma com o conteúdo
da variável texto.
Por fim, via função print( ), fazendo uso de f’strings criamos uma mensagem interpolando em suas máscaras de substituição 
o texto original e seu código Morse.
'''
