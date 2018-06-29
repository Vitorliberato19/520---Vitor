#!/usr/bin/python3

# arquivo = open('frutas.txt','a')
# arquivo.write("abacaxi")
# arquivo.close()

# with open('frutas.txt','a') as arquivo:
#     arquivo.write("maca\n")


# with open('frutas.txt','r') as arquivo:
#     print(arquivo.readline())
#     print(arquivo.readline())
#     arquivo.seek(0)#vai para o inicio do arquivo
#     print(arquivo.readline())

with open('arqNomes.txt','w') as arqNomes:
    arqNomes.write("")

while True:
    nome = input('digite o nome para incluir na lista ou sair para finalziar a lista: ')
    if nome.strip().lower() == 'sair':
        break
    with open('arqNomes.txt','a') as arqNomes:
        arqNomes.write(nome+"\n")
    
        
with open('arqNomes.txt','r') as arqNomes:
    print(arqNomes.read())


