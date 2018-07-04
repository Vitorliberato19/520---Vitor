#!/usr/bin/python3


def mult(**frutas):
    multiplica = frutas['valor'] * frutas['qt']
    print("o {} faturou {} reais".format(frutas['nome'],multiplica))

mult(nome = 'mamao', valor = 10, qt = 11)