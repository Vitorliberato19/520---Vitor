#!/usr/bin/python3
# ler o nome do aluno
# ler  duas notas e calcular a média
# mostrar a média   e o nome do aluno

nomeAluno =   input("Digite o Nome do Aluno: ")
# nota1 = int(input("Digite a primeira Nota: "))#numero inteiro
# nota2 = int(input("Digite a segunda Nota: "))#numero inteiro
nota1 = float(input("Digite a primeira Nota: "))#numero decimal
nota2 = float(input("Digite a segunda Nota: "))#numero decimal
# nomeAluno = nomeAluno.title() #colocar maiuscula no inicio da palavra
# nomeAluno = nomeAluno.upper() #colocar caixa alta
# nomeAluno = nomeAluno.lower() #colocar caixa baixa
nomeAluno = nomeAluno.replace('i','1') #substitui a letra
nomeAluno = nomeAluno.strip() #Tirar os espaços antes e depois da palavra 

mediaNota = (nota1 + nota2)/2



if mediaNota >= 7:
    result = 'APROVADO!'
elif mediaNota >= 5:
    result = 'RECUPERAÇÃO'
else:
    result = 'REPROVADO!'

print("O aluno {}, ficou \
com {} de média. O Aluno está {}".format(nomeAluno.upper(),mediaNota,result))

print("""   
            Aluno:      {}
            Média:      {}
            Situação:   {}
            """.format(nomeAluno.upper(),mediaNota,result))


