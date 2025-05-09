'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
'''

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

#verifica se pode ou não ser um triângulo
if a + b <= c or b + c <= a or a + c <= b:
    print('Não pode ser um triângulo')

#verifica se é equilátero
elif a == c and b == a and b == c:
    print('Sim é um triângulo e é Equilátero')

#verifica se é Isóceles
elif a == b or b == c:
    print('Sim é um triângulo e é Isóceles')

# se não é equilatero nem isoceles, então é escaleno
else:
    print('Sim é um triângulo e é Escaleno')