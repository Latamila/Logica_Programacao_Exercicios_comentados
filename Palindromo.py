frase=str(input('digite uma palavra ou frase: ')).strip().upper()
#metodos garantem que vai retornar string(str), 
#que vai retronar sem espacos no inicio e no final(strip) 
#e em letra maiuscula(upper)
palavras= frase.split()
caracteres=''.join(palavras)
print(frase)
print(palavras)
print(caracteres)
frase_invertida= ''
for i in range(len(caracteres)-1, -1, -1):
    frase_invertida += caracteres[i]
print(caracteres,frase_invertida)
if frase_invertida==caracteres:
    print('\té um palindromo')
else:
    print('\tnao é palindromo')
    
