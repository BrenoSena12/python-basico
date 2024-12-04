# WHILE

nome = None #cria uma variavel vazia

while True: #o True faz com que o laço seja infinito
    nome = input('Digite seu nome ou x para encerrar \n')
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo(a) {nome}')

print('Até logo!')

