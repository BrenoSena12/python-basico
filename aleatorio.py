import random

for x in range(5):
    valor = random.random()
    #round serve para arredondar o valor e o numero depois  da virgula indica as casas decimais e o *100 é para não ser numero menor que 1, pois usando um random.random ele só gerar numero float  aleatório  de 0 e 1
    print(f'numero Gerado: {round(valor * 100,2)}')

    #outra forma

    numero = random.uniform(1,100)
    print(f'numero: {round(numero,3)}' )

    #Pegando dados da lista

    lista = ['Breno' , 'Maria', 'José', 'Amanda']
    nome = random.choice(lista)  #choice = escolha
    print(nome)

    n = random.sample(lista,2) #escolhe a quantidade de itens após a virgula
    print(n)