class Conversor(object):
    def __init__(self):
        self.s = ""
    
    def recebe_string(self):
        self.s = input('Digite uma palavra/frase: ')
    def exibe_string(self):
        print(self.s.upper())
 
frase1 = Conversor()
frase1.recebe_string()
frase1.exibe_string()

'''
Seguindo as orientações do enunciado da questão, inicialmente criamos uma classe de nome Conversor que receberá um object.
Dentro do corpo dessa classe inicialmente é criado um método construtor/inicializador __init__( ), dentro do mesmo é criado um atributo de classe de nome s que simplesmente recebe uma string vazia.
Seguindo a indentação, é criado um método de classe de nome recebe_string( ), que pode receber um objeto qualquer, retornando o mesmo para o escopo geral da classe.
No corpo desse método de classe é instanciado o atributo de classe s, atribuindo para o mesmo via função input( ) alguma string digitada pelo usuário.
De forma parecida é criado um novo método de classe de nome exibe_string( ), que por sua vez, obedecendo o enunciado da questão, exibe em tela via print( ) o valor de s, tendo todos seus caracteres convertidos para letra maiúscula por meio do método upper( ).
De volta ao escopo global do código, é criada uma variável de nome frase1 que instancia a classe Conversor( ). A partir desse ponto, aplicando para frase1 o método recebe_string( ) será pedido que o usuário digite uma palavra ou frase, assim como aplicando o método exibe_string( ) a palavra/frase digitada pelo usuário será exibida em letras maiúsculas.
'''
