#!/usr/bin/python3
nomes   = ['daniel', 'maria', 'jose', 'joao']
numeros = list(range(40,100))

nomes2 = []
for nome in nomes:
    nomes2.append(nome.title())
    print(nome)

print(nomes)
print(nomes2)

# num = int(input("Digite um numero: "))
# for x in range(num):
#     if x % 2 ==0:
#         print("{} par".format(x))
#     else:
#         print("{} impar".format(x))


# for y in range(0,num,2):
#     print("{} par".format(y))

    
for y in range(0,100,2):
    print(y)
