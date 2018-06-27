#!/usr/bin/python3
nomes   = ['daniel', 'maria', 'jose', 'joao']

copia = nomes[:]#temos que fatiar a lista para copiar essa lista. Se não   fatiar, não copia
nomes[0] = 'pedro'#substituiro nome Daniel por pedroo
nomes.append('pedro2')#incluir no final
nomes.append(['daniel', 'prata'])#incluir no final uma lista
nomes.insert(0,'prata2')
copia.pop()#tira o ultimo elemento
copia.remove('daniel')#tira o ultimo elemento
print(nomes) 
if 'maria' in nomes:
    print('sim')
else:
    print('não')
print(copia) 
print(nomes[-1][0]) 


print(len(nomes))#quantidade de elementos dentro da lista

##############################################
#lista numerica
num =[1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros = list(range(40,100))
print(numeros)

if 43 in numeros:
    print('sim')
else:
    print('não')
