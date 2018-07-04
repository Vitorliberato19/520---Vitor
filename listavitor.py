#!/usr/bin/python3

# with open('listavitor.txt','r') as arq:
#     arq.write("")
# for b in range(1,10,1):
#     print(b)
#     with open('listavitor.txt','a') as arq:
#         arq.write(b)

# def lista(letra):
#     with open('listavitor.txt','a') as arq:
#         arq.write(letra+'\n')

# lista('a')

with open('listavitor.txt', 'w') as arquivo:
    arquivo.write("")

def listar(x1,x2, x3, x4):
    with open('listavitor.txt', 'a') as arquivo:
        result= "{}; {}; {}; {}\n".format(x1, x2, x3, x4)
        arquivo.write(result)


for a in range(1,11):
    for b in range(2,11):
        for c in range(3,11):
            for d in range(4,11):
                if a < b and b < c and c < d:
                    listar(a,b,c,d)

