import random

listaSorteio = [] #lista com os nomes dos doadores

while True: #Loop para receber os dados
    opcao = str(input('Deseja adicionar um doador?\n0-Não    Enter-Sim\n')).strip()
    if opcao == '0':
        break

    doador = str(input('Nome do doador: ')) #receber nome do doador
    valor_doado = float(input('Valor doado: R$')) #receber valor doado
    vezes_nome = int(valor_doado/10) #descobrir quantas vezes seu nome será adicionado à lista
    listaSorteio += vezes_nome * [doador] #adiciona o nome do doador de acordo com o numero de vezes


random.shuffle(listaSorteio) #embaralha a lista
sorteado = random.choice(listaSorteio) #seleciona um doador aleatorio
print(f'Lista: {listaSorteio}')
print(f'O vencedor(a) é {sorteado}')