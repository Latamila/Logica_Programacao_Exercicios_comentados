'''Crie um programa que mostra a data atual, formatada para dia-mês-ano, 
hora:minuto:segundo. '''
 
import datetime
 
agora = datetime.datetime.now()
 
print ("Data e hora atual: "
print (agora.strftime("%d-%m-%Y, %H:%M:%S"))

'''
Uma das bibliotecas mais úteis que temos à disposição para situações 
que envolvam a manipulação de intervalos de tempo é a biblioteca datetime. 
Esta por sua vez não vem pré-carregada junto a inicialização padrão do Python,
sendo necessário fazer a sua importação por meio do comando import datetime.
Em seguida para que mostre mos em tela a hora atual de acordo com o relógio 
interno do sistema basta chamar a função datetime.now( ) da biblioteca datetime.
Como para nosso exercício vamos aplicar uma formatação à nossa data e hora, atribuímos
tal função a nossa variável agora.
Em seguida criamos duas funções print( ), uma exibindo apenas uma mensagem e outra 
parametrizada com nossa variável agora, aplicando sobre a mesma o método 
strftime( ) que nos permite formatar manualmente como nossa data e hora serão exibidos.
Nesse caso, para exibir a data no formato como estamos habituados, sendo primeiro o dia,
seguido do mês, finalizando com o ano, basta que por justaposição passemos como primeiro 
parâmetro em strftime( ) %s-%m-%Y, assim como para a hora em formato 24h contando até os
segundos, repassamos como segundo parâmetro %H:%M:%S.
'''
       
