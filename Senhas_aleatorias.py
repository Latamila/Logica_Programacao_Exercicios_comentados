'''
Crie um programa que gera uma senha aleatória,
com um tamanho definido pelo usuário:
'''


import random
 
tamanho = int(input("enter the length of password"))
 
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
 
senha =  "".join(random.sample(s, tamanho))
 
print(senha)
