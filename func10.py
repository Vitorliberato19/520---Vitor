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
            arquivo.write(conteudo+'\n')
            return True

manipular_arquivo('frutas.txt','a','banana')
