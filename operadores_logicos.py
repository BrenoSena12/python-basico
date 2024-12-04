# AND = E / para ser verdadeira todas as condições tem que ser verdadeiras

idade = 20
altura = 1.73

resultado = (idade >= 18) and (altura >= 1.70)

mensagem = "Pode entrar na festa? " + str(resultado)

print(mensagem)


# OR = OU / só serar verdadeira quando uma das condições forem verdadeiras

porta  = 'fechada'
janela = 'aberta'

alarme = (porta == 'aberta') or (janela == 'aberta')

mensagem_alarme = "vai tocar o alarme? " + str(alarme)
print(mensagem_alarme)


# NOT = NÃO / inverte os valores, se for true é falso e se for false é true

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro

msg = 'Tem dinheiro? ' + str(tem_dinheiro)

print(msg) 
