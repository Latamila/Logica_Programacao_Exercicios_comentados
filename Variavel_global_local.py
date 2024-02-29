'''
Crie uma função que exibe em tela tanto o conteúdo de uma variável local quanto 
de uma variável global, sendo as variáveis de mesmo nome, porém uma
não substituindo a outra:
'''

def msg(): 
    global mensagem
    print(mensagem) 
    mensagem = 'Usufrua das funcionalidades do sistema.'
    print(mensagem)  
  
mensagem = 'Olá, seja bem-vindo(a)!'
msg()
