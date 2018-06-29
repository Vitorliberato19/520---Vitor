#!/usr/bin/python3
nome = input('digite o nome do arquivo: ')


with open(nome, 'r') as arquivo:
    conteudo = arquivo.readlines()

print(conteudo[0])

# shebang = '\#\!/usr/bin/python3\n'

if conteudo[0] != '\#\!/usr/bin/python3\n':
    conteudo.insert(0, '#!/usr/bin/python3\n')
    with open(nome,'w') as arquivo:
        for linha in conteudo:
            arquivo.write(linha)




# http://dontpad.com/520/noturno
#!/usr/bin/python3
from subprocess import subprocess

name = input("digite o nome do arquivo")
try:
    with open(name, 'r') as arquivo:
        conteudo = arquivo.readlines()
        conteudo.insert(0, '#!/usr/bin/python3\n')
    with open(name, 'w+') as arquivo:
        for x in conteudo:
            arquivo.write(x)

except FileNotFoundError:
    with open(name, 'a') as arquivo:
        arquivo.write('#!/usr/bin/python3\n')

run(['sudo', 'chmod', '+x', name])
            