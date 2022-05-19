
while True:
    awnser = str(input('Deseja inserir dados?\n0-Sair         Enter-Continuar \n')) #Verifica se o usuario que sair ou inserir dados
    if awnser == '0': #Verifica a escolha
        break

    nome = str(input('Nome do aluno: ')) #Recebe o nome do aluno
    nota = float(input('Nota Final: ')) #Recebe a nota do aluno

    #Descobrir em que conceito o aluno se enquadra
    if nota >= 0 and nota <= 2.9:
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito E')
    elif nota >= 3 and nota <= 4.9:
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito D')
    elif nota >= 5 and nota <= 6.9:
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito C')
    elif nota >= 7 and nota <= 8.9:
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito B')
    elif nota >= 9 and nota <= 10:
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito A')