class Conversor:
    def int_para_romano(self, num):
        val_int = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        val_rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"]
        numero_romano = ''
        i = 0
        while  num > 0:
            for _ in range(num // val_int[i]):
                numero_romano += val_rom[i]
                num -= val_int[i]
            i += 1
        return numero_romano
 
num = int(input('Digite um número a ser convertido: '))
 
print(Conversor().int_para_romano(num))



'''
De modo parecido com o feito nos exercícios de conversão de número
para Morse e conversão de algarismo para número por extenso, aqui 
temos uma aplicação interessante baseada em conversão onde iremos 
equiparar um número convencional para sua forma escrita em número Romano.
Inicialmente criamos nossa classe Conversor, dentro da mesma o método de 
classe int_para_romano( ), trabalhando dentro do escopo da classe (self), 
recebendo um atributo de classe, nesse caso, um número.
Dentro do corpo deste método de classe criamos uma lista de nome val_int, 
que por sua vez possui toda cadeia de algarismos necessários para que
possamos representar qualquer número.
Da mesma forma criamos uma segunda lista, essa de nome val_rom, com os
algarismos em sua representação romana, de forma que possa cobrir o mesmo 
número de algarismos em val_int, assim como expressar todo e qualquer número
em sua forma romana.
Na sequência criamos uma variável de nome numero_romano que será atualizada
com o número convertido pelo bloco de código seguinte.
É criada uma variável de controle i, inicialmente de valor 0, pois a validação 
que devemos fazer no processo de conversão se dá no número de elementos a 
serem convertidos,
'''
