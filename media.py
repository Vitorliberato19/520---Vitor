#!/usr/bin/python3
# ler o nome do aluno
# ler  duas notas e calcular a média
# mostrar a média   e o nome do aluno

nomeAluno =   input("Digite o Nome do Aluno: ")
nota1 = int(input("Digite a primeira Nota: "))
nota2 = int(input("Digite a segunda Nota: "))
# nomeAluno = nomeAluno.title() #colocar maiuscula no inicio da palavra
# nomeAluno = nomeAluno.upper() #colocar caixa alta
# nomeAluno = nomeAluno.lower() #colocar caixa baixa
nomeAluno = nomeAluno.replace('i','1') #substitui a letra
nomeAluno = nomeAluno.strip() #Tirar os espaços antes e depois da palavra 

mediaNota = (nota1 + nota2)/2

print("O aluno {}, ficou \
com {} de média.".format(nomeAluno.upper(),mediaNota))

