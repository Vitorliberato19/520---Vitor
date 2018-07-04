#!/usr/bin/python3

# with open('nome.txt','r') as arquivo:
#     conteudo = arquivo.readlines()

def manipular_arquivo(nome,modo,conteudo = None):
    if modo == 'r':
        with open(nome,modo) as arquivo:
            cont = arquivo.readlines()
            print(cont)
    elif modo == 'a':
         with open(nome,modo) as arquivo:
            arquivo.write(conteudo)
            return True

while True:
    arq = input('digite o nome do arquivo ou sair: ')
    if arq == 'sair':
        break
    print(manipular_arquivo(arq,'a','banana'))