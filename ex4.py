
from operator import itemgetter

listaProdutos = [] #lista para armazenar os dicionarios

while True: #Loop para receber os dados
    opcao = str(input('Deseja adicionar um produto?\n0-Não    Enter-Sim\n')).strip()
    if opcao == '0':
        break

    #Recebe as informações de cada produto
    codigo = int(input('Código: '))
    estoque = int(input('Estoque: '))
    minimo = int(input('Minimo: '))

    produto = {'codigo': codigo, 'estoque': estoque, 'minimo': minimo} #Criando um dicionario com os dados
    listaProdutos.append(produto) #Adicionando o dicionario em uma lista


listaOrdenada = sorted(listaProdutos, key=itemgetter('codigo')) #Colocando os itens ordenados pelo código

print(listaOrdenada)


