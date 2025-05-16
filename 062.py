'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos
'''
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
termos_mostrados = 0  # Contador de termos já mostrados

# Mostra os 10 primeiros termos
while c <= 10:
    termo = p1 + (termos_mostrados) * razao
    print(termo, end=' → ')
    termos_mostrados += 1
    c += 1

# Pergunta por mais termos
while True:
    mais_termos = int(input('Quantos termos a mais? (0 para sair): '))

    if mais_termos == 0:
        break

    # Mostra os termos adicionais solicitados
    c = 1
    while c <= mais_termos:
        termo = p1 + (termos_mostrados) * razao
        print(termo, end=' → ')
        termos_mostrados += 1
        c += 1