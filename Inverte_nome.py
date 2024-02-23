def inverte_nome(n):
  nome, sobrenome = n.split()
  return ' '.join([sobrenome, nome])
 
pessoa = input('Digite seu nome e sobrenome: ')
pessoa = inverte_nome(pessoa)
 
print(pessoa)
