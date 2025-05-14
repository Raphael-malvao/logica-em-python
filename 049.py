'''
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
num = int(input('Digite um valor: '))
c = int(0)
for c in range (1, 11):
    print(num * c)