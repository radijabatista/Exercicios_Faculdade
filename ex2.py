def devolve_email(nome:str, sobrenome:str):
    """
    Funcao para criar email usando nome, sobrenome e ultimos 2 numeros do RU
    :param nome: string com o primeiro nome
    :param sobrenome: string com o sobrenome
    :return: umas string com o email criado
    """
    return str(nome[0] + sobrenome + '27' + '@algoritmos.com.br').lower()


nome = str(input('Digite seu primeiro nome: ')).strip() #Recebe o nome e tira os espaços adicionais
sobrenome = str(input('Digite seu sobrenome: ')).strip() #Recebe o sobrenome e tira os espaços adicionais
email = devolve_email(nome=nome, sobrenome=sobrenome) #Salva o email em uma variavel
print(f'Sra {nome} {sobrenome}, seu email é {email}')