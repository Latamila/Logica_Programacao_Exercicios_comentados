def mensagem(nome):
    print(f'Bem vindo {nome}')
    
nome=input('digite seu nome: ')
nome=mensagem(nome)


def exp(num):
    print(num ** 2)

num = int(input('digite um numero: '))
num = exp(num)

def boas_vindas(nome, nacionalidade='Brasileir@'):
    print(f'{nome} é {nacionalidade}!!!')
  
nome= input('digite seu nome: ')
ex1=boas_vindas(nome)

nacionalidade=input("digite sua nacionalidade: ")
ex2= boas_vindas(nome,nacionalidade)
    
    
def pessoa1(nome, idade = 18, funcao ='técnico'):
  
  print(f'Eu, {nome}, maior de  {idade} anos, com a  função de {funcao} assino este contrato com duração de 1 ano')
 
p1 = pessoa1('Fernando', funcao = 'gerente')
