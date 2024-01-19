Crie uma função de número de parâmetros indefinido, que realiza a soma dos números repassados como parâmetro, independentemente da quantidade de números:'''

def soma(*args):
    num = 0
    for valordig in args:
        num+=valordig
        print(f'O valor da soma é {num}')
        
soma = soma(764,897,765,6758)


'''
Crie uma função que recebe parâmetros tanto por justaposição (*args) quanto nomeados (**kwargs):
    
'''

def identificacao(*args,**kwargs):
    for n in args:
        nome=n
        #print(n)
        
        for k, v in kwargs.items():
            idade=k
            sexo=v
            #print(f'{idade},{sexo}')
            
            print(f'Nome: {nome},{idade},{sexo}')
            
pessoa=identificacao('Fernando', idade=33, sexo= 'M')
