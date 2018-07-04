#!/usr/bin/python3

# with open('nome.txt','r') as arquivo:
#     conteudo = arquivo.readlines()

def ler_arquivo(nome):
    with open(nome,'r') as arquivo:
        conteudo = arquivo.readlines()
        print(conteudo)
        
variavel1 = ler_arquivo('NovoFrutas.txt')
variavel2 = ler_arquivo('frutas.txt')
variavel3 = ler_arquivo('arquivoNomes.txt')

print(variavel1)
print(variavel2)
print(variavel3)