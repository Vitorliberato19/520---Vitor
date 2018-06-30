#!/usr/bin/python3
#tratamenteo de excessão
while True:
    try:
        num = int(input("Digite um numero: "))
        print(num)
        break
    except ValueError as e:
        print("não é inteiro: {}".format(e))

    except exception as e:
        print("não é inteiro: {}".format(e))

