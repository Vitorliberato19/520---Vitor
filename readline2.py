#!/usr/bin/python3


with open('frutas2.txt','w') as arqNomes:
    arqNomes.write("")

with open('frutas.txt','r') as arquivo:
      var = arquivo.readlines()
    

print(var)
alterado = []
cont = 0 
for linha in var:
    linha = linha.replace('\n','-{}\n'.format(cont))
    alterado.append(linha)
    cont += 1

print(alterado)

for x in alterado:
    with open('frutas2.txt','a') as arq:
        arq.write(x)


with open('frutas2.txt','r') as arqNomes:
    print(arqNomes.read())


